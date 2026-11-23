// Web backend (D1, D15): serves the React build and forwards questions to the RAG service.
// Keeps the question-answer pairs of the active session in memory only, keyed by a session cookie;
// nothing is written to disk and the pairs are dropped when the session ends (C-10).
// Runs no content checks (D3): those are in the RAG service.
import crypto from "node:crypto";
import path from "node:path";
import { fileURLToPath } from "node:url";
import express from "express";
import cookieParser from "cookie-parser";
import { rateLimit } from "express-rate-limit";

const PORT = Number(process.env.PORT ?? 3000);
const RAG_URL = (process.env.RAG_URL ?? "http://localhost:8000").replace(/\/$/, "");
// Open session parameters (design document, section 7): these are first values, set in .env.
const SESSION_TTL_MS = Number(process.env.SESSION_TTL_MINUTES ?? 30) * 60_000;
const HISTORY_PAIRS = Number(process.env.HISTORY_PAIRS ?? 3);
const RATE_LIMIT_PER_MINUTE = Number(process.env.RATE_LIMIT_PER_MINUTE ?? 10);
const RAG_TIMEOUT_MS = Number(process.env.RAG_TIMEOUT_S ?? 180) * 1000;
const MAX_QUESTION_CHARS = 2000;
const COOKIE = "eliza_sid";

const publicDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), process.env.PUBLIC_DIR ?? "public");

// ------------------------------------------------------------------ sessions in memory (D15)
const sessions = new Map(); // session id -> { pairs: [{question, answer}], lastSeen }

function session(req, res) {
  let id = req.cookies[COOKIE];
  if (!id || !sessions.has(id)) {
    id = crypto.randomUUID();
    sessions.set(id, { pairs: [], lastSeen: Date.now() });
    // A browser-session cookie: no expiry date, so it ends when the browser is closed.
    res.cookie(COOKIE, id, { httpOnly: true, sameSite: "strict", secure: process.env.COOKIE_SECURE === "true" });
  }
  const s = sessions.get(id);
  s.lastSeen = Date.now();
  return { id, s };
}

setInterval(() => {
  const now = Date.now();
  for (const [id, s] of sessions) if (now - s.lastSeen > SESSION_TTL_MS) sessions.delete(id);
}, 60_000).unref();

// Anonymous log line: no question content, no session id (C-10).
const logLine = (fields) =>
  console.log(new Date().toISOString(), Object.entries(fields).map(([k, v]) => `${k}=${v}`).join(" "));

// ------------------------------------------------------------------ app
const app = express();
app.disable("x-powered-by");
app.use(express.json({ limit: "16kb" }));
app.use(cookieParser());

app.get("/api/health", async (_req, res) => {
  let rag = null;
  try {
    const r = await fetch(`${RAG_URL}/health`, { signal: AbortSignal.timeout(5000) });
    rag = await r.json();
  } catch {
    rag = null;
  }
  res.json({ status: "ok", sessions: sessions.size, rag });
});

const askLimiter = rateLimit({
  windowMs: 60_000,
  limit: RATE_LIMIT_PER_MINUTE,
  standardHeaders: "draft-8",
  legacyHeaders: false,
  handler: (_req, res) => res.status(429).json({ error: "rate_limited" }),
});

app.post("/api/ask", askLimiter, async (req, res) => {
  const started = Date.now();
  const question = typeof req.body?.question === "string" ? req.body.question.trim() : "";
  if (!question || question.length > MAX_QUESTION_CHARS) {
    return res.status(400).json({ error: "invalid_question" });
  }
  const { s } = session(req, res);

  let ragStatus = "none";
  try {
    const r = await fetch(`${RAG_URL}/answer`, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ question, history: s.pairs.slice(-HISTORY_PAIRS) }),
      signal: AbortSignal.timeout(RAG_TIMEOUT_MS),
    });
    ragStatus = r.status;
    if (!r.ok) {
      logLine({ event: "ask", status: 502, rag: ragStatus, ms: Date.now() - started });
      return res.status(502).json({ error: r.status === 503 ? "not_ready" : "no_answer" });
    }
    const body = await r.json();
    // Only answered questions are kept for follow-ups; a notice (for example personal data) is not kept.
    if (body.status === "answer") {
      s.pairs.push({ question, answer: body.answer });
      if (s.pairs.length > HISTORY_PAIRS) s.pairs.splice(0, s.pairs.length - HISTORY_PAIRS);
    }
    logLine({ event: "ask", status: 200, rag: ragStatus, mode: body.mode, result: body.kind ?? body.status,
              cited: body.citations?.length ?? 0, ms: Date.now() - started });
    return res.json(body);
  } catch (error) {
    const timeout = error?.name === "TimeoutError";
    logLine({ event: "ask", status: timeout ? 504 : 502, rag: ragStatus, error: error?.name ?? "Error", ms: Date.now() - started });
    return res.status(timeout ? 504 : 502).json({ error: timeout ? "timeout" : "no_answer" });
  }
});

// "New session": drops the pairs of this session and gives a new cookie.
app.post("/api/session/new", (req, res) => {
  const id = req.cookies[COOKIE];
  if (id) sessions.delete(id);
  res.clearCookie(COOKIE);
  session(req, res);
  res.json({ ok: true });
});

app.use("/api", (_req, res) => res.status(404).json({ error: "not_found" }));

// The React build (one page).
app.use(express.static(publicDir));
app.use((req, res, next) => (req.method === "GET" ? res.sendFile(path.join(publicDir, "index.html")) : next()));

app.listen(PORT, () => logLine({ event: "start", port: PORT, rag: RAG_URL, history_pairs: HISTORY_PAIRS }));
