# Story Requirements for Epic KAN-28: Evaluation

Version v2, Sprint 2 (08/11/2026). Source: Jira project KAN on 08/11/2026. Version v1 (27/10/2026) is in the Git history; what changed since then is listed at the end of this page. Back to the [User Story Map v2](02-user-story-map-v2.md) · [all story requirements pages](README.md).

| Epic | Evaluation |
|---|---|
| Summary | Everything that measures the assistant: the Q&A Generation-Dataset v1 (D2, Sprint 2) and v2 (D8, Sprint 3) with the evaluation rubric and data card, the evaluation runs on the `val` split, the pilot (D10) and the final evaluation on the held-out `test` split (D11) in Sprint 4, whose stories and tasks sit in the product epics: [KAN-72](https://yarengursoy.atlassian.net/browse/KAN-72) and the task [KAN-202](https://yarengursoy.atlassian.net/browse/KAN-202) (pilot), [KAN-77](https://yarengursoy.atlassian.net/browse/KAN-77) and the task [KAN-75](https://yarengursoy.atlassian.net/browse/KAN-75) (`test` split). |
| Features | Q&A datasets (D2, D8), rubric, evaluation runs on the `val` split |
| Document Owner | Yeşim (Product Owner) |
| Designer | Not applicable: this epic produces documents, not a user interface |
| Developers | Yeşim, Gözde Nur, Kaan, Yaren so far; later work is assigned at each sprint planning |
| Release Target (Sprint) | Sprint 2 (Alpha 0.1); Sprint 3 (Beta 0.5) |
| Traceability | Objectives: O1–O4. Major Activities rows 3, 23–27. |
| Jira | [KAN-28](https://yarengursoy.atlassian.net/browse/KAN-28) |

## Requirements

For more info you can visit: https://www.atlassian.com/agile/product-management/requirements.

### User stories

| # | User story title | User story description | Priority | Points | Owner | Sprint | Notes | Jira |
|---|---|---|---|---|---|---|---|---|
| S1 | [Test the assistant on in-scope questions checked against the official text](#s1--test-the-assistant-on-in-scope-questions-checked-against-the-official-text) | As an EdTech AI developer, I want the assistant to be tested on in-scope questions about the four education use cases, each checked against the official text, so that I can see how often it cites the expected provision before I rely on it for my own product. | High | 13 | Yeşim | Sprint 2 | Release: Alpha 0.1; Status: In progress. | [KAN-65](https://yarengursoy.atlassian.net/browse/KAN-65) |
| S2 | [Test the assistant's safety responses against a written rubric](#s2--test-the-assistants-safety-responses-against-a-written-rubric) | As a compliance officer in an EdTech provider's legal team, I want the assistant to be tested on legal-decision, out-of-scope, insufficient-evidence and adversarial questions, scored against a written rubric, so that I know how it responds when users ask beyond its limits. | High | 5 | Kaan | Sprint 2 | Release: Alpha 0.1; Status: To do. | [KAN-83](https://yarengursoy.atlassian.net/browse/KAN-83) |

### Tasks

Work that serves the users but is not a user goal of its own: evaluations, documents and delivery work. Since the Sprint 1 review (comment 3), such work is a Jira task, linked to the user stories it serves where there is one.

| # | Task | Purpose | Related user stories | Points | Owner | Sprint | Jira |
|---|---|---|---|---|---|---|---|
| T1 | [Extend the question set for the beta](#t1--extend-the-question-set-for-the-beta) | Extend the evaluation question set to v2 with new questions from the baseline errors, so that the beta is measured on more cases while the held-out test questions stay untouched. | [KAN-65](https://yarengursoy.atlassian.net/browse/KAN-65), [KAN-83](https://yarengursoy.atlassian.net/browse/KAN-83) | – | – | Sprint 3 | [KAN-170](https://yarengursoy.atlassian.net/browse/KAN-170) |

Priority, points, owner and sprint are as in Jira on 08/11/2026. Points are given with planning poker at each sprint planning; a dash means not estimated yet. Every current user story has test cases, written in Sprint 2 ([KAN-114](https://yarengursoy.atlassian.net/browse/KAN-114)); they are planned tests to run when the story is built, not results.

## S1 · Test the assistant on in-scope questions checked against the official text

[KAN-65](https://yarengursoy.atlassian.net/browse/KAN-65) · User story · Sprint 2 (Alpha 0.1) · Status In progress · Priority High · Points 13 · Owner Yeşim

**Story:** As an EdTech AI developer, I want the assistant to be tested on in-scope questions about the four education use cases, each checked against the official text, so that I can see how often it cites the expected provision before I rely on it for my own product.

**Acceptance criteria**

1. Each of the four Annex III point 3 use cases has at least 3 questions, and each question type (direct lookup, condition/exception, multi-provision, follow-up, boundary case) has at least 2 questions (D2 criteria 2–3). Follow-up questions stay in the set; they count towards the O2 and O4 results only if Feature 7 ([KAN-6](https://yarengursoy.atlassian.net/browse/KAN-6)) is built, and otherwise their results are reported separately.
2. Every in-scope question has a gold answer and at least one gold source at provision level (Article, paragraph or Annex point), checked against the official text (D2 criterion 5).
3. Every gold source appears in the D3 provision list; any missing provision is added to the list on 11/11/2026 (D3 criteria 3–4).
4. Every question records its origin; if an LLM helped write a question, the model and prompt are recorded (D2 criterion 6).
5. Every question is checked by a team member other than its author, and 0 questions remain flagged as unresolved (D2 criterion 7).
6. At least one third of the questions are marked `test`, the rest `val`; every question has a unique ID; follow-up pairs are in the same split; the `test` split is frozen on 11/11/2026 (D2 criteria 1, 8, 10).
7. The data card fills every section of the course's Q&A data report template (D2 criterion 14).

**Test cases**

Planned checks of question set v1 (D2); run before the D2 upload, results recorded in the data card.

* **TC-65.1** (criterion 1) Steps: count the questions in `docs/eval/eval-set-v1.csv` per use case and per question type. Expected: at least 3 per use case and at least 2 per question type; follow-up questions are present and marked, and their results are reported separately while Feature 7 ([KAN-6](https://yarengursoy.atlassian.net/browse/KAN-6)) is not built.
* **TC-65.2** (criterion 2) Steps: for every in-scope question, open each gold source in the official text. Expected: every in-scope question has a gold answer and at least one gold source at provision level, and the gold answer is stated in it.
* **TC-65.3** (criterion 3) Steps: compare every gold source with `data/provision-list.csv`. Expected: every gold source is in the list. A gold source that is not in the list is a failed check: it is recorded as a finding, and the provision is added only through a recorded scope decision (as in decision Q-20 of the data card) on 11/11/2026, after which the check is run again and passes.
* **TC-65.4** (criterion 4) Steps: check the origin column of every row; for every LLM-assisted question, check the model and prompt columns. Expected: every row has an origin; every LLM-assisted row has its model and prompt.
* **TC-65.5** (criterion 5) Steps: check the reviewer column against the author column. Expected: every question has a reviewer other than its author; 0 questions are flagged as unresolved.
* **TC-65.6** (criterion 6) Steps: count the `test` and `val` rows; check that IDs are unique; check that each follow-up pair has one split; check the commit that froze `test`. Expected: at least one third are `test`; IDs are unique; follow-up pairs are in the same split; `test` is frozen on 11/11/2026.
* **TC-65.7** (criterion 7) Steps: compare the data card with the sections of the course's Q&A data report template. Expected: every section is filled.

**Sub-tasks**

| Sub-task | Done when | Owner | Status | Jira |
|---|---|---|---|---|
| Write evaluation questions for use case (a) admission | 4-5 in-scope questions for use case (a) are in docs/eval/eval-set-v1.csv. Each has a question type, gold answer, gold source and origin; if an LLM helped write a question, the model and prompt are recorded. The questions include at least 1 direct lookup, 1 condition/exception and 2 boundary cases (for example Article 5(1)(f), Article 50(1)). Start from the scenarios in [KAN-10](https://yarengursoy.atlassian.net/browse/KAN-10) (emotion detection, Art. 5(1)(f): boundary case), [KAN-11](https://yarengursoy.atlassian.net/browse/KAN-11) (tutor chatbot, Art. 50(1): boundary case) and [KAN-12](https://yarengursoy.atlassian.net/browse/KAN-12) (admission ranking, Art. 6(3) and 6(4): condition/exception); record "adapted from [KAN-10](https://yarengursoy.atlassian.net/browse/KAN-10)/11/12" in the origin column. | Yeşim | To do | [KAN-45](https://yarengursoy.atlassian.net/browse/KAN-45) |
| Write evaluation questions for use case (b) learning-outcome assessment | 4-5 in-scope questions for use case (b) are in docs/eval/eval-set-v1.csv. Each has a question type, gold answer, gold source and origin; if an LLM helped write a question, the model and prompt are recorded. The questions include at least 1 direct lookup, 1 condition/exception and 2 multi-provision questions. | Gözde Nur | Done | [KAN-46](https://yarengursoy.atlassian.net/browse/KAN-46) |
| Write evaluation questions for use case (c) level placement | 4-5 in-scope questions for use case (c) are in docs/eval/eval-set-v1.csv. Each has a question type, gold answer, gold source and origin; if an LLM helped write a question, the model and prompt are recorded. The questions include at least 1 follow-up question, which names the ID of the question it follows; follow-up questions count towards the O2 and O4 results only if Feature 7 ([KAN-6](https://yarengursoy.atlassian.net/browse/KAN-6)) is built, and otherwise their results are reported separately. Together with the use case (a), (b) and (d) sub-tasks ([KAN-45](https://yarengursoy.atlassian.net/browse/KAN-45), [KAN-46](https://yarengursoy.atlassian.net/browse/KAN-46), [KAN-66](https://yarengursoy.atlassian.net/browse/KAN-66)), there are 15-19 in-scope questions. | Kaan | To do | [KAN-47](https://yarengursoy.atlassian.net/browse/KAN-47) |
| Select and adapt at least 5 questions from published work on the EU AI Act | By 04/11/2026, the licence of the AI Act Evaluation Benchmark (Davvetas et al., 2026) is re-checked, and at least 5 questions are taken or adapted from its question-answer file or scenarios (or from other published work if fewer are usable), each based on a provision in the D3 provision list. Each question records its source, attribution and, if an LLM helped adapt it, the model and prompt in the origin column. Each one is checked against the official text like any other question. These questions count inside the 20-30 questions, not on top of them. | Yeşim | Done | [KAN-48](https://yarengursoy.atlassian.net/browse/KAN-48) |
| Check the gold sources of all evaluation questions against the official text | Every in-scope question has at least one gold source at provision level (Article, paragraph or Annex point), checked against the official text. Questions that would need a legal interpretation beyond the text are rewritten or removed, and the change is logged. | Yeşim | To do | [KAN-51](https://yarengursoy.atlassian.net/browse/KAN-51) |
| Cross-check the evaluation questions and resolve the flags | Every question is checked by a team member other than its author. No question remains flagged as unresolved. Rewritten or removed questions are logged. | Yaren | To do | [KAN-52](https://yarengursoy.atlassian.net/browse/KAN-52) |
| Split the evaluation set into val and test and freeze the test split | * At least one third of the questions are marked `test`, with at least 1 question of each safety category. • Follow-up pairs are in the same split. • Every question has a unique ID. • The `test` questions are stored apart from the `val` questions and frozen on 11/11/2026. | Gözde Nur | To do | [KAN-53](https://yarengursoy.atlassian.net/browse/KAN-53) |
| Write evaluation questions for use case (d) exam monitoring | 3-4 in-scope questions for use case (d) are in docs/eval/eval-set-v1.csv. Each has a question type, gold answer, gold source and origin; if an LLM helped write a question, the model and prompt are recorded. The questions include at least 1 follow-up question, which names the ID of the question it follows; follow-up questions count towards the O2 and O4 results only if Feature 7 ([KAN-6](https://yarengursoy.atlassian.net/browse/KAN-6)) is built, and otherwise their results are reported separately. Together with the use case (a), (b) and (c) sub-tasks ([KAN-45](https://yarengursoy.atlassian.net/browse/KAN-45), [KAN-46](https://yarengursoy.atlassian.net/browse/KAN-46), [KAN-47](https://yarengursoy.atlassian.net/browse/KAN-47)), there are 15-19 in-scope questions. Start from the scenario in [KAN-13](https://yarengursoy.atlassian.net/browse/KAN-13) (proctoring tool: Annex III point 3(d), Art. 14(4), application date in Art. 113); record "adapted from [KAN-13](https://yarengursoy.atlassian.net/browse/KAN-13)" in the origin column. | Yaren | Done | [KAN-66](https://yarengursoy.atlassian.net/browse/KAN-66) |
| Map the provision list to the D2 questions | Every gold source in docs/eval/eval-set-v1.csv appears in the D3 provision list, and any missing provision has been added to the list. Every provision in the list is used by at least one D2 question or has a one-line reason for inclusion. | Kaan | To do | [KAN-84](https://yarengursoy.atlassian.net/browse/KAN-84) |
| Write the D2 data card | `Markdown Template/11-datasheets/03-qa-data-report.md` fills every section of the course's Q&A data report template, following Gebru et al. It states how the questions were written, how their source provisions were chosen from the D3 provision list, and names the exact model for every question an LLM helped write. It also has a decision log that records every decision that shaped the question set (sources, selection, adaptation, exclusions and the val/test split) with its reason; each decision is logged when it is made, not afterwards. | Yeşim | In progress | [KAN-85](https://yarengursoy.atlassian.net/browse/KAN-85) |

**Traceability**

Deliverable: D2 Q&A Generation-Dataset v1 (due 11/11/2026)  
Milestone: M4 Baseline (alpha) runs on the full validation question set (18/11/2026)  
Objective: O2 Evidence  
Major Activities: row 3  
Dependencies: rows 1, 2  
Assumption / Risk: A-03 / R-10 The law is unclear for some questions

## S2 · Test the assistant's safety responses against a written rubric

[KAN-83](https://yarengursoy.atlassian.net/browse/KAN-83) · User story · Sprint 2 (Alpha 0.1) · Status To do · Priority High · Points 5 · Owner Kaan

**Story:** As a compliance officer in an EdTech provider's legal team, I want the assistant to be tested on legal-decision, out-of-scope, insufficient-evidence and adversarial questions, scored against a written rubric, so that I know how it responds when users ask beyond its limits.

**Acceptance criteria**

1. At least 11 safety questions: at least 2 out-of-scope, 2 insufficient-evidence, 2 legal-decision and 5 inappropriate or adversarial inputs (D2 criterion 4).
2. Every safety question has an expected behaviour (answer, abstain, refuse or redirect) (D2 criterion 5).
3. The `test` split holds at least 1 question of each safety category (D2 criterion 11).
4. 0 questions contain personal data; questions about personal data use synthetic placeholders (D2 criterion 9).
5. `docs/eval/rubric.md` defines "fully supported" and each expected behaviour, with at least one example for each (D2 criterion 12).

**Test cases**

Planned checks of the safety questions in question set v1 (D2); run before the D2 upload, results recorded in the data card.

* **TC-83.1** (criterion 1) Steps: count the safety questions per category in `docs/eval/eval-set-v1.csv`. Expected: at least 2 out-of-scope, 2 insufficient-evidence, 2 legal-decision and 5 adversarial or inappropriate; at least 11 in total.
* **TC-83.2** (criterion 2) Steps: check the expected-behaviour column of every safety question. Expected: each has one of answer, abstain, refuse or redirect.
* **TC-83.3** (criterion 3) Steps: count the `test` safety questions per category. Expected: at least 1 in each category.
* **TC-83.4** (criterion 4) Steps: read every question for names, e-mail addresses, phone numbers or other personal data. Expected: none; questions about personal data use synthetic placeholders.
* **TC-83.5** (criterion 5) Steps: read `docs/eval/rubric.md`. Expected: it defines "fully supported" and each expected behaviour, with at least one example for each.

**Sub-tasks**

| Sub-task | Done when | Owner | Status | Jira |
|---|---|---|---|---|
| Write the safety evaluation questions | At least 11 safety questions are in docs/eval/eval-set-v1.csv, each with its expected behaviour and origin: • 2 out-of-scope • 2 insufficient-evidence • 2 legal-decision • 5 inappropriate or adversarial inputs (circumvention, concealment, prompt injection, and requests with synthetic personal-data placeholders) A safety question may mention a use case, but it is counted once, as a safety question. No question contains real personal data. | Yeşim | To do | [KAN-49](https://yarengursoy.atlassian.net/browse/KAN-49) |
| Write the evaluation rubric | docs/eval/rubric.md defines "fully supported" and each expected behaviour (answer, abstain, refuse, redirect), with at least one example for each. | Kaan | To do | [KAN-50](https://yarengursoy.atlassian.net/browse/KAN-50) |

**Traceability**

Deliverable: D2 Q&A Generation-Dataset v1 (due 11/11/2026)  
Milestone: M4 Baseline (alpha) runs on the full validation question set (18/11/2026)  
Objectives: O4 Safety; O2 Evidence (b) (the rubric defines "fully supported")  
Major Activities: row 3  
Constraint: C-08 Information, not legal advice

## T1 · Extend the question set for the beta

[KAN-170](https://yarengursoy.atlassian.net/browse/KAN-170) · Task · Sprint 3 (Beta 0.5) · Status To do · Priority High · Points – · Owner –

**Purpose:** Extend the evaluation question set to v2 with new questions from the baseline errors, so that the beta is measured on more cases while the held-out test questions stay untouched.

**Related user stories:** [KAN-65](https://yarengursoy.atlassian.net/browse/KAN-65), [KAN-83](https://yarengursoy.atlassian.net/browse/KAN-83)

**Acceptance criteria**

1. `docs/eval/eval-set-v2.csv` has at least 40 questions, including at least 5 new questions derived from the baseline evaluation findings; `eval-set-v1.csv` is unchanged (D8 criteria 1, 6).
2. Each split holds at least 3 application-date questions and at least 2 questions in each safety category, with at least 16 safety questions in total; follow-up pairs are in the same split (D8 criterion 2).
3. Every in-scope question has a gold answer and gold source; every other question has an expected behaviour (D8 criterion 3).
4. The `val` split is frozen on 01/12/2026; new `test` questions are fixed by 05/12/2026 and the original `test` questions are unchanged (D8 criteria 4, 5).
5. The data card's change log lists every added, edited or excluded question and why (D8 criterion 6; course Sprint 3 deliverable).

**Sub-tasks**

| Sub-task | Done when | Owner | Status | Jira |
|---|---|---|---|---|
| Add new questions from the baseline errors | `docs/eval/eval-set-v2.csv` has at least 40 questions, including at least 5 new ones derived from the baseline evaluation findings, each with a gold answer and gold source or an expected behaviour; `eval-set-v1.csv` is unchanged. | – | To do | [KAN-183](https://yarengursoy.atlassian.net/browse/KAN-183) |
| Balance the question categories in each split | Each split holds at least 3 application-date questions and at least 2 questions in each safety category; there are at least 16 safety questions in total; the four use cases are represented; follow-up pairs are in the same split. | – | To do | [KAN-184](https://yarengursoy.atlassian.net/browse/KAN-184) |
| Freeze the val split and fix the new test questions | The `val` split is frozen on 01/12/2026; new `test` questions are fixed in the repository by 05/12/2026 and are not used for tuning; the original `test` questions are unchanged and the split stays identifiable. | – | To do | [KAN-185](https://yarengursoy.atlassian.net/browse/KAN-185) |
| Update the data card change log | `Markdown Template/11-datasheets/03-qa-data-report.md` lists every added, edited or excluded question and why, and says what changed from v1. | – | To do | [KAN-186](https://yarengursoy.atlassian.net/browse/KAN-186) |

**Traceability**

Deliverable: D8 Q&A Generation-Dataset v2 (due 05/12/2026)  
Milestone: M7 (09/12/2026)  
Objectives: O2 Evidence; O4 Safety  
Major Activities: row 25  
Assumption / Risk: A-03 / R-10

## Changes since v1 (27/10/2026)

- [KAN-65](https://yarengursoy.atlassian.net/browse/KAN-65) Test the assistant on in-scope questions checked against the official text: test cases TC-65.1 to TC-65.7 added on 08/11/2026 ([KAN-114](https://yarengursoy.atlassian.net/browse/KAN-114)).
- [KAN-83](https://yarengursoy.atlassian.net/browse/KAN-83) Test the assistant's safety responses against a written rubric: test cases TC-83.1 to TC-83.5 added on 08/11/2026 ([KAN-114](https://yarengursoy.atlassian.net/browse/KAN-114)).
- [KAN-170](https://yarengursoy.atlassian.net/browse/KAN-170) Extend the question set for the beta: changed from a user story to a task on 07/11/2026 (Sprint 1 review, comment 3).
