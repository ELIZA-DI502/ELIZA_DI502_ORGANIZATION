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
