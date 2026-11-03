# Evaluation

Evaluation questions and their records (course repository structure: `docs/eval/`).

| File | What it is |
|---|---|
| [eval-set-v1.csv](eval-set-v1.csv) | The Q&A Generation-Dataset v1 (D2): question, type, gold answer and gold source of every question. Started on 04/11/2026 with the 7 questions adapted from the AI Act Evaluation Benchmark (`BM-01`–`BM-07`); each member adds the questions for their use case by 11/11/2026. Data card: [Q&A data report](../../Markdown%20Template/11-datasheets/03-qa-data-report.md) |
| [benchmark-selection.md](benchmark-selection.md) | How the 7 benchmark questions were selected and adapted (KAN-48): source and licence, selection criteria, the original items word for word, the questions, gold answers and gold sources, and the items not selected |
| [eval-set-v1-3b.csv](eval-set-v1-3b.csv) | Sprint 1: 8 questions on Annex III point 3(b), each with its gold source, used to test the candidate models in the [model selection spike](../spikes/model-selection-spike.md) |
| [prompts-3b.md](prompts-3b.md) | The prompts used to draft those questions, with the model and date |

Planned: `rubric.md` (D2, Sprint 2, due 11/11/2026) and `eval-set-v2.csv` (D8, Sprint 3).
