# E2: Answer prompt rules

**Note: this document uses HTML tags to disable rendering of instructions. View the raw file for further details.**

<!--
- Save one card per experiment as E<n>-<short-name>.md.
- Runs with the same setup count as one experiment.
- Never move or delete a card. When a later experiment supersedes it, change its status to deprecated.
-->

| Date | Author(s) | Status |
|---|---|---|
| 2026-11-26 | Gözde Nur Özdemir (runs, rules of PR #110: KAN-146, KAN-147, KAN-151, KAN-152); Aliye Yeşim Yaman (rules of PR #108: KAN-133, KAN-134, KAN-143, KAN-144) | completed |

**Aim:** Does the Sprint 3 answer prompt improve the answers of E1 on the same `val` questions, with the search unchanged? The prompt adds the answer template and the rules for insufficient evidence (PR #108) and the rules for legal decisions, requests to evade the rules, instructions inside the question and condition questions (PR #110). Compared with E1, counted with the rule of KAN-236: O2 (a) on the 21 in-scope `val` questions without the follow-ups (E1: 17/21 = 81%). A citation counts if it is the gold provision, a broader one or a more detailed one (Article 2(1)(c) for Article 2(1)), as in `src/evaluation.ipynb`.
<!-- The question you want to answer, and what you compare against: the baseline or another configuration. -->

**Setup:**

- Evaluation set: [`docs/eval/eval-set-v1.csv`](../../docs/eval/eval-set-v1.csv), the 30 `val` questions of E1; `test` is not used. Each run also answers the 6 questions of the story tests of PR #108 and the 6 of KAN-2 (TC-2.1 to TC-2.6).
- Configuration: [`config/rag.yaml`](../../config/rag.yaml) at commit `555a92c`, unchanged from E1 (search of D14, 8 chunks, Llama-3.1-8B-Instruct `Q4_K_M` with Ollama 0.40.15, temperature 0, seed 42, at most 300 answer tokens)
- Prompt file: [`prompts/answer.yaml`](../../prompts/answer.yaml); the version of each run is given by its commit or file below
- Notebook: [`src/prompt_check.ipynb`](../../src/prompt_check.ipynb) (answers, checks, reading of the rules of PR #110, charts); charts in [`docs/eval/prompt-check-results.pdf`](../../docs/eval/prompt-check-results.pdf)
- Answers: [`docs/eval/answers/`](../../docs/eval/answers/), `prompt-check-v1-k8-val.jsonl` to `prompt-check-v4-k8-val.jsonl`
- W&B: v1 [`tairu8re`](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/tairu8re), v2 [`51cozth5`](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/51cozth5), v3 [`mlq6288t`](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/mlq6288t), v4 [`31yapteu`](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/31yapteu) (final run, with the charts and the PDF; the same answers as runs [`6tkhqd29`](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/6tkhqd29) and [`152m29zv`](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/152m29zv))
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
| Answer prompt (`prompts/answer.yaml`) | E1 prompt; v1 (commit `07e6e39`): rules of PR #108 and the four rules of PR #110; v2 (commit `6cd96c1`): examples of legal-decision questions, a fixed legal-team sentence, a fixed form for the refusal; v3 (`prompt-check-v3-prompt.yaml`): more rules (legal-team sentence only for legal decisions, a fixed form for each condition line); v4 (commit `b5140a0`): v2 with three small fixes | v4 |

All other settings are those of E1.

**Search method and runs:** manual, one change at a time: each version was written from the failures of the run before, read, and kept or dropped. 4 runs on the Colab T4 GPU on 25/11/2026, 42 questions each; v4 was run three times with the same 42 answers (only the times differed). A fifth version (the rules of PR #110 placed after the fixed-sentence rules) was tried once on 26/11/2026 and dropped: one more verdict and 13 answers cut off at 300 tokens instead of 8.

**Summary of Results:**
<!-- The main scores go in the results table of the technical summary. Put the breakdown here: scores by question type, and failures by cause. -->

30 `val` questions, the answer as it is shown (citation check of KAN-128), counted as in [`src/evaluation.ipynb`](../../src/evaluation.ipynb):

| Run | O2 (a), 21 in-scope without follow-ups (target ≥ 80%) | Only the fixed sentence "The provided text does not answer this question." | Verdict found by the verdict check | Hedged verdict ("might", "likely") |
|---|---|---|---|---|
| E1 | 17/21 = 81% | 10/30 | 2 | 3 |
| v1 | 18/21 = 86% | 2/30 | 4 | 0 |
| v2 | 20/21 = 95% | 3/30 | 3 | 1 |
| v3 | 18/21 = 86% | 3/30 | 0 | 2 |
| **v4** | **19/21 = 90%** | **3/30** | **1** | **1** |

Counted without separating the questions (every `val` question with `gold_ids`, 29 questions), O2 (a) goes from 20/29 = 69% (E1) to 25/29 = 86% (v4), so the improvement does not come from the counting rule (KAN-236).

With v4, 8 of the 42 answers reach the limit of 300 answer tokens (none in E1), and the median answer has 115 words (85 in E1). The times were measured on the GPU and are not compared with E1, whose time was measured on a CPU with `src/answer_time.py` ([`docs/eval/answer-time.md`](../../docs/eval/answer-time.md)).

Rules of PR #110 after reading (v4, 12 questions, section 5 of the notebook): 8 pass. Legal decision 3/4 (B-S4 names no provision), request to evade the rules 2/3 (TC-2.4 names a provision that does not fit), instruction inside the question 0/1 (TC-2.5 refuses instead of answering as a legal decision), condition question 3/4 (B-01 hedged verdict). The story tests of PR #108 are read in section 5b by their author.

Failure causes of the 2 O2 (a) misses of v4 (E1 had 4):

| Failure cause | Count | % of failures |
|---|---|---|
| Retrieval: no gold provision among the 8 chunks (C-05) | 1 | 50% |
| Answer model: a gold provision was retrieved, but the answer cites another provision (D-03 cites Article 2(3) and 2(12) instead of Article 2(1) and Article 3, point (3)) | 1 | 50% |
| **Total** | **2** | **100%** |

The 3 answers with only the fixed sentence are B-S2 (out of scope), B-S3 (insufficient evidence, where it is expected) and B-S4 (legal decision, where the provisions should be explained); D-02, D-03 and D-07, refused in E1 with a gold provision among their chunks, are now answered. Follow-ups (reported apart, KAN-228): 3 of 4 (E1: 2 of 4); D-10 has no gold provision among the chunks.

**Discussion and Conclusion:**
<!-- What the numbers mean and what you will do next. Link the decision they led to (D?), if any. -->

The prompt is the first measured improvement over the baseline: O2 (a) goes from 17/21 to 19/21 (81% to 90%; E1 already met the target of 80%), and the fixed sentence falls from 10 to 3 answers. With 21 questions, one question changes O2 (a) by about 5 percentage points, so the differences between v1, v2 and v4 are within one or two questions. v4 was chosen over v2, which had the highest O2 (a), because it gives fewer verdicts and fewer legal-team sentences before ordinary answers (5 against 10 of the 30 `val` answers).

Each version that fixed one rule moved another: the 8B answer model does not follow every rule at the same time. Known failures that are not fixed by the prompt: B-S4 explains no provision (KAN-147); TC-2.5 refuses instead of answering as a legal decision (KAN-151; the input check of KAN-150 stops such instructions before the model); B-01 gives a hedged verdict that the verdict check of the service does not find; A-05 has a verdict sentence that the output check removes. O4 (a) is therefore not yet 0.

Next: prompt v4 is the prompt of the next experiment, E3 (number of chunks, 8, 10 and 12), whose reference run at 8 chunks is v4. The verdict patterns of the output check and the answer LLM (Sprint 4) are the places to remove the remaining verdicts.
