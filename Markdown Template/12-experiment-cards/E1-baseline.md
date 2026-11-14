# E1: Baseline

**Note: this document uses HTML tags to disable rendering of instructions. View the raw file for further details.**

<!--
- Save one card per experiment as E<n>-<short-name>.md.
- Runs with the same setup count as one experiment.
- Never move or delete a card. When a later experiment supersedes it, change its status to deprecated.
-->

| Date | Author(s) | Status |
|---|---|---|
| 2026-11-09 | Kaan, Gözde Nur | done |

**Aim:** How well does the retrieval chosen on the `val` questions find the gold provisions of the `val` questions, and what does retrieval add to the answers? Measured: Recall@5, Recall@8 and MRR against `gold_ids` (only questions with `gold_ids`), overall and for each label of the question-writing method, with the number of questions; the answers of the same LLM without and with the retrieved chunks, scored with the [rubric](../../docs/eval/rubric.md). Compared with: the O2 (a) target (at least 80% of in-scope questions cite the expected provision); the alpha has no pass level.
<!-- The question you want to answer, and what you compare against: the baseline or another configuration. -->

**Setup:**

- Evaluation set: [`docs/eval/eval-set-v1-val.csv`](../../docs/eval/eval-set-v1-val.csv), 30 questions, 27 with `gold_ids` (commit `842c692`, KAN-53)
- Corpus: SRC-02 in [`data/manifest.csv`](../../data/manifest.csv), consolidated text of 27/07/2026 (SHA-256 starting `e7184c2b0a8037fb`)
- Configuration: [`config/rag.yaml`](../../config/rag.yaml) at commit `a7d9180` (KAN-99)
- Prompt files: [`prompts/answer.yaml`](../../prompts/answer.yaml)
- W&B: retrieval settings and scores in [run `v7g5hhxh`](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/v7g5hhxh)
<!--
Links only:
- The public W&B sweep or project. W&B records every combination you tested, including the fixed parameters.
- The evaluation set version.
- The prompt files. To change a prompt, add a new file to prompts/ instead of editing the old one.
-->

**Design:**
<!-- The parameter space you tested. Add one row for each parameter you varied. For the baseline, give the single value each main parameter had. Then give the search method (grid, random or Bayesian) and the number of runs. -->

