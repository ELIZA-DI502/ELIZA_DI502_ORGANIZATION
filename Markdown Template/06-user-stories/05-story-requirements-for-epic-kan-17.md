# Story Requirements for Epic KAN-17: Show the Source

Version v1, end of Sprint 1 (27/10/2026). Source: Jira project KAN. Back to the [User Story Map v1](01-user-story-map-v1.md) · [all story requirements pages](README.md).

| Epic | Show the Source |
|---|---|
| Summary | Letting users check every answer against its source: the text of each cited provision shown under the answer with its reference, version date and a link to EUR-Lex (Feature 6), and the final check of the citations on the held-out `test` split (O2 (a)–(d); D11). |
| Features | F6 Check the source |
| Document Owner | Yeşim (Product Owner) |
| Designer | Gözde Nur (design decisions, KAN-58) and Kaan (design document, KAN-59) |
| Developers | Yaren (Sprint 1); later stories are assigned at each sprint planning |
| Release Target (Sprint) | Sprint 4 (Release candidate 1.0) |
| Traceability | Objective: O2 Evidence. Major Activities rows 15, 24, 27. Constraints: C-01, C-09. |
| Jira | [KAN-17](https://yarengursoy.atlassian.net/browse/KAN-17) |

## Requirements

For more info you can visit: https://www.atlassian.com/agile/product-management/requirements.

| # | User story title | User story description | Priority | Points | Owner | Sprint | Notes | Jira |
|---|---|---|---|---|---|---|---|---|
| S1 | [Read the cited source text behind an answer](#s1--read-the-cited-source-text-behind-an-answer) | As a compliance officer in an EdTech provider's legal team, I want to read the source text of each provision cited in an answer, so that I can verify the explanation before advising the development team. | High | – | – | Sprint 4 | Release: Release candidate 1.0; Feature: F6; Depends on [KAN-8](https://yarengursoy.atlassian.net/browse/KAN-8) (the cited provisions must be found first). Needed in the pilot version by 16/12/2026. | [KAN-22](https://yarengursoy.atlassian.net/browse/KAN-22) |
| S2 | [Rely on cited provisions confirmed on unseen questions](#s2--rely-on-cited-provisions-confirmed-on-unseen-questions) | As a compliance officer in an EdTech provider's legal team, I want the assistant's citations to be confirmed on questions it has not seen before, so that I can trust that developers receive the right Article or Annex with the correct version date. | High | – | Yaren | Sprint 4 | Release: Release candidate 1.0; Feature: F6. | [KAN-77](https://yarengursoy.atlassian.net/browse/KAN-77) |

Priority, points, owner and sprint are as in Jira on 27/10/2026. Sprint 1 stories were estimated with planning poker; the other stories are estimated and assigned at their sprint planning, starting with Sprint 2 on 28/10/2026. A dash means not decided yet.

## S1 · Read the cited source text behind an answer

[KAN-22](https://yarengursoy.atlassian.net/browse/KAN-22) · Sprint 4 (Release candidate 1.0) · Priority High · Points – · Owner –

**Story:** As a compliance officer in an EdTech provider's legal team, I want to read the source text of each provision cited in an answer, so that I can verify the explanation before advising the development team.

**Acceptance criteria**

1. When an answer cites a provision, the assistant shall let the user open the text of that provision under the answer.
2. When the text is shown, the assistant shall show it exactly as in the stored consolidated text of 27 July 2026, with its Article or Annex reference and the version date.
3. When the text is shown, the assistant shall name EUR-Lex as the source and link to the consolidated text.
4. For every provision cited in the answers to the D8 `val` split, the text shown shall match the corresponding cited provision in the stored consolidated text identified in the source manifest (D3).

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Open the cited provision under the answer | Every provision cited in an answer can be opened under that answer. | – | – | To do | [KAN-194](https://yarengursoy.atlassian.net/browse/KAN-194) |
| Show the stored text with its reference and version date | The opened text is exactly as in the stored consolidated text of 27/07/2026, with its Article or Annex reference and the version date. | – | – | To do | [KAN-195](https://yarengursoy.atlassian.net/browse/KAN-195) |
| Name EUR-Lex and link to the consolidated text | The opened text names EUR-Lex as the source and links to the consolidated text. | – | – | To do | [KAN-196](https://yarengursoy.atlassian.net/browse/KAN-196) |
| Check the shown texts on the val split | For every provision cited in the answers to the D8 `val` questions, the shown text matches the corresponding provision in the stored consolidated text identified in the source manifest (D3). | – | – | To do | [KAN-197](https://yarengursoy.atlassian.net/browse/KAN-197) |

Sub-task owners are assigned at the sprint planning.

**Traceability**

Feature: Feature 6 - Check the source        
Objective: O2 Evidence        
Deliverable: D11 Release Candidate and Final Evaluation (due 30/12/2026)        
Needed in the pilot version by 16/12/2026 (first week of Sprint 4; Release Plan; Dependencies row 13)        
Milestone: M10 (30/12/2026)        
Major Activities: row 15        
Constraints: C-01 Single source (consolidated text of 27/07/2026); C-09 EUR-Lex reuse with source acknowledgement        
Risk: R-01 Source text differs from the Official Journal        
Depends on: KAN-8

## S2 · Rely on cited provisions confirmed on unseen questions

[KAN-77](https://yarengursoy.atlassian.net/browse/KAN-77) · Sprint 4 (Release candidate 1.0) · Priority High · Points – · Owner Yaren

**Story:** As a compliance officer in an EdTech provider's legal team, I want the assistant's citations to be confirmed on questions it has not seen before, so that I can trust that developers receive the right Article or Annex with the correct version date.

**Acceptance criteria**

1. The release candidate answers every question in the held-out `test` split; the `test` questions were not used for tuning.
2. The expected provision is among the cited sources for at least 80% of the in-scope `test` questions (O2 (a)).
3. At least 75% of the in-scope `test` answers are fully supported by the passages they cite (O2 (b)); every in-scope answer is reviewed by one reviewer and a sample by a second reviewer.
4. 100% of substantive answers cite at least one Article or Annex with the version date (O2 (c)), and at most one application-date question gets a date that is not from the 27/07/2026 text (O2 (d)).
5. Every result is reported in the Sprint 4 technical summary and its experiment card, with a link to its W&B run.

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Run the release candidate on the held-out test split | The release candidate answers every question in the held-out `test` split, the runs are tracked in W&B, and no `test` question was used for tuning. | – | – | To do | [KAN-78](https://yarengursoy.atlassian.net/browse/KAN-78) |
| Review the in-scope test answers against the rubric | One reviewer checks every in-scope `test` answer against the rubric's "fully supported" definition, a second reviewer checks a sample, and disagreements are resolved and logged. | – | – | To do | [KAN-199](https://yarengursoy.atlassian.net/browse/KAN-199) |
| Report O2 (a)–(d) on the test split | O2 (a)–(d) on the `test` split are reported separately against the levels confirmed in Charter v2, in the Sprint 4 technical summary and the experiment card, each with a link to its W&B run. | – | – | To do | [KAN-200](https://yarengursoy.atlassian.net/browse/KAN-200) |

Sub-task owners are assigned at the sprint planning.

**Traceability**

Feature: Feature 6 - Check the source    
Objective: O2 Evidence (a)–(d)    
Deliverable: D11 Release Candidate and Final Evaluation (due 30/12/2026)    
Milestone: M10 (30/12/2026)    
Major Activities: rows 24, 27
