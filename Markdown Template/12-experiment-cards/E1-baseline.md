# E1: Baseline

**Note: this document uses HTML tags to disable rendering of instructions. View the raw file for further details.**

<!--
- Save one card per experiment as E<n>-<short-name>.md.
- Runs with the same setup count as one experiment.
- Never move or delete a card. When a later experiment supersedes it, change its status to deprecated.
-->

| Date | Author(s) | Status |
|---|---|---|
| 2026-11-09 | Kaan, Gözde Nur | in progress |

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
<!-- The main scores go in the results table of the technical summary. Put the breakdown here: scores by question type, and failures by cause. -->

| Failure cause | Count | % of failures |
|---|---|---|
|  |  |  |

**Discussion and Conclusion:**
<!-- What the numbers mean and what you will do next. Link the decision they led to (D?), if any. -->
