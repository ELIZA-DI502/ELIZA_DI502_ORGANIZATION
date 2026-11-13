# Preprocessing

*Preprocessing Report v1 (D5), Sprint 2, written by Yaren Gürsoy (KAN-95) from the chunking notebook [`src/chunking.ipynb`](../../src/chunking.ipynb) (Gözde Nur Özdemir, KAN-92, KAN-93) and the files in `data/`.*

This report says how the regulation text is turned into the chunks that the assistant searches and cites. The settings are in [`config/rag.yaml`](../../config/rag.yaml) (`chunking`), not here (D5 criterion 5).

## Source

| Item | Value |
|---|---|
| Text | Regulation (EU) 2024/1689, consolidated text of 27/07/2026 (CELEX 02024R1689-20260727), English; includes Regulation (EU) 2026/1744 (M1) |
| Parsing input | `data/CELEX_02024R1689-20260727_EN.html`, SRC-02 in [`data/manifest.csv`](../../data/manifest.csv) (design decision D8); 850,466 characters |
| Hash check | SHA-256 `e7184c2b0a8037fb…` matches `data/manifest.csv`: **yes** (D5 criterion 4) |
| Fallback | the PDF of the same version (SRC-01); it gives the same text for every listed provision except Article 15(5), where the PDF parser added a section heading |
| Scope | the 103 provisions of [`data/provision-list.csv`](../../data/provision-list.csv) (D3, C-01): 68 core, 28 supporting, 2 boundary, 5 if-time |

## Parsing

The EUR-Lex HTML marks every part of the law: each Article is a `div` with its number (`art_6`), each numbered paragraph starts with a `no-parag` span, and each point such as (a) is a list box. The notebook walks through every Article and the Annexes and stores each paragraph, subparagraph, point and sub-point as one unit.

| Count | Value |
|---|---|
| Articles found | 119 |
| Annexes found | 12 |
| Units read (paragraphs, subparagraphs, points, sub-points) | 1,377 |
| Units in scope (used by the 103 provisions) | 174 |
| Units outside the scope (not used, C-01) | 1,203 |

## Chunking

**One chunk per provision** of the provision list (design decision D7). The law is already divided into numbered parts, and every answer must cite the exact part (for example Article 6(3)(a)), so a chunk that is one provision gives the citation directly. Each reference in the provision list (for example `Article 6(3), second subparagraph, point (a)`) is turned into numbers (Article 6, paragraph 3, subparagraph 2, point a), and the matching units are joined.

A provision longer than `max_chars` (1,500 characters) is split at its points; each part keeps the heading and gets a suffix (`#1`, `#2`).

| Count | Value |
|---|---|
| Provisions in the list | 103 |
| Provisions found in the HTML | 103 of 103 (100%, D5 criterion 1) |
| Provisions split because they are longer than 1,500 characters | 2: Article 4a(1) and Article 13(3) |
| Chunks | 105 (101 from Articles, 4 from Annex III point 3) |
| Length in words | min 7, median 42, max 224; 6,155 in total |

**Compared with fixed-size chunks.** The same text cut into pieces of 1,000 characters gives 39 pieces: 36 of them mix two or more provisions and 36 start in the middle of a sentence. A citation from such a piece could not point to one provision.

Chunks by area:

| Area | Chunks |
|---|---|
| Requirements for high-risk systems (Articles 8–15) | 37 |
| Definitions (Article 3) | 15 |
| Scope (Article 2) | 13 |
| Provider obligations (Article 16) | 12 |
| High-risk classification (Article 6, Article 49(2)) | 9 |
| Application dates (Article 113) | 7 |
| If time, not committed (Articles 4 and 4a) | 6 |
| Education use cases (Annex III, point 3) | 4 |
| Boundary cases (Article 5(1)(f), Article 50(1)) | 2 |

## Metadata

Every chunk is a row of [`data/chunks.csv`](../../data/chunks.csv) and a line of [`data/chunks.jsonl`](../../data/chunks.jsonl) with these fields:

