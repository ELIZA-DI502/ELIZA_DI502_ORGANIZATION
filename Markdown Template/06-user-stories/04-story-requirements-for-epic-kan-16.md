# Story Requirements for Epic KAN-16: Find and Understand

Version v2, Sprint 2 (08/11/2026). Source: Jira project KAN on 08/11/2026. Version v1 (27/10/2026) is in the Git history; what changed since then is listed at the end of this page. Back to the [User Story Map v2](02-user-story-map-v2.md) · [all story requirements pages](README.md).

| Epic | Find and Understand |
|---|---|
| Summary | Finding the in-scope provisions for the user's education use case with their references and version date (Feature 2), including application dates, explaining them in plain language with their conditions and exceptions (Feature 3), and the pilot that measures whether users find the provisions faster and understand the answers (O1, O3; D10). Follow-up questions in one session (Feature 7, [KAN-6](https://yarengursoy.atlassian.net/browse/KAN-6)) are in the backlog and built only if time allows. |
| Features | F2 Find the relevant provisions · F3 Plain-language answer · F7 Follow-up questions (backlog) |
| Document Owner | Yeşim (Product Owner) |
| Designer | Gözde Nur (design decisions, KAN-58) and Kaan (design document, KAN-59) |
| Developers | Yeşim, Yaren, Gözde Nur, Kaan so far; later work is assigned at each sprint planning |
| Release Target (Sprint) | Sprint 2 (Alpha 0.1); Sprint 3 (Beta 0.5); Sprint 4 (Release candidate 1.0); backlog: KAN-6 (only if time allows) |
| Traceability | Objectives: O1 Search time; O2 Evidence; O3 Understanding. Major Activities rows 9, 10, 26. Constraints: C-01, C-04. |
| Jira | [KAN-16](https://yarengursoy.atlassian.net/browse/KAN-16) |

## Requirements

For more info you can visit: https://www.atlassian.com/agile/product-management/requirements.

### User stories

| # | User story title | User story description | Role (ISO/IEC 5339) | Priority | Points | Owner | Sprint | Notes | Jira |
|---|---|---|---|---|---|---|---|---|---|
| S1 | [See the provisions that relate to my use case, with their references](#s1--see-the-provisions-that-relate-to-my-use-case-with-their-references) | As an EdTech AI developer, I want to see which in-scope provisions relate to my use case, with their exact references and version date, so that I do not miss a requirement that may concern my product. | AI user | High | 8 | Yeşim | Sprint 2 | Release: Alpha 0.1; Feature: F2; Status: In progress. | [KAN-8](https://yarengursoy.atlassian.net/browse/KAN-8) |
| S2 | [Understand the relevant requirements in plain language](#s2--understand-the-relevant-requirements-in-plain-language) | As an EdTech AI developer, I want the assistant to explain the relevant EU AI Act requirements in plain language, so that I can understand what they mean for my product without interpreting legal terms on my own. | AI user | High | – | – | Sprint 3 | Release: Beta 0.5; Feature: F3; Status: To do. | [KAN-4](https://yarengursoy.atlassian.net/browse/KAN-4) |
| S3 | [See when the AI Act rules apply to our product](#s3--see-when-the-ai-act-rules-apply-to-our-product) | As an EdTech AI developer building an AI-based exam-grading tool, I want to see from which date each relevant EU AI Act rule applies, based on the designated consolidated text, so that my team can plan our releases around the correct application dates. | AI user | High | – | Gözde Nur | Sprint 4 | Release: Release candidate 1.0; Feature: F2; Status: To do; Needed in the pilot version by 16/12/2026. | [KAN-3](https://yarengursoy.atlassian.net/browse/KAN-3) |
| S4 | [Understand the assistant's answers without legal training](#s4--understand-the-assistants-answers-without-legal-training) | As an EdTech AI developer taking part in the pilot, I want the assistant's answers to be understandable without legal training, so that I can use them for my own education product without asking a lawyer to explain them first. | AI user | High | – | Yaren | Sprint 4 | Release: Release candidate 1.0; Feature: Pilot, O3; Status: To do; Uses Beta 0.5 with [KAN-3](https://yarengursoy.atlassian.net/browse/KAN-3) and [KAN-22](https://yarengursoy.atlassian.net/browse/KAN-22) (pilot version, 16/12/2026); its survey follows the timed tasks of [KAN-202](https://yarengursoy.atlassian.net/browse/KAN-202). | [KAN-72](https://yarengursoy.atlassian.net/browse/KAN-72) |
| S5 | [Ask follow-up questions about our product in the same session](#s5--ask-follow-up-questions-about-our-product-in-the-same-session) | As a technical lead at an EdTech provider, I want to describe our product once and then ask follow-up questions about it, so that I do not have to repeat the product details and receive answers relevant to the product I described. | AI user | Low | – | Kaan | Backlog | Feature: F7; Status: To do; Not committed (Feature 7); built only if time allows. | [KAN-6](https://yarengursoy.atlassian.net/browse/KAN-6) |

### Tasks

Work that serves the users but is not a user goal of its own: evaluations, documents and delivery work. Since the Sprint 1 review (comment 3), such work is a Jira task, linked to the user stories it serves where there is one.

| # | Task | Purpose | Related user stories | Points | Owner | Sprint | Jira |
|---|---|---|---|---|---|---|---|
| T1 | [Evaluate search-time improvement against manual lookup (O1)](#t1--evaluate-search-time-improvement-against-manual-lookup-o1) | Measure in the pilot whether developers find the relevant AI Act provisions faster with the assistant than by searching the regulation themselves (O1). Speed is not a separate user goal: this task checks it for the stories that let users ask in their own words and find the provisions ([KAN-19](https://yarengursoy.atlassian.net/browse/KAN-19), [KAN-8](https://yarengursoy.atlassian.net/browse/KAN-8)) in the browser interface ([KAN-21](https://yarengursoy.atlassian.net/browse/KAN-21)). The post-task survey that measures understanding ([KAN-72](https://yarengursoy.atlassian.net/browse/KAN-72), O3) is run after the same timed tasks. | [KAN-8](https://yarengursoy.atlassian.net/browse/KAN-8), [KAN-19](https://yarengursoy.atlassian.net/browse/KAN-19), [KAN-21](https://yarengursoy.atlassian.net/browse/KAN-21), [KAN-72](https://yarengursoy.atlassian.net/browse/KAN-72) | – | – | Sprint 4 | [KAN-202](https://yarengursoy.atlassian.net/browse/KAN-202) |

Priority, points, owner and sprint are as in Jira on 08/11/2026; the status of S1 and its sub-tasks is as in Jira on 14/11/2026. Points are given with planning poker at each sprint planning; a dash means not estimated yet. The roles are the ISO/IEC 5339 stakeholder roles from the [User Story Map v2](02-user-story-map-v2.md) ([KAN-116](https://yarengursoy.atlassian.net/browse/KAN-116)). Every current user story has test cases, written in Sprint 2 ([KAN-114](https://yarengursoy.atlassian.net/browse/KAN-114)); they are planned tests to run when the story is built, not results.

## S1 · See the provisions that relate to my use case, with their references

[KAN-8](https://yarengursoy.atlassian.net/browse/KAN-8) · User story · Sprint 2 (Alpha 0.1) · Status In progress · Priority High · Points 8 · Owner Yeşim

**Story:** As an EdTech AI developer, I want to see which in-scope provisions relate to my use case, with their exact references and version date, so that I do not miss a requirement that may concern my product.

**Acceptance criteria**

1. When the assistant answers an in-scope question, the assistant shall show each provision it uses with its Article or Annex reference (down to the paragraph or point) and the version date of the consolidated text (27 July 2026).
2. When an answer uses more than one provision (for example Annex III point 3(b) together with Article 6(3)), the assistant shall show them in the same answer and state how they relate where the source text supports it (for example "condition" or "exception").
3. The assistant shall cite only provisions that are among the retrieved chunks and that support the information it gives; a citation that does not match a retrieved chunk shall not be shown.
4. For every substantive answer to an in-scope question in the D2 `val` split, the assistant shall show at least one Article or Annex reference with the version date (O2(c)). The share of questions whose expected provision is cited (O2(a)) and the retrieval Recall@8 and Recall@5 shall be reported separately in the Sprint 2 technical summary (D6).

**Test cases**

Adapted from the use-case stories [KAN-10](https://yarengursoy.atlassian.net/browse/KAN-10), [KAN-11](https://yarengursoy.atlassian.net/browse/KAN-11), [KAN-12](https://yarengursoy.atlassian.net/browse/KAN-12) and [KAN-13](https://yarengursoy.atlassian.net/browse/KAN-13) (Gözde Nur Özdemir). In every case, each cited provision is shown with its reference down to the paragraph or point and the version date 27/07/2026 (criteria 1, 3).

* **TC-8.1 Emotion detection.** Input: "We are building a module that detects students' emotions during lessons in schools. Which AI Act provisions relate to it?" Expected: Art. 5(1)(f) with its exception for medical or safety reasons.
* **TC-8.2 Tutor chatbot.** Input: "Our AI tutor chatbot talks directly to students. Which transparency rules apply?" Expected: Art. 50(1); the answer also names the Annex III point 3 uses (for example evaluating learning outcomes) that would make the high-risk rules relevant if the chatbot grades students.
* **TC-8.3 Admission ranking.** Input: "Our tool ranks applicants for admission. Which provisions relate to it, and are there exceptions?" Expected: Annex III point 3(a) and Art. 6(2); the four conditions of Art. 6(3)(a)–(d), each in one sentence; that a system that profiles natural persons is always high-risk; the documentation duty in Art. 6(4). The provisions are shown in one answer with their relation (criterion 2).
* **TC-8.4 Exam monitoring.** Input: "Our proctoring tool flags students' behaviour during online exams. What do the human oversight rules require?" Expected: Annex III point 3(d) and Art. 6(2); the abilities listed in Art. 14(4), each in one sentence (criterion 2).

**Sub-tasks**

| Sub-task | Done when | Owner | Status | Jira |
|---|---|---|---|---|
| Generate answers from the retrieved chunks | The retriever from [KAN-87](https://yarengursoy.atlassian.net/browse/KAN-87) is connected to the language model with the fixed prompt templates in `prompts/`, and every D2 `val` question gets a response. In Sprint 2 this is the baseline answer: the retrieved provisions with their references and the version date, and a short answer based only on them. The plain-language answer format ([KAN-4](https://yarengursoy.atlassian.net/browse/KAN-4)) and the safety checks and notices ([KAN-2](https://yarengursoy.atlassian.net/browse/KAN-2), [KAN-5](https://yarengursoy.atlassian.net/browse/KAN-5), [KAN-23](https://yarengursoy.atlassian.net/browse/KAN-23)) are built in Sprint 3. | Gözde | Done | [KAN-125](https://yarengursoy.atlassian.net/browse/KAN-125) |
| Add each cited provision with its reference and the version date to the answers | Every substantive answer lists each provision it cites, with its Article/Annex reference and the version date of the consolidated text (27/07/2026), checked on the saved D2 `val` answers. Scope changed on 14/11/2026: the reference down to the paragraph or point and the sources line in the user interface moved to [KAN-222](https://yarengursoy.atlassian.net/browse/KAN-222). | Yeşim | Done | [KAN-126](https://yarengursoy.atlassian.net/browse/KAN-126) |
| Show how several provisions relate | When an answer uses more than one provision, they are shown in the same answer, with "condition" or "exception" where the source text supports it. | Yeşim | To do; carry-over to Sprint 3 agreed on 14/11/2026 | [KAN-127](https://yarengursoy.atlassian.net/browse/KAN-127) |
| Check every citation against the retrieved chunk IDs | A citation that does not match a retrieved chunk is removed before the answer is shown, and 100% of the shown citations match the IDs of the retrieved chunks. | Yaren | Done | [KAN-128](https://yarengursoy.atlassian.net/browse/KAN-128) |
| Report citation coverage and the expected-provision rate on the val split | O2 (c), the share of substantive answers with at least one Article/Annex reference and the version date, and O2 (a), the share of questions whose expected provision is cited, are logged with Recall@8 and Recall@5 for the D2 `val` split. | Yaren | Done | [KAN-129](https://yarengursoy.atlassian.net/browse/KAN-129) |

Related task: [KAN-222](https://yarengursoy.atlassian.net/browse/KAN-222) Cite every provision down to the paragraph or point and show the sources line in the interface · Task · Sprint 3 · Yeşim · To do. Split from KAN-126 on 14/11/2026 (story acceptance criterion 1).

**Traceability**

Feature: Feature 2 - Find the relevant provisions  
Objectives: O2 Evidence (a), (c); O1 Search time  
Deliverable: D6 Alpha Release (due 14/11/2026)  
Milestone: M4 Baseline (alpha) runs on the full validation question set (18/11/2026)  
Major Activities: row 9  
Constraints: C-01 Single source (consolidated text of 27/07/2026); C-09 EUR-Lex reuse with source acknowledgement  
Risk: R-11 The source format is uneven

## S2 · Understand the relevant requirements in plain language

[KAN-4](https://yarengursoy.atlassian.net/browse/KAN-4) · User story · Sprint 3 (Beta 0.5) · Status To do · Priority High · Points – · Owner –

**Story:** As an EdTech AI developer, I want the assistant to explain the relevant EU AI Act requirements in plain language, so that I can understand what they mean for my product without interpreting legal terms on my own.

**Acceptance criteria**

1. When the assistant answers an in-scope question, the assistant shall start with a summary of at most three sentences, followed by the relevant conditions and exceptions where applicable; where the user's description does not establish whether a condition is met, the assistant shall state that the answer depends on that condition and shall not assume it is met.
2. When an answer uses a term defined in Article 3, the assistant shall explain the term once in that answer, in one sentence, and cite its Article 3 point; other legal terms necessary to understand the answer shall be explained once, in one sentence, based only on the retrieved provisions.
3. The assistant shall base each explanation only on the retrieved provisions and shall not add obligations, exceptions or conclusions that they do not support.
4. For every in-scope question in the frozen D8 `val` split, the answer shall start with the summary defined in criterion 1 and present conditions and exceptions where applicable; for questions whose gold answers contain conditions or exceptions, the share of answers correctly stating them shall be reported in the Sprint 3 technical summary.

**Test cases**

Planned tests, not results: each is run when the story is built, and its result is recorded in the Sprint 3 technical summary.

* **TC-4.1** (criterion 1) Input: "Our AI tool ranks applicants for admission to our school. What do the rules require?" Expected: the answer starts with a summary of at most three sentences; after it, the conditions and exceptions of Art. 6(3) are given; because the question does not say whether the tool profiles applicants, the answer says that the result depends on this condition and does not assume it is met.
* **TC-4.2** (criterion 2) Input: "What does the AI Act mean by a provider, for a company that builds an essay-grading tool and sells it to schools?" Expected: the term "provider" is explained once, in one sentence, with its Article 3 point cited (Art. 3(3)); no other defined term is explained twice; the answer does not decide whether the company is a provider.
* **TC-4.3** (criterion 3) Steps: take the answers to TC-4.1 and TC-4.2; compare every obligation, exception and conclusion in them with the retrieved provisions shown under the answer. Expected: each one is stated in a retrieved provision; nothing is added that the provisions do not support.
* **TC-4.4** (criterion 4) Steps: run the frozen D8 `val` split; check every in-scope answer for the summary of criterion 1; for the questions whose gold answers contain conditions or exceptions, count the answers that state them correctly. Expected: every in-scope answer starts with the summary; the share is reported in the Sprint 3 technical summary.

**Sub-tasks**

| Sub-task | Done when | Owner | Status | Jira |
|---|---|---|---|---|
| Write the answer template | The prompt template in `prompts/` makes every in-scope answer start with a summary of at most three sentences, followed by the conditions and exceptions; if the user's description does not show whether a condition is met, the answer says that it depends on that condition. | – | To do | [KAN-133](https://yarengursoy.atlassian.net/browse/KAN-133) |
| Explain defined terms once with their Article 3 point | A term defined in Article 3 is explained once per answer, in one sentence, and cited with its Article 3 point; other legal terms needed for the answer are explained once, based only on the retrieved provisions. | – | To do | [KAN-134](https://yarengursoy.atlassian.net/browse/KAN-134) |
| Check that answers add nothing beyond the retrieved provisions | The answers to the frozen D8 `val` questions are checked against the rubric's definition of "fully supported"; obligations, exceptions or conclusions not supported by the retrieved provisions are listed as known failures in the Sprint 3 technical summary. | – | To do | [KAN-135](https://yarengursoy.atlassian.net/browse/KAN-135) |
| Report the answer format and the conditions result on the val split | For the in-scope questions in the frozen D8 `val` split, the share of answers that start with the summary, and for questions whose gold answers contain conditions or exceptions, the share that state them correctly, are reported in the Sprint 3 technical summary. | – | To do | [KAN-136](https://yarengursoy.atlassian.net/browse/KAN-136) |

**Traceability**

Feature: Feature 3 - Plain-language answer  
Objectives: O3 Understanding; O2 Evidence (b)  
Deliverable: D9 Beta Release (due 05/12/2026)  
Milestone: M7 (09/12/2026)  
Major Activities: row 10  
Constraint: C-08 Information, not legal advice

## S3 · See when the AI Act rules apply to our product

[KAN-3](https://yarengursoy.atlassian.net/browse/KAN-3) · User story · Sprint 4 (Release candidate 1.0) · Status To do · Priority High · Points – · Owner Gözde Nur

**Story:** As an EdTech AI developer building an AI-based exam-grading tool, I want to see from which date each relevant EU AI Act rule applies, based on the designated consolidated text, so that my team can plan our releases around the correct application dates.

**Acceptance criteria**

1. When a user asks when an in-scope provision applies, the assistant shall provide the application date supported by the designated consolidated text of 27 July 2026 and cite the provision supporting that date (for example Article 113).
2. When a user asks about the application date of high-risk requirements for an Annex III point 3 education use case, the assistant shall explain the relevant application-date provisions and, where necessary to answer the question, the related Article 6 conditions, without classifying the user's product as high-risk.
3. If the available in-scope provisions do not provide sufficient evidence to determine an application date, then the assistant shall state that the date cannot be determined from the available source and shall not invent one.
4. For every application-date question, the assistant shall give either a date with the provision that supports it or an insufficient-evidence response; the share of answers whose date matches the gold answer from the 27 July 2026 text is reported as the O2 (d) result on the held-out `test` split in the Sprint 4 technical summary.

**Test cases**

Adapted from the use-case stories [KAN-11](https://yarengursoy.atlassian.net/browse/KAN-11) and [KAN-13](https://yarengursoy.atlassian.net/browse/KAN-13) (Gözde Nur Özdemir). The expected dates are the gold answers taken from the 27/07/2026 text during D2.

* **TC-3.1** Input: "From when must our AI tutor chatbot tell students that they are talking to an AI?" Expected: the application date of Art. 50(1), with the provision of the 27/07/2026 text that supports it (criterion 1).
* **TC-3.2** Input: "From when do the human oversight rules apply to our exam proctoring tool?" Expected: the application date of the high-risk requirements for Annex III point 3 systems, citing Art. 113, without classifying the tool as high-risk (criteria 1, 2).

**Sub-tasks**

| Sub-task | Done when | Owner | Status | Jira |
|---|---|---|---|---|
| Answer application-date questions with the supporting provision | An application-date question gets the date from the 27/07/2026 text with the provision that supports it (for example Article 113); for Annex III point 3 use cases, the related Article 6 conditions are explained where needed, without classifying the product. | – | To do | [KAN-130](https://yarengursoy.atlassian.net/browse/KAN-130) |
| Give an insufficient-evidence response when no date is supported | If no retrieved provision supports an application date, the answer states that the date cannot be determined from the available source and gives no date. | – | To do | [KAN-131](https://yarengursoy.atlassian.net/browse/KAN-131) |
| Report the application-date result on the val and test splits | For the application-date questions in the evaluation set (D8 `val` split during development, the held-out `test` split for the final evaluation), the share of answers whose date matches the gold date from the 27/07/2026 text is logged as the O2 (d) result. | – | To do | [KAN-132](https://yarengursoy.atlassian.net/browse/KAN-132) |

**Traceability**

Feature: Feature 2 - Find the relevant provisions  
Objectives: O2 Evidence (d); O1 Search time  
Deliverable: D11 Release Candidate and Final Evaluation (due 30/12/2026)  
Needed in the pilot version by 16/12/2026 (first week of Sprint 4; Release Plan; Dependencies row 13)  
Milestone: M10 (30/12/2026)  
Major Activities: row 10  
Constraint: C-01 Single source (consolidated text of 27/07/2026)  
Assumption / Risk: A-02 / R-02 The law or its official reading changes

## S4 · Understand the assistant's answers without legal training

[KAN-72](https://yarengursoy.atlassian.net/browse/KAN-72) · User story · Sprint 4 (Release candidate 1.0) · Status To do · Priority High · Points – · Owner Yaren

**Story:** As an EdTech AI developer taking part in the pilot, I want the assistant's answers to be understandable without legal training, so that I can use them for my own education product without asking a lawyer to explain them first.

**Acceptance criteria**

1. After the timed tasks, every pilot user completes a post-task survey that rates the understandability of the answers on a 5-point scale.
2. At least 70% of the pilot users (at least 4 of 5 when there are 5) rate the answers 4 or 5 (O3).
3. The survey also records whether users would use the assistant as their first step before asking their legal team (business outcome: at least 60%) and whether they correctly answer that the assistant does not give legal decisions (O4 business outcome: at least 80%).
4. The results are recorded without names in `docs/eval/pilot.md` and in the Sprint 4 technical summary.

**Test cases**

Planned tests for the pilot (16/12–23/12/2026), not results; recorded in `docs/eval/pilot.md`.

* **TC-72.1** (criteria 1, 3) Steps: open the post-task survey before the pilot. Expected: it has a 5-point understandability question, the "first step before asking the legal team" question and the "does the assistant give legal decisions?" question; it asks for no name or personal data.
* **TC-72.2** (criterion 1) Steps: after the pilot, count the completed surveys against the pilot users. Expected: every pilot user completed the survey right after the timed tasks.
* **TC-72.3** (criteria 2, 3) Steps: compute the share of users rating 4 or 5, the share who would use the assistant first, and the share who answer that it gives no legal decisions. Expected: each share is reported against its target (70%, 60%, 80%), with whether the target is met.
* **TC-72.4** (criterion 4) Steps: read `docs/eval/pilot.md` and the Sprint 4 technical summary. Expected: the results are in both, with no participant names.

**Sub-tasks**

| Sub-task | Done when | Owner | Status | Jira |
|---|---|---|---|---|
| Write the post-task survey | The post-task survey has a 5-point understandability question, the "first step before asking the legal team" question and the "does the assistant give legal decisions?" question, and it collects no names or personal data. | – | To do | [KAN-73](https://yarengursoy.atlassian.net/browse/KAN-73) |
| Report the O3 result and the business outcomes | `docs/eval/pilot.md` gives the share of users rating the answers 4 or 5 against the O3 target (70%), the share who would use the assistant as their first step (60%) and the share who answer that it does not give legal decisions (80%), and states whether each target is met. | – | To do | [KAN-74](https://yarengursoy.atlassian.net/browse/KAN-74) |
| Run the survey after the timed tasks | Every pilot user completes the survey right after their timed tasks (16/12–23/12/2026), and the answers are stored without names. | – | To do | [KAN-198](https://yarengursoy.atlassian.net/browse/KAN-198) |

**Traceability**

Objective: O3 Understanding; O4 Safety (business outcome)  
Deliverable: D10 Pilot Evaluation Report (due 30/12/2026)  
Milestone: M9 Pilot measured (30/12/2026)  
Major Activities: row 26  
Assumptions / Risks: A-04, A-07 / R-03, R-08  
Constraint: C-10

## S5 · Ask follow-up questions about our product in the same session

[KAN-6](https://yarengursoy.atlassian.net/browse/KAN-6) · User story · Backlog (not committed) · Status To do · Priority Low · Points – · Owner Kaan

**Story:** As a technical lead at an EdTech provider, I want to describe our product once and then ask follow-up questions about it, so that I do not have to repeat the product details and receive answers relevant to the product I described.

**Built only if time allows** (backlog; Feature 7 is not committed in the charter).

**Acceptance criteria**

1. When a user describes their product (for example, "an AI tutor that also suggests grades for essays"), the assistant shall restate in one sentence the product features it understood, without stating a legal classification.
2. When a follow-up question in the same session does not repeat the product details (for example, "What are the transparency obligations?"), the assistant shall use the product description given earlier and answer only to the extent supported by the retrieved in-scope provisions, giving an out-of-scope or insufficient-evidence notice for any unsupported part.
3. If the user adds or changes a feature in the same session (for example, "We are also adding webcam proctoring"), then the assistant shall base later answers on the updated product description.
4. When a session ends, the assistant shall discard its stored session context, including the product description and conversation; when a new session starts, the assistant shall not use content from the previous session.
5. For every follow-up question in the `val` split, the assistant shall use the product description from the preceding conversation in the same session; the share of follow-up questions receiving the expected response defined in the evaluation rubric shall be reported separately in the technical summary of the sprint in which the feature is built.

**Test cases**

Built only if time allows; these tests are run only if the story is taken into a sprint.

* **TC-6.1** (criterion 1) Input: "Our product is an AI tutor that also suggests grades for essays." Expected: one sentence restates the features understood (tutoring; suggesting essay grades); no legal classification.
* **TC-6.2** (criterion 2) Precondition: TC-6.1 in the same session. Input: "What are the transparency obligations?" Expected: the answer uses the tutor described in TC-6.1 without asking for it again, cites only retrieved in-scope provisions, and gives an out-of-scope or insufficient-evidence notice for any part they do not support.
* **TC-6.3** (criterion 3) Precondition: TC-6.1 in the same session. Input: "We are also adding webcam proctoring." then "Which provisions relate to our product now?" Expected: the second answer also covers the proctoring feature (Annex III point 3(d)).
* **TC-6.4** (criterion 4) Steps: end the session after TC-6.3; start a new session; ask "What are the transparency obligations for our product?" Expected: the answer does not use the earlier product description; the first session's context is no longer in the web backend's memory. Depends on design decision D15 (conversation in the web backend's memory, supersedes D4): if D15 changes, criterion 4 and this test are updated together.
* **TC-6.5** (criterion 5) Steps: run every follow-up question of the `val` split after its preceding question in the same session; score against the rubric. Expected: each answer uses the earlier product description; the share with the expected response is reported separately in the technical summary of the sprint in which the feature is built.

**Sub-tasks**

*No sub-tasks yet: they are written at the sprint planning.*

**Traceability**

Feature: Feature 7 - Follow-up questions (not committed; built only if time allows)  
Objectives: O1 Search time; O3 Understanding  
Constraints: C-04 Education use cases only; follow-ups within one session; C-08 Information, not legal advice; C-10 No personal data requested; conversation deleted when the session ends

## T1 · Evaluate search-time improvement against manual lookup (O1)

[KAN-202](https://yarengursoy.atlassian.net/browse/KAN-202) · Task · Sprint 4 (Release candidate 1.0) · Status To do · Priority High · Points – · Owner –

**Purpose:** Measure in the pilot whether developers find the relevant AI Act provisions faster with the assistant than by searching the regulation themselves (O1). Speed is not a separate user goal: this task checks it for the stories that let users ask in their own words and find the provisions ([KAN-19](https://yarengursoy.atlassian.net/browse/KAN-19), [KAN-8](https://yarengursoy.atlassian.net/browse/KAN-8)) in the browser interface ([KAN-21](https://yarengursoy.atlassian.net/browse/KAN-21)). The post-task survey that measures understanding ([KAN-72](https://yarengursoy.atlassian.net/browse/KAN-72), O3) is run after the same timed tasks.

**Related user stories:** [KAN-8](https://yarengursoy.atlassian.net/browse/KAN-8), [KAN-19](https://yarengursoy.atlassian.net/browse/KAN-19), [KAN-21](https://yarengursoy.atlassian.net/browse/KAN-21), [KAN-72](https://yarengursoy.atlassian.net/browse/KAN-72)

**Acceptance criteria**

1. A pilot protocol is in the repository before the pilot: tasks taken from the `val` split, balanced across the four use cases, with the order of the two conditions (assistant / manual search) counterbalanced across participants. The protocol states how the tasks were chosen and that the `val` questions were used during development, so the pilot measures the users' search time, not the model's performance on unseen questions.
2. The pilot runs in person on a team computer set up only from the README; no cloud deployment is needed.
3. Every participant completes the timed tasks in both conditions between 16/12 and 23/12/2026.
4. The median time and the task success rate are reported per condition, together with whether O1 is met, in `docs/eval/pilot.md`.

**Sub-tasks**

| Sub-task | Done when | Owner | Status | Jira |
|---|---|---|---|---|
| Write the pilot protocol | The pilot protocol is in the repository: tasks taken from the `val` split, balanced across the four use cases, with the order of the two conditions counterbalanced across participants, and with the task-success definition written down. The protocol states how the tasks were chosen and that the `val` questions were used during development. | – | To do | [KAN-205](https://yarengursoy.atlassian.net/browse/KAN-205) |
| Prepare the pilot computer from the README | The release candidate runs on the pilot computer after following only the README, and one dry run of a task in each condition works. | – | To do | [KAN-206](https://yarengursoy.atlassian.net/browse/KAN-206) |
| Run the timed pilot tasks in person | Every participant completes the timed tasks in both conditions between 16/12 and 23/12/2026, and the times and task results are recorded without personal data. | – | To do | [KAN-207](https://yarengursoy.atlassian.net/browse/KAN-207) |
| Report the O1 pilot result | The median time and the task success rate per condition, and whether O1 is met, are reported in `docs/eval/pilot.md`. | – | To do | [KAN-208](https://yarengursoy.atlassian.net/browse/KAN-208) |

**Traceability**

Changed from a user story to a task after the Sprint 1 review (comment 4).  
Feature: Feature 1 - Ask in their own words  
Objective: O1 Search time  
Deliverable: D10 Pilot Evaluation Report (due 30/12/2026)  
Milestone: M9 Pilot measured (30/12/2026)  
Major Activities: row 26  
Assumptions / Risks: A-04, A-07 / R-03, R-08  
Constraint: C-10

## Changes since v1 (27/10/2026)

- [KAN-4](https://yarengursoy.atlassian.net/browse/KAN-4) Understand the relevant requirements in plain language: test cases TC-4.1 to TC-4.4 added on 08/11/2026 ([KAN-114](https://yarengursoy.atlassian.net/browse/KAN-114)).
- [KAN-6](https://yarengursoy.atlassian.net/browse/KAN-6) Ask follow-up questions about our product in the same session: test cases TC-6.1 to TC-6.5 added on 08/11/2026 ([KAN-114](https://yarengursoy.atlassian.net/browse/KAN-114)); TC-6.4 changed on 10/11/2026: the session context is kept in the web backend's memory instead of a session database (design decision D15, Sprint 1 review comment 8).
- [KAN-72](https://yarengursoy.atlassian.net/browse/KAN-72) Understand the assistant's answers without legal training: test cases TC-72.1 to TC-72.4 added on 08/11/2026 ([KAN-114](https://yarengursoy.atlassian.net/browse/KAN-114)).
- [KAN-202](https://yarengursoy.atlassian.net/browse/KAN-202) Evaluate search-time improvement against manual lookup (O1): changed from a user story to a task on 07/11/2026 (Sprint 1 review, comment 4); renamed from "Find the provisions faster than with manual search".
- [KAN-116](https://yarengursoy.atlassian.net/browse/KAN-116) Check the story roles against ISO/IEC 5339: role column added to the user stories table on 08/11/2026.
- [KAN-8](https://yarengursoy.atlassian.net/browse/KAN-8) See the provisions that relate to my use case, with their references: on 14/11/2026, [KAN-126](https://yarengursoy.atlassian.net/browse/KAN-126) was narrowed to its Sprint 2 scope; the reference down to the paragraph or point and the sources line in the interface moved to the new task [KAN-222](https://yarengursoy.atlassian.net/browse/KAN-222) (Sprint 3); the carry-over of [KAN-127](https://yarengursoy.atlassian.net/browse/KAN-127) to Sprint 3 was agreed.
