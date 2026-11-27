# E4: Search settings checked again

**Note: this document uses HTML tags to disable rendering of instructions. View the raw file for further details.**

<!--
- Save one card per experiment as E<n>-<short-name>.md.
- Runs with the same setup count as one experiment.
- Never move or delete a card. When a later experiment supersedes it, change its status to deprecated.
-->

| Date | Author(s) | Status |
|---|---|---|
| 2026-11-27 | Gözde Nur Özdemir | completed |

**Aim:** In Sprint 2 the search was chosen on BM25 alone and at 8 chunks (E1a, E1b). Is it still the best on the current `val` questions? And does BM25 lose provisions because it removes words with legal meaning (*must, only, may, except, under, first, shall*; risk 2 of the Sprint 2 review)? Compared with the Sprint 2 search: bge-m3, dense weight 0.8, BM25 without stopwords and the jury's words (Recall@8 0.59 in E1).
<!-- The question you want to answer, and what you compare against: the baseline or another configuration. -->

**Setup:**

- Evaluation set: [`docs/eval/eval-set-v1.csv`](../../docs/eval/eval-set-v1.csv), the 29 `val` questions with gold provisions (27 in Sprint 2; B-S1 and C-S3 got gold provisions in the D2 review). `test` is not used.
- Configuration: [`config/rag.yaml`](../../config/rag.yaml) (the Sprint 2 search); the jury's words are those of Sprint 2 (10/11/2026), not asked again.
- Notebook: [`src/search_and_k.ipynb`](../../src/search_and_k.ipynb), Part 1
- Tables: [`docs/eval/answers/`](../../docs/eval/answers/), `e4-*.csv`
- W&B: [`fzohutgx`](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/fzohutgx) (group `E3-E4-search-and-k`)
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
| Embedding model | all-MiniLM-L6-v2, bge-small, bge-base, bge-large, bge-m3 | bge-m3 |
| Dense weight in weighted RRF | 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 | 0.8 |
| BM25 word list (BM25 alone, as in Sprint 2) | none, jury, stopwords, stopwords + jury, frequent words, stopwords + frequent words | stopwords + jury |
| BM25 word list inside the hybrid search | the same 6 lists; each list that removes legal words also with them kept (11 versions) | stopwords + jury, legal words kept |
| Words removed before embedding | none and the same 5 lists | none |

**Search method and runs:** grid search, scored by Recall@8, then MRR (the Sprint 2 rules). A setting changes only if it is better on one and worse on neither; a tie keeps the Sprint 2 setting. One run on the Colab T4 GPU on 27/11/2026 (the search is deterministic).

**Summary of Results:**
<!-- The main scores go in the results table of the technical summary. Put the breakdown here: scores by question type, and failures by cause. -->

| Search | Recall@8 | MRR |
|---|---|---|
| BM25 only, no word removed | 0.37 | 0.43 |
| BM25 only, stopwords + jury (Sprint 2) | 0.47 | 0.52 |
| bge-m3 only | 0.55 | – |
| Hybrid, Sprint 2 setting | 0.61 | 0.62 |
| **Hybrid, legal words kept in BM25** | **0.62** | **0.62** |
| Hybrid, no word removed from BM25 | 0.48 | 0.58 |

bge-m3 with weight 0.8 is still the best model (bge-large 0.59 at weight 0.9, bge-base 0.57). Removing words before embedding makes bge-m3 worse (0.45–0.55), as in Sprint 2. Only 9 `val` questions use a legal word (*only* 6, *under* 2, *must* 1).

Where the 132 gold provisions of the 29 questions are ranked with the chosen search:

| Failure cause | Count | % of failures |
|---|---|---|
| Ranked 9–10 (more chunks can bring it in) | 3 | 3% |
| Ranked 11–20 | 19 | 22% |
| Not in the first 20 | 65 | 75% |
| **Missed in the first 8** | **87** | **100%** |

58 of the 87 come from four questions that ask for a whole set of requirements (D-08, D-09, D-05, B-05).

Question by question, Recall@8 is 0 for C-05, D-10 and B-06 and 0.10–0.18 for the four questions above. The first gold provision is at rank 1 for 14 of the 29 questions; it is lowest for C-05 (not found), D-10 (15), B-06 (9), C-06 (8), D-03 and C-02 (7).

**Discussion and Conclusion:**
<!-- What the numbers mean and what you will do next. Link the decision they led to (D?), if any. -->

The Sprint 2 search holds: same model, weight and word lists. The reviewer was right that the legal words matter a little: keeping them in BM25 finds one more gold provision, so they should stay in BM25. The gain is small because few questions use them; the frozen D8 `val` split will show more.

Most missed provisions are far down the list, in questions that need many provisions. More chunks cannot fix this (see E3); a search that splits such a question into smaller ones (query decomposition) is the next thing to try, in Sprint 4.

`config/rag.yaml` is not changed here: keeping the legal words goes into it together with k = 10 (E3), after the CPU time is measured (KAN-163) and the best configuration is re-run (KAN-179).
