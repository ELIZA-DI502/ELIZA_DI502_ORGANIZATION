# Prompts

One file per prompt template. The model settings (temperature, answer length) are in [`config/rag.yaml`](../config/rag.yaml).

| File | What it is | Used in | Placeholders |
|---|---|---|---|
| [`answer.yaml`](answer.yaml) | The answer prompt: the rules, one example, then the retrieved provisions and the question. It also holds the fixed texts of the input and output checks (refusal, out of scope, "not a legal decision" notice). | The baseline answers (KAN-99). First tested in the [model selection spike](../docs/spikes/model-selection-spike.md), run 5. | `{provisions}`, `{previous}`, `{question}`, `{previous_question}` |
| [`answer_full_text.yaml`](answer_full_text.yaml) | The baseline without retrieval (instructor's suggestion): the same rules as `answer.yaml`, sent once in a claude.ai chat with the whole consolidated text attached, then the 30 `val` questions in 3 messages of 10. | The answers of Claude Haiku 5.5 of 12/11/2026 in `docs/eval/answers/`, read by [`src/rag_vs_no_rag.ipynb`](../src/rag_vs_no_rag.ipynb) (KAN-99). | `{part}` (1–3) |
| [`jury.txt`](jury.txt) | The question to the LLM jury: should keyword search ignore or keep a frequent word? | Step 4 of [`src/embedding.ipynb`](../src/embedding.ipynb) (KAN-221), with qwen3:14b, phi4:14b and gemma3:12b. The notebook has the same text in its code. | `{examples}` (three chunks that contain the word), `{word}` |

The prompts used to **write** the evaluation questions are not system prompts; they are recorded with the questions in [`docs/eval/prompts-3b.md`](../docs/eval/prompts-3b.md) and [`docs/eval/question-writing-method.md`](../docs/eval/question-writing-method.md).
