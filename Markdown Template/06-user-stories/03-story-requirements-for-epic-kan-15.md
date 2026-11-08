# Story Requirements for Epic KAN-15: Ask

Version v2, Sprint 2 (08/11/2026). Source: Jira project KAN on 08/11/2026. Version v1 (27/10/2026) is in the Git history; what changed since then is listed at the end of this page. Back to the [User Story Map v2](02-user-story-map-v2.md) · [all story requirements pages](README.md).

| Epic | Ask |
|---|---|
| Summary | How a user puts a question to the assistant: in their own words, without article numbers or legal terms (Feature 1), on the one-page web interface run from `README.md` ([KAN-21](https://yarengursoy.atlassian.net/browse/KAN-21)), and, only if time allows, starting from example questions or a chosen use case (Feature 5, [KAN-20](https://yarengursoy.atlassian.net/browse/KAN-20) in the backlog). |
| Features | F1 Ask in their own words · F5 Guided start (backlog) |
| Document Owner | Yeşim (Product Owner) |
| Designer | Gözde Nur (design decisions, KAN-58) and Kaan (design document, KAN-59) |
| Developers | Assigned at each sprint planning |
| Release Target (Sprint) | Sprint 3 (Beta 0.5); backlog: KAN-20 (only if time allows) |
| Traceability | Objectives: O1 Search time; O3 Understanding. Major Activities rows 10, 14. Constraints: C-02, C-04. |
| Jira | [KAN-15](https://yarengursoy.atlassian.net/browse/KAN-15) |

## Requirements

For more info you can visit: https://www.atlassian.com/agile/product-management/requirements.

### User stories

| # | User story title | User story description | Role (ISO/IEC 5339) | Priority | Points | Owner | Sprint | Notes | Jira |
|---|---|---|---|---|---|---|---|---|---|
| S1 | [Ask about my product in my own words](#s1--ask-about-my-product-in-my-own-words) | As an EdTech AI developer new to the AI Act, I want to describe my product and ask my question in my own words, so that I can find the relevant provisions without knowing article numbers or legal terms. | AI user | High | – | – | Sprint 3 | Release: Beta 0.5; Feature: F1; Status: To do. | [KAN-19](https://yarengursoy.atlassian.net/browse/KAN-19) |
| S2 | [Use the assistant in my browser](#s2--use-the-assistant-in-my-browser) | As a technical lead taking part in the pilot, I want to open the assistant in a web browser without installing anything, so that I can try it during the pilot with my own questions. | AI user | High | – | – | Sprint 3 | Release: Beta 0.5; Feature: Interface; Status: To do; Depends on [KAN-168](https://yarengursoy.atlassian.net/browse/KAN-168) (the whole pipeline runs from one README). | [KAN-21](https://yarengursoy.atlassian.net/browse/KAN-21) |
| S3 | [Start from example questions or my use case](#s3--start-from-example-questions-or-my-use-case) | As an EdTech AI developer new to the AI Act, I want to start from example questions and optionally choose my education use case from a list, so that I can ask a useful first question without knowing legal terms. | AI user | Low | – | – | Backlog | Feature: F5; Status: To do; Not committed (Feature 5); built only if time allows. | [KAN-20](https://yarengursoy.atlassian.net/browse/KAN-20) |

Priority, points, owner and sprint are as in Jira on 08/11/2026. Points are given with planning poker at each sprint planning; a dash means not estimated yet. The roles are the ISO/IEC 5339 stakeholder roles from the [User Story Map v2](02-user-story-map-v2.md) ([KAN-116](https://yarengursoy.atlassian.net/browse/KAN-116)). Every current user story has test cases, written in Sprint 2 ([KAN-114](https://yarengursoy.atlassian.net/browse/KAN-114)); they are planned tests to run when the story is built, not results.

## S1 · Ask about my product in my own words

[KAN-19](https://yarengursoy.atlassian.net/browse/KAN-19) · User story · Sprint 3 (Beta 0.5) · Status To do · Priority High · Points – · Owner –

**Story:** As an EdTech AI developer new to the AI Act, I want to describe my product and ask my question in my own words, so that I can find the relevant provisions without knowing article numbers or legal terms.

**Acceptance criteria**

1. When a user asks an in-scope question in everyday words without naming an article (for example, "Our AI grades exams. What applies?"), the assistant shall identify and cite the relevant in-scope provisions that address the described use case (for example, Annex III point 3(b)), without classifying the user's product.
2. When the assistant links a product described in everyday words to an in-scope use case, the assistant shall state in one sentence how the user's description relates to the wording of the retrieved provision, where supported by the source text (for example, "grading exams" relates to "evaluate learning outcomes" in Annex III point 3(b)).
3. If a question is not in English, then the assistant shall state in one sentence that it answers questions in English only.
4. For the in-scope questions in the frozen D8 `val` split that name no article, the share whose expected provision is among the cited provisions shall be reported separately in the Sprint 3 technical summary.

**Test cases**

Planned tests, not results: each is run when the story is built, and its result is recorded in the Sprint 3 technical summary.

* **TC-19.1** (criteria 1, 2) Input: "Our AI grades exams. What applies?" Expected: Annex III point 3(b) is cited; one sentence relates "grades exams" to "evaluate learning outcomes" in Annex III point 3(b); the product is not classified.
* **TC-19.2** (criteria 1, 2) Input: "Our app decides which English class level a new student joins. What should we look at?" Expected: Annex III point 3(c) is cited; one sentence relates "decides which class level" to the wording of point 3(c); the product is not classified.
* **TC-19.3** (criterion 3) Input: "Sınavları puanlayan yapay zekâ aracımız için hangi kurallar geçerli?" (Turkish). Expected: one sentence that the assistant answers questions in English only; no provision cited.
* **TC-19.4** (criterion 4) Steps: run the in-scope questions of the frozen D8 `val` split that name no article; for each, check whether the expected provision is among the cited provisions. Expected: the share is reported separately in the Sprint 3 technical summary.

**Sub-tasks**

| Sub-task | Done when | Owner | Status | Jira |
|---|---|---|---|---|
| Link everyday descriptions to the use case wording | For an in-scope question that names no article, the answer cites the relevant in-scope provision and states in one sentence how the user's words relate to its wording (for example "grading exams" relates to "evaluate learning outcomes" in Annex III point 3(b)), without classifying the product. | – | To do | [KAN-137](https://yarengursoy.atlassian.net/browse/KAN-137) |
| Answer non-English questions with the English-only notice | A question that is not in English gets a one-sentence notice that the assistant answers questions in English only. | – | To do | [KAN-138](https://yarengursoy.atlassian.net/browse/KAN-138) |
| Report the expected-provision rate for questions that name no article | For the in-scope questions in the frozen D8 `val` split that name no article, the share whose expected provision is among the cited provisions is reported separately in the Sprint 3 technical summary. | – | To do | [KAN-139](https://yarengursoy.atlassian.net/browse/KAN-139) |

**Traceability**

Feature: Feature 1 - Ask in their own words  
Objectives: O1 Search time; O3 Understanding; O2 Evidence (a) (supporting)  
Deliverable: D9 Beta Release (due 05/12/2026)  
Milestone: M7 (09/12/2026)  
Major Activities: row 10  
Constraints: C-02 English only; C-04 Education use cases only; follow-ups within one session

## S2 · Use the assistant in my browser

[KAN-21](https://yarengursoy.atlassian.net/browse/KAN-21) · User story · Sprint 3 (Beta 0.5) · Status To do · Priority High · Points – · Owner –

**Story:** As a technical lead taking part in the pilot, I want to open the assistant in a web browser without installing anything, so that I can try it during the pilot with my own questions.

**Acceptance criteria**

1. When the assistant has been started from `README.md`, its page shall show the question box in a current desktop browser without asking the user for an installation or an account.
2. While the assistant is preparing an answer, the assistant shall show that the answer is being prepared.
3. If the assistant cannot produce an answer because of a system error, then the assistant shall show an error message without technical details and let the user submit another question.
4. On the computer used for the pilot, the median answer time on the frozen D8 `val` questions shall be measured and recorded against the answer-time limit in the design document (D9 criterion 7).

**Test cases**

Planned tests, not results: each is run when the story is built, and its result is recorded in the Sprint 3 technical summary (TC-21.5 on the pilot computer).

* **TC-21.1** (criterion 1) Precondition: the assistant is started on a team computer by following only `README.md`. Steps: open the page in a current desktop browser (Chrome or Firefox). Expected: the question box is shown; no installation, account or login is asked for.
* **TC-21.2** (criterion 2) Steps: submit an in-scope question. Expected: until the answer appears, the page shows that the answer is being prepared.
* **TC-21.3** (criterion 3) Steps: stop the answer-generation service; submit a question. Expected: an error message without technical details (no stack trace, path or code); the question box stays usable.
* **TC-21.4** (criterion 3) Precondition: TC-21.3. Steps: restart the service; submit another question in the same page. Expected: it is answered normally.
* **TC-21.5** (criterion 4) Steps: on the pilot computer, send every question of the frozen D8 `val` split and record each answer time. Expected: the median answer time is recorded and compared with the answer-time limit in the design document (D9 criterion 7).

**Sub-tasks**

| Sub-task | Done when | Owner | Status | Jira |
|---|---|---|---|---|
| Build the one-page interface | A single page has a question box and an answer view that shows the answer with its citations and the version date (Features 1–3), and space for the permanent not-legal-advice notice ([KAN-2](https://yarengursoy.atlassian.net/browse/KAN-2)) and the personal-data reminder ([KAN-26](https://yarengursoy.atlassian.net/browse/KAN-26)); the interface technology is the one recorded in the design document. | – | To do | [KAN-154](https://yarengursoy.atlassian.net/browse/KAN-154) |
| Open the assistant without installation or an account | On the computer that runs the assistant from `README.md`, its page opens the question box in a current desktop browser without asking for an installation or an account. | – | To do | [KAN-160](https://yarengursoy.atlassian.net/browse/KAN-160) |
| Show that the answer is being prepared | While an answer is being prepared, the page shows that it is being prepared. | – | To do | [KAN-161](https://yarengursoy.atlassian.net/browse/KAN-161) |
| Show a plain error message on a system error | If an answer cannot be produced because of a system error, the page shows an error message without technical details and lets the user submit another question. | – | To do | [KAN-162](https://yarengursoy.atlassian.net/browse/KAN-162) |
| Measure the answer time on the pilot computer | On the computer that will be used for the pilot, the median answer time on the frozen D8 `val` questions is measured and recorded against the answer-time limit in the design document by 09/12/2026, so that the pilot's timed tasks are not slowed by the system. | – | To do | [KAN-163](https://yarengursoy.atlassian.net/browse/KAN-163) |

**Traceability**

Feature: Web interface supporting Features 1–4 and 6 (Major Activities row 14)  
Objectives: O1 Search time; O3 Understanding (measured in the D10 pilot)  
Deliverable: D9 Beta Release (due 05/12/2026)  
Milestone: M7 (09/12/2026)  
Major Activities: row 29  
Constraints: C-05 CPU only; C-10 No personal data requested; conversation deleted when the session ends  
Risks: R-09 The system does not install on the pilot computer; R-12 The answer time does not meet the limit on the pilot computer

## S3 · Start from example questions or my use case

[KAN-20](https://yarengursoy.atlassian.net/browse/KAN-20) · User story · Backlog (not committed) · Status To do · Priority Low · Points – · Owner –

**Story:** As an EdTech AI developer new to the AI Act, I want to start from example questions and optionally choose my education use case from a list, so that I can ask a useful first question without knowing legal terms.

**Built only if time allows** (backlog; Feature 5 is not committed in the charter).

**Acceptance criteria**

1. The assistant shall show at least four example questions, at least one for each Annex III point 3 use case (admission, assessment, level placement, exam monitoring).
2. When the user selects an example question, the assistant shall send it as a question and answer it.
3. Where the use-case list is shown, the assistant shall offer the four Annex III point 3 use cases and "Not sure", and choosing one shall be optional.
4. When a user has chosen a use case and asks a question, the assistant shall use the choice as context for that question; if the question describes a different use case, the assistant shall follow the question; in neither case shall it treat the choice as a legal classification. If the user selects "Not sure", the assistant shall not assume a use case.
5. The example questions shall not be taken from the held-out `test` split of the evaluation set.

**Test cases**

Built only if time allows; these tests are run only if the story is taken into a sprint.

* **TC-20.1** (criterion 1) Steps: open the assistant's page. Expected: at least four example questions are shown, with at least one for each Annex III point 3 use case (admission, assessment, level placement, exam monitoring).
* **TC-20.2** (criterion 2) Steps: select one example question. Expected: it is sent as a question and answered, without the user typing it.
* **TC-20.3** (criterion 3) Steps: open the use-case list; then ask a question without choosing from it. Expected: the list offers the four use cases and "Not sure"; the question is answered without a choice.
* **TC-20.4** (criterion 4) Steps: choose "Admission"; ask "Which provisions relate to our tool?"; then ask "Our tool also flags cheating in online exams. Which provisions relate to that?" Expected: the first answer uses admission (Annex III point 3(a)) as context; the second follows the question (Annex III point 3(d)); neither answer says the tool is high-risk.
* **TC-20.5** (criterion 4) Steps: choose "Not sure"; ask "Which provisions relate to our tool?" Expected: the answer does not assume a use case; it asks for or names the use cases instead.
* **TC-20.6** (criterion 5) Steps: compare the text of every example question with the questions of the held-out `test` split in the evaluation set. Expected: no example question is a `test` question.

**Sub-tasks**

*No sub-tasks yet: they are written at the sprint planning.*

**Traceability**

Feature: Feature 5 - Guided start (not committed; built only if time allows)  
Objectives: O1 Search time; O3 Understanding  
Constraint: C-08 Information, not legal advice

## Changes since v1 (27/10/2026)

- [KAN-19](https://yarengursoy.atlassian.net/browse/KAN-19) Ask about my product in my own words: test cases TC-19.1 to TC-19.4 added on 08/11/2026 ([KAN-114](https://yarengursoy.atlassian.net/browse/KAN-114)).
- [KAN-20](https://yarengursoy.atlassian.net/browse/KAN-20) Start from example questions or my use case: test cases TC-20.1 to TC-20.6 added on 08/11/2026 ([KAN-114](https://yarengursoy.atlassian.net/browse/KAN-114)).
- [KAN-21](https://yarengursoy.atlassian.net/browse/KAN-21) Use the assistant in my browser: test cases TC-21.1 to TC-21.5 added on 08/11/2026 ([KAN-114](https://yarengursoy.atlassian.net/browse/KAN-114)).
