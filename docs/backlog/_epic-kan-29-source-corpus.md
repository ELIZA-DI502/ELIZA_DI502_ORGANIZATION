# Story Requirements for Epic KAN-29: Source corpus

Jira export of 27/10/2026, Sprint 1. The same content is on the story requirements page [`09-story-requirements-for-epic-kan-29.md`](../../Markdown%20Template/06-user-stories/09-story-requirements-for-epic-kan-29.md). Back to the [User Story Map v1](../../Markdown%20Template/06-user-stories/01-user-story-map-v1.md) · [all story requirements pages](_README.md).

| Epic | Source corpus |
|---|---|
| Summary | The single source behind every answer: the stored consolidated text of 27/07/2026 with its manifest and provision list (D3, Sprint 1), its parsing and chunking with the preprocessing report (D5, Sprint 2), the check against the Official Journal and the sprint-start check for a newer version. |
| Features | Source manifest and provision list (D3), preprocessing (D5) |
| Document Owner | Yeşim (Product Owner) |
| Designer | Not applicable: this epic produces documents, not a user interface |
| Developers | Yeşim (Sprint 1); later stories are assigned at each sprint planning |
| Release Target (Sprint) | Sprint 1 (Pre-alpha); Sprint 2 (Alpha 0.1) |
| Traceability | Constraints: C-01, C-09. Major Activities rows 4, 8, 32. |
| Jira | [KAN-29](https://yarengursoy.atlassian.net/browse/KAN-29) |

## Requirements

For more info you can visit: https://www.atlassian.com/agile/product-management/requirements.

| # | User story title | User story description | Priority | Points | Owner | Sprint | Notes | Jira |
|---|---|---|---|---|---|---|---|---|
| S1 | [Work from one verified copy of the source](#s1--work-from-one-verified-copy-of-the-source) | As a Data Scientist, I want one stored copy of the consolidated text with its manifest and a list of the in-scope provisions, so that the index and the evaluation questions are built from the same source version. | High | 5 | Yeşim | Sprint 1 | Release: Pre-alpha; Status: Done (27/10/2026). | [KAN-67](https://yarengursoy.atlassian.net/browse/KAN-67) |
| S2 | [Index every in-scope provision with its reference and version date](#s2--index-every-in-scope-provision-with-its-reference-and-version-date) | As a Data Scientist, I want every in-scope provision stored as its own chunk with its Article or Annex reference and the version date, so that retrieval and citations can be checked against the source text. | High | – | – | Sprint 2 | Release: Alpha 0.1. | [KAN-86](https://yarengursoy.atlassian.net/browse/KAN-86) |

Priority, points, owner and sprint are as in Jira on 27/10/2026. Sprint 1 stories were estimated with planning poker; the other stories are estimated and assigned at their sprint planning, starting with Sprint 2 on 28/10/2026. A dash means not decided yet.

Test cases: KAN-8, KAN-2 and KAN-3 already have test cases; a test for every story (the input or steps and the expected result) is added next to it in Sprint 2 ([KAN-90](https://yarengursoy.atlassian.net/browse/KAN-90)).

## S1 · Work from one verified copy of the source

[KAN-67](https://yarengursoy.atlassian.net/browse/KAN-67) · Sprint 1 (Pre-alpha) · Priority High · Points 5 · Owner Yeşim

**Story:** As a Data Scientist, I want one stored copy of the consolidated text with its manifest and a list of the in-scope provisions, so that the index and the evaluation questions are built from the same source version.

**Acceptance criteria**

1. The consolidated text of 27/07/2026 (CELEX 02024R1689-20260727) is stored in the repository, and `data/manifest.csv` records its URL, CELEX number, version date, reuse basis and SHA-256 hash.
2. The reuse basis cites Commission Decision 2011/833/EU and states that only the Official Journal text is legally authentic.
3. The hash in the manifest matches the stored file.
4. The provision list contains the in-scope provisions from the Executive Summary, each marked core, supporting, boundary or if-time.

The mapping of the provision list to the D2 questions is done in Sprint 2, when D2 is complete (11/11/2026).

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Store the consolidated text and write the source manifest | The consolidated text (CELEX 02024R1689-20260727) is stored in the repository. data/manifest.csv has the URL, CELEX number, version date, reuse basis and SHA-256 hash. The reuse basis cites Commission Decision 2011/833/EU and notes that only the Official Journal text is legally binding. The hash matches the stored file. | Yeşim | – | Done | [KAN-54](https://yarengursoy.atlassian.net/browse/KAN-54) |
| Write the in-scope provision list | The provision list contains the in-scope provisions from the Executive Summary (Scope Definition), each with its Article/Annex reference and marked core, supporting, boundary or if-time. The mapping of the list to the D2 questions (D3 criteria 3 and 4) is done in Sprint 2, when D2 is complete (11/11/2026), in a separate task. | Yeşim | – | Done | [KAN-55](https://yarengursoy.atlassian.net/browse/KAN-55) |

The story carries the points and its sub-tasks are not estimated separately (Model A of the course's [Jira sync guide](../JIRA_SYNC_SETUP.md)).

**Traceability**

Deliverable: D3 Source Inventory and Manifest v1 (due 27/10/2026)      
Milestone: M2 Sources and first design ready (28/10/2026)      
Assumptions / constraints / risks: A-01, A-05; C-01, C-09; R-01, R-11

## S2 · Index every in-scope provision with its reference and version date

[KAN-86](https://yarengursoy.atlassian.net/browse/KAN-86) · Sprint 2 (Alpha 0.1) · Priority High · Points – · Owner –

**Story:** As a Data Scientist, I want every in-scope provision stored as its own chunk with its Article or Annex reference and the version date, so that retrieval and citations can be checked against the source text.

**Acceptance criteria**

1. 100% of the provisions in the D3 list are present in the index (D5 criterion 1).
2. 0 chunks lack a structural identifier: Article or Annex number, plus paragraph or point where the text has one (D5 criterion 2).
3. Every chunk carries the version date of the source (D5 criterion 3).
4. The source file hash matches D3 (D5 criterion 4).
5. Chunking parameters are in `config/rag.yaml` (D5 criterion 5).
6. The report gives the share of chunks corrected by hand (A-05 holds at 5% or less) and the number of discrepancies in a random sample of 20 chunks compared word for word with the source (D5 criterion 6).
7. The corpus is described in the course's dataset register or dataset report (course Sprint 2 deliverable).

**Sub-tasks**

| Sub-task | Done when | Owner | Estimate | Status | Jira |
|---|---|---|---|---|---|
| Parse the stored EUR-Lex text into provisions | Every provision in the D3 list is extracted from the stored file with its Article or Annex identifier; the file hash is checked against `data/manifest.csv` before parsing. | – | – | To do | [KAN-92](https://yarengursoy.atlassian.net/browse/KAN-92) |
| Chunk the provisions and add their metadata | There is one chunk per Article paragraph or Annex point, each with its identifier and the version date; the chunking parameters are in `config/rag.yaml`. | – | – | To do | [KAN-93](https://yarengursoy.atlassian.net/browse/KAN-93) |
| Check 20 random chunks against the source text | 20 randomly chosen chunks are compared word for word with the source text; the number of discrepancies and the share of chunks corrected by hand are recorded (A-05 holds at 5% or less). | – | – | To do | [KAN-94](https://yarengursoy.atlassian.net/browse/KAN-94) |
| Write the preprocessing report | `docs/eval/preprocessing.md` describes parsing, chunking and metadata with counts, and gives the results of the 20-chunk check. | – | – | To do | [KAN-95](https://yarengursoy.atlassian.net/browse/KAN-95) |
| Complete the corpus datasheet | The consolidated text has its entry in `Markdown Template/11-datasheets/01-third-party-dataset-register.md` (or `02-dataset-report.md`), with source, version, licence and preprocessing. | – | – | To do | [KAN-96](https://yarengursoy.atlassian.net/browse/KAN-96) |
| Check EUR-Lex for a newer consolidated version | At the start of Sprint 2, EUR-Lex is checked for a consolidated version newer than 27/07/2026 or an amendment to an in-scope provision; the result and the check date are recorded. A change of the designated version needs Product Owner approval and an ADR. | – | – | To do | [KAN-157](https://yarengursoy.atlassian.net/browse/KAN-157) |

Sub-task owners are assigned at the sprint planning.

**Traceability**

Deliverable: D5 Preprocessing Report v1 (due 14/11/2026)      
Milestone: M4 Baseline (alpha) runs on the full validation question set (18/11/2026)      
Major Activities: row 8      
Dependencies: rows 3, 4      
Constraint: C-01 Single source (consolidated text of 27/07/2026)      
Assumption / Risk: A-05 / R-11 The source format is uneven
