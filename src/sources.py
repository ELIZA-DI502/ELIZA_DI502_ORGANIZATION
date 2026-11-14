"""Sources line of the answers: each cited provision with its reference and version date (KAN-126; D6 criterion 3, O2 (c)).

The answer model does not write the version date (E1). add_sources() runs after check_citations() of
src/citations.py (KAN-128): it appends one line that lists every provision left cited in the shown answer, at
the level of detail of the citation (paragraph or point when the answer names one), with the version date
stored in the retrieved chunk(s) the citation matches, for example:

    Sources (consolidated text of 27/07/2026): Article 6(3), first subparagraph; Annex III, point 3(b)

An answer that cites nothing (for example the fixed sentence "The provided text does not answer this question.")
is not a substantive answer and gets no sources line.

Run from the repository root to apply it to the saved baseline answers on the val split
(docs/eval/answers/val-with-retrieval-chunks.jsonl, written by src/rag_vs_no_rag.ipynb, KAN-125); it prints the
result and writes docs/eval/answers/val-with-retrieval-shown.csv (the answers as they are shown):
    python src/sources.py
"""
import csv
import json
import pathlib

from citations import CITE, NO_ANSWER, check_citations, contains, norm


def cited_sources(answer, chunks):
    """The sources of `answer`: one (reference, version date) pair for each provision it cites, in the order
    they are first cited, without repeats.

    `chunks` are the retrieved chunks, each a dict with 'ref' and 'version_date'. The shown reference keeps the
    level of detail of the citation:
    - the citation is the reference of a retrieved chunk: the chunk's reference, in the spelling of the
      provision list ('Article 6(3)(a)' is shown as 'Article 6(3), second subparagraph, point (a)');
    - otherwise the citation is a part of a retrieved chunk ('Article 10(2)(f)' in the chunk 'Article 10(2)')
      or contains retrieved chunks ('Article 9' for the chunk 'Article 9(6)'): the citation as the answer
      writes it, because the chunk is wider or narrower than what the answer used.
    A citation that matches no retrieved chunk is skipped (check_citations() has already removed it).
    The version date is the one stored in the matching chunk(s); the two parts of a split chunk share it."""
    sources, seen = [], set()
    for cite in CITE.findall(answer):
        c = norm(cite)
        if c in seen:
            continue
        exact = [ch for ch in chunks if norm(ch["ref"]) == c]
        related = exact or [ch for ch in chunks if contains(c, norm(ch["ref"])) or contains(norm(ch["ref"]), c)]
        if not related:
            continue
        seen.add(c)
        ref = exact[0]["ref"] if exact else " ".join(cite.split())
        for date in dict.fromkeys(ch["version_date"] for ch in related):
            sources.append((ref, date))
    return sources


def add_sources(answer, chunks):
    """`answer` with a sources line that lists every cited provision with the version date of its chunk.

    Returns (shown_answer, sources) where sources is the list of shown references; if the answer cites
    nothing, it is returned unchanged with an empty list."""
    used = cited_sources(answer, chunks)
    if not used:
        return answer, []
    by_date = {}
    for ref, date in used:                               # one group per version date (all 27/07/2026 in v1)
        by_date.setdefault(date, []).append(ref)
    lines = [f"Sources (consolidated text of {date}): " + "; ".join(refs) for date, refs in by_date.items()]
    return answer.rstrip() + "\n\n" + "\n".join(lines), [ref for ref, _ in used]


def shown_answer(answer, chunks):
    """The answer as the assistant shows it: the citation check of KAN-128, then the sources line of KAN-126."""
    checked, removed = check_citations(answer, [c["ref"] for c in chunks])
    shown, sources = add_sources(checked, chunks)
    return shown, sources, removed


if __name__ == "__main__":
    root = pathlib.Path(__file__).resolve().parent.parent
    source = root / "docs/eval/answers/val-with-retrieval-chunks.jsonl"
    target = root / "docs/eval/answers/val-with-retrieval-shown.csv"
    rows = []
    with_sources = with_sources_dated = 0          # answers that cite at least one provision after the check
    e1 = e1_dated = 0                              # E1 definition: answers without the fixed sentence (20 in E1)
    for line in source.open(encoding="utf-8"):
        r = json.loads(line)
        shown, sources, removed = shown_answer(r["answer"], r["chunks"])
        dated = bool(sources) and "Sources (consolidated text of " in shown
        if sources:
            with_sources += 1
            with_sources_dated += dated
        checked = shown.split("\n\nSources (consolidated text of ")[0]
        if NO_ANSWER not in checked:
            e1 += 1
            e1_dated += dated
        rows.append({"id": r["id"], "shown_answer": shown, "sources": "; ".join(sources),
                     "removed_citations": "; ".join(removed)})
    with target.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "shown_answer", "sources", "removed_citations"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} answers")
    print(f"O2 (c), E1 definition (answers without the fixed sentence): {e1_dated} of {e1} with references and the version date")
    print(f"all answers that cite a provision after the citation check: {with_sources_dated} of {with_sources} with references and the version date")
    print(f"written: {target.relative_to(root)}")
