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
| Sprint | The actions agreed in the Sprint 1 retrospective have been carried out by their owners (course minimum). |
| Sprint | The team has agreed on this Definition of Ready and Done and on the one-sentence sprint goal above (course minimum). |
| Sprint | Every Sprint 2 story is in the Sprint 2 sprint in Jira; each story has a story point estimate agreed with planning poker at the Sprint 2 planning (28/10/2026) and an owner, and each sub-task has an owner and an hour estimate (course minimum; assigned at the start of the sprint, not during it). |
| Sprint | Every team member has access to the course template pages, the stored source text in `data/`, Jira, GitHub and Weights & Biases (the W&B account and its free-tier limits are checked before the first experiment, [Facilities & Resources](03-project-canvas/09-facilities-and-resources.md) row 12). |
| Sprint | The Sprint 1 review comments are recorded for Charter v2 (KAN-89), the risk register and the assumption checks are reviewed, and EUR-Lex is checked for a version newer than 27/07/2026 (KAN-117, KAN-157). |
| Story | The story says who it is for and how it serves that role ("As a …, I want …, so that …"), with the role taken from the ISO/IEC 5339 categories in the [Project Executive Summary](03-project-canvas/01-project-executive-summary.md). |
| Story | Its acceptance criteria are testable (a measured value, or a yes/no check), and the story names its objective or feature, deliverable and milestone. |
| Story | It can be finished in this sprint, and each of its sub-tasks has a "Done when" condition and one owner. |
| Story | What it needs first is done or planned before it in this sprint: the stored source text and its hash (D3) for parsing; the D2 questions and the indexed text (D5) for the baseline measurement (KAN-87); the model and embedding choices in the design document for the baseline. |
| Story | Its test case (input or steps, and the expected result) is written, or a sub-task to write it is in the sprint (KAN-90). |

| Column | Definition of Done |
|---|---|
| Story | Every acceptance criterion is met and checked by a team member other than the owner; all sub-tasks are done; the evidence (commit, file or W&B run) is linked in a Jira comment. |
| Story | Its test case is in the story requirements page next to the story, and its result is recorded. |
| Code / Git | The work is on a branch named with its Jira key; a teammate has read and run the change; it is merged into `main` with `git merge --no-ff`; commit messages and the pull request have the Jira key. |
| Code | An answer shown by the assistant has its question, the answer, the cited provisions with their Article or Annex reference and version date, and any notice in the same conversation view. |
| Code / Git | It runs from `README.md` on a team member's computer: pinned `requirements.txt`, parameters in `config/rag.yaml`, prompts (if any) in `prompts/`, random seeds set; no API keys, debug prints or large generated files in the commit. |
| Experiment | Every experiment has an experiment card in `Markdown Template/12-experiment-cards/` with its parameters, the measured numbers and a link to its public W&B run, and is compared with something concrete (the charter target or an earlier run). |
| Experiment | Evaluation uses the `val` split only; the `test` split, frozen on 11/11/2026, is not used for any tuning. |
| Data | The source file hash matches `data/manifest.csv` before parsing; every chunk has its Article or Annex identifier and the version date; the D2 questions are in `docs/eval/eval-set-v1.csv` with their data card; no personal data is stored (C-10). |
| Documents | The design document has a decision record for every decision taken this sprint, and the SBOM lists every model tried with its version, licence and use. |
| Documents | Every charter page that changed passes its own checklist, and IDs and dates match on all pages and in Jira (Sprint 1 retrospective action). |
| Sprint | Every Sprint 2 deliverable of the course is uploaded to ODTUClass by 14/11/2026 23:59, and the welcome page links to it: Charter v2, story map v2, story requirements with test cases, baseline, Q&A dataset v1 with its data card, corpus datasheet, technical summary with the baseline experiment card, design document, UI mockup, burndown chart, Jira export, retrospective and spike notes. |
| Sprint | The demo (10 minutes or less) is ready for the review on 18/11/2026. |

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
