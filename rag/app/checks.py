"""Rule-based input and output checks of the RAG service (D3).

The verdict, evasion and out-of-scope patterns are taken from the model selection spike, run 5
(docs/spikes/model-selection/checks.py on the KAN-30-evaluation-gozde-nur branch). The fixed texts
come from prompts/answer.yaml. Open (section 7 of the design document): the personal-data rules
and the citation-ID check (KAN-49), and the legal-decision patterns (KAN-2).
"""
import re

from .config import PERSONAL_DATA, PROMPT_RAG

REFUSAL = PROMPT_RAG["refusal"]
OUT_OF_SCOPE = PROMPT_RAG["out_of_scope"]
NOTICE = PROMPT_RAG["notice"]
PERSONAL_DATA_NOTICE = PROMPT_RAG.get(
    "personal_data",
    "Your question seems to contain personal data, such as an e-mail address or a phone number. "
    "Please remove it and ask again; I do not need personal data to explain the provisions.")

# ---------------------------------------------------------------- input check

EVADE = r"(avoid|skip|get around|circumvent|bypass|evade|escape|loophole|hide|conceal|don'?t have to (follow|comply)|do not have to (follow|comply)|look(s)? like (a|just)|keep us out of)"
EVADE_TARGET = r"(rule|requirement|high-risk|authorit|regulat|ai act|document)"
OOS = r"\b(fine|fines|penalt\w*|sanction\w*|enforcement|gdpr|data protection|parental consent)\b"
# Draft (KAN-2): a question that asks for a decision about the user's own system. Flagged, not blocked.
VERDICT_REQUEST = (
    r"\b(is|are|would|will|does|do)\s+(our|my|this|the|we|it)\b[^?.]*\b"
    r"(high-risk|compliant|comply|allowed|prohibited|banned|legal|exempt|fall under)\b")

_EMAIL = re.compile(PERSONAL_DATA["email"], re.I)
_PHONE = re.compile(PERSONAL_DATA["phone"], re.I)


def has_personal_data(text):
    if _EMAIL.search(text):
        return True
    return any(sum(ch.isdigit() for ch in m.group()) >= PERSONAL_DATA["phone_min_digits"]
               for m in _PHONE.finditer(text))


def input_check(question):
    """Returns (kind, notice, flags). kind is None when the question goes on to the model."""
    q = question.lower()
    flags = {"verdict_request": bool(re.search(VERDICT_REQUEST, q))}
    if has_personal_data(question):
        return "personal_data", PERSONAL_DATA_NOTICE, flags
    if re.search(EVADE, q) and re.search(EVADE_TARGET, q):
        return "refuse", REFUSAL, flags
    if re.search(OOS, q):
        return "out_of_scope", OUT_OF_SCOPE, flags
    return None, None, flags

# ---------------------------------------------------------------- output check: verdicts

# Spike patterns; the noun list of the first pattern is extended with test, platform, service, solution,
# software, chatbot and assistant (an answer said "Your placement test is high-risk." and was not caught).
VERDICT = [
    r"\b(your|the|this|our)\s+(\w+\s+){0,3}?(system|tool|product|grader|app|application|feature|calculator|ai|test|platform|service|solution|software|chatbot|assistant)\s+(is|are|would be|will be)\s+(not\s+)?(considered\s+)?(a\s+)?(high-risk|compliant|prohibited|allowed|exempt|lawful)",
    r"\b(it|this|that)\s+is\s+(not\s+)?(a\s+)?(problem|issue|violation)\s+under\s+the\s+(ai act|regulation)",
    r"\b(it|this|that)\s+(is|would be|will be)\s+(not\s+)?(considered\s+)?(a\s+)?(high-risk|compliant|prohibited|exempt)\b",
    r"\bnot a problem under the (ai act|regulation)",
    r"\b(does not|doesn't|would not|will not) (violate|breach) (the )?(ai act|regulation|rules)",
    r"\b(fits|meets|satisfies) (this|the|that) (description|condition|exception)",
    r"\b(so|therefore|thus|hence),? (it|your \w+( \w+)?) (falls|fall) under\b",
    r"\byou are (not )?(compliant|allowed|permitted)\b",
    r"\b(complies|is compliant|are compliant) with (the )?(ai act|regulation)",
]
COND_BEFORE = r"\b(if|when|where|unless|whether|says that|states that|provides that|means that|only if)\b[^,;]*$"
COND_AFTER = r"^[^,;.]*?\b(if|unless|where|provided that)\b"


