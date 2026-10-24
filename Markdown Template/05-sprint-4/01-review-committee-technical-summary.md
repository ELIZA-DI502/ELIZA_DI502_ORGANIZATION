# Sprint 4: Review Committee Technical Summary

**Note: this document uses HTML tags to disable rendering of instructions. View the raw file for further details.**

<!--
- Write a new summary each sprint. Save each experiment card as its own file in this folder (E1-baseline.md, E2-..., numbered across the whole project).
- Keep the summary to two pages at most. Link to details rather than repeating them: config/rag.yaml holds only the product configuration, each experiment card records the parameter space it tested, the tested combinations are in W&B, decisions are in the design document, and details are in the experiment cards.
-->

| Team | Sprint | Last updated |
|---|---|---|
|  |  | yyyy-mm-dd |

## 1. Summary

<!-- In 3 to 5 sentences: what you tried this sprint, the main result compared with the baseline and the target, and what you will do next. -->

**Decisions this sprint:** <!-- Links to the decision records in the design document, for example D3, D4. -->

## 2. Metrics

<!-- Fill this in during Sprint 2. Change it later only if a metric changes, and explain why in section 1. Take each target from the charter's success criteria. -->

| Metric | Why it fits | Target |
|---|---|---|
|  |  |  |

## 3. Results

<!--
- Add one row for each experiment, showing its best combination, and link that run in W&B.
- Run every experiment on the same evaluation set. If the set changes, run the baseline again on the new set.
- Run the best combination again n times with different seeds. Report each score as the mean ± std over those repeats, and bold the best value in each column.
- Write "null" for missing or failed outputs, and explain it under the table. Do not record them as 0.
- Leave out deprecated experiments.
- In Sprint 4, add a row for the product configuration in config/rag.yaml.
-->

**Evaluation set:** `docs/eval/eval-set-v?.csv`

| Experiment | Best run (W&B) | Metric 1 | Metric 2 | Repeats (n) |
|---|---|---|---|---|
| Target (charter) | — |  |  | — |
| [E1 Baseline]('/12-experiment-cards/E1-baseline.md') | link |  |  |  |
| [E2 Experiment]('/12-experiment-cards/E2-experiment-name.md') | link |  |  |  |
|  |  |  |  |  |

**Best configuration:** <!-- From Sprint 3 on. Link its W&B run, and say whether config/rag.yaml now uses it. -->

## 4. Story test results

<!-- From Sprint 3 on. Add one row for each story you have built. The tests themselves are in the story requirements. -->

| Story | Result | Note |
|---|---|---|
|  | pass / fail |  |

## Checklist before submitting

- [ ] The summary is two pages or shorter.
- [ ] Every row in Results links to an experiment card. Every card from this sprint either has a row or is marked deprecated.
- [ ] Every decision in section 1 has a record in the design document.
