"""Settings of the RAG service.

Everything comes from config/rag.yaml and prompts/answer.yaml, the files that src/rag_vs_no_rag.ipynb
(KAN-99) reads, so the service answers with the same retrieval, prompt and model settings as the notebook.
Environment variables (docker-compose.yml, .env) can override the model, the Ollama address and the mode.
"""
import json
import os
from pathlib import Path

import yaml

ROOT = Path(os.environ.get("ELIZA_ROOT", Path(__file__).resolve().parents[2]))

CONFIG = yaml.safe_load((ROOT / "config" / "rag.yaml").read_text(encoding="utf-8"))
PROMPT = yaml.safe_load((ROOT / "prompts" / "answer.yaml").read_text(encoding="utf-8"))
PERSONAL_DATA = json.loads((ROOT / "config" / "personal-data.json").read_text(encoding="utf-8"))

# The 105 chunks of data/chunks.jsonl (src/chunking.ipynb), in file order. Small enough to keep in memory.
CHUNKS = [json.loads(line) for line in (ROOT / "data" / "chunks.jsonl").open(encoding="utf-8")]

# The answer settings of the notebook (config/rag.yaml, answer:): model, temperature 0, num_predict 300, seed 42.
# The notebook does not set num_ctx, so in "rag" mode the service does not set it either (same answers).
ANSWER = CONFIG["answer"]
GENERATION = {
    "model": os.environ.get("LLM_MODEL") or ANSWER["model"],
    "temperature": ANSWER["temperature"],
    "num_predict": ANSWER["num_predict"],
    "seed": ANSWER["seed"],
}
# "no_rag" mode puts all 105 chunks in the prompt (8,743 tokens with the Llama 3.1 tokenizer, 17/11/2026),
# so Ollama needs a larger context window: room for the prompt, a follow-up question and 300 answer tokens.
NUM_CTX_ALL_CHUNKS = int(os.environ.get("NUM_CTX_ALL_CHUNKS", "12288"))

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434").rstrip("/")
LLM_TIMEOUT_S = float(os.environ.get("LLM_TIMEOUT_S", "600"))

# "rag":    the 8 chunks found by the retrieval (D14) are in the prompt.
# "no_rag": no retrieval; all 105 chunks are in the prompt, so the model still answers from the text.
DEFAULT_MODE = os.environ.get("DEFAULT_MODE", "rag")

# D11: the Chroma store written by rag/ingest.py. config/rag.yaml gives its path relative to src/ (the notebooks);
# the container mounts it elsewhere.
VECTOR_STORE_PATH = Path(os.environ.get(
    "VECTOR_STORE_PATH", (ROOT / "src" / CONFIG["vector_store"]["path"]).resolve()))
CHUNKS_PATH = ROOT / "data" / "chunks.jsonl"

VERSION_DATE = CONFIG["chunking"]["version_date"]
CELEX = CONFIG["chunking"]["celex"]
SOURCE_URL = f"https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:{CELEX}"
