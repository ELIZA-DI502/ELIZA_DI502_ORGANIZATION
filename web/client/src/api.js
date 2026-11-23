// Calls to the web backend (POST /api/ask, JSON, session cookie).
const MESSAGES = {
  rate_limited: "You have asked many questions in a short time. Wait a minute and try again.",
  timeout: "The answer took too long to prepare. Try again, or ask a shorter question.",
  not_ready: "Eliza is still starting. Try again in a minute.",
  default: "Your question was not lost. Try again, or change the question and ask it again.",
};

export class AskError extends Error {}

export async function ask(question) {
  let res;
  try {
    res = await fetch("/api/ask", {
      method: "POST",
      headers: { "content-type": "application/json" },
      credentials: "same-origin",
      body: JSON.stringify({ question }),
    });
  } catch {
    throw new AskError(MESSAGES.default);
  }
  const body = await res.json().catch(() => ({}));
  if (!res.ok) throw new AskError(MESSAGES[body.error] ?? MESSAGES.default);
  return body;
}

export async function newSession() {
  await fetch("/api/session/new", { method: "POST", credentials: "same-origin" }).catch(() => {});
}

export async function health() {
  try {
    const res = await fetch("/api/health", { credentials: "same-origin" });
    return await res.json();
  } catch {
    return null;
  }
}
