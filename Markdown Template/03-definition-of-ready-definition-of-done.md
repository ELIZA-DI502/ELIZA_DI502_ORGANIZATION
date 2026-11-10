# Definiton of Ready Definiton of Done

For each sprint, please check the full list of the definition of ready and the definition of done.

Add rows if needed.

**How ELIZA uses this page.** The **Column** is the level the item checks: the **sprint** as a whole, a **story** (with its sub-tasks), or a kind of work inside a story (**code**, **experiment**, **data**, **documents**). A story moves into the sprint only when every Ready item applies to it, and moves to *Done* in Jira only when every Done item for its kind of work is met; the evidence (commit, file or W&B run) is linked in a Jira comment. Story points are on the stories and hours on the sub-tasks (Model A of the course's [Jira sync guide](../docs/JIRA_SYNC_SETUP.md)). The lists are agreed by the whole team before the sprint starts.

## Sprint 1:

Sprint 1 (14/10–28/10/2026) was a discovery sprint without production code (C-07). The team worked with the rules below; they are recorded here at the end of the sprint.

| Column | Definition of Ready |
|---|---|
| Sprint | The sprint goal is written in Jira: know what to build and why, and prepare everything needed to measure it. |
| Sprint | Every team member has access to the course template pages, the source text on EUR-Lex, Jira and GitHub. |
| Story | The story is in Jira with an epic, acceptance criteria that can be checked with yes or no, and a traceability section (deliverable and milestone). |
| Story | The story fits in the sprint, and its story points are agreed by the team with planning poker. |
| Story | Each charter page has one owner and a Jira sub-task. |

| Column | Definition of Done |
|---|---|
| Documents | The page passes its own "Checklist before submitting" in the course template. |
| Documents | IDs (O, D, M, A, C, R) and dates match on all charter pages and in Jira. |
| Documents | Each page is reviewed by a team member other than its author; the review comments are resolved, and the review is noted on the page's Jira sub-task. |
| Code / Git | The change is in the repository with the Jira key in the branch or commit message. |
| Story | The work is linked from the Sprint 1 page and uploaded to ODTUClass by 27/10/2026. |
| Sprint | Charter v1 is presented at the Sprint 1 review on 28/10/2026; the reviewers' feedback is recorded on the Sprint 1 review page and in Jira (KAN-89, for Charter v2), and the approval of Charter v1 (M1) is noted in Jira. |

## Sprint 2:

**Sprint 2 (28/10–18/11/2026) · Alpha 0.1 (baseline).** Sprint goal (Jira): *Q&A dataset v1 (D2) and the indexed source text (D5) are ready, the baseline retrieval is measured with Recall@5 against the charter target and gives answers with Article/Annex citations and the version date, and Project Charter v2 (D7) is ready for the Sprint 2 review on 18/11/2026.*

The rows marked *Data (question set)* and *Experiment (baseline)*, the row on design decisions and experiment cards, and the checklist below were added on 08/11/2026, after the instructor's feedback on 04/11/2026 and the Sprint 1 review (comment 6). The questions written before that date are checked against them as well.

| Column | Definition of Ready |
|---|---|
| Sprint | The actions agreed in the Sprint 1 retrospective have been carried out by their owners; the team has agreed on this Definition of Ready and Done and on the sprint goal above (course minimum). |
| Sprint | Every Sprint 2 story is in the Sprint 2 sprint in Jira with an owner and a story point estimate agreed with planning poker; points are on the stories, not on the sub-tasks; the backlog is ordered by priority; each sub-task has an owner and an hour estimate. |
| Sprint | Every team member has access to the course template pages, the stored source text in `data/`, Jira, GitHub and Weights & Biases (the W&B account and its free-tier limits are checked before the first experiment). |
| Sprint | The Sprint 1 review comments are recorded for Charter v2 (KAN-89), the risk register and the assumption checks are reviewed, and EUR-Lex is checked for a version newer than 27/07/2026 (KAN-117, KAN-157). |
| Sprint | The halfway checks are planned: the user interface technology is chosen and the metrics with their targets are drafted by 11/11/2026. |
| Story | The story says who it is for ("As a …, I want …, so that …"), with the role from the ISO/IEC 5339 categories; its acceptance criteria are testable (a measured value or a yes/no check), and it names its objective or feature, deliverable and milestone. |
| Story | It can be finished in this sprint, and each of its sub-tasks has a "Done when" condition and one owner. |
| Story | What it needs first is done or planned before it: the source text and its hash (D3) for parsing; the D2 questions and the indexed text (D5) for the baseline (KAN-87); the ADRs for model, embedding, vector store and user interface before the baseline is built. |
| Story | An evaluation question is only taken into D2 if its gold source is in the D3 provision list (a question with no gold source is allowed only where the question-writing method allows it). |
| Data (question set) | Before new questions are written, the team has agreed on how they are written and how many of each kind are needed: the [question-writing method](../docs/eval/question-writing-method.md), based on the course lecture *Building test datasets for RAG* (04/11/2026), with its target counts and the author of each use case. |
| Data (question set) | Each author knows the columns to fill in `docs/eval/eval-set-v1.csv`, including the labels of the method (`user`, `premise`, `hops`, `challenge`, `gold_ids`). |
| Experiment (baseline) | The `val` split of D2 is fixed before the baseline is run. |
| Experiment (baseline) | The baseline experiment card states, before the run, what is measured (Recall@8 and Recall@5 against `gold_ids` on `val`, and the answers without and with retrieval), the settings in `config/rag.yaml`, and what the result is compared with (the charter target). |
| Story | Its test case (steps and expected result) is written, or a sub-task to write it is in the sprint; this applies to the 17 current product stories (the seven Sprint 1 stories stay unchanged as records) (KAN-90, KAN-114). |

| Column | Definition of Done |
|---|---|
| Story | Every acceptance criterion is met and checked by a team member other than the owner; all sub-tasks are done; the evidence (commit, file or W&B run) is linked in a Jira comment; the test case is in the story requirements page with its result. |
| Code / Git | The work is on a branch named with its Jira key; a teammate has read and run the change; it is merged into `main` with `git merge --no-ff`; commit messages and the pull request have the Jira key. |
| Code | It runs from `README.md` on a team member's computer: `requirements.txt` with 0 unpinned packages, parameters in `config/rag.yaml`, prompts in `prompts/`, random seeds set; no API keys, debug prints or large generated files in the commit. |
| Code | An answer shown by the assistant has its question, the answer, the cited provisions with Article or Annex reference and version date, and any notice in the same conversation view. |
| Experiment | Every experiment has a card in `Markdown Template/12-experiment-cards/` with its parameters, the corpus version from `data/manifest.csv`, the numbers and a link to its public W&B run, compared with the charter target or an earlier run; evaluation uses the `val` split only, and the `test` split (frozen 11/11/2026) is never used for tuning. |
| Experiment | Recall@8 and Recall@5 (for questions with a gold source) and the answers without and with retrieval are logged in W&B for every `val` question; the known failures are listed; the alpha has no pass level, so results are reported as analysis. |
| Experiment | Every evaluation run records, in its W&B run and its experiment card, the commit of the evaluation set, the split it used (`val` or `test`) and its configuration (the commit of `config/rag.yaml`), so that the use of `test` can be checked later (KAN-77, TC-77.1). |
| Experiment (baseline) | The baseline experiment card (E1) reports Recall@8 and Recall@5 on `val` against `gold_ids`, overall and for each value of the method's labels with its number of questions, and the comparison of answers without and with retrieval; Recall@k is computed only for questions with a gold source (non-empty `gold_ids`), and the others are scored with the rubric; if Recall@5 is below the charter target, the gap, its likely causes and the next experiment are written in the card, the technical summary and on the welcome page (KAN-99, KAN-100). |
| Data (D5) | The source hash matches `data/manifest.csv` before parsing; 100% of the D3 provisions are indexed; 0 chunks lack their Article or Annex identifier; every chunk has the version date; chunking parameters are in `config/rag.yaml`; 20 random chunks are compared word for word with the source and the share corrected by hand is 5% or less (A-05). |
| Data (D2) | Every question is in `docs/eval/eval-set-v1.csv`, checked by a reviewer other than its author, with 0 flags left; every gold source is in the D3 list (a missing provision is added only by a recorded decision on 11/11/2026); `test` is frozen and committed on 11/11/2026; the data card has every section, names the model for each LLM-assisted question and has a decision log written when each decision was made; no personal data is stored (C-10). |
| Data (question set) | The question set meets the D2 acceptance criteria in [Deliverables](03-project-canvas/05-deliverables.md) and the target counts of the [question-writing method](../docs/eval/question-writing-method.md); every question has all its columns and labels filled as the method defines them (a column may be empty only where the method allows it). |
| Data (question set) | The reviewer checks each question against the official text: for an in-scope question, its gold source is the right provision and its gold answer is stated in that provision and fully answers the question; for a safety question, its expected behaviour matches the rubric (KAN-50, KAN-51, KAN-52). |
| Data (question set) | Every multi-hop question has been tried with each of its gold sources alone, and with no source; it is relabelled `single` if one source is enough. |
| Data (question set) | The data card says how the questions were written and chosen (the method, the target counts and the actual counts) and how the questions taken from published work were made by their authors (KAN-48, KAN-85). |
| Documents | The design document has a decision record for every decision this sprint, each RAG stage with its parameters, and the user interface technology (chosen by 11/11/2026); the UI mockup shows the question box, the answer with citations and version date, and the permanent notice; the SBOM lists every model tried with version, licence and use; every spike has its note in `docs/spikes/`. |
| Documents | Every design-document decision that rests on an experiment links to its experiment card; a decision taken without an experiment names its evidence (Sprint 1 review, comment 6). |
| Documents | The technical summary gives the chosen metrics and why, the baseline score, the charter target and the known failures on `val`, and links the baseline experiment card. |
| Documents | Story map v2 shows every story in its release row (Alpha 0.1, Beta 0.5, RC 1.0); every epic has a story requirements page; every product story has a test case. |
| Documents | Charter v2: every Sprint 1 review comment is in the response table (accepted with the change, or not accepted with a reason); the O1 and O3 targets are reviewed once with the alpha results; the feedback on O2 and O4 levels is recorded; Risks has an entry for each Sprint 2 problem and all risks are re-scored after the baseline; every changed page states what is new compared with v1, passes its own checklist, and IDs and dates match on all pages and in Jira. |
| Sprint | Every Sprint 2 deliverable is uploaded to ODTUClass by 14/11/2026 23:59 and linked from the welcome page: Charter v2, story map v2, story requirements with test cases, baseline, Q&A dataset v1 with data card, corpus datasheet, technical summary with baseline experiment card, design document, UI mockup, burndown chart, Jira export, retrospective, spike notes. |
| Sprint | The burndown chart (from Jira) is in the sprint folder, the Jira backlog export is in `docs/backlog/`, and the retrospective has an action and an owner for every "what went bad" row. |
| Sprint | The demo (10 minutes or less) is ready for the review on 18/11/2026; the assigned team's Sprint 2 deliverables are reviewed between 15/11 and 18/11 and the completed review page is copied into the sprint folder. |

### Checklist before closing Sprint 2

Ticked by the team before the upload on 14/11/2026 and again before the review on 18/11/2026. Every item checks a Definition of Done row above. An unticked item is not Done: it is fixed before the upload, or the story it belongs to stays open in Jira and the item is written on the welcome page with the reason and the plan to finish it.

**Stories**

- [ ] Every acceptance criterion of every Sprint 2 story is met and checked by a team member other than the owner
- [ ] Every sub-task is done, and the evidence (commit, file or W&B run) is linked in a Jira comment
- [ ] Every current product story has its test case on its story requirements page
- [ ] Every story closed in Sprint 2 has its test run and its result recorded

**Code and Git**

- [ ] Every change is on a branch named with its Jira key, and commits and pull requests have the Jira key
- [ ] Every change was read and run by a teammate and merged into `main` with `git merge --no-ff`
- [ ] The code runs from `README.md` on a team member's computer
- [ ] `requirements.txt` has 0 unpinned packages, the parameters are in `config/rag.yaml`, the prompts are in `prompts/` and random seeds are set
- [ ] No API keys, debug prints or large generated files are in the repository
- [ ] An answer shows the question, the answer, the cited provisions with their reference and version date, and any notice in the same view

**Source text and chunks (D5)**

- [ ] The source hash matches `data/manifest.csv`
- [ ] 100% of the D3 provisions are indexed; 0 chunks lack their Article or Annex identifier; every chunk has the version date
- [ ] The chunking parameters are in `config/rag.yaml`
- [ ] 20 random chunks were compared word for word with the source, and the share corrected by hand is 5% or less (A-05)
- [ ] No personal data is stored (C-10)

**Question set (D2)**

- [ ] The question-writing method and its target counts were agreed before the new questions were written
- [ ] `docs/eval/eval-set-v1.csv` meets the D2 acceptance criteria and the target counts of the method
- [ ] Every row has all its columns filled as the method defines them, including `user`, `premise`, `hops`, `challenge` and `gold_ids`
- [ ] Every gold source is in `data/provision-list.csv`
- [ ] Every question was checked against the official text by a reviewer other than its author, with 0 flags left
- [ ] Every multi-hop question was tried with each gold source alone and with no source
- [ ] The model and prompt used for every LLM-drafted question are recorded
- [ ] At least one third of the questions are in `test`, with at least one question of each safety category, and `test` was frozen and committed on 11/11/2026
- [ ] The data card has every section, the method, the target and actual counts, how the published questions were made, and its decision log

**Baseline experiment**

- [ ] The `val` split was fixed before the baseline was run
- [ ] Recall@8 and Recall@5 (for questions with a gold source) and the answers without and with retrieval are logged in W&B for every `val` question
- [ ] Recall@8 and Recall@5 are reported overall and for each label of the method, with the number of questions in each, only for questions with non-empty `gold_ids`
- [ ] The result is compared with the charter target; the known failures, and any gap with its next experiment, are written down
- [ ] The experiment card (E1) has the parameters, the corpus version, the numbers and the public W&B run
- [ ] The W&B run and the experiment card record the commit of the evaluation set, the split used (`val` or `test`) and the commit of `config/rag.yaml`
- [ ] `test` was not used for any choice

**Documents**

- [ ] The design document has a decision record for every Sprint 2 decision, each RAG stage with its parameters, and the user interface technology
- [ ] Every design-document decision based on an experiment links to its experiment card, and every other decision names its evidence
- [ ] The UI mockup shows the question box, the answer with citations and version date, and the permanent notice
- [ ] The SBOM lists every model tried with its version, licence and use; every spike has its note in `docs/spikes/`
- [ ] The technical summary gives the chosen metrics and why, the baseline score, the charter target and the known failures, and links the baseline experiment card
- [ ] Story map v2, the story requirements page of every epic and the test case of every product story are published
- [ ] Charter v2 has the Sprint 1 review response table, the reviewed targets and re-scored risks; every changed page states what is new and passes its own checklist

**Sprint**

- [ ] Every Sprint 2 deliverable is uploaded to ODTUClass by 14/11/2026 23:59 and linked from the welcome page
- [ ] The burndown chart is in the sprint folder, the Jira export is in `docs/backlog/`, and every "what went bad" row of the retrospective has an action and an owner
- [ ] The demo (10 minutes or less) is ready for the review on 18/11/2026
- [ ] The assigned team's deliverables were reviewed between 15/11 and 18/11, and the completed review page is in the sprint folder

## Sprint 3:

To be agreed at the start of Sprint 3 (18/11/2026), after the Sprint 2 retrospective and review (KAN-187).

| Column | Definition of Ready |
|---|---|
|   |   |

| Column | Definition of Done |
|---|---|
|   |   |

## Sprint 4:

To be agreed at the start of Sprint 4 (09/12/2026), after the Sprint 3 retrospective and review (KAN-213).

| Column | Definition of Ready |
|---|---|
|   |   |

| Column | Definition of Done |
|---|---|
|   |   |
