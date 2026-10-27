# Story Requirements for Epic KAN-27: Project charter and sprint reporting

Version v1, end of Sprint 1 (27/10/2026). Source: Jira project KAN. Back to the [User Story Map v1](01-user-story-map-v1.md) · [all story requirements pages](README.md).

| Epic | Project charter and sprint reporting |
|---|---|
| Summary | Project-management work across all sprints: the Project Charter (D1 v1 in Sprint 1, D7 v2 in Sprint 2), the backlog and User Story Map, the story requirements and test cases, the pilot evaluation report (D10; the pilot itself is measured in KAN-202 and KAN-72), and the documents delivered every sprint (welcome page, Definition of Ready and Done, burndown chart, retrospective, review page, technical summary, Jira backlog export). |
| Features | Charter v1 and v2 (D1, D7), user stories, sprint documents |
| Document Owner | Yaren |
| Designer | Not applicable: this epic produces documents, not a user interface |
| Developers | Gözde Nur, Kaan, Yaren, Yeşim (Sprint 1); later stories are assigned at each sprint planning |
| Release Target (Sprint) | Sprint 1 (Pre-alpha); Sprint 2 (Alpha 0.1); Sprint 3 (Beta 0.5); Sprint 4 (Release candidate 1.0) |
| Traceability | Major Activities rows 1, 34, 37, 38, 40. |
| Jira | [KAN-27](https://yarengursoy.atlassian.net/browse/KAN-27) |

## Requirements

For more info you can visit: https://www.atlassian.com/agile/product-management/requirements.

| # | User story title | User story description | Priority | Points | Owner | Sprint | Notes | Jira |
|---|---|---|---|---|---|---|---|---|
| S1 | [Judge whether the plan can hold](#s1--judge-whether-the-plan-can-hold) | As a Project Review Committee member, I want to see the assumptions, constraints, dependencies, resources and risks with their owners and checks, so that I can judge whether the plan can hold. | High | 8 | Gözde Nur | Sprint 1 | Release: Pre-alpha; Status: In progress (27/10/2026). | [KAN-69](https://yarengursoy.atlassian.net/browse/KAN-69) |
| S2 | [Check that the delivery plan fits the course calendar](#s2--check-that-the-delivery-plan-fits-the-course-calendar) | As a Project Review Committee member, I want to see what the team delivers, when, and who is responsible, so that I can check that the plan fits the course calendar. | High | 8 | Yeşim | Sprint 1 | Release: Pre-alpha; Status: Done (27/10/2026). | [KAN-70](https://yarengursoy.atlassian.net/browse/KAN-70) |
| S3 | [Decide whether to approve the project's purpose and scope](#s3--decide-whether-to-approve-the-projects-purpose-and-scope) | As a Project Review Committee member, I want to see the problem, the users, the objectives with measurable success criteria and the scope of the assistant, so that I can decide whether to approve the project. | High | 13 | Kaan | Sprint 1 | Release: Pre-alpha; Status: Done (27/10/2026). | [KAN-79](https://yarengursoy.atlassian.net/browse/KAN-79) |
| S4 | [Know which stories I can start and when my work is done](#s4--know-which-stories-i-can-start-and-when-my-work-is-done) | As a Data Scientist, I want the backlog, the story map and the Definition of Ready and Done agreed before Sprint 2 starts, so that I know which stories I can start and when my work counts as done. | Medium | 5 | Yaren | Sprint 1 | Release: Pre-alpha; Status: In progress (27/10/2026). | [KAN-80](https://yarengursoy.atlassian.net/browse/KAN-80) |
| S5 | [Check that the Sprint 1 feedback changed the charter](#s5--check-that-the-sprint-1-feedback-changed-the-charter) | As a Project Review Committee member, I want to see how each Sprint 1 review comment changed the charter, so that I can approve Charter v2. | High | – | – | Sprint 2 | Release: Alpha 0.1. | [KAN-89](https://yarengursoy.atlassian.net/browse/KAN-89) |
| S6 | [Judge the final user stories and how each one is tested](#s6--judge-the-final-user-stories-and-how-each-one-is-tested) | As a Project Review Committee member, I want the final user stories with a test for each one and an estimated, prioritized backlog, so that I can check that every story can be verified. | Medium | – | – | Sprint 2 | Release: Alpha 0.1. | [KAN-90](https://yarengursoy.atlassian.net/browse/KAN-90) |
| S7 | [Follow Sprint 2 from one welcome page](#s7--follow-sprint-2-from-one-welcome-page) | As a Project Review Committee member, I want to open one welcome page that links to every Sprint 2 deliverable and shows the sprint goal, the results and the submitted commit, so that I can review the sprint without searching the repository. | Medium | – | – | Sprint 2 | Release: Alpha 0.1. | [KAN-91](https://yarengursoy.atlassian.net/browse/KAN-91) |
| S8 | [Follow Sprint 3 from one welcome page](#s8--follow-sprint-3-from-one-welcome-page) | As a Project Review Committee member, I want to open one welcome page that links to every Sprint 3 deliverable and shows the sprint goal, the results and the submitted commit, so that I can review the sprint without searching the repository. | Medium | – | – | Sprint 3 | Release: Beta 0.5. | [KAN-171](https://yarengursoy.atlassian.net/browse/KAN-171) |
| S9 | [Follow Sprint 4 from one welcome page](#s9--follow-sprint-4-from-one-welcome-page) | As a Project Review Committee member, I want to follow all of Sprint 4 from one welcome page, so that I can review the final product, its test results and the team's process without searching the repository. | Medium | – | – | Sprint 4 | Release: Release candidate 1.0. | [KAN-204](https://yarengursoy.atlassian.net/browse/KAN-204) |

Priority, points, owner and sprint are as in Jira on 27/10/2026. Sprint 1 stories were estimated with planning poker; the other stories are estimated and assigned at their sprint planning, starting with Sprint 2 on 28/10/2026. A dash means not decided yet.

Test cases: KAN-8, KAN-2 and KAN-3 already have test cases; a test for every story (the input or steps and the expected result) is added next to it in Sprint 2 ([KAN-90](https://yarengursoy.atlassian.net/browse/KAN-90)).

## S1 · Judge whether the plan can hold

[KAN-69](https://yarengursoy.atlassian.net/browse/KAN-69) · Sprint 1 (Pre-alpha) · Priority High · Points 8 · Owner Gözde Nur

**Story:** As a Project Review Committee member, I want to see the assumptions, constraints, dependencies, resources and risks with their owners and checks, so that I can judge whether the plan can hold.

**Acceptance criteria**

1. Every assumption has a basis, a dated validation, an owner and a linked risk, and the IDs match in both directions.
2. Every constraint has a category and links to its Major Activities rows.
3. Every dependency names what must happen first and what waits for it, with a critical date and a named contact.
4. The risk register has at least one risk in each of the five layers, and every risk with a score of 10 or more has a mitigation, a trigger, a contingency plan and an owner.
5. Every resource has a responsible person and a dated status.

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Write Risks page and link it to Assumptions & Constraints | The risk register lists R-01 to R-12 with at least one risk from each of the five layers (data, model, infrastructure, integration, people/process); every assumption A-01 to A-09 has its linked risk and the IDs match both ways; probabilities are residual and each has a basis; every risk scoring 10 or more has a mitigation, a numeric trigger with a date or sprint, a contingency plan and a named owner; every risk that comes from a constraint names the Major Activities row that mitigates it; the page passes its checklist. | Gözde Nur | – | Done | [KAN-14](https://yarengursoy.atlassian.net/browse/KAN-14) |
| Write the Assumptions and Constraints Page | Assumptions A-01 to A-09 with basis, check, owner and linked risk; constraints C-01 to C-10 with their links to Major Activities and Risks; the page passes its checklist. | Gözde Nur | – | Done | [KAN-33](https://yarengursoy.atlassian.net/browse/KAN-33) |
| Write the Facilities and Resources Page | The page lists the team computers (including the computer used for the pilot and the final demo, which is also the deployment environment), Google Colab, the Google Cloud credit ($100, C-06, kept as a reserve), the open-source models from Hugging Face and the other tools the team uses, and passes its checklist. | Kaan | – | In progress | [KAN-38](https://yarengursoy.atlassian.net/browse/KAN-38) |
| Write the Dependencies Page | The page lists the external dependencies (EUR-Lex for the source text, Hugging Face for the open-source model files, published benchmark questions) and the order dependencies between activities, including EUR-Lex for R-01 and the pilot computer set-up for R-09 and R-12, and passes its checklist. | Yaren | – | Done | [KAN-39](https://yarengursoy.atlassian.net/browse/KAN-39) |

The story carries the points and its sub-tasks are not estimated separately (Model A of the course's [Jira sync guide](../../docs/JIRA_SYNC_SETUP.md)).

**Traceability**

Deliverable: D1 Project Charter v1 (due 27/10/2026)      
Milestone: M1 Charter v1 approved (28/10/2026)      
Pages: Assumptions & Constraints, Dependencies, Facilities & Resources, Risks

## S2 · Check that the delivery plan fits the course calendar

[KAN-70](https://yarengursoy.atlassian.net/browse/KAN-70) · Sprint 1 (Pre-alpha) · Priority High · Points 8 · Owner Yeşim

**Story:** As a Project Review Committee member, I want to see what the team delivers, when, and who is responsible, so that I can check that the plan fits the course calendar.

**Acceptance criteria**

1. Every milestone has at least one deliverable, and every deliverable is due on or before the course upload date of its sprint (27/10, 14/11, 05/12, 30/12/2026).
2. Every deliverable has measurable acceptance criteria, a due date and an approving stakeholder.
3. Each of the four sprints is mapped to a release stage with its key deliverables.
4. Every activity has a life cycle stage and is marked In Scope or Out of Scope, with a reason for each Out of Scope row.
5. Every owner, approver and contact named on other pages appears in Project Organization.

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Write the Milestones Page | Milestones M1-M10 with dates on the sprint calendar, each with at least one associated deliverable; the page passes its checklist. | Yaren | – | Done | [KAN-32](https://yarengursoy.atlassian.net/browse/KAN-32) |
| Write the Deliverables Page | Deliverables D1–D11 have a description, measurable acceptance criteria, a due date and an approving stakeholder; the page passes its checklist. | Yeşim | – | Done | [KAN-34](https://yarengursoy.atlassian.net/browse/KAN-34) |
| Write the Project Organization Page | Scrum roles (Product Owner, Scrum Master, Development Team) and each member's responsibilities are named; the page passes its checklist. | Yeşim | – | Done | [KAN-35](https://yarengursoy.atlassian.net/browse/KAN-35) |
| Write the Major Activities Page | Activities with one ISO/IEC 5338 stage each, In Scope or Out of Scope, constraint IDs on the rows they create; the page passes its checklist. | Yeşim | – | Done | [KAN-36](https://yarengursoy.atlassian.net/browse/KAN-36) |
| Write the Release Plan Page | One row per sprint (Pre-alpha, Alpha 0.1, Beta 0.5, Release candidate 1.0) with dates and key deliverables matching the Deliverables page; the page passes its checklist. | Yeşim | – | Done | [KAN-37](https://yarengursoy.atlassian.net/browse/KAN-37) |

The story carries the points and its sub-tasks are not estimated separately (Model A of the course's [Jira sync guide](../../docs/JIRA_SYNC_SETUP.md)).

**Traceability**

Deliverable: D1 Project Charter v1 (due 27/10/2026)      
Milestone: M1 Charter v1 approved (28/10/2026)      
Pages: Milestones, Deliverables, Project Organization, Major Activities, Release Plan

## S3 · Decide whether to approve the project's purpose and scope

[KAN-79](https://yarengursoy.atlassian.net/browse/KAN-79) · Sprint 1 (Pre-alpha) · Priority High · Points 13 · Owner Kaan

**Story:** As a Project Review Committee member, I want to see the problem, the users, the objectives with measurable success criteria and the scope of the assistant, so that I can decide whether to approve the project.

**Acceptance criteria**

1. The Executive Summary passes every item of its "Checklist before submitting".
2. Each objective (O1–O4) has at least one numeric success criterion with a method, an owner and a date.
3. Every feature names the objective it serves.
4. The same IDs, names and dates appear on all charter pages.

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Write the Project Executive Summary (Scope) Page | The Executive Summary reflects the Week 2 feedback: AI users, objectives O1-O4 with numeric success criteria, features 1-7 and the Scope Definition; the page passes its checklist. | Kaan | – | Done | [KAN-31](https://yarengursoy.atlassian.net/browse/KAN-31) |
| Check consistency across all charter pages and submit Project Charter v1 | All ten charter pages are in the repository and each passes its own 'Checklist before submitting' (D1 criterion 1); milestone and deliverable numbers match on all pages (D1 criterion 3). | Yeşim | – | In progress | [KAN-40](https://yarengursoy.atlassian.net/browse/KAN-40) |

The story carries the points and its sub-tasks are not estimated separately (Model A of the course's [Jira sync guide](../../docs/JIRA_SYNC_SETUP.md)).

**Traceability**

Deliverable: D1 Project Charter v1 (due 27/10/2026)      
Milestone: M1 Charter v1 approved (28/10/2026)      
Pages: Project Executive Summary; consistency across all Project Canvas pages

## S4 · Know which stories I can start and when my work is done

[KAN-80](https://yarengursoy.atlassian.net/browse/KAN-80) · Sprint 1 (Pre-alpha) · Priority Medium · Points 5 · Owner Yaren

**Story:** As a Data Scientist, I want the backlog, the story map and the Definition of Ready and Done agreed before Sprint 2 starts, so that I know which stories I can start and when my work counts as done.

**Acceptance criteria**

1. Every user story for Sprints 2–4 has the form "As a … I want … so that …", acceptance criteria and an epic.
2. User Story Map v1 shows the feature–epic–story–task hierarchy, and each product epic has a story requirements page listing each story's tasks and success criteria.
3. The Sprint 2 Definition of Ready and Done are agreed by the team and recorded in `03-definition-of-ready-definition-of-done.md` before Sprint 2 planning (28/10/2026).
4. The Sprint 1 output folders exist in the repository, and the Sprint 1 page links every Sprint 1 deliverable.

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Review and rewrite the user stories in Jira | The user stories are in Jira under the eight epics (product epics Ask, Find and Understand, Show the Source and Know the Limits; project epics Project charter and sprint reporting, Evaluation, Source corpus, and System design and delivery). Each story has "As a …, I want …, so that …", testable acceptance criteria and a traceability section (feature or objective, deliverable, milestone, constraints, assumptions, risks), and is placed in Sprints 1–4 as in the Release Plan. The stories that the charter does not commit (KAN-6, KAN-20) are in the backlog, marked "built only if time allows". The use-case scenarios KAN-10 to KAN-13 are closed, and their content is moved into KAN-8, KAN-2, KAN-3 and the D2 questions. Owners and story points are set at each sprint's planning. Course requirement: "User stories in Jira" (Week 3) and "Updated user stories in Jira" (Week 4). | Yeşim | – | Done | [KAN-41](https://yarengursoy.atlassian.net/browse/KAN-41) |
| Write the Story Requirements pages and User Story Map v1 | One Story Requirements page per epic with the stories and their acceptance criteria; User Story Map v1 with the releases Alpha 0.1, Beta 0.5 and RC 1.0 as rows; every story names its deliverables and milestones. | Yeşim | – | To do | [KAN-42](https://yarengursoy.atlassian.net/browse/KAN-42) |
| Write the Definition of Ready and Definition of Done | A DoR and a DoD that apply to every backlog item; the DoD includes that the question, answer, citations and notices are shown in the same conversation view. | Yaren | – | In progress | [KAN-43](https://yarengursoy.atlassian.net/browse/KAN-43) |
| Write the Sprint 1 report and prepare the Sprint 1 review | The Sprint 1 welcome page (`Markdown Template/04-sprint-1/README.md`) lists the completed and unfinished work and links every Sprint 1 deliverable; the burndown chart is in `04-burndown-chart.md`; the retrospective is in `02-sprint-1-retrospective.md`; the review agenda for 28/10 includes asking the Project Review Committee for feedback on the O2 and O4 target levels (A-06). | Yeşim | – | To do | [KAN-44](https://yarengursoy.atlassian.net/browse/KAN-44) |
| Set up the repository folders for Sprint 1 outputs | The folders below exist in the repository, following the course repository structure, each with a short README that says what goes in it. The folder names match the paths used in the charter. No production code. • docs/eval/ - evaluation question set (eval-set-v1.csv) and rubric (rubric.md) (D2) • data/ - stored consolidated text and manifest.csv (D3) • docs/adr/ - architecture decision records (D4) • docs/spikes/ - technical and learning spike notes (D4) • docs/backlog/ - Jira export • Markdown Template/04-sprint-1/ - Sprint 1 welcome page, review page and retrospective (one folder per sprint) Done first, before the team adds files. | Yaren | – | In progress | [KAN-64](https://yarengursoy.atlassian.net/browse/KAN-64) |

The story carries the points and its sub-tasks are not estimated separately (Model A of the course's [Jira sync guide](../../docs/JIRA_SYNC_SETUP.md)).

**Traceability**

Deliverable: D1 Project Charter v1 (due 27/10/2026)    
Milestone: M3 Checkpoint: Sprint 1 reviewed, development starts (28/10/2026)    
Pages: User Story Map v1, story requirements, Definition of Ready and Done, Sprint 1 page

## S5 · Check that the Sprint 1 feedback changed the charter

[KAN-89](https://yarengursoy.atlassian.net/browse/KAN-89) · Sprint 2 (Alpha 0.1) · Priority High · Points – · Owner –

**Story:** As a Project Review Committee member, I want to see how each Sprint 1 review comment changed the charter, so that I can approve Charter v2.

**Acceptance criteria** (D7 criteria 1–6)

1. A response table lists every Sprint 1 review comment as accepted (with the change) or not accepted (with a reason).
2. The final provision list from D3 is reflected in the Scope Definition.
3. The O1 and O3 target levels are reviewed once using the alpha results; any change is recorded with its reason.
4. The Project Review Committee's feedback on the O2 and O4 levels is recorded (A-06); the decision on a level for the difference with and without retrieval is recorded.
5. Risks lists at least one entry for each problem met in Sprint 2.
6. Each changed page states what is new compared with v1.

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Write the response table for the Sprint 1 review comments | Every comment from the Sprint 1 review (28/10/2026) is listed as accepted, with the change, or not accepted, with a reason. The Sprint 1 feedback is addressed by 11/11/2026 (course halfway check). | – | – | To do | [KAN-106](https://yarengursoy.atlassian.net/browse/KAN-106) |
| Update the Scope Definition with the final provision list | The Scope Definition in the Executive Summary matches the D3 provision list after the D2 mapping on 11/11/2026. | – | – | To do | [KAN-107](https://yarengursoy.atlassian.net/browse/KAN-107) |
| Review the O1 and O3 target levels with the alpha results | The O1 and O3 target levels are reviewed once using the alpha results; the review and any change, with its reason, are recorded in the Executive Summary. | – | – | To do | [KAN-108](https://yarengursoy.atlassian.net/browse/KAN-108) |
| Record the feedback on the O2 and O4 levels | The Project Review Committee's feedback on the O2 and O4 levels is recorded (A-06), and the decision on a level for the difference between answers with and without retrieval is recorded: set from the alpha results with its reason, or left as a reported analysis result. | – | – | To do | [KAN-109](https://yarengursoy.atlassian.net/browse/KAN-109) |
| Update Risks with the Sprint 2 problems | Risks has at least one entry for each problem met in Sprint 2, and every risk is re-scored after the baseline evaluation. | – | – | To do | [KAN-110](https://yarengursoy.atlassian.net/browse/KAN-110) |
| Mark what is new on every changed page and open the pull request | Each changed charter page states what is new compared with v1, and the charter and story revisions are in a pull request by 11/11/2026 (course halfway check). | – | – | To do | [KAN-111](https://yarengursoy.atlassian.net/browse/KAN-111) |
| Name the five pilot users and confirm their dates | At least 5 technical professionals are named as pilot users by 18/11/2026, each has confirmed availability between 16/12 and 23/12/2026, and at least 3 of them have worked on an AI or education software product. The result is recorded in the A-04 and A-07 checks. | – | – | To do | [KAN-158](https://yarengursoy.atlassian.net/browse/KAN-158) |

Sub-task owners are assigned at the sprint planning.

**Traceability**

Deliverable: D7 Project Charter v2 (due 14/11/2026)      
Milestone: M5 Charter v2 approved (18/11/2026)      
Objectives: O1 Search time; O3 Understanding (target review)      
Dependency: row 5      
Assumption / Risk: A-06 / R-04 Targets change after review

## S6 · Judge the final user stories and how each one is tested

[KAN-90](https://yarengursoy.atlassian.net/browse/KAN-90) · Sprint 2 (Alpha 0.1) · Priority Medium · Points – · Owner –

**Story:** As a Project Review Committee member, I want the final user stories with a test for each one and an estimated, prioritized backlog, so that I can check that every story can be verified.

**Acceptance criteria** (course Sprint 2 deliverable: "Final user stories")

1. Story Map v2 shows every story in its release row (Alpha 0.1, Beta 0.5, RC 1.0).
2. Every epic has a story requirements page.
3. Every user story has a test next to it in its story requirements page: the input or steps, and the expected result for its acceptance criteria (Major Activities row 40).
4. The backlog is estimated with planning poker and ordered by priority; the estimates are entered as story points in Jira.
5. The roles in the stories come from the ISO/IEC 5339 stakeholder categories.

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Update the User Story Map to v2 | The User Story Map shows every story in its release row (Alpha 0.1, Beta 0.5, RC 1.0), and stories added or removed in Sprint 2 are marked. | – | – | To do | [KAN-112](https://yarengursoy.atlassian.net/browse/KAN-112) |
| Write the story requirements page for every epic | Every epic has a story requirements page in `Markdown Template/06-user-stories/` with its stories and their acceptance criteria. | – | – | To do | [KAN-113](https://yarengursoy.atlassian.net/browse/KAN-113) |
| Write a test case for every user story | Every user story has a test next to it in its story requirements page: the input or steps, and the expected result for its acceptance criteria. | – | – | To do | [KAN-114](https://yarengursoy.atlassian.net/browse/KAN-114) |
| Estimate the backlog with planning poker | Every story in Sprint 2 has a story point estimate in Jira agreed with planning poker, and the backlog is ordered by priority. Points are put on the stories, not on the sub-tasks: sub-task points stay hidden in the burndown until the whole story is done (course note, "lessons from last year's reviews"). | – | – | To do | [KAN-115](https://yarengursoy.atlassian.net/browse/KAN-115) |
| Check the story roles against ISO/IEC 5339 | Every "As a ..." role in the user stories maps to an ISO/IEC 5339 stakeholder category, and the mapping is shown in the story requirements pages. | – | – | To do | [KAN-116](https://yarengursoy.atlassian.net/browse/KAN-116) |

Sub-task owners are assigned at the sprint planning.

**Traceability**

Deliverable: D7 Project Charter v2 (story map and story requirements belong to the Project Canvas)      
Milestone: M5 Charter v2 approved (18/11/2026)      
Major Activities: row 40

## S7 · Follow Sprint 2 from one welcome page

[KAN-91](https://yarengursoy.atlassian.net/browse/KAN-91) · Sprint 2 (Alpha 0.1) · Priority Medium · Points – · Owner –

**Story:** As a Project Review Committee member, I want to open one welcome page that links to every Sprint 2 deliverable and shows the sprint goal, the results and the submitted commit, so that I can review the sprint without searching the repository.

**Acceptance criteria** (course "Every sprint" deliverables)

1. The team agrees on the Definition of Ready and Done and a one-sentence sprint goal in the first week of Sprint 2 (course DoR minimum).
2. `05-sprint-2/README.md` gives the sprint goal, the results, links to every deliverable and the Git commit submitted on 14/11/2026.
3. The burndown chart for the whole sprint, taken from Jira, is in the sprint folder.
4. The Jira backlog export is in `docs/backlog/`.
5. The retrospective gives an action and an owner for every "what went bad" row.
6. The demo at the 18/11/2026 presentation takes 10 minutes or less; the team answers every reviewer item and copies the completed review page into the sprint folder.
7. The team reviews its assigned team's Sprint 2 deliverables between 15/11 and 18/11/2026.

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Agree on the Sprint 2 DoR, DoD and sprint goal | In the first week of Sprint 2: • the actions agreed in the Sprint 1 retrospective have been carried out by their owners; • the risk register and the assumption checks have been reviewed, and triggers and owners updated in Risks; • the team has agreed on the Definition of Ready and Done and on a one-sentence sprint goal; the Sprint 2 lists are in `Markdown Template/03-definition-of-ready-definition-of-done.md` and the goal is entered in Jira. | – | – | To do | [KAN-117](https://yarengursoy.atlassian.net/browse/KAN-117) |
| Add the Sprint 2 burndown chart | The burndown chart for the whole sprint is taken from Jira and added to the sprint folder (`04-burndown-chart.md`). The current burndown is also shown in class every week. | – | – | To do | [KAN-118](https://yarengursoy.atlassian.net/browse/KAN-118) |
| Export the Jira backlog | The Jira backlog export is in `docs/backlog/` (Markdown with the Jira sync, or `.xlsx` if the sync does not work) before the 14/11/2026 upload. | – | – | To do | [KAN-119](https://yarengursoy.atlassian.net/browse/KAN-119) |
| Hold the Sprint 2 retrospective | `Markdown Template/05-sprint-2/02-sprint-2-retrospective.md` has an action and an owner for every "what went bad" row. | – | – | To do | [KAN-120](https://yarengursoy.atlassian.net/browse/KAN-120) |
| Write the Sprint 2 welcome page | `Markdown Template/05-sprint-2/README.md` gives the sprint goal, what was achieved, links to every Sprint 2 deliverable and the Git commit submitted on 14/11/2026. | – | – | To do | [KAN-121](https://yarengursoy.atlassian.net/browse/KAN-121) |
| Prepare the Sprint 2 demo | A demo of 10 minutes or less is rehearsed before the 18/11/2026 presentation. It shows the baseline returning the relevant provisions for at least one question from each of the four Annex III point 3 use cases, and the baseline score against the charter target. | – | – | To do | [KAN-122](https://yarengursoy.atlassian.net/browse/KAN-122) |
| Review the assigned team's Sprint 2 deliverables | Between 15/11 and 18/11/2026 every team member reviews part of the assigned team's deliverables on Confluence, starting from their welcome page, and one member installs and runs their system from their `README.md`; the review page is filled in. | – | – | To do | [KAN-123](https://yarengursoy.atlassian.net/browse/KAN-123) |
| Answer the reviewers and copy the review page | Every reviewer item is answered at the 18/11/2026 presentation (accepted, accepted with rework, or rejected with a reason), and the completed page is copied into `Markdown Template/05-sprint-2/03-sprint-2-review-page.md` for the Sprint 3 upload. | – | – | To do | [KAN-124](https://yarengursoy.atlassian.net/browse/KAN-124) |

Sub-task owners are assigned at the sprint planning.

**Traceability**

Deliverables: common sprint documents (Deliverables page, introduction); D6 and D7 are linked from the welcome page      
Milestone: M6 Checkpoint: go/no-go for the beta (18/11/2026)      
Major Activities: row 37      
Risk: R-07 Work falls behind

## S8 · Follow Sprint 3 from one welcome page

[KAN-171](https://yarengursoy.atlassian.net/browse/KAN-171) · Sprint 3 (Beta 0.5) · Priority Medium · Points – · Owner –

**Story:** As a Project Review Committee member, I want to open one welcome page that links to every Sprint 3 deliverable and shows the sprint goal, the results and the submitted commit, so that I can review the sprint without searching the repository.

**Acceptance criteria** (course "Every sprint" deliverables)

1. In the first week, the Sprint 2 retrospective actions are done, every Sprint 2 review item is answered and the accepted ones are addressed, and the team agrees on the DoR, DoD and a one-sentence sprint goal.
2. The Sprint 2 review page has an answer for every item and a link to the fix for every accepted item.
3. `07-sprint-3/README.md` gives the sprint goal, the results, links to every deliverable and the Git commit submitted on 05/12/2026.
4. The burndown chart, the Jira backlog export and the retrospective (an action and an owner for every "what went bad" row) are delivered.
5. The demo on 09/12/2026 takes 10 minutes or less; the team reviews its assigned team between 06/12 and 09/12/2026 and answers its own reviewers.

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Agree on the Sprint 3 DoR, DoD and sprint goal | In the first week of Sprint 3: the Sprint 2 retrospective actions are done; every Sprint 2 review item is answered and the accepted ones are addressed; the risk register and assumption checks are reviewed; EUR-Lex is checked for a newer consolidated version; the DoR, DoD and a one-sentence sprint goal are agreed and the goal is in Jira. | – | – | To do | [KAN-187](https://yarengursoy.atlassian.net/browse/KAN-187) |
| Answer the Sprint 2 review items with links to the fixes | The Sprint 2 review page has an answer for every item (accepted, accepted with rework, or rejected with a reason) and a link to the fix for every accepted item, before the 05/12/2026 upload. | – | – | To do | [KAN-188](https://yarengursoy.atlassian.net/browse/KAN-188) |
| Add the Sprint 3 burndown chart | The burndown chart for the whole sprint is taken from Jira and added to the Sprint 3 folder; the current burndown is shown in class every week. | – | – | To do | [KAN-189](https://yarengursoy.atlassian.net/browse/KAN-189) |
| Export the Jira backlog for Sprint 3 | The Jira backlog export is in `docs/backlog/` (Markdown with the Jira sync, or `.xlsx`) before the 05/12/2026 upload. | – | – | To do | [KAN-190](https://yarengursoy.atlassian.net/browse/KAN-190) |
| Hold the Sprint 3 retrospective | The Sprint 3 retrospective in the sprint folder has an action and an owner for every "what went bad" row. | – | – | To do | [KAN-191](https://yarengursoy.atlassian.net/browse/KAN-191) |
| Write the Sprint 3 welcome page | `Markdown Template/07-sprint-3/README.md` gives the sprint goal, what was achieved, links to every Sprint 3 deliverable and the Git commit submitted on 05/12/2026. | – | – | To do | [KAN-192](https://yarengursoy.atlassian.net/browse/KAN-192) |
| Prepare the Sprint 3 demo and do the reviews | A demo of 10 minutes or less is rehearsed for 09/12/2026; between 06/12 and 09/12/2026 every member reviews part of the assigned team's deliverables and one member runs their system from their README; every item from our own reviewers is answered and the completed review page is copied into the sprint folder. | – | – | To do | [KAN-193](https://yarengursoy.atlassian.net/browse/KAN-193) |

Sub-task owners are assigned at the sprint planning.

**Traceability**

Deliverables: common sprint documents; D8 and D9 are linked from the welcome page      
Milestone: M8 Checkpoint (09/12/2026)      
Major Activities: rows 32, 37, 38      
Risk: R-07 Work falls behind

## S9 · Follow Sprint 4 from one welcome page

[KAN-204](https://yarengursoy.atlassian.net/browse/KAN-204) · Sprint 4 (Release candidate 1.0) · Priority Medium · Points – · Owner –

**Story:** As a Project Review Committee member, I want to follow all of Sprint 4 from one welcome page, so that I can review the final product, its test results and the team's process without searching the repository.

**Acceptance criteria**

1. The Sprint 4 goal, DoR and DoD are written at the start of the sprint, together with the answers to the Sprint 3 retrospective and review, a risk and assumption check, and a check that the EUR-Lex version is still current.
2. Every story's test is run and its result reported by 23/12/2026.
3. The Sprint 4 technical summary reports the final system against the baseline and the charter targets.
4. The burndown chart, Jira export and retrospective are in the repository.
5. The welcome page links to every Sprint 4 document, and the final demo is given on 30/12/2026.

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Write the Sprint 4 goal, DoR and DoD with the Sprint 3 follow-ups | The Sprint 4 goal, DoR and DoD are written, with the answers to the Sprint 3 retrospective and review, a risk and assumption check, and a check that the EUR-Lex version is still current. | – | – | To do | [KAN-213](https://yarengursoy.atlassian.net/browse/KAN-213) |
| Run every story test and report the results | The test of every story is run on the release candidate and its result is reported by 23/12/2026. | – | – | To do | [KAN-214](https://yarengursoy.atlassian.net/browse/KAN-214) |
| Write the Sprint 4 technical summary | The Sprint 4 technical summary reports the story tests and compares the final system with the baseline and the charter targets. | – | – | To do | [KAN-215](https://yarengursoy.atlassian.net/browse/KAN-215) |
| Add the Sprint 4 burndown, Jira export and retrospective | The Sprint 4 burndown chart, Jira export and retrospective notes are in the repository. | – | – | To do | [KAN-216](https://yarengursoy.atlassian.net/browse/KAN-216) |
| Write the Sprint 4 welcome page | The Sprint 4 welcome page links to every Sprint 4 document. | – | – | To do | [KAN-217](https://yarengursoy.atlassian.net/browse/KAN-217) |
| Give the final demo | The release candidate is demonstrated live on 30/12/2026. | – | – | To do | [KAN-218](https://yarengursoy.atlassian.net/browse/KAN-218) |

Sub-task owners are assigned at the sprint planning.

**Traceability**

Deliverable: D11 Release Candidate and Final Evaluation (due 30/12/2026)        
Milestone: M10 (30/12/2026)        
Major Activities: sprint reporting rows
