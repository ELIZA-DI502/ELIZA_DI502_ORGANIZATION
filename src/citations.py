"""Citation check of the answers (KAN-128; KAN-8, acceptance criterion 3).

The assistant may show only citations that match one of the chunks it retrieved for the question.
check_citations() runs after the answer model and before the answer is shown: every sentence or list
item that cites a provision that is not among the retrieved chunks is removed, so 100% of the shown
citations match the retrieved chunk IDs.

The citation pattern and norm() are the same as in the automatic checks of src/rag_vs_no_rag.ipynb
(cell "5. Automatic checks"), with one fix: "Article 1" no longer matches "Article 10(2)".

Run from the repository root to apply the check to the saved baseline answers on the val split
(docs/eval/answers/val-with-retrieval-chunks.jsonl) and print the result; no file is written:
    python src/citations.py
"""
import json
import pathlib
import re

# An Article or Annex reference as the answer model writes it, e.g. "Article 6(3)(a)",
# "Article 113, third paragraph, point (c)(i)", "Annex III, point 3(d)".
CITE = re.compile(
    r"(Article\s+\d+[a-z]?(?:\s*\(\d+\))?(?:,?\s*(?:first|second|third|fourth|fifth)\s+(?:sub)?paragraph)?"
    r"(?:,?\s*point)?(?:\s*\([a-z0-9]+\))*"
    r"|Annex\s+[IVX]+(?:,?\s*point\s*\d+(?:\s*\([a-z]\))?)?)",
    re.I,
)

# Shown when every sentence of the answer had to be removed (the fixed sentence of prompts/answer.yaml).
NO_ANSWER = "The provided text does not answer this question."


def norm(ref):
    """One spelling for a reference: 'Article 6(3), second subparagraph, point (a)' and 'Article 6(3)(a)'
    both become 'article6(3)(a)'; 'Article 113, third paragraph, point (c)(i)' becomes 'article113(3)(c)(i)'."""
    ref = ref.lower()
    ref = re.sub(r"(first|second|third|fourth|fifth) subparagraph", "", ref)
    for n, word in enumerate(["first", "second", "third", "fourth"], 1):      # Article 113, third paragraph = Article 113(3)
        ref = ref.replace(f", {word} paragraph", f"({n})")
    return re.sub(r"[\s,]|point|paragraph", "", ref)


def contains(outer, inner):
    """True if the reference `outer` contains `inner`: 'article6(3)' contains 'article6(3)(a)', and the bare
    'annexiii' contains 'annexiii3(d)'; but 'article1' does not contain 'article10(2)'."""
    if not inner.startswith(outer) or inner == outer:
        return False
    nxt = inner[len(outer)]
    return nxt == "(" or (re.fullmatch(r"annex[ivx]+", outer) is not None and nxt.isdigit())


def matches(cited, allowed):
    """True if the cited reference is one of the allowed (retrieved) references, or a part of one of them
    ('article6(3)(a)' in the chunk 'article6(3)'), or the paragraph or Annex that contains one of them
    ('article6(3)' or 'annexiii' for the chunks 'article6(3)(a)' and 'annexiii3(d)').
    Both arguments are already normalised."""
    return any(cited == a or contains(cited, a) or contains(a, cited) for a in allowed)


def split_units(answer):
    """The answer cut into lines, and each line into sentences; the separators are kept so that the
    answer can be put back together with its original layout."""
    units = []
    for line in answer.splitlines(keepends=True):
        units += re.split(r"(?<=[.!?])(\s+)(?=[A-Z*•\-])", line)
    return units


def check_citations(answer, retrieved_refs):
    """Remove every sentence or list item of `answer` that cites a provision not in `retrieved_refs`
    (the 'ref' field of the retrieved chunks, e.g. 'Article 6(3), second subparagraph, point (a)').

    Returns (shown_answer, removed), where removed lists the citations that did not match, in the
    order they appeared. Sentences without a citation are kept as they are."""
    allowed = {norm(r) for r in retrieved_refs}
    kept, removed = [], []
    for unit in split_units(answer):
        bad = [c for c in CITE.findall(unit) if not matches(norm(c), allowed)]
        if bad:
            removed += bad
            continue
        kept.append(unit)
    shown = re.sub(r"[ \t]{2,}", " ", "".join(kept))
    shown = re.sub(r"\n{3,}", "\n\n", shown).strip()
    if not CITE.search(shown) and removed:            # nothing supported is left
        shown = NO_ANSWER
    return shown, removed


def shown_citations_match(answer, retrieved_refs):
    """True if every citation in `answer` matches a retrieved chunk (the Done-when check of KAN-128)."""
    allowed = {norm(r) for r in retrieved_refs}
    return all(matches(norm(c), allowed) for c in CITE.findall(answer))


if __name__ == "__main__":
    source = pathlib.Path(__file__).resolve().parent.parent / "docs/eval/answers/val-with-retrieval-chunks.jsonl"
    answers, changed, before, after = 0, 0, 0, 0
    for line in source.open(encoding="utf-8"):
        r = json.loads(line)
        refs = [c["ref"] for c in r["chunks"]]
        shown, removed = check_citations(r["answer"], refs)
        assert shown_citations_match(shown, refs), r["id"]      # Done when of KAN-128: 100% of the shown citations match
        answers += 1
        before += len(CITE.findall(r["answer"]))
        after += len(CITE.findall(shown))
        if removed:
            changed += 1
            print(f"{r['id']}: removed {'; '.join(removed)}")
    print(f"{answers} answers; {changed} had a citation that did not match a retrieved chunk")
    print(f"citations before the check: {before}; shown after the check: {after}; shown and matching: 100%")
