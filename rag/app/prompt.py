"""Prompt builder: fills the template of prompts/ with the retrieved chunks and the session history.

mode "rag":    prompts/answer.yaml with the retrieved provisions.
mode "no_rag": prompts/answer-no-rag.yaml, the same rules and example without provisions
               (the no-RAG baseline of the design document, section 5, Evaluation).
"""
from .config import PROMPT_NO_RAG, PROMPT_RAG


def _previous(template, history):
    """The prompt has room for the earlier question of a follow-up; the last question of the history is used."""
    if not history:
        return ""
    return template["previous_question"].format(previous_question=history[-1]["question"])


def build_messages(question, history, chunks=None, mode="rag"):
    template = PROMPT_RAG if mode == "rag" else PROMPT_NO_RAG
    fields = {"question": question, "previous": _previous(template, history)}
    if mode == "rag":
        fields["provisions"] = "\n\n".join(f"[{c['ref']}] {c['text']}" for c in chunks or [])
    return [
        {"role": "system", "content": template["system"]},
        {"role": "user", "content": template["example_user"]},
        {"role": "assistant", "content": template["example_answer"]},
        {"role": "user", "content": template["user"].format(**fields)},
    ]
