// The one-page interface of D1, following user interface mockup v1 (KAN-104):
// question box (KAN-21), personal-data reminder and warning (KAN-26), answer with the cited provisions
// and their text (KAN-22), permanent not-legal-advice notice (KAN-25), waiting and error states.
import { useEffect, useRef, useState } from "react";
import { ask, AskError, health, newSession } from "./api.js";
import { findPersonalData } from "./personalData.js";

const VERSION_TEXT = "Text: Regulation (EU) 2024/1689, consolidated version of 27 July 2026";

export default function App() {
  const [turns, setTurns] = useState([]); // { id, question, status: "pending" | "done" | "error", response?, error? }
  const [draft, setDraft] = useState("");
  const [warning, setWarning] = useState(null); // personal data found before sending
  const [mode, setMode] = useState(null);
  const endRef = useRef(null);
  const busy = turns.some((t) => t.status === "pending");

  useEffect(() => {
    health().then((h) => setMode(h?.rag?.default_mode ?? null));
  }, []);
  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth", block: "end" });
  }, [turns]);

  async function send(question, { checked = false } = {}) {
    const q = question.trim();
    if (!q || busy) return;
    if (!checked) {
      const found = findPersonalData(q);
      if (found.length) return setWarning(found);
    }
    setWarning(null);
    const id = crypto.randomUUID();
    setTurns((ts) => [...ts.filter((t) => t.status !== "error"), { id, question: q, status: "pending" }]);
    try {
      const response = await ask(q);
      if (response.mode) setMode(response.mode);
      setTurns((ts) => ts.map((t) => (t.id === id ? { ...t, status: "done", response } : t)));
      setDraft("");
    } catch (e) {
      const error = e instanceof AskError ? e.message : "Your question was not lost. Try again.";
      setTurns((ts) => ts.map((t) => (t.id === id ? { ...t, status: "error", error } : t)));
      setDraft(q); // the question stays in the box (KAN-21, criterion 3)
    }
  }

  async function startNewSession() {
    await newSession();
    setTurns([]);
    setDraft("");
    setWarning(null);
  }

  return (
    <div className="app">
      <header className="top">
        <div className="brand">
          <b>Eliza</b>
          <span>EU AI Act provisions for AI products in education</span>
        </div>
        <div className="top-right">
          <span className="version">{VERSION_TEXT}</span>
          <button className="btn-ghost" onClick={startNewSession} disabled={busy}>New session</button>
        </div>
      </header>

      <div className="notice" role="note">
        <InfoIcon />
        <div>
          <strong>Information, not legal advice.</strong> Decisions about your product, such as whether it is
          high-risk, belong to your company's legal team. The consolidated EUR-Lex text is a documentation tool;
          only the text published in the Official Journal is legally authentic.
        </div>
      </div>

      {mode === "no_rag" && (
        <div className="mode" role="note">
          <strong>Baseline mode (no retrieval).</strong> Answers come from the language model alone, without the
          provisions of the regulation. Citations are not checked against the text and may be wrong.
        </div>
      )}

      <main className="conv">
        {turns.length === 0 && (
          <p className="empty">
            Describe your product and ask which provisions of the AI Act relate to it. Eliza answers from the
            consolidated text and cites the Article or Annex for every statement.
          </p>
        )}
        {turns.map((t) => (
          <Turn key={t.id} turn={t} onRetry={() => send(t.question, { checked: true })} />
        ))}
        <div ref={endRef} />
      </main>

      <div className="composer">
        {warning && (
          <div className="pd-warn" role="alert">
            <p>
              Your question seems to contain {warning.join(" and ")}. Eliza does not need personal information to
              explain the provisions.
            </p>
            <div className="pd-actions">
              <button className="btn-ghost" onClick={() => setWarning(null)}>Edit question</button>
              <button className="btn-link" onClick={() => send(draft, { checked: true })}>Send anyway</button>
            </div>
          </div>
        )}
        <form
          className={`box${busy ? " busy" : ""}`}
          onSubmit={(e) => {
            e.preventDefault();
            send(draft);
          }}
        >
          <textarea
            value={draft}
            onChange={(e) => {
              setDraft(e.target.value);
              if (warning) setWarning(null);
            }}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                send(draft);
              }
            }}
            placeholder={
              busy
                ? "You can ask your next question when this answer is ready."
                : 'Describe your product and ask your question, for example: "Which requirements apply to our exam-proctoring tool?"'
            }
            disabled={busy}
            maxLength={2000}
            rows={2}
            aria-label="Your question"
          />
          <button className="send" type="submit" disabled={busy || !draft.trim()}>Ask</button>
        </form>
        <div className="privacy">
          <LockIcon />
          <span>
            Do not enter personal information, such as names, e-mail addresses or student and staff records. This
            conversation is deleted when the session ends.
          </span>
        </div>
      </div>
    </div>
  );
}

