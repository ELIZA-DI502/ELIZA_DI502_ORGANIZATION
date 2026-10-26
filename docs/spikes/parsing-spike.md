# Spike: parsing and chunking the regulation

**Sprint:** 1 · **Date:** 25/10/2026 · **Jira:** KAN-56 · **Results:** [`parsing-chunks.csv`](parsing-chunks.csv)

## Question

Can the text be split into one chunk per point, or per paragraph when it has no points, each with the correct Article number (D7)?

## How we tested

Article 6 and Annex III point 3 were taken from the EUR-Lex PDF of 27/07/2026 and split line by line:

```python
for line in lines:
    if line starts with "1." or "1a.":   start a new paragraph chunk   -> Article 6(1a)
    elif line starts with "(a)":         start a new point chunk       -> Article 6(3)(a)
    elif after a point, back at the paragraph's indent:
                                         start a new subparagraph chunk -> Article 6(3), second subparagraph
    else:                                add the line to the current chunk
# a word broken at the end of a line ("malfunc-" + "tioning") is joined again
```

## Results

**22 chunks**, all with the correct ID: 18 from Article 6 and 4 from Annex III point 3 (3(a)–3(d)).

Three problems were found and fixed:

1. The sentence after the last point (the profiling rule of Article 6(3)) was attached to point (d). It is now its own chunk.
2. Words broken across lines stayed split ("malfunc tioning"). They are now joined.
3. Amended paragraphs have letters in their numbers (6(1a), 6(1b), 6(1c)). They are now recognised.

## Decision

D7 works. The same rules go into `rag/ingest.py` in Sprint 2, where the HTML version (D8) is also tried.
