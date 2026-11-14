# Sprint 2 Welcome Page

Welcome. This is the main page of Sprint 2 of team **ELIZA**: an information assistant on the EU AI Act for technical teams at EdTech providers ([project overview](../../README.md)).

| Sprint 2 · Alpha 0.1 (baseline) | |
|---|---|
| Dates | 28/10/2026 – 18/11/2026 (upload 14/11/2026, review 18/11/2026) |
| Release | Alpha 0.1: the baseline retrieval and answers, measured on the `val` split |
| Team | Yeşim (Product Owner) · Yaren (Scrum Master) · Kaan and Gözde Nur (Data Scientists) |
| Jira | Project KAN, sprint "KAN Sprint 2": 3 user stories and 6 tasks, 73 story points, 53 sub-tasks |
| Submitted version | Git tag [`sprint-2`](https://github.com/ELIZA-DI502/ELIZA_DI502_ORGANIZATION/tree/sprint-2) on `main`: the commit uploaded to ODTUClass on 14/11/2026, with every deliverable and this page |

## Sprint goal

> Alpha 0.1 (baseline): Q&A dataset v1 (D2) and the indexed source text (D5) are ready, the baseline retrieval is measured with Recall@5 against the charter target and gives answers with Article/Annex citations and the version date, and Project Charter v2 (D7) is ready for the Sprint 2 review on 18/11/2026.

Recall@8 became the main retrieval score on 10/11/2026, because the answer model gets 8 chunks (design decision D14); Recall@5 is still reported.

## What we achieved

- **A reviewed question set.** [Q&A dataset v1](../../docs/eval/eval-set-v1.csv) (D2) has 46 questions on the four education use cases of Annex III point 3, 13 of them safety questions and 7 adapted from published work. Every question was checked against the official text and reviewed by a member who did not write it; no flag is open. Split membership (30 `val`, 16 `test`) was fixed on 09/11/2026, and the reviewed v1 was frozen on 14/11/2026 at commit `c62de1c`. The [data card](../11-datasheets/03-qa-data-report.md) records how the questions were written and every decision behind them.
- **An indexed source text.** The consolidated text of 27/07/2026 is split into 105 provision chunks, each with its Article or Annex reference and the version date (D5); 20 random chunks were compared word for word with the stored PDF: 19 matched after normalisation and one differed only by a space before a full stop; no chunk was corrected by hand ([preprocessing report](../../docs/eval/preprocessing.md), [dataset report](../11-datasheets/02-dataset-report.md)).
- **A measured baseline.** On the 27 `val` questions with gold provisions, bge-m3 with some BM25 reaches Recall@8 0.59 (Recall@5 0.43), and at least one gold provision is among the top 8 chunks for 24 of the 27. With these chunks, Llama-3.1-8B on CPU cites the expected provision in 19 of 27 answers (70%), below the O2 (a) target of 80%. Without retrieval, a different model, Claude Haiku 5.5 with the whole text attached, cites it in 22 of 27 (81%), so the two results compare two setups, not retrieval alone. Every citation is checked against the retrieved chunks, and a sources line added afterwards to the saved E1 answers gives each cited provision with the version date (20 of 20 substantive answers). The [baseline experiment card (E1)](../12-experiment-cards/E1-baseline.md) lists the failures, and the [technical summary](01-review-committee-technical-summary.md) gives the metrics and the next steps: the answer step first, then the three questions where retrieval misses the gold provision.
- **Project Charter v2.** Every Sprint 1 review comment is answered in the [response table](../04-sprint-1/01-sprint-1-review-page.md); the O1 and O3 targets were reviewed with the alpha results, the feedback on the O2 and O4 levels is recorded, the risks are re-scored after the baseline, and every changed page says what is new ([Project Canvas](../03-project-canvas/README.md)).
- **Final user stories.** [Story Map v2](../06-user-stories/02-user-story-map-v2.md), a [story requirements page for every epic](../06-user-stories/README.md) and a test case for every product story; the backlog was estimated with planning poker and the roles follow the ISO/IEC 5339 stakeholder categories.
- **Design.** The [design document](../11-system-architecture-design-document.md) records every Sprint 2 decision (React + Node.js interface, bge-m3, hybrid search with top 8, session memory) and links the experiment-based decisions to E1; the [user interface mockup](../../docs/images/ui-mockup-v1.png) shows the answer with its cited provisions, the version date and the permanent notice; the [SBOM](../10-software-bill-of-materials.md) lists every model tried.

## Sprint results

Status in Jira at the upload on 14/11/2026: **4 of 9 items done (37 of 73 story points)**.

| Item | Type | Points | Status |
|---|---|---|---|
| [KAN-86](https://yarengursoy.atlassian.net/browse/KAN-86) Index every in-scope provision with its reference and version date | Task | 8 | Done |
| [KAN-87](https://yarengursoy.atlassian.net/browse/KAN-87) Build and measure the baseline retrieval | Task | 13 | Done |
| [KAN-88](https://yarengursoy.atlassian.net/browse/KAN-88) Update the Sprint 2 architecture design and technical documentation | Task | 8 | Done |
| [KAN-90](https://yarengursoy.atlassian.net/browse/KAN-90) Finalize the user stories, Story Map v2 and the story tests | Task | 8 | Done |
| [KAN-65](https://yarengursoy.atlassian.net/browse/KAN-65) Test the assistant on in-scope questions checked against the official text | Story | 13 | In progress |
| [KAN-8](https://yarengursoy.atlassian.net/browse/KAN-8) See the provisions that relate to my use case, with their references | Story | 8 | In progress |
| [KAN-83](https://yarengursoy.atlassian.net/browse/KAN-83) Test the assistant's safety responses against a written rubric | Story | 5 | To do |
| [KAN-89](https://yarengursoy.atlassian.net/browse/KAN-89) Write Project Charter v2 from the Sprint 1 feedback | Task | 5 | In progress |
| [KAN-91](https://yarengursoy.atlassian.net/browse/KAN-91) Run the Sprint 2 reporting: welcome page, burndown, retrospective and review | Task | 5 | In progress |

**Not finished at the upload, and why:**

- [KAN-65](https://yarengursoy.atlassian.net/browse/KAN-65): all sub-tasks are done, but two checks are not fully met: the results of the 4 follow-up questions are not yet reported separately (TC-65.1), and `prompt_file` is empty for the 13 use case (d) questions, because their original prompts were not archived (TC-65.4). Results: [story requirements page, S1](../06-user-stories/08-story-requirements-for-epic-kan-28.md#s1--test-the-assistant-on-in-scope-questions-checked-against-the-official-text). Carry-over to Sprint 3 planned.
- [KAN-8](https://yarengursoy.atlassian.net/browse/KAN-8): citing every provision down to the paragraph or point and showing the sources line in the interface moved to [KAN-222](https://yarengursoy.atlassian.net/browse/KAN-222), already in Sprint 3; [KAN-127](https://yarengursoy.atlassian.net/browse/KAN-127) (how several provisions relate) is in progress. Carry-over of KAN-8 and KAN-127 to Sprint 3 planned.
- [KAN-83](https://yarengursoy.atlassian.net/browse/KAN-83): its checks cover the safety questions and the rubric. The safety questions (KAN-49) are done, but the rubric (KAN-50) was finished only on 14/11/2026, so the test cases TC-83.1 to TC-83.5 are not yet run and recorded ([Sprint 2 retrospective](02-sprint-2-retrospective.md)). Carry-over to Sprint 3 planned.
- [KAN-89](https://yarengursoy.atlassian.net/browse/KAN-89): Charter v2 is complete; pilot user confirmations are pending, due 18/11/2026 ([KAN-158](https://yarengursoy.atlassian.net/browse/KAN-158)).
- [KAN-91](https://yarengursoy.atlassian.net/browse/KAN-91): the demo, the review of the assigned team and the answers to the reviewers belong to 15–18/11/2026 (KAN-122, KAN-123, KAN-124).

**Definition of Done checklist.** The [checklist before closing Sprint 2](../03-definition-of-ready-definition-of-done.md#checklist-before-closing-sprint-2) was ticked before the upload with the evidence of each item. Besides the stories above, these items are open, each with its reason on that page:

- Git rules: several files were uploaded directly to `main` through the GitHub web interface; branches, teammate review and `--no-ff` merges are enforced in Sprint 3.
- The install test from `README.md` by a member who did not build the baseline is not recorded (KAN-87, criterion 4).
- There is no interface yet, so an answer is not yet shown with its sources and notice in one view (KAN-222, Sprint 3).
- Question set: the 13 missing prompt files (above); no record of the multi-hop check of the 5 multi-hop questions.
- Baseline: Recall@8 and Recall@5 are reported overall, not yet for each label of the question-writing method; the W&B runs were not checked for both commits.
- Debug prints in the repository were not checked one by one.

## Deliverables

| Deliverable | Pages | Jira |
|---|---|---|
| Welcome page | This page | [KAN-121](https://yarengursoy.atlassian.net/browse/KAN-121) |
| Definition of Ready and Done | [Definition of Ready and Definition of Done](../03-definition-of-ready-definition-of-done.md), Sprint 2, with the checklist before closing the sprint | [KAN-117](https://yarengursoy.atlassian.net/browse/KAN-117) |
| Burndown chart | [Burndown chart](../04-burndown-chart.md#sprint-2), Sprint 2 | [KAN-118](https://yarengursoy.atlassian.net/browse/KAN-118) |
| Retrospective | [Sprint 2 Retrospective](02-sprint-2-retrospective.md) | [KAN-120](https://yarengursoy.atlassian.net/browse/KAN-120) |
| Technical summary and baseline experiment card | [Review committee technical summary](01-review-committee-technical-summary.md), [E1 baseline experiment card](../12-experiment-cards/E1-baseline.md) | [KAN-101](https://yarengursoy.atlassian.net/browse/KAN-101), [KAN-100](https://yarengursoy.atlassian.net/browse/KAN-100) |
| Design document | [System Architecture Design Document](../11-system-architecture-design-document.md) | [KAN-102](https://yarengursoy.atlassian.net/browse/KAN-102) |
| Spike notes | [docs/spikes](../../docs/spikes/README.md): no spikes were conducted in Sprint 2; the comparisons were run as experiments (E1) | – |
| SBOM | [Software Bill of Materials](../10-software-bill-of-materials.md) | [KAN-105](https://yarengursoy.atlassian.net/browse/KAN-105) |
| Jira backlog export | [Jira backlog index](../../docs/backlog/_README.md) and [14/11/2026 Jira export (.xlsx)](../../docs/backlog/jira-export-2026-11-14.xlsx), the Sprint 2 submission snapshot | [KAN-119](https://yarengursoy.atlassian.net/browse/KAN-119) |
| D7 Project Charter v2 | [Project Canvas](../03-project-canvas/README.md) (every changed page starts with "What is new in Charter v2"), [Sprint 1 review response table](../04-sprint-1/01-sprint-1-review-page.md) | [KAN-89](https://yarengursoy.atlassian.net/browse/KAN-89) |
| Final user stories and their test cases | [User Story Map v2](../06-user-stories/02-user-story-map-v2.md), [story requirements for each epic](../06-user-stories/README.md), with a test case next to every story | [KAN-90](https://yarengursoy.atlassian.net/browse/KAN-90) |
| D6 Baseline (alpha) | [README](../../README.md) (install and run), [`requirements.txt`](../../requirements.txt), [`config/rag.yaml`](../../config/rag.yaml), [`prompts/`](../../prompts/), [E1 baseline experiment card](../12-experiment-cards/E1-baseline.md) | [KAN-87](https://yarengursoy.atlassian.net/browse/KAN-87) |
| D2 Q&A dataset v1 and data card | [`docs/eval/eval-set-v1.csv`](../../docs/eval/eval-set-v1.csv) (frozen at commit `c62de1c`), [Q&A data report](../11-datasheets/03-qa-data-report.md) | [KAN-65](https://yarengursoy.atlassian.net/browse/KAN-65), [KAN-85](https://yarengursoy.atlassian.net/browse/KAN-85) |
| D5 Retrieval corpus | [Third-party dataset register](../11-datasheets/01-third-party-dataset-register.md), [Dataset report](../11-datasheets/02-dataset-report.md) | [KAN-86](https://yarengursoy.atlassian.net/browse/KAN-86), [KAN-96](https://yarengursoy.atlassian.net/browse/KAN-96) |
| User interface mockup | [Mockup v1](../../docs/images/ui-mockup-v1.png) and its [waiting and error states](../../docs/images/ui-mockup-v1-states.png) | [KAN-104](https://yarengursoy.atlassian.net/browse/KAN-104) |
| Last sprint's review | [Sprint 1 Review Page](../04-sprint-1/01-sprint-1-review-page.md): our answer to every Sprint 1 review comment, with a link to its fix | [KAN-106](https://yarengursoy.atlassian.net/browse/KAN-106) |

## Who did what

From the Sprint 2 sub-tasks in Jira.

| Member | Role | Main Sprint 2 work |
|---|---|---|
| Yeşim | Product Owner | Use case (a) and safety questions, the questions adapted from published work, the gold-source check and the data card (D2); the corpus datasheet; the sources line of the answers (KAN-126); Story Map v2, the story requirements pages and the story test cases; the Sprint 1 review response table and the "What is new" notes of Charter v2; this page, the burndown and the backlog export |
| Yaren | Scrum Master | Sprint 2 Definition of Ready and Done, planning poker and the ISO/IEC 5339 role check; use case (d) questions; the 20-chunk check and the preprocessing report; the citation check and its report (KAN-128, KAN-129); the O1 and O3 review and the Risks update; the retrospective |
| Kaan | Data Scientist | Design document, user interface technology and mockup, SBOM; the E1 baseline experiment card and the technical summary; the evaluation rubric; use case (c) questions and the provision mapping; the scope definition and the O2 and O4 feedback in Charter v2 |
| Gözde Nur | Data Scientist | Parsing and chunking (D5), the vector index and the retriever, the README, pinned requirements and prompts; the settings run and the comparison without and with retrieval (KAN-99, KAN-221); the answers of the baseline (KAN-125); use case (b) questions and the val/test split |

## Sprint 2 review (18/11/2026)

Planned: the demo (10 minutes or less) in [KAN-122](https://yarengursoy.atlassian.net/browse/KAN-122); the review of the assigned team's Sprint 2 deliverables between 15/11 and 18/11/2026 ([KAN-123](https://yarengursoy.atlassian.net/browse/KAN-123)), and the answers to the review of our deliverables on the [Sprint 2 review page](03-sprint-2-review-page.md) ([KAN-124](https://yarengursoy.atlassian.net/browse/KAN-124)).
