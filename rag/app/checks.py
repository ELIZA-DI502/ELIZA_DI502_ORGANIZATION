"""Rule-based input and output checks of the RAG service (D3).

The verdict, evasion and out-of-scope patterns are taken from the model selection spike, run 5
(docs/spikes/model-selection/checks.py on the KAN-30-evaluation-gozde-nur branch). The fixed texts
come from prompts/answer.yaml. Open (section 7 of the design document): the personal-data rules
and the citation-ID check (KAN-49), and the legal-decision patterns (KAN-2).
"""
import re

from .config import PERSONAL_DATA, PROMPT

REFUSAL = PROMPT["refusal"]
OUT_OF_SCOPE = PROMPT["out_of_scope"]
OUT_OF_SCOPE_PART = PROMPT.get(
    "out_of_scope_part",
    "The part of your question about {topics} is outside my scope: I cover the education use cases in Annex III, "
    "point 3, of the EU AI Act.")
NOTICE = PROMPT["notice"]
PERSONAL_DATA_NOTICE = PROMPT.get(
    "personal_data",
    "Your question seems to contain personal data, such as an e-mail address or a phone number. "
    "Please remove it and ask again; I do not need personal data to explain the provisions.")

# ---------------------------------------------------------------- input check

EVADE = r"(avoid|skip|get around|circumvent|bypass|evade|escape|loophole|hide|conceal|don'?t have to (follow|comply)|do not have to (follow|comply)|look(s)? like (a|just)|keep us out of)"
EVADE_TARGET = r"(rule|requirement|high-risk|authorit|regulat|ai act|document)"
# Out of scope (C-04, KAN-5): each topic the assistant does not cover, with the words that show it in a question.
OOS_TOPICS = {
    "penalties and enforcement": r"\b(fine|fines|penalt\w*|sanction\w*|enforcement)\b",
    "data-protection law": r"\b(gdpr|data protection|parental consent)\b",
    "the obligations of schools as deployers": (
        r"\bas (?:a|the) deployers?\b|\bdeployers?'? obligations\b"
        r"|\bobligations of (?:the |our |a )?(?:schools?|universit(?:y|ies)|deployers?)\b"
        r"|\bwhat (?:must|should|do|does) (?:the |our |a )?(?:schools?|universit(?:y|ies)|teachers?|deployers?)\b[^?]*\b(?:do|ensure)\b"),
    "AI systems outside education": (
        r"\b(job applicants?|job candidates?|recruit\w*|hiring|employees?|employment|workers?"
        r"|credit scoring|creditworthiness|loans?|insurance|patients?|medical diagnos\w*|police|law enforcement|border|migration|asylum)\b"),
}
# A part of a question that asks about the AI Act rules for the user's education product.
IN_SCOPE_ASK = r"\b(provisions?|articles?|annex|rules?|requirements?|obligations?|apply|applies|ai act|regulation|high-risk)\b"
# A question is split into its parts at "?", ";" and at "and" before a new question word.
_PARTS = re.compile(r"\?|;|,?\s+\band\b\s+(?=(?:what|which|how|when|does|do|is|are|can|must|should|whether)\b)", re.I)


def out_of_scope_topics(question):
    """Returns (topics found, whether another part of the question asks an in-scope question).
    A part is in scope when it asks about the rules and names no out-of-scope topic."""
    topics, in_scope_part = [], False
    for part in (p.strip() for p in _PARTS.split(question.lower()) if p and p.strip()):
        found = [name for name, pattern in OOS_TOPICS.items() if re.search(pattern, part)]
        topics += [name for name in found if name not in topics]
        if not found and re.search(IN_SCOPE_ASK, part):
            in_scope_part = True
    return topics, in_scope_part


def out_of_scope_part_notice(topics):
    """The one sentence added to an answer when only part of the question is out of scope (KAN-5, criterion 2)."""
    return OUT_OF_SCOPE_PART.format(topics=" and ".join(topics))
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
    topics, in_scope_part = out_of_scope_topics(question)
    if topics and not in_scope_part:          # entirely out of scope: notice only, no answer, no citation
        return "out_of_scope", OUT_OF_SCOPE, flags
    if topics:                                # partly out of scope: the in-scope part goes on to the model
        flags["partly_out_of_scope"] = topics
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
# "Ensure that the system is compliant ..." is an instruction to the provider, not a verdict (B-05 in the Sprint 2
# answers, KAN-226), so a match after "ensure that" or "make sure" is skipped like a condition.
COND_BEFORE = r"\b(if|when|where|unless|whether|says that|states that|provides that|means that|only if|ensure that|make sure(?: that)?)\b[^,;]*$"
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
    """Splits the citations of the answer into those found among the chunks in the prompt and those not found.
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
