# Prompts

One file per prompt template. The model settings (temperature, answer length) are in [`config/rag.yaml`](../config/rag.yaml).

| File | What it is | Used in | Placeholders |
|---|---|---|---|
| [`answer.yaml`](answer.yaml) | The answer prompt: the rules, one example, then the retrieved provisions and the question. It also holds the fixed texts of the input and output checks (refusal, out of scope, "not a legal decision" notice). | The baseline answers (KAN-99). First tested in the [model selection spike](../docs/spikes/model-selection-spike.md), run 5. | `{provisions}`, `{previous}`, `{question}`, `{previous_question}` |
| [`jury.txt`](jury.txt) | The question to the LLM jury: should keyword search ignore or keep a frequent word? | Step 4 of [`src/embedding.ipynb`](../src/embedding.ipynb) (KAN-221), with qwen3:14b, phi4:14b and gemma3:12b. The notebook has the same text in its code. | `{examples}` (three chunks that contain the word), `{word}` |

The prompts used to **write** the evaluation questions are not system prompts; they are recorded with the questions in [`docs/eval/prompts-3b.md`](../docs/eval/prompts-3b.md) and [`docs/eval/question-writing-method.md`](../docs/eval/question-writing-method.md).
