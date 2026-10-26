# Source Inventory and Manifest v1 (D3)

**Deliverable:** D3 Source Inventory and Manifest v1 · **Due:** 27/10/2026 · **Approver:** Product Owner · **Jira:** [KAN-67](https://yarengursoy.atlassian.net/browse/KAN-67) ([KAN-54](https://yarengursoy.atlassian.net/browse/KAN-54), [KAN-55](https://yarengursoy.atlassian.net/browse/KAN-55)) · **Charter:** [Deliverables](../Markdown%20Template/03-project-canvas/05-deliverables.md), constraints C-01 and C-09

This folder holds the single source behind every answer (C-01): the consolidated text of Regulation (EU) 2024/1689 of 27/07/2026, its manifest and the list of in-scope provisions.

## Files

| File | What it is |
|---|---|
| `CELEX_02024R1689-20260727_EN.pdf` | The stored consolidated text (EUR-Lex, CELEX 02024R1689-20260727, English, 151 pages). It includes the amendment by Regulation (EU) 2026/1744 (marked ▼M1 in the text). |
| `manifest.csv` | One row per stored document: source URL, CELEX number, version date, reuse basis and SHA-256 hash, plus the format, the amendments included and notes. |
| `provision-list.csv` | The in-scope provisions, one row per paragraph, point or definition, each marked core, supporting, boundary or if-time as in the [Project Executive Summary](../Markdown%20Template/03-project-canvas/01-project-executive-summary.md) (Scope Definition). |

## Checking the stored file

The hash in `manifest.csv` must match the stored file (D3 criterion 6). From the repository root:

```bash
sha256sum data/CELEX_02024R1689-20260727_EN.pdf
# expected: 1ccd38d1c78482cf2053b70110115adcc5080700acc8bd7bead8cb3579143ccf
```

Result on 26/10/2026: **match (yes)**. The parsing script checks the same hash before every run (D5, [KAN-92](https://yarengursoy.atlassian.net/browse/KAN-92)).

## Reuse basis and legal status

EUR-Lex content is reused under Commission Decision 2011/833/EU, with source acknowledgement: © European Union, https://eur-lex.europa.eu (C-09). The consolidated text is a documentation tool with no legal effect; only the texts published in the *Official Journal of the European Union* are authentic. The assistant states this on its page ([KAN-25](https://yarengursoy.atlassian.net/browse/KAN-25)), and the risk that the consolidated text differs from the Official Journal is R-01.

## Provision list

101 provisions: 66 core, 28 supporting, 2 boundary and 5 if-time. They follow the provision priority in the Scope Definition:

| Priority | Area | Provisions | Count |
|---|---|---|---|
| core | Education use cases | Annex III, point 3(a); Annex III, point 3(b); Annex III, point 3(c); Annex III, point 3(d) | 4 |
| core | High-risk classification | Article 6(2) … Article 6(3), third subparagraph | 7 |
| core | Requirements for high-risk systems | Article 8(1) … Article 15(5) | 36 |
| core | Provider obligations | Article 16, point (a) … Article 16, point (l) | 12 |
| core | Application dates | Article 113, first paragraph … Article 113, third paragraph, point (d) | 7 |
| supporting | Scope | Article 2(1) … Article 2(13) | 13 |
| supporting | Definitions | Article 3, point (1) … Article 3, point (52) | 15 |
| boundary | Boundary cases | Article 5(1), first subparagraph, point (f); Article 50(1) | 2 |
| if-time | If time (not committed) | Article 4(1) … Article 4a(2) | 5 |

**Columns of `provision-list.csv`:** `provision_id` (stable ID used in the evaluation set and the chunks), `reference` (as it is cited in answers), `title` (Article title or defined term), `priority`, `area`, `amended_by_2026_1744` (filled when the provision is marked ▼M1 in the stored text), `reason_for_inclusion` (one line) and `d2_questions` (filled on 11/11/2026).

**Notes on the stored version**

- 14 listed provisions are marked as amended by Regulation (EU) 2026/1744, among them the application dates in Article 113 (points (a), (c) and (d)). Answers about these provisions use the 27/07/2026 wording only (C-01).
- Article 10(5) is deleted in this version (marked ▼M1), so it is not in the list. Article 4a, added by the same amendment, covers the processing of special categories of personal data for bias detection; it is listed as if-time.
- Only the selected definitions in Article 3 that the core and boundary provisions use are listed (supporting). Other definitions are added only if a D2 question needs them.
- Commission guidelines and other documents are not added (single source, C-01).

## Still to do (Sprint 2)

| What | When | Jira |
|---|---|---|
| Map every D2 gold source to this list; add any missing provision within the scope; give every provision not used by a question a one-line reason (D3 criteria 3 and 4) | 11/11/2026 | [KAN-84](https://yarengursoy.atlassian.net/browse/KAN-84) |
| Check EUR-Lex for a version newer than 27/07/2026 or an amendment to an in-scope provision | Start of Sprint 2 | [KAN-157](https://yarengursoy.atlassian.net/browse/KAN-157) |
| Store the HTML version of the same consolidated text (design decision D8) and add it to `manifest.csv` with its hash | Sprint 2 | [KAN-92](https://yarengursoy.atlassian.net/browse/KAN-92) |

## D3 acceptance criteria

| # | Criterion | Status on 26/10/2026 |
|---|---|---|
| 1 | Every document has all five manifest fields (URL, CELEX, version date, reuse basis, SHA-256 hash) | Yes (1 document) |
| 2 | The reuse basis cites Commission Decision 2011/833/EU and notes that only the Official Journal text is legally binding | Yes |
| 3 | 100% of the D2 gold sources appear in the provision list | Checked on 11/11/2026, when D2 is complete (KAN-84) |
| 4 | Every provision is needed by at least one D2 question or has a one-line reason | Every provision has a reason now; the question mapping is checked on 11/11/2026 (KAN-84) |
| 5 | Each provision is marked core, supporting, boundary or if-time | Yes |
| 6 | The hash in the manifest matches the stored file | Yes |
