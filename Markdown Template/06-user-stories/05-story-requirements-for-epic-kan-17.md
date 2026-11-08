# Story Requirements for Epic KAN-17: Show the Source

Version v2, Sprint 2 (08/11/2026). Source: Jira project KAN on 08/11/2026. Version v1 (27/10/2026) is in the Git history; what changed since then is listed at the end of this page. Back to the [User Story Map v2](02-user-story-map-v2.md) · [all story requirements pages](README.md).

| Epic | Show the Source |
|---|---|
| Summary | Letting users check every answer against its source: the text of each cited provision shown under the answer with its reference, version date and a link to EUR-Lex (Feature 6), and the final check of the citations on the held-out `test` split (O2 (a)–(d); D11). |
| Features | F6 Check the source |
| Document Owner | Yeşim (Product Owner) |
| Designer | Gözde Nur (design decisions, KAN-58) and Kaan (design document, KAN-59) |
| Developers | Yaren so far; later work is assigned at each sprint planning |
| Release Target (Sprint) | Sprint 4 (Release candidate 1.0) |
| Traceability | Objective: O2 Evidence. Major Activities rows 15, 24, 27. Constraints: C-01, C-09. |
| Jira | [KAN-17](https://yarengursoy.atlassian.net/browse/KAN-17) |

## Requirements

For more info you can visit: https://www.atlassian.com/agile/product-management/requirements.

### User stories

| # | User story title | User story description | Role (ISO/IEC 5339) | Priority | Points | Owner | Sprint | Notes | Jira |
|---|---|---|---|---|---|---|---|---|---|
| S1 | [Read the cited source text behind an answer](#s1--read-the-cited-source-text-behind-an-answer) | As a compliance officer in an EdTech provider's legal team, I want to read the source text of each provision cited in an answer, so that I can verify the explanation before advising the development team. | AI customer | High | – | – | Sprint 4 | Release: Release candidate 1.0; Feature: F6; Status: To do; Depends on [KAN-8](https://yarengursoy.atlassian.net/browse/KAN-8) (the cited provisions must be found first). Needed in the pilot version by 16/12/2026. | [KAN-22](https://yarengursoy.atlassian.net/browse/KAN-22) |
| S2 | [Rely on cited provisions confirmed on unseen questions](#s2--rely-on-cited-provisions-confirmed-on-unseen-questions) | As a compliance officer in an EdTech provider's legal team, I want the assistant's citations to be confirmed on questions it has not seen before, so that I can trust that developers receive the right Article or Annex with the correct version date. | AI customer | High | – | Yaren | Sprint 4 | Release: Release candidate 1.0; Feature: F6; Status: To do. | [KAN-77](https://yarengursoy.atlassian.net/browse/KAN-77) |

Priority, points, owner and sprint are as in Jira on 08/11/2026. Points are given with planning poker at each sprint planning; a dash means not estimated yet. The roles are the ISO/IEC 5339 stakeholder roles from the [User Story Map v2](02-user-story-map-v2.md) ([KAN-116](https://yarengursoy.atlassian.net/browse/KAN-116)). Every current user story has test cases, written in Sprint 2 ([KAN-114](https://yarengursoy.atlassian.net/browse/KAN-114)); they are planned tests to run when the story is built, not results.

## S1 · Read the cited source text behind an answer

[KAN-22](https://yarengursoy.atlassian.net/browse/KAN-22) · User story · Sprint 4 (Release candidate 1.0) · Status To do · Priority High · Points – · Owner –

**Story:** As a compliance officer in an EdTech provider's legal team, I want to read the source text of each provision cited in an answer, so that I can verify the explanation before advising the development team.

**Acceptance criteria**

1. When an answer cites a provision, the assistant shall let the user open the text of that provision under the answer.
2. When the text is shown, the assistant shall show it exactly as in the stored consolidated text of 27 July 2026, with its Article or Annex reference and the version date.
3. When the text is shown, the assistant shall name EUR-Lex as the source and link to the consolidated text.
4. For every provision cited in the answers to the D8 `val` split, the text shown shall match the corresponding cited provision in the stored consolidated text identified in the source manifest (D3).

**Test cases**

Planned tests, not results: each is run when the story is built, and its result is recorded in the Sprint 4 technical summary.

* **TC-22.1** (criterion 1) Input: "Which provisions relate to our exam-proctoring tool?" Steps: open each cited provision under the answer. Expected: every cited provision can be opened under the answer, without leaving the page.
* **TC-22.2** (criterion 2) Steps: compare each text opened in TC-22.1 with the same provision in the stored consolidated text of 27/07/2026. Expected: the text is identical; its Article or Annex reference and the version date 27/07/2026 are shown with it.
* **TC-22.3** (criterion 3) Steps: look at the text opened in TC-22.1 and follow its link. Expected: EUR-Lex is named as the source; the link opens the consolidated text on EUR-Lex.
* **TC-22.4** (criterion 4) Steps: for every provision cited in the answers to the D8 `val` split, compare the text shown with the cited provision in the stored text identified in the source manifest (D3), by script. Expected: every text matches; any mismatch is listed.

**Sub-tasks**

| Sub-task | Done when | Owner | Status | Jira |
|---|---|---|---|---|
| Open the cited provision under the answer | Every provision cited in an answer can be opened under that answer. | – | To do | [KAN-194](https://yarengursoy.atlassian.net/browse/KAN-194) |
| Show the stored text with its reference and version date | The opened text is exactly as in the stored consolidated text of 27/07/2026, with its Article or Annex reference and the version date. | – | To do | [KAN-195](https://yarengursoy.atlassian.net/browse/KAN-195) |
| Name EUR-Lex and link to the consolidated text | The opened text names EUR-Lex as the source and links to the consolidated text. | – | To do | [KAN-196](https://yarengursoy.atlassian.net/browse/KAN-196) |
| Check the shown texts on the val split | For every provision cited in the answers to the D8 `val` questions, the shown text matches the corresponding provision in the stored consolidated text identified in the source manifest (D3). | – | To do | [KAN-197](https://yarengursoy.atlassian.net/browse/KAN-197) |

**Traceability**

Feature: Feature 6 - Check the source  
Objective: O2 Evidence  
Deliverable: D11 Release Candidate and Final Evaluation (due 30/12/2026)  
Needed in the pilot version by 16/12/2026 (first week of Sprint 4; Release Plan; Dependencies row 13)  
Milestone: M10 (30/12/2026)  
Major Activities: row 15  
Constraints: C-01 Single source (consolidated text of 27/07/2026); C-09 EUR-Lex reuse with source acknowledgement  
Risk: R-01 Source text differs from the Official Journal  
Depends on: [KAN-8](https://yarengursoy.atlassian.net/browse/KAN-8)

## S2 · Rely on cited provisions confirmed on unseen questions

[KAN-77](https://yarengursoy.atlassian.net/browse/KAN-77) · User story · Sprint 4 (Release candidate 1.0) · Status To do · Priority High · Points – · Owner Yaren

**Story:** As a compliance officer in an EdTech provider's legal team, I want the assistant's citations to be confirmed on questions it has not seen before, so that I can trust that developers receive the right Article or Annex with the correct version date.

**Acceptance criteria**

1. The release candidate answers every question in the held-out `test` split; the `test` questions were not used for tuning.
2. The expected provision is among the cited sources for at least 80% of the in-scope `test` questions (O2 (a)).
3. At least 75% of the in-scope `test` answers are fully supported by the passages they cite (O2 (b)); every in-scope answer is reviewed by one reviewer and a sample by a second reviewer.
4. 100% of substantive answers cite at least one Article or Annex with the version date (O2 (c)), and at most one application-date question gets a date that is not from the 27/07/2026 text (O2 (d)).
5. Every result is reported in the Sprint 4 technical summary and its experiment card, with a link to its W&B run.

**Test cases**

Planned tests on the held-out `test` split, not results; recorded in the Sprint 4 technical summary.

* **TC-77.1** (criterion 1) Steps: run the release candidate on every `test` question. Then collect the evidence that the `test` questions were not used before: (a) the commits that froze the `test` split (11/11/2026 for v1, 05/12/2026 for the new v2 questions) and the `git log` of the evaluation set after them; (b) for every W&B run before this one, the split recorded in the run and its experiment card; (c) the evaluation script, which selects questions by the `split` column; (d) the `config/rag.yaml` history. Expected: every `test` question is answered; the `test` rows are unchanged since they were frozen; every earlier run and experiment card names `val` only; no setting was changed after a `test` result was seen. The evidence is listed in the Sprint 4 technical summary.
* **TC-77.2** (criterion 2) Steps: for every in-scope `test` question, check whether its expected provision is among the cited sources. Expected: the share is at least 80% (O2 (a)).
* **TC-77.3** (criterion 3) Steps: one reviewer checks every in-scope `test` answer against the rubric's "fully supported" definition; a second reviewer checks a sample. Expected: at least 75% are fully supported (O2 (b)); disagreements are logged.
* **TC-77.4** (criterion 4) Steps: check every substantive answer for an Article or Annex citation with the version date; compare every application-date answer with the gold date from the 27/07/2026 text. Expected: 100% of substantive answers have such a citation (O2 (c)); at most one application-date answer has a date that is not from the 27/07/2026 text (O2 (d)).
* **TC-77.5** (criterion 5) Steps: read the Sprint 4 technical summary and the experiment card. Expected: every result above is in both, each with a link to its W&B run.

**Sub-tasks**

| Sub-task | Done when | Owner | Status | Jira |
|---|---|---|---|---|
| Run the release candidate on the held-out test split | The release candidate answers every question in the held-out `test` split, the runs are tracked in W&B, and no `test` question was used for tuning. | – | To do | [KAN-78](https://yarengursoy.atlassian.net/browse/KAN-78) |
| Review the in-scope test answers against the rubric | One reviewer checks every in-scope `test` answer against the rubric's "fully supported" definition, a second reviewer checks a sample, and disagreements are resolved and logged. | – | To do | [KAN-199](https://yarengursoy.atlassian.net/browse/KAN-199) |
| Report O2 (a)–(d) on the test split | O2 (a)–(d) on the `test` split are reported separately against the levels confirmed in Charter v2, in the Sprint 4 technical summary and the experiment card, each with a link to its W&B run. | – | To do | [KAN-200](https://yarengursoy.atlassian.net/browse/KAN-200) |

**Traceability**

Feature: Feature 6 - Check the source  
Objective: O2 Evidence (a)–(d)  
Deliverable: D11 Release Candidate and Final Evaluation (due 30/12/2026)  
Milestone: M10 (30/12/2026)  
Major Activities: rows 24, 27

## Changes since v1 (27/10/2026)

- [KAN-22](https://yarengursoy.atlassian.net/browse/KAN-22) Read the cited source text behind an answer: test cases TC-22.1 to TC-22.4 added on 08/11/2026 ([KAN-114](https://yarengursoy.atlassian.net/browse/KAN-114)).
- [KAN-77](https://yarengursoy.atlassian.net/browse/KAN-77) Rely on cited provisions confirmed on unseen questions: test cases TC-77.1 to TC-77.5 added on 08/11/2026 ([KAN-114](https://yarengursoy.atlassian.net/browse/KAN-114)).
- - [KAN-116](https://yarengursoy.atlassian.net/browse/KAN-116) Check the story roles against ISO/IEC 5339: role column added to the user stories table on 08/11/2026.
