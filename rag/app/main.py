"""RAG service (D2): a stateless FastAPI service with POST /answer.

Input check -> retriever -> prompt builder -> LLM (Ollama) -> output check, as in the system
architecture diagram (v4). The history comes with every request; nothing is stored here.
The API contract is a draft until the web and RAG sides agree on it (design document, section 7).
"""
import logging
import threading
import time
from contextlib import asynccontextmanager
from typing import Literal, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from . import checks, llm
from .config import DEFAULT_MODE, GENERATION, SOURCE_URL, VERSION_DATE
from .prompt import build_messages

log = logging.getLogger("rag")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")

# The retriever loads bge-m3 and the stores in the background, so /health and no_rag answers work at once.
state = {"retriever": None, "retriever_error": None}


def _load_retriever():
    try:
        from .retrieval import Retriever
        started = time.time()
        state["retriever"] = Retriever()
        log.info("retriever ready in %.0f s (%d chunks)", time.time() - started, len(state["retriever"].ids))
    except Exception as error:   # the service keeps running; rag mode answers 503 until this is fixed
        state["retriever_error"] = f"{type(error).__name__}: {error}"
        log.warning("retriever not available: %s", state["retriever_error"])


@asynccontextmanager
async def lifespan(_app):
    threading.Thread(target=_load_retriever, daemon=True).start()
    yield


app = FastAPI(title="ELIZA RAG service", version="0.1.0", lifespan=lifespan)


class Turn(BaseModel):
    question: str
    answer: str = ""


class AnswerRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)
    history: list[Turn] = Field(default_factory=list, max_length=10)
    mode: Optional[Literal["rag", "no_rag"]] = None


class Citation(BaseModel):
    n: int
    chunk_id: str
    ref: str
    cited_as: str                            # the citation as written in the answer, e.g. "Article 6(3)"
    text: str
    version_date: Optional[str]
    source_url: str


class AnswerResponse(BaseModel):
    status: Literal["answer", "notice"]
    kind: Optional[Literal["refuse", "out_of_scope", "personal_data"]] = None   # why a notice was returned
    answer: str
    notice: Optional[str] = None             # the "not a legal decision" line, when the output check adds it
    citations: list[Citation] = []           # cited provisions found among the retrieved chunks
    unsupported_citations: list[str] = []    # cited in the answer but not among the retrieved chunks (KAN-49)
    retrieved: list[str] = []                # chunk IDs given to the model, best first (for Recall@k)
    flags: dict = {}
    mode: Literal["rag", "no_rag"]
    model: Optional[str] = None
    version_date: str = VERSION_DATE
    timing_ms: dict = {}


@app.get("/health")
def health():
    return {
        "status": "ok",
        "default_mode": DEFAULT_MODE,
        "rag_ready": state["retriever"] is not None,
        "rag_error": state["retriever_error"],
        "model": GENERATION["model"],
        "ollama_models": llm.available(),
    }


@app.post("/answer", response_model=AnswerResponse)
def answer(req: AnswerRequest):
    mode = req.mode or DEFAULT_MODE
    started = time.time()
    timing = {}
    question = req.question.strip()

    # 1. Input check (D3)
    kind, notice_text, flags = checks.input_check(question)
    if kind:
        log.info("mode=%s notice=%s", mode, kind)            # no question content in the logs (C-10)
        return AnswerResponse(status="notice", kind=kind, answer=notice_text, flags=flags, mode=mode,
                              timing_ms={"total": int((time.time() - started) * 1000)})

    # 2. Retriever
    chunks = []
    if mode == "rag":
        retriever = state["retriever"]
        if retriever is None:
            detail = "retrieval is still loading" if state["retriever_error"] is None else "retrieval is not available"
            raise HTTPException(status_code=503, detail=detail)
        t = time.time()
        chunks = retriever.search(question)
        timing["retrieval"] = int((time.time() - t) * 1000)

    # 3. Prompt builder and LLM
    messages = build_messages(question, [h.model_dump() for h in req.history], chunks, mode)
    t = time.time()
    try:
        draft = llm.chat(messages)
    except llm.LLMError as error:
        log.error("mode=%s llm_error=%s", mode, error)
        raise HTTPException(status_code=502, detail="the language model did not answer")
    timing["llm"] = int((time.time() - t) * 1000)

    # 4. Output check: verdict wording, citations, version date
    text, removed = checks.remove_verdicts(draft)
    flags["verdicts_removed"] = removed
    notice = checks.NOTICE if (removed or flags.get("verdict_request")) else None
    cited, unsupported = checks.check_citations(text, chunks)
    citations = [Citation(n=n, chunk_id=c["chunk_id"], ref=c["ref"], cited_as=c["cited_as"], text=c["text"],
                          version_date=c.get("version_date") or VERSION_DATE, source_url=SOURCE_URL)
                 for n, c in enumerate(cited, 1)]

    timing["total"] = int((time.time() - started) * 1000)
    log.info("mode=%s chunks=%d cited=%d unsupported=%d verdicts_removed=%d total_ms=%d",
             mode, len(chunks), len(citations), len(unsupported), removed, timing["total"])
    return AnswerResponse(status="answer", answer=text, notice=notice, citations=citations,
                          unsupported_citations=unsupported, retrieved=[c["chunk_id"] for c in chunks],
                          flags=flags, mode=mode, model=GENERATION["model"], timing_ms=timing)
