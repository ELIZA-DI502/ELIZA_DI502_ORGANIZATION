"""Parsing spike (25/10/2026): split Article 6 and Annex III point 3 into chunks.

Input: text from the EUR-Lex PDF of 27/07/2026 (pdftotext -layout), cut to art6.txt and annex3.txt.
Spike code, not production code.

Rules:
- a line "1." or "1a." starts a paragraph (amended paragraphs have a letter: 1a, 1b, 1c);
- a line "(a)" starts a point;
- a line at the paragraph's indent after a point starts a new subparagraph
  (for example the profiling rule of Article 6(3)), so it is not attached to the last point;
- a word broken at the end of a line (soft hyphen) is joined again; a real hyphen is kept.
"""
import re
import sys

ORDINALS = ["first", "second", "third", "fourth", "fifth"]


def read_lines(path):
    """Return (indent, text) for every content line; drop page headers and amendment markers."""
    out = []
    for raw in open(path, encoding="utf-8"):
        raw = raw.rstrip("\n")
        text = raw.strip()
        if not text or text.startswith("▼") or re.match(r"^\d{5}R\d{4} — EN", text):
            continue
        out.append((len(raw) - len(raw.lstrip(" ")), text))
    return out


def join(parts):
    """Join lines; a line ending in a soft hyphen or "-" before a lowercase word is joined without a space."""
    text = ""
    for p in parts:
        if text.endswith("­"):
            text = text.rstrip("­") + p
        elif text.endswith("-") and p[:1].islower():
            text = text + p  # keep a real hyphen, e.g. "decision-making"
        else:
            text = (text + " " + p).strip()
    return text.replace("­", "")


def chunks_article(path, art):
    lines = read_lines(path)[2:]  # skip "Article N" and its title
    res, buf = [], []
    para = point = None
    base = None  # indent of the paragraph text
    sub = 1  # subparagraph number inside the paragraph

    def flush(cid):
        if buf and cid:
            res.append((cid, join(buf)))

    cid = None
    for indent, t in lines:
        m = re.match(r"^(\d+[a-z]?)\.\s+(.*)", t)
        n = re.match(r"^\(([a-z])\)\s+(.*)", t)
        if m:
            flush(cid)
            para, point, sub, base = m.group(1), None, 1, indent
            cid, buf = f"Article {art}({para})", [m.group(2)]
        elif n and para:
            flush(cid)
            point = n.group(1)
            cid, buf = f"Article {art}({para})({point})", [n.group(2)]
        elif point and indent <= base and buf and buf[-1].endswith((".", ";", ":")):
            # back at the paragraph's indent after a point: a new subparagraph
            flush(cid)
            point, sub = None, sub + 1
            cid, buf = f"Article {art}({para}), {ORDINALS[sub - 1]} subparagraph", [t]
        else:
            buf.append(t)
    flush(cid)
    return res


def chunks_annex3_point3(path):
    res, buf = [], []
    area = point = None
    for _, t in read_lines(path):
        m = re.match(r"^(\d+)\.\s+(.*)", t)
        n = re.match(r"^\(([a-z])\)\s+(.*)", t)
        if m:
            if area == "3" and point:
                res.append((f"Annex III 3({point})", join(buf)))
            area, point, buf = m.group(1), None, []
        elif n:
            if area == "3" and point:
                res.append((f"Annex III 3({point})", join(buf)))
            point, buf = n.group(1), [n.group(2)]
        elif point:
            buf.append(t)
    if area == "3" and point:
        res.append((f"Annex III 3({point})", join(buf)))
    return res


if __name__ == "__main__":
    art6, annex3 = sys.argv[1:3]
    chunks = chunks_article(art6, "6") + chunks_annex3_point3(annex3)
    for cid, text in chunks:
        print(f"{cid:38} {len(text.split()):3} words | {text[:70]}")
    print(len(chunks), "chunks")
