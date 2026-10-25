"""Rule-based safety checks used in model selection spike run 5 (Gozde Nur, 25/10/2026).
input_check: runs before the model (evasion requests, out-of-scope topics).
output_check: runs after the model (removes compliance verdicts, adds a notice).
Spike code, not production code."""
import re
HEDGE = r"\b(if|whether|unless|when|where|may|might|could|can be|depends|assess|check)\b"
SUBJ = r"\b(your|the|this|our|their|it)\b(\s+\w+){0,3}?\s*\b(system|tool|product|grader|app|application|feature|calculator|model|ai)?"
VERDICT = [
    r"\b(your|the|this|our)\s+(\w+\s+){0,3}?(system|tool|product|grader|app|application|feature|calculator|ai)\s+(is|are|would be|will be)\s+(not\s+)?(considered\s+)?(a\s+)?(high-risk|compliant|prohibited|allowed|exempt|lawful)",
    r"\b(it|this|that)\s+is\s+(not\s+)?(a\s+)?(problem|issue|violation)\s+under\s+the\s+(ai act|regulation)",
    r"\b(it|this|that)\s+(is|would be|will be)\s+(not\s+)?(considered\s+)?(a\s+)?(high-risk|compliant|prohibited|exempt)\b",
    r"\bnot a problem under the (ai act|regulation)",
    r"\b(does not|doesn't|would not|will not) (violate|breach) (the )?(ai act|regulation|rules)",
    r"\b(fits|meets|satisfies) (this|the|that) (description|condition|exception)",
    r"\b(so|therefore|thus|hence),? (it|your \w+( \w+)?) (falls|fall) under\b",
    r"\byou are (not )?(compliant|allowed|permitted)\b",
    r"\b(complies|is compliant|are compliant) with (the )?(ai act|regulation)",
]
NOTICE = "Note: this is not a legal decision. Assess your system against the cited provisions."
def split_sents(t): return [s for s in re.split(r"(?<=[.!?])\s+", t.strip()) if s]
COND_BEFORE = r"\b(if|when|where|unless|whether|says that|states that|provides that|means that|only if)\b[^,;]*$"
COND_AFTER = r"^[^,;.]*?\b(if|unless|where|provided that)\b"
def is_verdict(s):
    hit = False
    for p in VERDICT:
        for m in re.finditer(p, s, re.I):
            if re.search(COND_BEFORE, s[:m.start()], re.I) or re.match(COND_AFTER, s[m.end():], re.I):
                continue
            hit = True
    if not hit: return False
    # a sentence that only states a condition is not a verdict ("If your system is not high-risk, ...")
    if re.match(r"^\s*(if|when|where|unless|whether)\b", s, re.I): return False
    if re.search(r"\b(may|might|could)\s+(not\s+)?(be|fall|violate)\b", s, re.I): return False
    return True
def verdict_sentences(t): return [s for s in split_sents(t) if is_verdict(s)]
def output_check(answer):
    sents = split_sents(answer)
    bad = [s for s in sents if is_verdict(s)]
    if not bad: return answer, 0
    kept = [s for s in sents if s not in bad]
    body = " ".join(kept).strip() or "I cannot decide this for your system."
    return body + "\n\n" + NOTICE, len(bad)


EVADE = r"(avoid|skip|get around|circumvent|bypass|evade|escape|loophole|hide|conceal|don'?t have to (follow|comply)|do not have to (follow|comply)|look(s)? like (a|just)|keep us out of)"
OOS = r"\b(fine|fines|penalt\w*|sanction\w*|enforcement|gdpr|data protection|parental consent)\b"
REFUSAL = "I can't help with avoiding or hiding from the AI Act's rules. I can explain what the relevant provisions require."
OUT_OF_SCOPE = "This question is outside my scope: I cover the EU AI Act provisions on AI systems in education, not penalties, enforcement or data-protection law."


def input_check(question):
    q = question.lower()
    if re.search(EVADE, q) and re.search(r"(rule|requirement|high-risk|authorit|regulat|ai act|document)", q):
        return "refuse", REFUSAL
    if re.search(OOS, q):
        return "out_of_scope", OUT_OF_SCOPE
    return None, None
