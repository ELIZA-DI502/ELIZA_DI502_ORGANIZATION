# Sprint 2: Review Committee Technical Summary

**Note: this document uses HTML tags to disable rendering of instructions. View the raw file for further details.**

**Suggestion: You can use tools like [marp](https://github.com/marp-team/marp-cli) to convert this to a presentation for your end-of-sprint demo.**

<!--
- This is a document where you will summarize experiments ran this sprint, their metrics, and results. Experiments are recorded in detail in experiment cards in the Markdown Template/12-experiment-cards/ folder. You should only link the relevant experiment here and report it's main results in here.
- Keep the summary to two pages at most. Link to details rather than repeating them: config/rag.yaml holds only the product configuration, each experiment card records the parameter space it tested, the tested combinations are in W&B, and decisions are in the design document.
-->

| Team | Sprint | Last updated |
|---|---|---|
| ELIZA | 2 | 2026-11-08 |

## 1. Summary

<!-- In 3 to 5 sentences: what you tried this sprint, the main result compared with the baseline and the target, and what you will do next. -->

**Decisions this sprint:** <!-- Links to the decision records in the design document, for example D3, D4. -->

## 2. Metrics

<!-- Fill this in during Sprint 2. Change it later only if a metric changes, and explain why in section 1. Take each target from the charter's success criteria. -->

Drafted on 08/11/2026 for the halfway check (KAN-101). The targets are the success criteria O2 and O4 of the [Executive Summary](../03-project-canvas/01-project-executive-summary.md). The alpha has no pass level ([Milestones](../03-project-canvas/02-milestones.md), M4), so the baseline results are reported against these targets as analysis; the levels apply from the beta on the frozen D8 `val` split. How an answer is judged is defined in the [evaluation rubric](../../docs/eval/rubric.md).

| Metric | Why it fits | Target |
|---|---|---|
| **Recall@5** (provision level, against `gold_ids`) | The LLM sees only the top 5 passages, so a provision missing there cannot be cited. Computed from the gold IDs, without an LLM judge, overall and per slice of the [question-writing method](../../docs/eval/question-writing-method.md) (for example multi-hop) | No pass level (analysis, D6 criterion 5); read against O2 (a) |
| **MRR** (provision level) | Shows whether the first gold provision is near the top of the list; used to compare ranking settings in Sprint 3 (D12) | No pass level (analysis) |
| **Expected provision cited** (O2 (a)) | The user's need is to find the provision that applies to their use case | ≥ 80% of in-scope questions |
| **Fully supported answers** (O2 (b)), with faithfulness behind it | An answer can cite the right provision and still add claims that are not in it; checked by a reviewer with the rubric | ≥ 75% of in-scope answers; faithfulness: no target |
| **Citation with version date** (O2 (c)) and **citation match** | Every claim must be checkable in the cited text of the 27/07/2026 version; a cited ID that was not retrieved points to the model's memory | 100% of substantive answers; 100% of citations match a retrieved chunk (D6 criterion 4) |
| **Application date from the 27/07/2026 text** (O2 (d)) | Regulation (EU) 2026/1744 moved the high-risk dates; a model that answers from memory gives the 2024 dates | At most 1 application-date question per split with a wrong date |
| **Answers without vs with retrieval** | Shows what retrieval adds over the model's own knowledge of the Act | No level yet; decided in Charter v2 from the alpha results (KAN-109) |
| **Safety responses** (O4 (a)–(c)), scored with the rubric | The assistant gives information, not legal decisions (C-08), and must say when it cannot answer | 0 answers with a verdict; 100% of legal-decision questions and ≥ 80% of the out-of-scope, insufficient-evidence and adversarial questions get the expected response |

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

**Evaluation set:** `docs/eval/eval-set-v?.csv`

| Experiment | Sprint | Best run (W&B) | Metric 1 | Metric 2 | Repeats (n) |
|---|---|---|---|---|---|
| Target (charter) | — | — |  |  | — |
| [E1 Baseline](../12-experiment-cards/E1-baseline.md) | 2 | link |  |  |  |
| [E2 short-name](../12-experiment-cards/E2-short-name.md) |  | link |  |  |  |

**Best configuration:** <!-- From Sprint 3 on. Link its W&B run, and say whether config/rag.yaml now uses it. -->

## 4. User story test results

<!-- From Sprint 3 on. Add one row for each user story you have built. The tests themselves are in the story requirements. -->

| Story | Result | Note |
|---|---|---|
|  | pass / fail |  |

## Checklist before submitting

- [ ] The summary is two pages or shorter.
- [ ] Every row in Results links to an experiment card. Every card from this sprint either has a row or is marked deprecated.
- [ ] Every decision in section 1 has a record in the design document.
