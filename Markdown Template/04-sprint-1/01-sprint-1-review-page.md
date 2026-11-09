# Sprint 1 Review Page

This page is reserved for when Sprint 1 is finished. A group will be assigned to review your documents and fill in this form.

Please put your feedback and review document here.

Thank you for your feedback in advance.

## Sprint 1 Review

| **REVIEW DOCUMENT** |  |  |  |
|---|---|---|---|
| Start Date: |   |   |   |
| Project Name: |   | Number of Pages: |   |
| Product Name: |   | Product Definition: |   |
| Roles: | Review Leader: |   |   |
|   | Reviewers: |   |   |
| Review Materials: | · *You might have multiple materials regarding each artefact. List and enumerate them hierarchically: A.1.. might refer to a data artefact regarding one of your data sets.* |   |   |
| Total Number of Errors: |   |   |   |
| Assessment Status: | ACCEPTED | as it is / with rework |   |
|   | REJECTED | ____ review again |   |

**ERROR TYPES**

| Error Type Number | Error Type Definition | Number of Errors Found |
|---|---|---|
| 1 | Spelling (grammar, punctuation, etc) |   |
| 2 | Inconsistency with the guidelines (Scrum, TDSP, templates) |   |
| 3 | Uncertain |   |
| 4 | Incorrect |   |
| 5 | Inapplicable |   |
| 6 | Internal Inconsistency |   |
| 7 | External Inconsistency |   |
| 8 | Incomplete/Insufficient/Missing |   |
| 9 | Other |   |
| TOTAL |   |   |

**Importance Types**

| Importance Type | Number of Errors Found |
|---|---|
| Little |   |
| Medium |   |
| Important |   |
| TOTAL |   |

| # | Reviewed Material ID | Section | Page | Line/No | Error Type | Importance | Explanation | Correction Status | Correction Explanation |
|---|---|---|---|---|---|---|---|---|---|
| 1 |   |   |   |   |   |   |   |   |   |
| 2 |   |   |   |   |   |   |   |   |   |
| 3 |   |   |   |   |   |   |   |   |   |
| 4 |   |   |   |   |   |   |   |   |   |
| 5 |   |   |   |   |   |   |   |   |   |
| 6 |   |   |   |   |   |   |   |   |   |

## Responses to the Project Review Committee feedback (Sprint 1)

Written feedback on the Sprint 1 deliverables, received after the review on 28/10/2026. Each comment is listed with our decision. **Done** means the change is made; **Planned** means the decision is taken and the change is tracked in the linked Jira item; **Open** means the decision is still to be taken, by the date given. We did not receive a review from another team for Sprint 1, so the review form above is empty.

| # | Document | Comment (summary) | Decision | What we changed or will change | Tracked in | Status |
|---|---|---|---|---|---|---|
| 1 | Project Charter | The Q&A set needs a datasheet in Sprint 2 that logs every decision behind the dataset. | Accepted | The data card is part of D2 (criterion 14, since 25/10/2026) and its decision log records every dataset decision ([Q&A data report](../11-datasheets/03-qa-data-report.md)). Charter v2 names the data card in the D2 title and points to the decision log. | KAN-85, KAN-106 | Planned |
| 2 | Project Charter | The CPU-only inference constraint may need to be reconsidered after tests. | Accepted | C-05 stays in force. It is reviewed against the answer times measured in the baseline (Sprint 2) and on the pilot computer (Sprint 4). If the measurements show that CPU-only inference cannot meet the project's needs, we propose a change to C-05 after weighing latency, cost, access and the other constraints; the Google Cloud credit (C-06, R-12) is one option to evaluate, not an automatic solution. Charter v2 adds this review note to C-05. | KAN-106, KAN-99 | Planned |
| 3 | User Stories | No user stories for the Project Review Committee; such work can be tasks, or tasks linked to user stories. | Accepted | The Sprint 2 committee stories became tasks on 01/11/2026 (KAN-86–91). The open Sprint 3 and 4 committee stories became tasks on 07/11/2026 (KAN-168–171, KAN-204); KAN-168–170 are linked to the user stories they serve, and the sprint reporting tasks KAN-171 and KAN-204 serve the course, so they are not linked to a user story. The closed Sprint 1 stories stay as they are, because they are part of the Sprint 1 record (burndown and backlog export). [Story Map v2](../06-user-stories/02-user-story-map-v2.md) shows committee work as tasks, not as a user role (KAN-112). | KAN-168–171, KAN-204, KAN-112 | Done |
| 4 | User Stories | KAN-202 ("fast service") is an acceptance criterion rather than a story; its subtasks can move. | Accepted | KAN-202 is no longer a user story. It became the task "Evaluate search-time improvement against manual lookup (O1)", keeping its four pilot subtasks, and is linked to the stories whose speed it measures (KAN-19, KAN-8, KAN-21) and to the understanding survey (KAN-72, O3), which runs in the same pilot sessions. It is not merged into KAN-72, because KAN-72 measures understanding (O3), a different objective. | KAN-202 | Done |
| 5 | User Stories | KAN-75, KAN-24 and KAN-25 can be one story about a user asking for legal advice; add detail in the tasks instead. | Accepted | KAN-24 and KAN-25 are merged into KAN-2, which keeps all their acceptance criteria and subtasks. The final test-split check (KAN-75) became a Sprint 4 task linked to KAN-2, so that the Sprint 4 test does not block the Sprint 3 story. | KAN-2, KAN-75 | Done |
| 6 | Architecture Design Document | Keep recording decisions, and link them to experiment cards. | Accepted | Every decision based on an experiment links to its experiment card; a decision without an experiment names its evidence. This rule is added to the Definition of Done. | KAN-102, KAN-117 | Planned |
| 7 | Architecture Design Document | The UI decision (D1) cites unshared spikes and requirements "beyond a default chat widget"; say which ones. | Accepted | D1 lists the interface requirements a default chat widget does not cover and the stories they come from. The Spike 01 note is added to `docs/spikes/`, or the reference is replaced by evidence that is in the repository. | KAN-102, KAN-103 | Planned |
| 8 | Architecture Design Document | D4 (chat history): without user accounts, whose conversation is shown after a restart? It may not be needed unless used for analytics. | Accepted | On 09/11/2026 the team decided that the conversation is not kept after a restart. The question-answer pairs of the active session are kept only in the memory of the web backend, and the conversation is not written to disk. Without user accounts a stored conversation has no owner, and the history is used only for follow-up questions (Feature 7, KAN-6, not committed), not for analytics (C-10 does not allow user questions to be logged), so a separate database is not needed. If the backend restarts, the active conversation is lost. C-10 was updated in Charter v2 on 09/11/2026. D4, the diagram, the component and interface tables, KAN-26 and KAN-6 will be updated to match (KAN-102). | KAN-102, KAN-89, KAN-26, KAN-6 | Planned |
| 9 | Learning Spikes | Fine. In future, say what was learned from a course in relation to the product; experiment setups belong in the experiments folder. | Accepted | From Sprint 2, each learning spike states what it changes in the product, and experiment setups are written in `Markdown Template/12-experiment-cards/`. | KAN-88 | Planned |
| 10 | Retrospective | The actions are appropriate. | No change needed | – | – | No action |
