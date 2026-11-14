"""LLM client: the Ollama HTTP API on the internal Docker network (D9)."""
import requests

from .config import GENERATION, LLM_TIMEOUT_S, OLLAMA_URL


class LLMError(RuntimeError):
    pass


def chat(messages, model=None):
    """Sends the messages to Ollama and returns the answer text. No streaming (non-goal)."""
    payload = {
        "model": model or GENERATION["model"],
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": GENERATION["temperature"],
            "num_predict": GENERATION["num_predict"],
            "num_ctx": GENERATION["num_ctx"],
        },
    }
    try:
        r = requests.post(f"{OLLAMA_URL}/api/chat", json=payload, timeout=LLM_TIMEOUT_S)
    except requests.RequestException as error:
        raise LLMError(f"Ollama not reachable at {OLLAMA_URL}: {type(error).__name__}") from error
    if r.status_code == 404:
        raise LLMError(f"model {payload['model']} is not in Ollama; run: ollama pull {payload['model']}")
    if not r.ok:
        raise LLMError(f"Ollama answered {r.status_code}")
    return r.json()["message"]["content"].strip()


def available():
    """The model names Ollama has, or None if Ollama cannot be reached."""
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        return [m["name"] for m in r.json().get("models", [])]
    except (requests.RequestException, ValueError):
        return None
