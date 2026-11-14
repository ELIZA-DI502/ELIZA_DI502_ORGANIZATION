"""Settings of the RAG service.

Chosen values come from config/rag.yaml (chunking, embedding, retrieval) and the prompt texts from
prompts/. The generation values are the planned settings of D9 until config/rag.yaml has a
`generation:` section; environment variables override both (docker-compose.yml, .env).
"""
import json
import os
from pathlib import Path

import yaml

ROOT = Path(os.environ.get("ELIZA_ROOT", Path(__file__).resolve().parents[2]))

CONFIG = yaml.safe_load((ROOT / "config" / "rag.yaml").read_text(encoding="utf-8"))
PROMPT_RAG = yaml.safe_load((ROOT / "prompts" / "answer.yaml").read_text(encoding="utf-8"))
PROMPT_NO_RAG = yaml.safe_load((ROOT / "prompts" / "answer-no-rag.yaml").read_text(encoding="utf-8"))
PERSONAL_DATA = json.loads((ROOT / "config" / "personal-data.json").read_text(encoding="utf-8"))

# D9: Llama-3.1-8B-Instruct Q4_K_M, temperature 0, at most 300 answer tokens, context window 4,096 tokens.
_GEN_DEFAULTS = {
    "model": "llama3.1:8b-instruct-q4_K_M",           # Ollama tag in the AI SBOM
    "fallback_model": "phi4-mini:3.8b-q4_K_M",
    "temperature": 0,
    "num_predict": 300,
    "num_ctx": 4096,
}
GENERATION = {**_GEN_DEFAULTS, **(CONFIG.get("generation") or {})}
if os.environ.get("LLM_MODEL"):
    GENERATION["model"] = os.environ["LLM_MODEL"]

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434").rstrip("/")
LLM_TIMEOUT_S = float(os.environ.get("LLM_TIMEOUT_S", "180"))

# "rag": retrieved provisions in the prompt; "no_rag": the same LLM without them (baseline of section 5, Evaluation).
DEFAULT_MODE = os.environ.get("DEFAULT_MODE", "rag")

# config/rag.yaml gives the store path relative to src/ (the notebooks); the container mounts it elsewhere.
VECTOR_STORE_PATH = Path(os.environ.get(
    "VECTOR_STORE_PATH", (ROOT / "src" / CONFIG["vector_store"]["path"]).resolve()))
CHUNKS_PATH = ROOT / "data" / "chunks.jsonl"

VERSION_DATE = CONFIG["chunking"]["version_date"]
CELEX = CONFIG["chunking"]["celex"]
SOURCE_URL = f"https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:{CELEX}"