def split_sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]


def is_verdict(sentence):
    hit = False
    for pattern in VERDICT:
        for m in re.finditer(pattern, sentence, re.I):
            if re.search(COND_BEFORE, sentence[:m.start()], re.I) or re.match(COND_AFTER, sentence[m.end():], re.I):
                continue
            hit = True
    if not hit:
        return False
    if re.match(r"^\s*(if|when|where|unless|whether)\b", sentence, re.I):   # only states a condition
        return False
    if re.search(r"\b(may|might|could)\s+(not\s+)?(be|fall|violate)\b", sentence, re.I):
        return False
    return True


def remove_verdicts(answer):
    """Removes verdict sentences (C-08). Returns (text, number removed)."""
    paragraphs, removed = [], 0
    for paragraph in re.split(r"\n\s*\n", answer.strip()):      # keep the paragraphs of the answer
        sentences = split_sentences(paragraph)
        kept = [s for s in sentences if not is_verdict(s)]
        removed += len(sentences) - len(kept)
        if kept:
            paragraphs.append(" ".join(kept) if len(kept) < len(sentences) else paragraph.strip())
    if not removed:
        return answer.strip(), 0
    return ("\n\n".join(paragraphs) or "I cannot decide this for your system."), removed

# ---------------------------------------------------------------- output check: citations

# "Article 6(3)(a)", "Article 113", "Article 4a(1)", "Annex III, point 3(a)", "Annex III"
_ARTICLE = re.compile(r"\bArticle\s+(\d+[a-z]?)(?:\s*\((\d+)\))?", re.I)
_ANNEX = re.compile(r"\bAnnex\s+([IVXLC]+)\b(?:,?\s*point\s+(\d+(?:\s*\([a-z]\))?))?", re.I)


def cited_keys(text):
    """Each Article/Annex the text cites, as (kind, number, paragraph or point, as written), in order."""
    found = [(m.start(), ("article", m.group(1).lower(), m.group(2), m.group(0))) for m in _ARTICLE.finditer(text)]
    found += [(m.start(), ("annex", m.group(1).upper(), m.group(2) and re.sub(r"\s+", "", m.group(2).lower()), m.group(0)))
              for m in _ANNEX.finditer(text)]
    return [key for _, key in sorted(found)]


def _chunk_key(ref):
    keys = cited_keys(ref)
    return keys[0] if keys else None


def matches(citation, chunk_ref):
    """A citation matches a chunk when the Article (or Annex) is the same and the paragraph (or point)
    is the same or not given on one side: "Article 6(3)" matches "Article 6(3), second subparagraph, point (a)",
    "Annex III, point 3" matches "Annex III, point 3(c)", but "Annex III, point 3(c)" does not match point 3(a)."""
    key = _chunk_key(chunk_ref)
    if not key or key[:2] != citation[:2]:
        return False
    a, b = citation[2], key[2]
    return a is None or b is None or a == b or a.startswith(b + "(") or b.startswith(a + "(")


def check_citations(answer, chunks):
    """Splits the citations of the answer into those found among the retrieved chunks and those not found.
    Returns (cited chunks in order of first mention, unsupported citations as written)."""
    cited, unsupported, seen = [], [], set()
    citations = cited_keys(answer)
    specific = {c[:2] for c in citations if c[2] is not None}
    for citation in citations:
        if citation[2] is None and citation[:2] in specific:
            continue    # "Annex III" next to "Annex III, point 3(c)" refers to the same point, not to every point

        hits = [c for c in chunks if matches(citation, c["ref"])]
        if not hits and citation[3] not in unsupported:
            unsupported.append(citation[3])
        for c in hits:
            if c["chunk_id"] not in seen:
                seen.add(c["chunk_id"])
                cited.append({**c, "cited_as": citation[3]})   # how the answer wrote it, for the markers in the interface
    return cited, unsupported
