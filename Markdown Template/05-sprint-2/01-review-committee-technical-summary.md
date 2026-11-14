# Sprint 2: Review Committee Technical Summary

**Note: this document uses HTML tags to disable rendering of instructions. View the raw file for further details.**

**Suggestion: You can use tools like [marp](https://github.com/marp-team/marp-cli) to convert this to a presentation for your end-of-sprint demo.**

<!--
- This is a document where you will summarize experiments ran this sprint, their metrics, and results. Experiments are recorded in detail in experiment cards in the Markdown Template/12-experiment-cards/ folder. You should only link the relevant experiment here and report it's main results in here.
- Keep the summary to two pages at most. Link to details rather than repeating them: config/rag.yaml holds only the product configuration, each experiment card records the parameter space it tested, the tested combinations are in W&B, and decisions are in the design document.
-->

| Team | Sprint | Last updated |
|---|---|---|
| ELIZA | 2 | 2026-11-14 |

## 1. Summary

<!-- In 3 to 5 sentences: what you tried this sprint, the main result compared with the baseline and the target, and what you will do next. -->

This sprint we built the baseline ([E1](../12-experiment-cards/E1-baseline.md)): the consolidated text of 27/07/2026 split into provision chunks, embedded with bge-m3 and searched with dense search plus some BM25, top 8 chunks (D13, D14), with Llama-3.1-8B writing the answers. On the 27 `val` questions with gold provisions, Recall@8 is 0.59 and Recall@5 0.43, and the answers cite the expected provision for 19 of 27 questions (70%), **below the O2 (a) target of 80%**; the alpha has no pass level, so this is an analysis result. A gold provision is among the 8 chunks for 24 of the 27 questions, so most misses come from the answer model, which gives the fixed "does not answer" sentence for 10 of the 30 questions. Every substantive answer cites an Article or Annex, and the version date is added by the sources line of the shown answers (20 of 20, KAN-126). In Sprint 3 we improve the answer step first and measure every change against E1 on the same `val` questions.

**Decisions this sprint:** [D1](../11-system-architecture-design-document.md#d1-web-interface-and-backend-react--nodejsexpress) (interface, accepted), [D13](../11-system-architecture-design-document.md#d13-embedding-model-bge-m3-supersedes-d10) (embedding model), [D14](../11-system-architecture-design-document.md#d14-retrieval-dense-search-with-some-bm25-top-8-chunks-revises-d12) (retrieval), [D15](../11-system-architecture-design-document.md#d15-conversation-of-the-current-session-in-the-web-backends-memory-supersedes-d4) (conversation in memory) <!-- Links to the decision records in the design document, for example D3, D4. -->

## 2. Metrics

<!-- Fill this in during Sprint 2. Change it later only if a metric changes, and explain why in section 1. Take each target from the charter's success criteria. -->

Targets from O2 and O4 of the [Executive Summary](../03-project-canvas/01-project-executive-summary.md). The alpha has no pass level (M4), so the baseline is reported against them as analysis. Answers are judged with the [rubric](../../docs/eval/rubric.md).

| Metric | Why it fits | Target |
|---|---|---|
| **Recall@5 and Recall@8** (provision level, against `gold_ids`) | A provision not among the top 8 (D14) cannot be cited; computed from `gold_ids`, per slice | No pass level (analysis, D6 criterion 5); read against O2 (a) |
| **MRR** (provision level) | Shows whether the first gold provision is near the top | No pass level (analysis) |
| **Expected provision cited** (O2 (a)) | The user needs the provision that applies | ≥ 80% of in-scope questions |
| **Fully supported answers** (O2 (b)), with faithfulness behind it | A right citation can still carry unsupported claims | ≥ 75% of in-scope answers; faithfulness: no target |
| **Citation with version date** (O2 (c)) and **citation match** | Every claim must be checkable in the cited text | 100% of substantive answers; 100% of citations match a retrieved chunk (D6 criterion 4) |
| **Application date from the 27/07/2026 text** (O2 (d)) | Regulation (EU) 2026/1744 moved the high-risk dates | At most 1 application-date question per split with a wrong date |
| **Answers without vs with retrieval** | Shows what retrieval adds | No level: kept as an analysis result in Charter v2, because the two sides of the alpha use different models (KAN-109) |
| **Safety responses** (O4 (a)–(c)), scored with the rubric | Information, not legal decisions (C-08) | 0 answers with a verdict; 100% of legal-decision questions and ≥ 80% of the out-of-scope, insufficient-evidence and adversarial questions get the expected response |

## 3. Results

<!--
- Include the baseline, the best experiment from earlier sprints if it is not the baseline, and every experiment run this sprint. In the Sprint column, write the sprint each experiment ran in.
- Each row shows the experiment's best combination. Link that run in W&B.
- Run every row on the same evaluation set. If the set changes, run the baseline and the earlier best again on the new set.
- Run the best combination again n times with different seeds. Report each score as the mean ± std over those repeats, and bold the best value in each column.
- Write "null" for missing or failed outputs, and explain it under the table. Do not record them as 0.
- Leave out deprecated experiments.
- In Sprint 4, add a row for the product configuration in config/rag.yaml.
-->

**Evaluation set:** [`docs/eval/eval-set-v1.csv`](../../docs/eval/eval-set-v1.csv), `val` split ([`eval-set-v1-val.csv`](../../docs/eval/eval-set-v1-val.csv)): 30 questions, 27 with gold provisions. The `test` split is not used until Sprint 4.

| Experiment | Sprint | Best run (W&B) | Recall@8 / Recall@5 | O2 (a) expected provision cited | O2 (c) reference / with version date | Repeats (n) |
|---|---|---|---|---|---|---|
| Target (charter) | — | — | no pass level | ≥ 80% of in-scope questions | 100% / 100% of substantive answers | — |
| [E1 Baseline](../12-experiment-cards/E1-baseline.md) | 2 | [`v7g5hhxh`](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/v7g5hhxh) (retrieval), [`lgogwegq`](https://wandb.ai/gozdenur104-metu-middle-east-technical-university/eliza-rag/runs/lgogwegq) (answers) | 0.59 / 0.43 | 19 of 27 = 70% | 20 of 20 = 100% / 0 of 20 in the raw answers, 20 of 20 with the sources line (KAN-126) | 1 (temperature 0) |

No E2 row: dense and hybrid search were compared in the settings run of E1 ([`src/embedding.ipynb`](../../src/embedding.ipynb), D14), so no separate experiment was run. **Without retrieval** (Claude Haiku 5.5 with the whole consolidated text, the comparison of D6 criterion 5): the expected provision is cited for 22 of 27 questions (81%); the two sides use different models, so the difference is not the effect of retrieval alone.

**Known failures on `val`** (counted in the [E1 card](../12-experiment-cards/E1-baseline.md)): of the 8 questions where the expected provision is not cited, 3 are retrieval misses (B-06, C-05, D-10), 3 get the fixed "does not answer" sentence although a gold provision was retrieved (B-S4, D-02, D-03), and 2 cite another provision or point (C-03, C-06). Also: A-01 and D-12 are cut off at 300 answer tokens; B-07 accepts its false premise; the refusals of B-S1 and C-S3 name no provision.

**Best configuration:** <!-- From Sprint 3 on. Link its W&B run, and say whether config/rag.yaml now uses it. -->

## 4. User story test results

<!-- From Sprint 3 on. Add one row for each user story you have built. The tests themselves are in the story requirements. -->

| Story | Result | Note |
|---|---|---|
|  | pass / fail |  |

## Checklist before submitting

- [x] The summary is two pages or shorter.
- [x] Every row in Results links to an experiment card. Every card from this sprint either has a row or is marked deprecated.
- [x] Every decision in section 1 has a record in the design document.
