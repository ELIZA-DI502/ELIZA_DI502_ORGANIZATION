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
| Story | An evaluation question is only taken into D2 if its gold source is in the D3 provision list. |
| Story | Its test case (steps and expected result) is written, or a sub-task to write it is in the sprint; this applies to the 17 current product stories (the seven Sprint 1 stories stay unchanged as records) (KAN-90, KAN-114). |

| Column | Definition of Done |
|---|---|
| Story | Every acceptance criterion is met and checked by a team member other than the owner; all sub-tasks are done; the evidence (commit, file or W&B run) is linked in a Jira comment; the test case is in the story requirements page with its result. |
| Code / Git | The work is on a branch named with its Jira key; a teammate has read and run the change; it is merged into `main` with `git merge --no-ff`; commit messages and the pull request have the Jira key. |
| Code | It runs from `README.md` on a team member's computer: `requirements.txt` with 0 unpinned packages, parameters in `config/rag.yaml`, prompts in `prompts/`, random seeds set; no API keys, debug prints or large generated files in the commit. |
| Code | An answer shown by the assistant has its question, the answer, the cited provisions with Article or Annex reference and version date, and any notice in the same conversation view. |
| Experiment | Every experiment has a card in `Markdown Template/12-experiment-cards/` with its parameters, the corpus version from `data/manifest.csv`, the numbers and a link to its public W&B run, compared with the charter target or an earlier run; evaluation uses the `val` split only, and the `test` split (frozen 11/11/2026) is never used for tuning. |
| Experiment | Recall@5 and the answers without and with retrieval are logged in W&B for every `val` question; the known failures are listed; the alpha has no pass level, so results are reported as analysis. |
| Data (D5) | The source hash matches `data/manifest.csv` before parsing; 100% of the D3 provisions are indexed; 0 chunks lack their Article or Annex identifier; every chunk has the version date; chunking parameters are in `config/rag.yaml`; 20 random chunks are compared word for word with the source and the share corrected by hand is 5% or less (A-05). |
| Data (D2) | Every question is in `docs/eval/eval-set-v1.csv`, checked by a reviewer other than its author, with 0 flags left; every gold source is in the D3 list (a missing provision is added only by a recorded decision on 11/11/2026); `test` is frozen and committed on 11/11/2026; the data card has every section, names the model for each LLM-assisted question and has a decision log written when each decision was made; no personal data is stored (C-10). |
| Documents | The design document has a decision record for every decision this sprint, each RAG stage with its parameters, and the user interface technology (chosen by 11/11/2026); the UI mockup shows the question box, the answer with citations and version date, and the permanent notice; the SBOM lists every model tried with version, licence and use; every spike has its note in `docs/spikes/`. |
| Documents | The technical summary gives the chosen metrics and why, the baseline score, the charter target and the known failures on `val`, and links the baseline experiment card. |
| Documents | Story map v2 shows every story in its release row (Alpha 0.1, Beta 0.5, RC 1.0); every epic has a story requirements page; every product story has a test case. |
| Documents | Charter v2: every Sprint 1 review comment is in the response table (accepted with the change, or not accepted with a reason); the O1 and O3 targets are reviewed once with the alpha results; the feedback on O2 and O4 levels is recorded; Risks has an entry for each Sprint 2 problem and all risks are re-scored after the baseline; every changed page states what is new compared with v1, passes its own checklist, and IDs and dates match on all pages and in Jira. |
| Sprint | Every Sprint 2 deliverable is uploaded to ODTUClass by 14/11/2026 23:59 and linked from the welcome page: Charter v2, story map v2, story requirements with test cases, baseline, Q&A dataset v1 with data card, corpus datasheet, technical summary with baseline experiment card, design document, UI mockup, burndown chart, Jira export, retrospective, spike notes. |
| Sprint | The burndown chart (from Jira) is in the sprint folder, the Jira backlog export is in `docs/backlog/`, and the retrospective has an action and an owner for every "what went bad" row. |
| Sprint | The demo (10 minutes or less) is ready for the review on 18/11/2026; the assigned team's Sprint 2 deliverables are reviewed between 15/11 and 18/11 and the completed review page is copied into the sprint folder. |

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
