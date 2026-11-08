# Evaluation

Evaluation questions and their records (course repository structure: `docs/eval/`).

| File | What it is |
|---|---|
| [eval-set-v1.csv](eval-set-v1.csv) | The Q&A Generation-Dataset v1 (D2): question, type, gold answer and gold source of every question. Started on 04/11/2026 with the 7 questions adapted from the AI Act Evaluation Benchmark (`BM-01`–`BM-07`); each member adds the questions for their use case by 11/11/2026. Data card: [Q&A data report](../../Markdown%20Template/11-datasheets/03-qa-data-report.md) |
| [benchmark-selection.md](benchmark-selection.md) | How the 7 benchmark questions were selected and adapted (KAN-48): source and licence, selection criteria, the original items word for word, the questions, gold answers and gold sources, and the items not selected |
| [prompts-3b.md](prompts-3b.md) | How the B questions (`B-01`–`B-07`, `B-S1`–`B-S3`, use case (b), author Gözde Nur) were written with an LLM: the steps, the prompts, the model and the dates. The Sprint 1 questions were used in the [model selection spike](../spikes/model-selection-spike.md) |
| [rubric.md](rubric.md) | How an answer is judged (D2 criterion 12, KAN-50): the definition of "fully supported" (O2 (b)), the four expected behaviours `answer`, `abstain`, `refuse` and `redirect` (O4) with examples, what counts as a verdict (C-08), and how a review is done. Draft, for team review |

**IDs:** `BM` = adapted from the benchmark, `EM` = exam monitoring (d), `B` = learning-outcome assessment (b), `C` = level placement (c); `-S` marks a safety question.

Planned: `eval-set-v2.csv` (D8, Sprint 3).