| Field | What it holds |
|---|---|
| `chunk_id` | unique ID, e.g. `ART6-3-a`; `#1`, `#2` for the parts of a split provision |
| `ref`, `parent` | the reference as it is cited (`Article 6(3), second subparagraph, point (a)`) and the paragraph it belongs to |
| `kind`, `number`, `title`, `chapter` | Article or Annex, its number, heading and chapter |
| `priority`, `area` | from the provision list: core, supporting, boundary or if-time, and the area |
| `version_date`, `celex`, `language`, `source` | 27/07/2026, 02024R1689-20260727, en, the HTML file |
| `amended_by` | Regulation (EU) 2026/1744 where the 2026 amendment changed the provision |
| `text` | the provision itself, as an answer quotes it |
| `heading`, `intro`, `embed_text` | the Article heading and the sentence that introduces a point; `embed_text` = heading + intro + text, which is what the search embeds, so that a short point such as "(a) the AI system is intended to perform a narrow procedural task" still says what it belongs to |
| `order`, `units`, `prev_id`, `next_id`, `words` | position in the law, the HTML units used, the chunks before and after it in the same Article, and the length |

| Check | Result |
|---|---|
| Chunks without a structural identifier (D5 criterion 2) | 0 of 105 |
| Duplicate chunk IDs | 0 |
| Chunks with the version date of the source (D5 criterion 3) | 105 of 105 (27/07/2026) |
| Chunks changed by Regulation (EU) 2026/1744 | 15 (Article 2(2), 2(7), 2(13); Article 4; Article 4a; Article 10(1), 10(6); Article 113, third paragraph, points (a), (c)(i), (c)(ii), (d)) |
| Chunks corrected by hand (D5 criterion 6, A-05) | 0 of 105 (0%), see the check below |

## Check of 20 random chunks (KAN-94)

**Sample:** 20 of the 105 chunks in `data/chunks.csv`, drawn with `random.seed(42)`.
**Source:** `data/CELEX_02024R1689-20260727_EN.pdf` (SHA-256 matches `data/manifest.csv`: yes).
**Method:** each chunk's `text` was compared word for word with the text of the stored PDF by a script. Before the comparison, line breaks, page footers, amendment markers (▼M1, ▼B), soft hyphens and typographic quote and dash marks were normalised. Chunks that did not match were checked against the raw PDF text and the HTML source.

| chunk_id | Provision | Words | Result | Note |
|---|---|---|---|---|
| ART2-4 | Article 2(4) | 83 | Match | The PDF splits "cooperation" at a line break; the chunk is correct. |
| ART2-5 | Article 2(5) | 29 | Match | |
| ART2-12 | Article 2(12) | 42 | Match | |
| ART3-1 | Article 3, point (1) | 55 | Match | |
| ART3-2 | Article 3, point (2) | 19 | Match | |
| ART3-9 | Article 3, point (9) | 23 | Match | |
| ART3-52 | Article 3, point (52) | 15 | Match | |
| ART4-1 | Article 4(1) | 92 | Match | |
| ART4-2 | Article 4(2) | 61 | Match | |
| ART4A-1#1 | Article 4a(1) | 205 | Match | The PDF splits four words at line breaks; the chunk is correct. |
| ART6-2 | Article 6(2) | 26 | Match | |
| ART9-10 | Article 9(10) | 48 | Match | |
| ART12-2 | Article 12(2) | 86 | Match | |
| ART13-3#2 | Article 13(3) | 149 | Match | |
| ART14-2 | Article 14(2) | 57 | Match | |
| ART15-1 | Article 15(1) | 35 | Match | |
| ART15-3 | Article 15(3) | 23 | Match | |
| ART16-b | Article 16, point (b) | 39 | Match | |
| ART16-g | Article 16, point (g) | 13 | Match | |
| ART113-1 | Article 113, first paragraph | 24 | Discrepancy | A space before the final full stop ("European Union ."), caused by the italic tag in the HTML source. No word, number or reference differs. |

**Result:** 20 chunks compared; 19 identical to the source, 1 discrepancy (formatting only: a space before a full stop). The same pattern was searched in all 105 chunks and found only in ART113-1.
**Corrected by hand:** 0 of 105 chunks (0%). The space in ART113-1 changes no word, number or reference, so the chunk is left as it is and the space is removed in the parsing code with the next re-index (KAN-93).
**Assumption A-05:** holds. 1 of the 20 sampled chunks (5%) differs from the source, in formatting only, and 0% of the chunks needed a fix by hand, within the 5% limit. Risk R-11 is not triggered.
