# Evaluation

Evaluation questions and their records (course repository structure: `docs/eval/`).

| File | What it is |
|---|---|
| [eval-set-v1.csv](eval-set-v1.csv) | The Q&A Generation-Dataset v1 (D2): question, type, gold answer and gold source of every question. Started on 04/11/2026 with the 7 questions adapted from the AI Act Evaluation Benchmark; 46 questions on 09/11/2026, 10 to 15 for each use case. Data card: [Q&A data report](../../Markdown%20Template/11-datasheets/03-qa-data-report.md) |
| [eval-set-v1-val.csv](eval-set-v1-val.csv), [eval-set-v1-test.csv](eval-set-v1-test.csv) | Historical snapshots of the `val` / `test` split made by `src/split.ipynb` (KAN-53), not the reviewed v1: the test file is the split of 09/11/2026 (SHA-256 prefix `f68bfa56`); the val file also has the use case (d) review notes and `answer_origin` updates of 10/11/2026. Review corrections are made only in `eval-set-v1.csv`, which is the authoritative v1; the held-out test input is generated from its `split = test` rows (data card, decision Q-32) |
| [benchmark-selection.md](benchmark-selection.md) | How the 7 benchmark questions were selected and adapted (KAN-48): source and licence, selection criteria, the original items word for word, the questions, gold answers and gold sources, and the items not selected |
| [prompts-3b.md](prompts-3b.md) | How the B questions (`B-01`, `B-03`–`B-07`, `B-S1`–`B-S4`, use case (b), author Gözde Nur) were written with an LLM: the steps, the prompts, the model and the dates. The Sprint 1 questions were used in the [model selection spike](../spikes/model-selection-spike.md) |
| [rubric.md](rubric.md) | How an answer is judged (D2 criterion 12, KAN-50): the definition of "fully supported" (O2 (b)), the four expected behaviours `answer`, `abstain`, `refuse` and `redirect` (O4) with examples, what counts as a verdict (C-08), and how a review is done. v1, used for the D2 review and the E1 card |

**IDs:** every question has the letter of its use case: `A` = admission (a), `B` = learning-outcome assessment (b), `C` = level placement (c), `D` = exam monitoring (d); `-S` marks a safety question. A question adapted from the benchmark is marked in the `origin` column.

**ID changes on 09/11/2026** (team meeting). Older records (Sprint 1 pages, `prompts-3b.md`, earlier decisions in the data card) keep the old IDs.

| Until 09/11/2026 | From 09/11/2026 |
|---|---|
| `BM-01`, `BM-02`, `BM-07` | `A-05`, `A-06`, `A-07` |
| `BM-03` | `B-08` |
| `B-02` | `B-S4` |
| `BM-04` | `C-07` |
| `EM-01`–`EM-10` | `D-01`–`D-10` |
| `BM-05`, `BM-06` | `D-11`, `D-12` |
| `EM-S1`–`EM-S3` | `D-S1`–`D-S3` |

Planned: `eval-set-v2.csv` (D8, Sprint 3).
