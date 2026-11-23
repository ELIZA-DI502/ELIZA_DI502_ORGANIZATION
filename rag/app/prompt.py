"""Prompt builder: prompts/answer.yaml filled as in src/rag_vs_no_rag.ipynb (cell "ask").

Both modes use the same template and rules; only the PROVISIONS differ:
  "rag":    the 8 retrieved chunks, best first;
  "no_rag": all 105 chunks in the order of data/chunks.jsonl (no retrieval). The provisions come before
            the question and never change, so Ollama can reuse the processed beginning of the prompt.
"""
from .config import PROMPT


def _previous(history):
    """The earlier question of a follow-up; the service uses the last question of the history."""
    if not history:
        return ""
    return PROMPT["previous_question"].format(previous_question=history[-1]["question"])


def build_messages(question, history, chunks):
    provisions = "\n\n".join(f"[{c['ref']}] {c['text']}" for c in chunks)
    return [
        {"role": "system", "content": PROMPT["system"]},
        {"role": "user", "content": PROMPT["example_user"]},
        {"role": "assistant", "content": PROMPT["example_answer"]},
        {"role": "user", "content": PROMPT["user"].format(provisions=provisions, previous=_previous(history),
                                                          question=question)},
    ]