| Parameter | Values or range tested | Best value |
|---|---|---|
| Source text | SRC-02 HTML, CELEX 02024R1689-20260727 (D8) | – |
| Chunking | one chunk per Article paragraph or Annex point; `max_chars` 1,500 (D7) | – |
| Embedding model | `BAAI/bge-m3`, no words removed (D13) | – |
| Vector store | Chroma, cosine distance (D11) | – |
| Retrieval | dense search with BM25 (weighted RRF, dense weight 0.8; stopwords and the LLM jury's words removed for BM25), top-k 8 (D14) | – |
| LLM for the answers | Llama-3.1-8B-Instruct `Q4_K_M` via Ollama, temperature 0, at most 300 answer tokens (D9) | – |

**Search method and runs:** none; one configuration, the baseline. Its settings were chosen on the `val` questions in [`src/embedding.ipynb`](../../src/embedding.ipynb), Part 1 (KAN-99).

**Summary of Results:**
Baseline on the D2 `val` split (30 questions, 27 with `gold_ids`), answers of 12/11/2026 (`docs/eval/answers/val-with-retrieval-chunks.jsonl`), counted with `src/citations.py` (KAN-129):

| Metric | Result | Charter target |
|---|---|---|
| Recall@8 / Recall@5 (27 questions with `gold_ids`) | 0.59 / 0.43 (W&B run `v7g5hhxh`) | no pass level |
| O2 (a) expected provision cited | 19 of 27 = 70% | at least 80% |
| O2 (c) substantive answers with at least one Article/Annex reference | 20 of 20 = 100% | 100% |
| O2 (c) substantive answers with a reference **and** the version date | 0 of 20 = 0% | 100% |
| O2 (c) the same answers with the sources line added (KAN-126, 14/11/2026): reference **and** the version date | 20 of 20 = 100% (`src/sources.py`, commit `72d3e5b`; [`val-with-retrieval-shown.csv`](../../docs/eval/answers/val-with-retrieval-shown.csv), commit `6860e94`) | 100% |
| Answers that end with a fixed sentence (no answer, refusal) | 10 of 30 | – |
| After the citation check (KAN-128) | same results; the 4 removed citations were not gold provisions | – |

The version date is not written by the answer model. Every retrieved chunk carries it (27/07/2026), so `src/sources.py` (KAN-126) adds a sources line after the citation check: each cited provision with the version date of its chunk. On 14/11/2026 it was applied to the saved answers of this run; this is a check of the answer format on the same answers, not a new run. In 15 of the 20 answers every shown citation is at paragraph or point level; citing every provision at that level and showing the sources line in the user interface are in KAN-222 (Sprint 3).

Without retrieval, Claude Haiku 5.5 with the whole consolidated text attached ([`prompts/answer_full_text.yaml`](../../prompts/answer_full_text.yaml), answers of 12/11/2026 in [`val-full-text-claude-haiku-5-5.csv`](../../docs/eval/answers/val-full-text-claude-haiku-5-5.csv)) cites the expected provision for 22 of 27 questions (81%), against 19 of 27 (70%) with retrieval ([`src/rag_vs_no_rag.ipynb`](../../src/rag_vs_no_rag.ipynb), [W&B run `lgogwegq`](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/lgogwegq)). The two sides use different models, so the difference shows the model and the retrieval together, not the retrieval alone.

Failure causes of the 8 `val` questions (of 27 with `gold_ids`) where the expected provision is not cited (O2 (a)):

| Failure cause | Count | % of failures |
|---|---|---|
| Retrieval: no gold provision among the 8 chunks (B-06, C-05, D-10) | 3 | 38% |
| Answer model: a gold provision was retrieved, but the answer is the fixed sentence "The provided text does not answer this question" (B-S4, D-02, D-03) | 3 | 38% |
| Answer model: a gold provision was retrieved, but the answer cites another provision or another point (C-03 cites Article 49(2) and 6(4) instead of Article 11(1); C-06 cites Article 2(1)(c) instead of Article 2(1)) | 2 | 25% |
| **Total** | **8** | **100%** |

Other known failures on `val`, not counted above: the version date is missing in 20 of 20 substantive raw answers (added by the sources line, KAN-126); A-01 and D-12 are cut off at 300 answer tokens; B-07 accepts its false premise; the refusals of B-S1 and C-S3 name no provision, and B-S4 (legal decision) shows no provision, which the [rubric](../../docs/eval/rubric.md) asks for. Some answers add a provision that is not among their chunks (for example Article 6(2) in A-05); the citation check removes these 4 citations (KAN-128).

**Discussion and Conclusion:**
<!-- What the numbers mean and what you will do next. Link the decision they led to (D?), if any. -->

Retrieval is not the weak part: a gold provision is among the 8 chunks for 24 of the 27 questions, which supports keeping 8 chunks ([D14](../11-system-architecture-design-document.md#d14-retrieval-dense-search-with-some-bm25-top-8-chunks-revises-d12)) and bge-m3 ([D13](../11-system-architecture-design-document.md#d13-embedding-model-bge-m3-supersedes-d10)). Recall@8 is 0.59 because many questions have several gold provisions and the chunks often hold only some of them. The answer model is the weak part: 5 of the 8 misses had a gold provision in its chunks, and it gives the fixed "does not answer" sentence for 10 of the 30 questions (33%). With 70%, the baseline is below the O2 (a) target of 80%; the alpha has no pass level, so this is an analysis result.

Next (Sprint 3), each change measured against this card on the same `val` questions: the answer step first (prompt and the fixed-sentence rule, more answer tokens, input and output checks for the safety questions, KAN-2), then the three retrieval misses. The answer model ([D9](../11-system-architecture-design-document.md#d9-llm-llama-31-8b-instruct-with-phi-4-mini-instruct-as-fallback)) is compared again only if these changes do not close the gap.