function Turn({ turn, onRetry }) {
  return (
    <section className="turn">
      <div className="q-wrap">
        <p className="who">You</p>
        <div className="q">{turn.question}</div>
      </div>
      <p className="who">Eliza</p>
      {turn.status === "pending" && (
        <div className="state">
          <div className="dots3"><i /><i /><i /></div>
          <div>
            <p className="t">Preparing your answer</p>
            <p className="s">Eliza is finding the provisions that relate to your question. This can take about a minute.</p>
          </div>
        </div>
      )}
      {turn.status === "error" && (
        <div className="state err" role="alert">
          <div>
            <p className="t">The answer could not be prepared</p>
            <p className="s">{turn.error}</p>
            <button className="retry" onClick={onRetry}>Try again</button>
          </div>
        </div>
      )}
      {turn.status === "done" && <Answer response={turn.response} />}
    </section>
  );
}

function Answer({ response }) {
  if (response.status === "notice") {
    return (
      <article className="a">
        <p className="notice-answer">{response.answer}</p>
      </article>
    );
  }
  const citations = response.citations ?? [];
  const paragraphs = withMarkers(response.answer, citations);
  return (
    <article className="a">
      {paragraphs.map((p, i) => (
        <p key={i} className={i === 0 ? "summary" : undefined}>{p}</p>
      ))}
      {response.notice && <p className="decline">{response.notice}</p>}

      {citations.length > 0 && (
        <div className="cited">
          {citations.map((c) => <Cite key={c.chunk_id} c={c} />)}
        </div>
      )}
      {response.unsupported_citations?.length > 0 && (
        <p className="unsupported">
          {response.mode === "no_rag"
            ? "Cited by the model, not checked against the text: "
            : "Cited but not among the retrieved provisions: "}
          {response.unsupported_citations.join(", ")}
        </p>
      )}
    </article>
  );
}

function Cite({ c }) {
  const [open, setOpen] = useState(false);
  return (
    <div className="cite">
      <span className="n">{c.n}</span>
      <div>
        <span className="ref">{c.ref}</span> <span className="ver">version of {c.version_date}</span>
      </div>
      <button className="toggle" onClick={() => setOpen(!open)} aria-expanded={open}>
        {open ? "Hide text" : "Show text"}
      </button>
      {open && (
        <div className="excerpt">
          <p className="oj">{c.text}</p>
          <div className="src">
            Source: EUR-Lex, CELEX 02024R1689-20260727.{" "}
            <a href={c.source_url} target="_blank" rel="noreferrer">Open on EUR-Lex</a>
          </div>
        </div>
      )}
    </div>
  );
}

// Splits the answer into paragraphs and puts the citation numbers after the first mention of each citation.
function withMarkers(text, citations) {
  const numbers = new Map(); // as written -> [n]
  for (const c of citations) numbers.set(c.cited_as, [...(numbers.get(c.cited_as) ?? []), c.n]);
  const placed = new Set();
  return text.split(/\n\s*\n/).map((para) => {
    const marks = [];
    for (const [written, ns] of numbers) {
      if (placed.has(written)) continue;
      // The first mention that is not the start of a longer citation ("Annex III" in "Annex III, point 3(c)").
      let at = para.indexOf(written);
      while (at >= 0 && /^,?\s*point\b/i.test(para.slice(at + written.length))) {
        at = para.indexOf(written, at + 1);
      }
      if (at >= 0) {
        marks.push({ at: at + written.length, ns });
        placed.add(written);
      }
    }
    marks.sort((a, b) => a.at - b.at);
    const out = [];
    let from = 0;
    marks.forEach((m, i) => {
      out.push(para.slice(from, m.at));
      out.push(<sup key={i} className="c">{m.ns.join(",")}</sup>);
      from = m.at;
    });
    out.push(para.slice(from));
    return out;
  });
}

function InfoIcon() {
  return (
    <svg width="18" height="18" viewBox="0 0 20 20" aria-hidden="true">
      <circle cx="10" cy="10" r="9" fill="none" stroke="currentColor" strokeWidth="1.6" />
      <rect x="9.1" y="8.4" width="1.8" height="6" fill="currentColor" />
      <rect x="9.1" y="5.2" width="1.8" height="1.9" fill="currentColor" />
    </svg>
  );
}

function LockIcon() {
  return (
    <svg width="15" height="15" viewBox="0 0 20 20" aria-hidden="true">
      <rect x="3.5" y="9" width="13" height="9" rx="1.5" fill="none" stroke="currentColor" strokeWidth="1.6" />
      <path d="M6.5 9V6.5a3.5 3.5 0 0 1 7 0V9" fill="none" stroke="currentColor" strokeWidth="1.6" />
    </svg>
  );
}
