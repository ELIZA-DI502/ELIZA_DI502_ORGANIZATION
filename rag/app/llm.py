"""LLM client: the Ollama HTTP API (D9), with the options of src/rag_vs_no_rag.ipynb."""
import requests

from .config import GENERATION, LLM_TIMEOUT_S, OLLAMA_URL


class LLMError(RuntimeError):
    pass


def chat(messages, num_ctx=None, model=None):
    """Sends the messages to Ollama and returns (answer text, Ollama's token counts). No streaming (non-goal).
    num_ctx is sent only when given (no_rag mode); the notebook does not send it."""
    options = {k: GENERATION[k] for k in ("temperature", "num_predict", "seed")}
    if num_ctx:
        options["num_ctx"] = num_ctx
    payload = {"model": model or GENERATION["model"], "messages": messages, "stream": False, "options": options}
    try:
        r = requests.post(f"{OLLAMA_URL}/api/chat", json=payload, timeout=LLM_TIMEOUT_S)
    except requests.RequestException as error:
        raise LLMError(f"Ollama not reachable at {OLLAMA_URL}: {type(error).__name__}") from error
    if r.status_code == 404:
        raise LLMError(f"model {payload['model']} is not in Ollama; run: ollama pull {payload['model']}")
    if not r.ok:
        raise LLMError(f"Ollama answered {r.status_code}")
    reply = r.json()
    if "error" in reply:
        raise LLMError(reply["error"])
    tokens = {"prompt": reply.get("prompt_eval_count"), "answer": reply.get("eval_count")}
    return reply["message"]["content"].strip(), tokens


def available():
    """The model names Ollama has, or None if Ollama cannot be reached."""
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        return [m["name"] for m in r.json().get("models", [])]
    except (requests.RequestException, ValueError):
        return None
