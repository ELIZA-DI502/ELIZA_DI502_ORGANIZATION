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
| 1 | Project Charter | The Q&A set needs a datasheet in Sprint 2 that logs every decision behind the dataset. | Accepted | The data card is part of D2 (criterion 14, since 25/10/2026) and its decision log records every dataset decision ([Q&A data report](../11-datasheets/03-qa-data-report.md)). On 09/11/2026 Charter v2 named the data card in the D2 title and pointed to the decision log in D2 criterion 14 ([Deliverables](../03-project-canvas/05-deliverables.md)). | KAN-85, KAN-106 | Done |
| 2 | Project Charter | The CPU-only inference constraint may need to be reconsidered after tests. | Accepted | C-05 stays in force. It is reviewed against the answer times measured in the baseline (Sprint 2) and on the pilot computer (Sprint 4). If the measurements show that CPU-only inference cannot meet the project's needs, we propose a change to C-05 after weighing latency, cost, access and the other constraints; the Google Cloud credit (C-06, R-12) is one option to evaluate, not an automatic solution. On 09/11/2026 Charter v2 added this review note to C-05 ([Assumptions & Constraints](../03-project-canvas/03-assumptions-and-constraints.md)). | KAN-106, KAN-99 | Done |
| 3 | User Stories | No user stories for the Project Review Committee; such work can be tasks, or tasks linked to user stories. | Accepted | The Sprint 2 committee stories became tasks on 01/11/2026 (KAN-86–91). The open Sprint 3 and 4 committee stories became tasks on 07/11/2026 (KAN-168–171, KAN-204); KAN-168–170 are linked to the user stories they serve, and the sprint reporting tasks KAN-171 and KAN-204 serve the course, so they are not linked to a user story. The closed Sprint 1 stories stay as they are, because they are part of the Sprint 1 record (burndown and backlog export). [Story Map v2](../06-user-stories/02-user-story-map-v2.md) shows committee work as tasks, not as a user role (KAN-112). | KAN-168–171, KAN-204, KAN-112 | Done |
| 4 | User Stories | KAN-202 ("fast service") is an acceptance criterion rather than a story; its subtasks can move. | Accepted | KAN-202 is no longer a user story. It became the task "Evaluate search-time improvement against manual lookup (O1)", keeping its four pilot subtasks, and is linked to the stories whose speed it measures (KAN-19, KAN-8, KAN-21) and to the understanding survey (KAN-72, O3), which runs in the same pilot sessions. It is not merged into KAN-72, because KAN-72 measures understanding (O3), a different objective. See [T1 on the story requirements page of epic KAN-16](../06-user-stories/04-story-requirements-for-epic-kan-16.md#t1--evaluate-search-time-improvement-against-manual-lookup-o1) and [Story Map v2](../06-user-stories/02-user-story-map-v2.md). | KAN-202 | Done |
| 5 | User Stories | KAN-75, KAN-24 and KAN-25 can be one story about a user asking for legal advice; add detail in the tasks instead. | Accepted | KAN-24 and KAN-25 are merged into KAN-2, which keeps all their acceptance criteria and subtasks. The final test-split check (KAN-75) became a Sprint 4 task linked to KAN-2, so that the Sprint 4 test does not block the Sprint 3 story. See [S1 on the story requirements page of epic KAN-18](../06-user-stories/06-story-requirements-for-epic-kan-18.md#s1--get-regulatory-information-never-a-legal-decision) (KAN-2) and [T1](../06-user-stories/06-story-requirements-for-epic-kan-18.md#t1--run-the-final-o4-safety-evaluation-on-the-held-out-test-split) (KAN-75). | KAN-2, KAN-75 | Done |
| 6 | Architecture Design Document | Keep recording decisions, and link them to experiment cards. | Accepted | Every decision based on an experiment links to its experiment card, and a decision without an experiment names its evidence; this rule is in the [Definition of Done](../03-definition-of-ready-definition-of-done.md). On 14/11/2026 the [design document](../11-system-architecture-design-document.md) links the [E1 baseline experiment card](../12-experiment-cards/E1-baseline.md) from the experiment-based decisions D9, D10, D12, D13 and D14, and its RAG pipeline table and top-k rule follow D14 (there is no separate E2 card). | KAN-102, KAN-117 | Done |
| 7 | Architecture Design Document | The UI decision (D1) cites unshared spikes and requirements "beyond a default chat widget"; say which ones. | Accepted | On 14/11/2026 [D1](../11-system-architecture-design-document.md#d1-web-interface-and-backend-react--nodejsexpress) lists the interface requirements a default chat widget does not cover, with the stories they come from (KAN-2, KAN-8, KAN-21, KAN-22, KAN-26) and the [user interface mockup](../../docs/images/ui-mockup-v1.png). D1, D2, D3 and D10 no longer cite the unshared Spike 01; D1's evidence states that no spike note was written for the team discussion of 19/10/2026. | KAN-102, KAN-103 | Done |
| 8 | Architecture Design Document | D4 (chat history): without user accounts, whose conversation is shown after a restart? It may not be needed unless used for analytics. | Accepted | On 09/11/2026 the team decided that the conversation is not kept after a restart. The question-answer pairs of the active session are kept only in the memory of the web backend, and the conversation is not written to disk. Without user accounts a stored conversation has no owner, and the history is used only for follow-up questions (Feature 7, KAN-6, not committed), not for analytics (C-10 does not allow user questions to be logged), so a separate database is not needed. If the backend restarts, the active conversation is lost. C-10 was updated in Charter v2 on 09/11/2026. On 10/11/2026 design decision D15 replaced D4 (the db container was removed), and KAN-26 and KAN-6 were updated to match ([design document, D15](../11-system-architecture-design-document.md)). | KAN-102, KAN-89, KAN-26, KAN-6 | Done |
| 9 | Learning Spikes | Fine. In future, say what was learned from a course in relation to the product; experiment setups belong in the experiments folder. | Accepted | From Sprint 2, each learning spike states what it changes in the product, and experiment setups are written in `Markdown Template/12-experiment-cards/`. This rule was added to the [spikes README](../../docs/spikes/README.md) on 10/11/2026; Sprint 2 has no learning spike. | KAN-88 | Done |
| 10 | Retrospective | The actions are appropriate. | No change needed | – | – | No action |
