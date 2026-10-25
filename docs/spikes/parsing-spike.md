# Spike: parsing and chunking the regulation

**Sprint:** 1 · **Date:** 25/10/2026 · **Jira:** KAN-56

## Question

Can the text be split into one chunk per point, or per paragraph when it has no points, each with the correct Article number (D7)?

## What was done

Article 6 and Annex III point 3 were taken from the EUR-Lex PDF of 27/07/2026 and split with a short script ([`parse_spike.py`](parsing/parse_spike.py)):

- A line that starts with `1.` (or `1a.`) begins a paragraph.
- A line that starts with `(a)` begins a point.
- A sentence after the last point, at the paragraph's indent, begins a new subparagraph.

## Result

The script made **22 chunks**, and every chunk got the correct ID.

| Text | Chunks |
|---|---|
| Article 6 | 18: paragraphs 1, 1a, 1b, 1c and 2–8; points 6(1)(a)–(b) and 6(3)(a)–(d); the second subparagraph of 6(3) (the profiling rule) |
| Annex III point 3 | 4: 3(a), 3(b), 3(c), 3(d) |

## Problems found and fixed

1. **The sentence after the last point was attached to that point.** The profiling rule of Article 6(3) ended up in chunk 6(3)(d). It is now its own chunk, "Article 6(3), second subparagraph", because the evaluation questions cite it.
2. **Words broken across lines stayed split**, for example "malfunc tioning" and "appro priate". They are now joined again ("malfunctioning", "appropriate"); real hyphens such as "decision-making" are kept.
3. **Amended paragraphs have letters in their numbers**: 6(1a), 6(1b) and 6(1c). The parser recognises them.

## Decision

D7 works. The same rules go into `rag/ingest.py` in Sprint 2, where the HTML version (D8) is also tried. This spike used the PDF.
