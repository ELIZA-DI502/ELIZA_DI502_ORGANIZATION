# E3: Number of chunks with the Sprint 3 prompt

**Note: this document uses HTML tags to disable rendering of instructions. View the raw file for further details.**

<!--
- Save one card per experiment as E<n>-<short-name>.md.
- Runs with the same setup count as one experiment.
- Never move or delete a card. When a later experiment supersedes it, change its status to deprecated.
-->

| Date | Author(s) | Status |
|---|---|---|
| 2026-11-27 | Gözde Nur Özdemir | completed |

**Aim:** In Sprint 2, k = 8 was chosen by Recall@k only; more than 8 chunks were never tried with answers. With prompt v4 (E2) and the search of E4, does a larger k give better answers? Compared with k = 8: O2 (a) on the 21 in-scope `val` questions (KAN-236), verdict sentences (O4 (a), target 0), wrong dates (O2 (d)) and answer time.
<!-- The question you want to answer, and what you compare against: the baseline or another configuration. -->

**Setup:**

- Evaluation set: [`docs/eval/eval-set-v1.csv`](../../docs/eval/eval-set-v1.csv), the 30 `val` questions; `test` is not used.
- Configuration: the search of E4 (bge-m3, dense weight 0.8, BM25 without stopwords and jury words, legal words kept); Llama-3.1-8B-Instruct `Q4_K_M` with Ollama 0.40.15, temperature 0, seed 42, at most 300 answer tokens, context window 4,096
- Prompt file: [`prompts/answer.yaml`](../../prompts/answer.yaml) at commit `b5140a0` (prompt v4, E2)
- Notebook: [`src/search_and_k.ipynb`](../../src/search_and_k.ipynb), Part 2; charts in [`docs/eval/e3-top-k-results.pdf`](../../docs/eval/e3-top-k-results.pdf)
- Answers: [`docs/eval/answers/`](../../docs/eval/answers/), `e3-k8-val.jsonl`, `e3-k10-val.jsonl`, `e3-k16-val.jsonl`
- W&B: ranks [`qx2rgzus`](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/qx2rgzus), k = 8 [`zxrho7cs`](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/zxrho7cs), k = 10 [`ih4q72rv`](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/ih4q72rv), k = 16 [`5ce22zts`](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/5ce22zts) (group `E3-E4-search-and-k`)
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
| Number of chunks k | Recall@k for k = 5 to 20; answers for k = 8, 10 and 16 | 10 |

**Search method and runs:** first the search alone: the rank of every gold provision up to 20. Only the k values that bring a missing gold provision in were answered: k = 10 (B-06, rank 9) and k = 16 (D-10, rank 15). The rule was written before the run: a larger k replaces 8 only if it cites the expected provision for at least one more question, gives no more verdicts, is at most 1.5 times slower and fits the context window. Six runs on the Colab T4 GPU on 26–27/11/2026 while the search of E4 was being settled; the two runs with its final search gave the same 90 answers, word for word, and k = 10 was at least as good as k = 8 in all six.

**Summary of Results:**
<!-- The main scores go in the results table of the technical summary. Put the breakdown here: scores by question type, and failures by cause. -->

| k | O2 (a) | Verdict sentences | Wrong dates | Follow-ups cited | Median time (GPU) | Largest prompt |
|---|---|---|---|---|---|---|
| 8 | 20/21 = 95% | 2 | 1 | 3/4 | 7.6 s | 2,520 tokens |
| **10** | **20/21 = 95%** | **0** | **0** | 2/4 | 7.4 s | 2,802 tokens |
| 16 | 19/21 = 90% | 4 | 0 | 3/4 | 9.0 s | 3,325 tokens |

Reading the answers that changed: k = 10 is better on A-05 (no verdict), B-06 (Article 113 comes in, the date is right) and B-S4 (the provisions are explained after the legal-team sentence), and worse on C-03 (another provision) and D-04 (an extra legal-team sentence).

| Failure cause (k = 10) | Count | % of failures |
|---|---|---|
| Search: gold provision not in the first 20 (C-05) | 1 | 33% |
| Search: gold provision at rank 15 (D-10, follow-up) | 1 | 33% |
| Answer model: gold provision in the chunks, another one cited (C-03, follow-up) | 1 | 33% |
| **Total** | **3** | **100%** |

**Discussion and Conclusion:**
<!-- What the numbers mean and what you will do next. Link the decision they led to (D?), if any. -->

By the rule alone k stays 8, because k = 10 ties on O2 (a). We choose **k = 10** and say so openly: in every run it cites at least as many expected provisions as k = 8, and it is the only setting with no verdict sentence (the charter target of O4 (a)) and no wrong date, at about the same time. Its cost is one follow-up.

k = 16 brings 14 more gold provisions, but most go to questions that already cite one, so O2 (a) cannot rise; with more chunks the model mixes up provisions (4 verdict sentences, D-04 left without an answer). More chunks help only when the missing provision is just below the cut, as for B-06 and D-03 at rank 9. C-05 cannot be fixed by k: the question says *webcam* and *stressed*, the provision says *infer emotions*.

A one-question difference is within the noise of 21 questions. Before `config/rag.yaml` changes to k = 10, the choice is checked on the frozen D8 `val` split, the CPU time of k = 10 is measured on the pilot computer (KAN-163, O1: median at most 60 s), and the configuration is re-run with three seeds (KAN-179).
