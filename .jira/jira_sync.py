#!/usr/bin/env python3
"""Sync epic markdown files (docs/backlog/*.md) to Jira Cloud.

Commands
  validate  Check every epic file and print the plan. Needs no Jira access.
  sync      Validate, then create/update issues in Jira and write issue keys
            back into the markdown files.
  doctor    Check the Jira connection, issue types, fields and team members.

Environment
  JIRA_BASE_URL     e.g. https://your-team.atlassian.net
  JIRA_EMAIL        Jira login email of the API token owner
  JIRA_API_TOKEN    API token (https://id.atlassian.com/manage-profile/security/api-tokens)
  JIRA_PROJECT_KEY  e.g. DI
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Optional

import yaml

try:
    import requests
except ImportError:  # validate works without requests
    requests = None

# --------------------------------------------------------------------------
# Markdown parsing
# --------------------------------------------------------------------------

KEY_RE = re.compile(r"\b([A-Z][A-Z0-9_]+-\d+)\b")
PIPE_RE = re.compile(r"(?<!\\)\|")
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
SEP_RE = re.compile(r"^\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
STORY_HEADING_RE = re.compile(r"^##\s+(S?\d+)\b\s*[·:\-–—.]?\s*(.*)$", re.I)
MARKER_RE = re.compile(
    r"^\s*(?:\*\*|#{3,6}\s+)\s*(acceptance criteria|sub-?tasks|tasks)\s*:?\s*(?:\*\*)?\s*:?\s*$",
    re.I,
)
LIST_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(.*)$")
STORY_FORMAT_RE = re.compile(r"\bas an?\b.+\bi want\b.+\bso that\b", re.I | re.S)
ESTIMATE_RE = re.compile(r"^\d+(\.\d+)?[wdhm](\s+\d+(\.\d+)?[wdhm])*$")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9# ]", " ", s.lower())).strip()


def plain(s: str) -> str:
    """Strip simple markdown emphasis from a cell value."""
    s = re.sub(r"(\*\*|__)(.+?)\1", r"\2", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\1", s)
    return s.replace("<br>", " ").replace("<br/>", " ").strip()


def split_row(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip().replace("\\|", "|") for c in PIPE_RE.split(s)]


@dataclass
class Table:
    header_line: int
    header: list[str]
    rows: list[tuple[int, list[str]]]  # (line index, cells)

    def col(self, *names: str) -> Optional[int]:
        normed = [norm(h) for h in self.header]
        for n in names:
            if n in normed:
                return normed.index(n)
        return None


def table_at(lines: list[str], i: int) -> Optional[Table]:
    if i + 1 >= len(lines):
        return None
    if not lines[i].strip().startswith("|") or not SEP_RE.match(lines[i + 1].strip()):
        return None
    header = split_row(lines[i])
    rows = []
    j = i + 2
    while j < len(lines) and lines[j].strip().startswith("|"):
        rows.append((j, split_row(lines[j])))
        j += 1
    return Table(i, header, rows)


def first_table(lines: list[str], start: int, end: int) -> Optional[Table]:
    for i in range(start, end):
        t = table_at(lines, i)
        if t:
            return t
    return None


def cell(cells: list[str], idx: Optional[int]) -> str:
    if idx is None or idx >= len(cells):
        return ""
    return cells[idx].strip()


def key_in(s: str) -> Optional[str]:
    m = KEY_RE.search(s or "")
    return m.group(1) if m else None


def parse_points(s: str):
    s = re.sub(r"(?i)\s*(sp|pts?|points?)$", "", plain(s)).strip()
    if s in ("", "-", "—", "–"):
        return None
    try:
        v = float(s)
    except ValueError:
        return "invalid"
    return int(v) if v.is_integer() else v


@dataclass
class Item:
    kind: str  # "subtask" or "task"
    title: str
    owner: str
    estimate: str
    points: object
    key: Optional[str]
    line: int
    jira_col: Optional[int]


@dataclass
class Story:
    sid: str
    title: str
    description: str
    priority: str
    points: object
    notes: str
    key: Optional[str]
    line: int
    jira_col: Optional[int]
    ac: list[str] = field(default_factory=list)
    breakdown: Optional[str] = None  # "subtasks" | "tasks" | None
    both_breakdowns: bool = False
    items: list[Item] = field(default_factory=list)
    has_section: bool = False


@dataclass
class Epic:
    path: Path
    rel: str
    lines: list[str]
    name: str = ""
    summary: str = ""
    owner: str = ""
    designer: str = ""
    developers: str = ""
    release: str = ""
    key: Optional[str] = None
    key_line: Optional[int] = None
    key_col: int = 1
    stories: list[Story] = field(default_factory=list)
    problems: list[tuple[str, int, str]] = field(default_factory=list)  # (level, line, msg)
    dirty: bool = False

    def err(self, line: int, msg: str):
        self.problems.append(("error", line, msg))

    def warn(self, line: int, msg: str):
        self.problems.append(("warning", line, msg))

    @property
    def errors(self):
        return [p for p in self.problems if p[0] == "error"]

    def set_cell(self, line: int, col: int, value: str):
        raw = self.lines[line]
        cr = "\r" if raw.endswith("\r") else ""
        raw = raw.rstrip("\r")
        indent = raw[: len(raw) - len(raw.lstrip())]
        s = raw.strip()
        if s.startswith("|"):
            s = s[1:]
        if s.endswith("|") and not s.endswith("\\|"):
            s = s[:-1]
        parts = PIPE_RE.split(s)
        while len(parts) <= col:
            parts.append(" ")
        parts[col] = f" {value} "
        self.lines[line] = indent + "|" + "|".join(parts) + "|" + cr
        self.dirty = True

    def save(self):
        if self.dirty:
            self.path.write_text("\n".join(self.lines), encoding="utf-8")
            self.dirty = False


def norm_id(s: str) -> str:
    s = plain(s).upper()
    return s if s.startswith("S") else "S" + s


def parse_epic(path: Path, rel: str) -> Epic:
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    clean_text = COMMENT_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    clean = clean_text.split("\n")
    ep = Epic(path=path, rel=rel, lines=lines)

    headings = [(i, len(m.group(1)), m.group(2)) for i, l in enumerate(clean) if (m := HEADING_RE.match(l))]
    req_i = next((i for i, lvl, t in headings if lvl == 2 and norm(t) == "requirements"), None)

    # --- header table (first table before ## Requirements) ---
    ht = first_table(clean, 0, req_i if req_i is not None else len(clean))
    if not ht:
        ep.err(1, "Missing the epic table (| Epic | ... |) at the top of the file.")
    else:
        kv = [(ht.header_line, ht.header)] + ht.rows
        for line, cells in kv:
            k = norm(cell(cells, 0))
            v = cell(cells, 1)
            if k == "epic":
                ep.name = plain(v)
            elif k in ("summary", "epic summary", "description"):
                ep.summary = plain(v)
            elif k == "document owner":
                ep.owner = v
            elif k == "designer":
                ep.designer = v
            elif k == "developers":
                ep.developers = v
            elif k.startswith("release target"):
                ep.release = plain(v)
            elif k == "jira":
                ep.key, ep.key_line = key_in(v), line
        if not ep.name:
            ep.err(ht.header_line + 1, "The Epic row is empty: give the epic a name.")
        if ep.key_line is None:
            ep.err(ht.header_line + 1, "The epic table needs a 'Jira' row (leave its value empty).")

    # --- requirements table ---
    if req_i is None:
        ep.err(1, "Missing the '## Requirements' section.")
        return ep
    next_h = next((i for i, lvl, _ in headings if i > req_i and lvl <= 2), len(clean))
    rt = first_table(clean, req_i, next_h)
    if not rt:
        ep.err(req_i + 1, "The Requirements section has no table.")
        return ep
    c_id = rt.col("#", "id")
    c_title = rt.col("user story title", "title")
    c_desc = rt.col("user story description", "description")
    c_prio = rt.col("priority")
    c_pts = rt.col("points", "story points")
    c_notes = rt.col("notes")
    c_jira = rt.col("jira")
    for name, c in (("#", c_id), ("User story title", c_title), ("User story description", c_desc), ("Jira", c_jira)):
        if c is None:
            ep.err(rt.header_line + 1, f"The Requirements table needs a '{name}' column.")
    if c_id is None or c_title is None:
        return ep
    seen = {}
    for line, cells in rt.rows:
        if not any(plain(c) for i, c in enumerate(cells) if i != c_id):
            continue  # empty template row
        sid = norm_id(cell(cells, c_id)) if cell(cells, c_id) else ""
        if not re.fullmatch(r"S\d+", sid):
            ep.err(line + 1, f"Story id '{cell(cells, c_id)}' should look like S1, S2, ...")
            continue
        if sid in seen:
            ep.err(line + 1, f"Story id {sid} is used twice.")
            continue
        st = Story(
            sid=sid,
            title=plain(cell(cells, c_title)),
            description=plain(cell(cells, c_desc)),
            priority=plain(cell(cells, c_prio)),
            points=parse_points(cell(cells, c_pts)),
            notes=plain(cell(cells, c_notes)),
            key=key_in(cell(cells, c_jira)),
            line=line,
            jira_col=c_jira,
        )
        seen[sid] = st
        ep.stories.append(st)

    # --- story sections ---
    sections = [(i, m) for i, lvl, t in headings if lvl == 2 and (m := STORY_HEADING_RE.match(clean[i]))]
    for n, (start, m) in enumerate(sections):
        sid = norm_id(m.group(1))
        end = next((i for i, lvl, _ in headings if i > start and lvl <= 2), len(clean))
        st = seen.get(sid)
        if not st:
            ep.err(start + 1, f"Section '{clean[start].strip()}' has no row with id {sid} in the Requirements table.")
            continue
        if st.has_section:
            ep.err(start + 1, f"Story {sid} has two sections.")
            continue
        st.has_section = True
        mode = None
        i = start + 1
        while i < end:
            l = clean[i]
            mm = MARKER_RE.match(l)
            if mm:
                word = mm.group(1).lower().replace("-", "")
                mode = "ac" if word.startswith("acceptance") else ("subtasks" if word == "subtasks" else "tasks")
                if mode in ("subtasks", "tasks"):
                    if st.breakdown and st.breakdown != mode:
                        st.both_breakdowns = True
                    st.breakdown = mode
                    t = first_table(clean, i + 1, end)
                    if t:
                        parse_items(ep, st, t, mode)
                        i = t.rows[-1][0] + 1 if t.rows else t.header_line + 2
                        mode = None
                        continue
                i += 1
                continue
            if mode == "ac":
                lm = LIST_RE.match(l)
                if lm and lm.group(1).strip():
                    st.ac.append(lm.group(1).strip())
                elif l.strip() and st.ac and l.startswith((" ", "\t")):
                    st.ac[-1] += " " + l.strip()
            i += 1
    return ep


def parse_items(ep: Epic, st: Story, t: Table, mode: str):
    c_title = t.col("sub task", "subtask", "task", "title")
    c_owner = t.col("owner", "assignee")
    c_est = t.col("estimate", "original estimate")
    c_pts = t.col("points", "story points")
    c_jira = t.col("jira")
    if c_title is None:
        ep.err(t.header_line + 1, f"{st.sid}: the table needs a '{'Sub-task' if mode == 'subtasks' else 'Task'}' column.")
        return
    if c_jira is None:
        ep.err(t.header_line + 1, f"{st.sid}: the table needs a 'Jira' column.")
    for line, cells in t.rows:
        if not any(plain(c) for i, c in enumerate(cells) if i != c_jira):
            continue
        st.items.append(
            Item(
                kind="subtask" if mode == "subtasks" else "task",
                title=plain(cell(cells, c_title)),
                owner=plain(cell(cells, c_owner)).lstrip("@"),
                estimate=plain(cell(cells, c_est)),
                points=parse_points(cell(cells, c_pts)) if c_pts is not None else None,
                key=key_in(cell(cells, c_jira)),
                line=line,
                jira_col=c_jira,
            )
        )
        if mode == "subtasks" and c_pts is not None and plain(cell(cells, c_pts)):
            ep.err(line + 1, f"{st.sid}: sub-tasks don't carry points. Put the points on the story or use a Tasks table.")


# --------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------


def validate(ep: Epic, cfg: dict, team: dict):
    scale = set(cfg["points_scale"])
    prios = {p.lower(): p for p in cfg["priorities"]}
    keys = {}

    def check_key(k, line):
        if k:
            if k in keys:
                ep.err(line + 1, f"Jira key {k} appears twice (also on line {keys[k] + 1}).")
            keys[k] = line

    check_key(ep.key, ep.key_line or 0)
    if not ep.stories and not ep.errors:
        ep.warn(1, "No stories yet.")
    for st in ep.stories:
        L = st.line + 1
        check_key(st.key, st.line)
        if not st.title:
            ep.err(L, f"{st.sid}: title is empty.")
        if not st.description:
            ep.err(L, f"{st.sid}: description is empty.")
        elif not STORY_FORMAT_RE.search(st.description):
            ep.warn(L, f"{st.sid}: description doesn't follow 'As a <role>, I want <goal>, so that <benefit>'.")
        if st.priority and st.priority.lower() not in prios:
            ep.err(L, f"{st.sid}: priority '{st.priority}' is not one of {', '.join(cfg['priorities'])}.")
        elif st.priority:
            st.priority = prios[st.priority.lower()]
        if st.points == "invalid" or (st.points is not None and st.points not in scale):
            ep.err(L, f"{st.sid}: points '{st.points}' are not on the scale {sorted(scale)}.")
        if not st.has_section:
            ep.err(L, f"{st.sid}: add a section '## {st.sid} · {st.title}' with its acceptance criteria.")
            continue
        if not st.ac:
            ep.warn(L, f"{st.sid}: no acceptance criteria.")
        if st.both_breakdowns:
            ep.err(L, f"{st.sid}: use either a Sub-tasks table or a Tasks table, not both.")
        if st.breakdown == "tasks":
            if st.points is not None:
                ep.err(L, f"{st.sid}: this story uses Tasks, so the tasks carry the points. Leave the story's Points cell empty.")
        elif st.points is None:
            ep.warn(L, f"{st.sid}: no story points yet.")
        for it in st.items:
            IL = it.line + 1
            check_key(it.key, it.line)
            if not it.title:
                ep.err(IL, f"{st.sid}: a {it.kind} row has no title.")
            if it.owner:
                if re.search(r"[,;&]|\s", it.owner):
                    ep.err(IL, f"{st.sid}: '{it.title}' can have only one owner.")
                elif it.owner not in team:
                    ep.err(IL, f"{st.sid}: owner @{it.owner} is not in .jira/team.yml.")
            if it.kind == "subtask" and it.estimate and not ESTIMATE_RE.match(it.estimate):
                ep.err(IL, f"{st.sid}: estimate '{it.estimate}' should look like 4h, 1d or 1d 4h.")
            if it.kind == "task":
                if it.points is None:
                    ep.warn(IL, f"{st.sid}: task '{it.title}' has no points yet.")
                elif it.points == "invalid" or it.points not in scale:
                    ep.err(IL, f"{st.sid}: points '{it.points}' on '{it.title}' are not on the scale {sorted(scale)}.")


# --------------------------------------------------------------------------
# Reports
# --------------------------------------------------------------------------


def problems_md(epics: list[Epic]) -> str:
    out = []
    for ep in epics:
        for level, line, msg in sorted(ep.problems, key=lambda p: (p[0] != "error", p[1])):
            icon = "❌" if level == "error" else "⚠️"
            out.append(f"- {icon} `{ep.rel}:{line}` {msg}")
    return "\n".join(out)


def plan_md(epics: list[Epic]) -> str:
    out = []
    act = lambda k: f"sync {k}" if k else "create"
    for ep in epics:
        if ep.errors:
            continue
        out.append(f"\n**{ep.rel}**: epic *{ep.name}* ({act(ep.key)})\n")
        out.append("| Item | Type | Points / estimate | Owner | Action |")
        out.append("|---|---|---|---|---|")
        for st in ep.stories:
            model = {"subtasks": "story + sub-tasks", "tasks": "story + tasks"}.get(st.breakdown, "story")
            out.append(f"| {st.sid} {st.title} | {model} | {st.points if st.points is not None else '—'} | | {act(st.key)} |")
            for it in st.items:
                size = (it.estimate or "—") if it.kind == "subtask" else (it.points if it.points is not None else "—")
                typ = "sub-task" if it.kind == "subtask" else f"task, blocks {st.sid}"
                own = f"@{it.owner}" if it.owner else ""
                out.append(f"| ↳ {it.title} | {typ} | {size} | {own} | {act(it.key)} |")
    return "\n".join(out)


def write_report(path: Optional[str], text: str):
    print(text)
    if path:
        Path(path).write_text(text, encoding="utf-8")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(text + "\n")


# --------------------------------------------------------------------------
# Jira client
# --------------------------------------------------------------------------


class JiraError(Exception):
    def __init__(self, method, path, status, body):
        detail = body
        try:
            j = json.loads(body)
            msgs = list(j.get("errorMessages", [])) + [f"{k}: {v}" for k, v in (j.get("errors") or {}).items()]
            if msgs:
                detail = "; ".join(msgs)
        except Exception:
            detail = (body or "")[:300]
        super().__init__(f"{method} {path} -> HTTP {status}: {detail}")
        self.status = status


class Jira:
    def __init__(self, base: str, email: str, token: str):
        if requests is None:
            sys.exit("The 'requests' package is required: pip install -r .jira/requirements.txt")
        self.base = base.rstrip("/")
        self.s = requests.Session()
        self.s.auth = (email, token)
        self.s.headers.update({"Accept": "application/json", "Content-Type": "application/json"})

    def req(self, method: str, path: str, **kw):
        for attempt in range(5):
            r = self.s.request(method, self.base + path, timeout=30, **kw)
            if (r.status_code == 429 or r.status_code >= 500) and attempt < 4:
                time.sleep(float(r.headers.get("Retry-After") or 2 ** attempt))
                continue
            break
        if r.status_code >= 400:
            raise JiraError(method, path, r.status_code, r.text)
        return r.json() if r.content else None

    def get(self, path, **kw):
        return self.req("GET", path, **kw)

    def post(self, path, **kw):
        return self.req("POST", path, **kw)

    def put(self, path, **kw):
        return self.req("PUT", path, **kw)

    def delete(self, path, **kw):
        return self.req("DELETE", path, **kw)


class Meta:
    """What the Jira project offers: issue types and the fields each one accepts."""

    def __init__(self, jira: Jira, project: str, cfg: dict):
        self.jira, self.project, self.cfg = jira, project, cfg
        self.proj = jira.get(f"/rest/api/3/project/{project}")
        types = self.proj.get("issueTypes", [])
        names = cfg["issue_types"]

        def by_name(n):
            return next((t for t in types if t["name"].lower() == n.lower() and not t.get("subtask")), None)

        self.types = {
            "epic": by_name(names["epic"]) or next((t for t in types if t.get("hierarchyLevel") == 1), None),
            "story": by_name(names["story"]),
            "task": by_name(names["task"]),
            "subtask": next((t for t in types if t.get("subtask")), None),
        }
        self.all_fields = jira.get("/rest/api/3/field")
        self._fields: dict[str, dict] = {}

    def fields(self, kind: str) -> dict:
        """fieldId -> createmeta entry for this issue type."""
        if kind in self._fields:
            return self._fields[kind]
        t = self.types.get(kind)
        out: dict = {}
        if t:
            start = 0
            while True:
                d = self.jira.get(
                    f"/rest/api/3/issue/createmeta/{self.project}/issuetypes/{t['id']}",
                    params={"startAt": start, "maxResults": 100},
                )
                fl = d.get("fields") or d.get("results") or d.get("values") or []
                for f in fl:
                    out[f.get("fieldId") or f.get("key")] = f
                start += len(fl)
                if not fl or start >= d.get("total", start):
                    break
        self._fields[kind] = out
        return out

    def field_ids(self, name_or_id: str) -> list[str]:
        if name_or_id.startswith("customfield_"):
            return [name_or_id]
        return [f["id"] for f in self.all_fields if f["name"].lower() == name_or_id.lower()]

    def find_field(self, setting: str, defaults: list[str], kind: str) -> Optional[str]:
        names = defaults if setting == "auto" else [setting]
        available = self.fields(kind)
        for n in names:
            for fid in self.field_ids(n):
                if fid in available:
                    return fid
        return None

    def points_field(self, kind: str) -> Optional[str]:
        return self.find_field(self.cfg["story_points_field"], ["Story point estimate", "Story Points"], kind)

    def ac_field(self) -> Optional[tuple[str, bool]]:
        name = str(self.cfg.get("acceptance_criteria_field") or "none")
        if name.lower() == "none":
            return None
        fid = self.find_field(name, [name], "story")
        if not fid:
            return None
        f = next((f for f in self.all_fields if f["id"] == fid), {})
        is_rich = "textarea" in (f.get("schema", {}).get("custom") or "")
        return fid, is_rich


# --------------------------------------------------------------------------
# Atlassian Document Format helpers
# --------------------------------------------------------------------------

LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)|(https?://[^\s)]+)")


def inline(s: str, marks: Optional[list] = None) -> list[dict]:
    nodes, pos = [], 0
    for m in LINK_RE.finditer(s):
        if m.start() > pos:
            nodes.append({"type": "text", "text": s[pos : m.start()]})
        text, url = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(3))
        nodes.append({"type": "text", "text": text, "marks": [{"type": "link", "attrs": {"href": url}}]})
        pos = m.end()
    if pos < len(s):
        nodes.append({"type": "text", "text": s[pos:]})
    if marks:
        for n in nodes:
            n["marks"] = n.get("marks", []) + marks
    return [n for n in nodes if n["text"]]


def para(s: str, marks=None) -> Optional[dict]:
    s = plain(s)
    return {"type": "paragraph", "content": inline(s, marks)} if s else None


def heading(s: str, level: int = 3) -> dict:
    return {"type": "heading", "attrs": {"level": level}, "content": [{"type": "text", "text": s}]}


def bullets(items: list[str]) -> Optional[dict]:
    items = [plain(i) for i in items if plain(i)]
    if not items:
        return None
    return {
        "type": "bulletList",
        "content": [{"type": "listItem", "content": [{"type": "paragraph", "content": inline(i)}]} for i in items],
    }


def adf(*blocks) -> dict:
    content = [b for b in blocks if b]
    return {"type": "doc", "version": 1, "content": content or [{"type": "paragraph", "content": []}]}


# --------------------------------------------------------------------------
# Sync
# --------------------------------------------------------------------------

PROP = "md-sync"


class Syncer:
    def __init__(self, jira: Jira, meta: Meta, cfg: dict, team: dict, force: bool = False):
        self.jira, self.meta, self.cfg, self.team, self.force = jira, meta, cfg, team, force
        self.log: list[tuple[str, str, str, str]] = []  # (file, item, action, detail)
        self.failures = 0
        self.users: dict[str, Optional[str]] = {}
        self.warned: set[str] = set()
        self.ac = meta.ac_field()
        server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
        repo = os.environ.get("GITHUB_REPOSITORY")
        self.blob = f"{server}/{repo}/blob/{cfg['default_branch']}/" if repo else None

    # -- helpers --
    def note(self, ep, item, action, detail=""):
        self.log.append((ep.rel, item, action, detail))

    def warn_once(self, msg):
        if msg not in self.warned:
            self.warned.add(msg)
            print(f"::warning::{msg}")

    def account(self, handle: str) -> Optional[str]:
        if handle in self.users:
            return self.users[handle]
        val = str(self.team.get(handle) or "")
        acc = None
        if "@" in val:
            res = self.jira.get("/rest/api/3/user/search", params={"query": val})
            exact = [u for u in res if (u.get("emailAddress") or "").lower() == val.lower()]
            pick = exact or (res if len(res) == 1 else [])
            acc = pick[0]["accountId"] if pick else None
            if not acc:
                self.warn_once(f"No single Jira user found for @{handle} ({val}); the issue stays unassigned.")
        elif val:
            acc = val
        self.users[handle] = acc
        return acc

    def footer(self, ep: Epic):
        src = f"{self.blob}{ep.rel}" if self.blob else ep.rel
        return para(f"Synced from {src}. Edit it there; changes made here to synced fields are overwritten.", [{"type": "em"}])

    def labels(self, ep: Epic) -> list[str]:
        labels = list(self.cfg["labels"])
        if ep.release:
            slug = re.sub(r"[^a-z0-9]+", "-", ep.release.lower()).strip("-")
            labels.append(self.cfg["release_target_label_prefix"] + slug)
        return labels

    def put_field(self, fields: dict, kind: str, fid: str, value, label: str):
        if fid in self.meta.fields(kind):
            fields[fid] = value
        else:
            self.warn_once(f"'{label}' is not available on {kind} issues in Jira; skipped. Run the doctor command for details.")

    def upsert(self, ep: Epic, kind: str, label: str, key: Optional[str], fields: dict,
               writeback: Callable[[str], None], on_update_drop: tuple = ()) -> str:
        labels = self.labels(ep)
        digest = hashlib.sha256(json.dumps([fields, labels], sort_keys=True).encode()).hexdigest()
        if key is None:
            create = {k: v for k, v in fields.items() if v is not None}
            create["labels"] = labels
            self.check_required(kind, create)
            res = self.jira.post("/rest/api/3/issue", json={"fields": create})
            key = res["key"]
            writeback(key)
            ep.save()  # save right away so a later failure can't cause duplicates
            self.set_prop(key, digest, ep.rel)
            self.note(ep, label, "created", key)
            return key
        old = self.get_prop(key)
        if old == digest and not self.force:
            self.note(ep, label, "unchanged", key)
            return key
        upd = {k: v for k, v in fields.items() if k not in ("project", "issuetype") + on_update_drop}
        self.jira.put(f"/rest/api/3/issue/{key}", json={"fields": upd, "update": {"labels": [{"add": l} for l in labels]}})
        self.set_prop(key, digest, ep.rel)
        self.note(ep, label, "updated", key)
        return key

    def check_required(self, kind: str, fields: dict):
        missing = []
        for fid, f in self.meta.fields(kind).items():
            if f.get("required") and not f.get("hasDefaultValue") and fid not in fields:
                if (f.get("name") or "").lower() == "epic name" and "summary" in fields:
                    fields[fid] = fields["summary"]
                elif fid not in ("project", "issuetype", "summary", "reporter"):
                    missing.append(f.get("name") or fid)
        if missing:
            raise RuntimeError(f"Jira requires fields this sync doesn't fill on {kind} issues: {', '.join(missing)}")

    def get_prop(self, key):
        try:
            return (self.jira.get(f"/rest/api/3/issue/{key}/properties/{PROP}") or {}).get("value", {}).get("hash")
        except JiraError as e:
            if e.status == 404:
                return None
            raise

    def set_prop(self, key, digest, rel):
        self.jira.put(f"/rest/api/3/issue/{key}/properties/{PROP}", json={"hash": digest, "source": rel})

    def base(self, kind: str, summary: str) -> dict:
        t = self.meta.types[kind]
        if not t:
            raise RuntimeError(f"The Jira project has no '{kind}' issue type.")
        return {"project": {"key": self.meta.project}, "issuetype": {"id": t["id"]}, "summary": summary[:254]}

    # -- links --
    def ensure_link(self, task: str, story: str):
        lt = str(self.cfg.get("link_type") or "none")
        if lt.lower() == "none":
            return

        def state():
            links = self.jira.get(f"/rest/api/3/issue/{story}", params={"fields": "issuelinks"})["fields"].get("issuelinks", [])
            good, bad = [], []
            for l in links:
                if l["type"]["name"].lower() != lt.lower():
                    continue
                # On the story: an inwardIssue entry reads "story <inward> task", i.e. "is blocked by".
                if (l.get("inwardIssue") or {}).get("key") == task:
                    good.append(l["id"])
                elif (l.get("outwardIssue") or {}).get("key") == task:
                    bad.append(l["id"])
            return good, bad

        good, bad = state()
        if good:
            return
        for lid in bad:
            self.jira.delete(f"/rest/api/3/issueLink/{lid}")
        body = {"type": {"name": lt}, "inwardIssue": {"key": task}, "outwardIssue": {"key": story}}
        self.jira.post("/rest/api/3/issueLink", json=body)
        good, bad = state()
        if not good and bad:  # direction was reversed on this site: swap
            for lid in bad:
                self.jira.delete(f"/rest/api/3/issueLink/{lid}")
            body["inwardIssue"], body["outwardIssue"] = body["outwardIssue"], body["inwardIssue"]
            self.jira.post("/rest/api/3/issueLink", json=body)

    # -- main --
    def sync_epic(self, ep: Epic):
        fields = self.base("epic", ep.name)
        people = [f"{k}: {v}" for k, v in (("Document owner", ep.owner), ("Designer", ep.designer), ("Developers", ep.developers)) if v]
        fields["description"] = adf(para(ep.summary), para(" · ".join(people)), self.footer(ep))
        try:
            ep.key = self.upsert(ep, "epic", f"Epic: {ep.name}", ep.key, fields,
                                 lambda k: ep.set_cell(ep.key_line, ep.key_col, self.cell(k)))
        except Exception as e:
            self.fail(ep, f"Epic: {ep.name}", e)
            return
        for st in ep.stories:
            self.sync_story(ep, st)

    def cell(self, key):
        return f"[{key}]({self.jira.base}/browse/{key})"

    def fail(self, ep, label, e):
        self.failures += 1
        self.note(ep, label, "FAILED", str(e))
        print(f"::error file={ep.rel}::{label}: {e}")

    def sync_story(self, ep: Epic, st: Story):
        label = f"{st.sid} {st.title}"
        f = self.base("story", st.title)
        f["parent"] = {"key": ep.key}
        blocks = [para(st.description)]
        if st.notes:
            blocks.append(para(f"Notes: {st.notes}"))
        if st.ac and not self.ac:
            blocks += [heading("Acceptance criteria"), bullets(st.ac)]
        blocks.append(self.footer(ep))
        f["description"] = adf(*blocks)
        if self.ac and st.ac:
            fid, rich = self.ac
            f[fid] = adf(bullets(st.ac)) if rich else "\n".join(f"- {a}" for a in st.ac)
        if st.priority:
            self.put_field(f, "story", "priority", {"name": st.priority}, "Priority")
        pf = self.meta.points_field("story")
        if pf:
            f[pf] = st.points  # None clears it (Model B or not estimated)
        elif st.points is not None:
            self.warn_once("No story points field found on Story issues; points skipped. Run the doctor command.")
        try:
            st.key = self.upsert(ep, "story", label, st.key, f,
                                 lambda k: ep.set_cell(st.line, st.jira_col, self.cell(k)))
        except Exception as e:
            self.fail(ep, label, e)
            return
        for it in st.items:
            try:
                self.sync_item(ep, st, it)
            except Exception as e:
                self.fail(ep, f"  {it.title}", e)

    def sync_item(self, ep: Epic, st: Story, it: Item):
        kind = it.kind
        f = self.base(kind, it.title)
        blocks = []
        if kind == "subtask":
            f["parent"] = {"key": st.key}
            if it.estimate:
                if "timetracking" in self.meta.fields("subtask"):
                    f["timetracking"] = {"originalEstimate": it.estimate}
                else:
                    self.warn_once("Time tracking is not available on sub-tasks; estimates are written into the description instead.")
                    blocks.append(para(f"Estimate: {it.estimate}"))
        else:
            f["parent"] = {"key": ep.key}
            blocks.append(para(f"Part of story {st.key}: {st.title}"))
            pf = self.meta.points_field("task")
            if pf:
                f[pf] = it.points
            elif it.points is not None:
                self.warn_once("No story points field on Task issues; task points skipped. Ask a Jira admin to add it, or run the doctor command.")
        blocks.append(self.footer(ep))
        f["description"] = adf(*blocks)
        if it.owner:
            acc = self.account(it.owner)
            if acc:
                self.put_field(f, kind, "assignee", {"accountId": acc}, "Assignee")
        drop = ("parent",) if kind == "subtask" else ()
        it.key = self.upsert(ep, kind, f"  {it.title}", it.key, f,
                             lambda k: ep.set_cell(it.line, it.jira_col, self.cell(k)), on_update_drop=drop)
        if kind == "task":
            self.ensure_link(it.key, st.key)

    def orphans(self, epics: list[Epic]) -> list[str]:
        known = set()
        for ep in epics:
            known.add(ep.key)
            for st in ep.stories:
                known.add(st.key)
                known.update(it.key for it in st.items)
        jql = f'project = "{self.meta.project}" AND labels = "{self.cfg["labels"][0]}" ORDER BY key'
        found, token = [], None
        while True:
            params = {"jql": jql, "fields": "summary", "maxResults": 100}
            if token:
                params["nextPageToken"] = token
            d = self.jira.get("/rest/api/3/search/jql", params=params)
            found += [(i["key"], i["fields"].get("summary", "")) for i in d.get("issues", [])]
            token = d.get("nextPageToken")
            if not token or d.get("isLast", True):
                break
        return [f"{k} {s}" for k, s in found if k not in known]


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def load(root: Path):
    cfg = yaml.safe_load((root / ".jira/config.yml").read_text(encoding="utf-8")) or {}
    defaults = {
        "backlog_dir": "docs/backlog",
        "default_branch": "main",
        "points_scale": [0, 1, 2, 3, 5, 8, 13],
        "priorities": ["Highest", "High", "Medium", "Low", "Lowest"],
        "issue_types": {"epic": "Epic", "story": "Story", "task": "Task"},
        "story_points_field": "auto",
        "acceptance_criteria_field": "none",
        "link_type": "Blocks",
        "labels": ["md-sync"],
        "release_target_label_prefix": "target-",
    }
    for k, v in defaults.items():
        cfg.setdefault(k, v)
    team_file = root / ".jira/team.yml"
    team = yaml.safe_load(team_file.read_text(encoding="utf-8")) if team_file.exists() else {}
    team = {str(k).lstrip("@"): v for k, v in (team or {}).items()}
    files = sorted(p for p in (root / cfg["backlog_dir"]).glob("*.md") if not p.name.startswith("_"))
    epics = []
    for p in files:
        ep = parse_epic(p, p.relative_to(root).as_posix())
        validate(ep, cfg, team)
        epics.append(ep)
    return cfg, team, epics


def env(name: str) -> str:
    v = os.environ.get(name, "").strip()
    if not v:
        sys.exit(f"Missing environment variable {name}. See docs/JIRA_SYNC_SETUP.md.")
    return v


def cmd_validate(root, report):
    cfg, team, epics = load(root)
    n_err = sum(len(e.errors) for e in epics)
    n_warn = sum(len(e.problems) for e in epics) - n_err
    head = "## Jira sync check\n\n"
    if not epics:
        head += f"No epic files found in `{cfg['backlog_dir']}/` (files starting with `_` are skipped).\n"
    elif n_err:
        head += f"❌ {n_err} error(s), {n_warn} warning(s). Fix the errors before merging; nothing is sent to Jira until then.\n"
    else:
        head += f"✅ No errors ({n_warn} warning(s)). On merge, the sync will do this:\n"
    body = problems_md(epics)
    text = head + ("\n" + body + "\n" if body else "") + plan_md(epics)
    write_report(report, text)
    return 1 if n_err else 0


def cmd_sync(root, report, force):
    cfg, team, epics = load(root)
    if any(e.errors for e in epics):
        write_report(report, "## Jira sync\n\n❌ Validation errors; nothing was sent to Jira.\n\n" + problems_md(epics))
        return 1
    jira = Jira(env("JIRA_BASE_URL"), env("JIRA_EMAIL"), env("JIRA_API_TOKEN"))
    meta = Meta(jira, env("JIRA_PROJECT_KEY"), cfg)
    sy = Syncer(jira, meta, cfg, team, force)
    for ep in epics:
        sy.sync_epic(ep)
        ep.save()
    lines = ["## Jira sync", "", "| File | Item | Result | Key / detail |", "|---|---|---|---|"]
    lines += [f"| {f} | {i.strip()} | {a} | {d} |" for f, i, a, d in sy.log]
    try:
        orphans = sy.orphans(epics)
        if orphans:
            lines += ["", "**In Jira but no longer in the markdown** (not deleted; close or delete them in Jira if intended):", ""]
            lines += [f"- {o}" for o in orphans]
    except Exception as e:
        lines += ["", f"⚠️ Could not check for removed items: {e}"]
    if sy.warned:
        lines += ["", "**Warnings**", ""] + [f"- {w}" for w in sorted(sy.warned)]
    write_report(report, "\n".join(lines))
    return 1 if sy.failures else 0


def cmd_doctor(root, report):
    cfg, team, epics = load(root)
    out = ["## Jira sync doctor", ""]
    ok = True
    jira = Jira(env("JIRA_BASE_URL"), env("JIRA_EMAIL"), env("JIRA_API_TOKEN"))
    try:
        me = jira.get("/rest/api/3/myself")
        out.append(f"✅ Logged in as **{me.get('displayName')}**")
    except JiraError as e:
        write_report(report, "\n".join(out + [f"❌ Login failed: {e}", "", "Check JIRA_BASE_URL, JIRA_EMAIL and JIRA_API_TOKEN."]))
        return 1
    try:
        meta = Meta(jira, env("JIRA_PROJECT_KEY"), cfg)
    except JiraError as e:
        write_report(report, "\n".join(out + [f"❌ Project {os.environ.get('JIRA_PROJECT_KEY')} not readable: {e}"]))
        return 1
    style = {"next-gen": "team-managed", "classic": "company-managed"}.get(meta.proj.get("style"), meta.proj.get("style", "?"))
    out.append(f"✅ Project **{meta.proj.get('key')} – {meta.proj.get('name')}** ({style})")
    out += ["", "| Check | Epic | Story | Task | Sub-task |", "|---|---|---|---|---|"]
    kinds = ["epic", "story", "task", "subtask"]
    row = ["Issue type"] + [("✅ " + meta.types[k]["name"]) if meta.types[k] else "❌ missing" for k in kinds]
    out.append("| " + " | ".join(row) + " |")
    if not meta.types["epic"] or not meta.types["story"]:
        ok = False
    need = {
        "Description": ("description", ["epic", "story", "task", "subtask"]),
        "Priority": ("priority", ["story"]),
        "Assignee": ("assignee", ["task", "subtask"]),
        "Labels": ("labels", ["epic", "story", "task", "subtask"]),
        "Parent": ("parent", ["story", "task", "subtask"]),
        "Time tracking": ("timetracking", ["subtask"]),
    }
    for label, (fid, used) in need.items():
        cells = [label]
        for k in kinds:
            if not meta.types[k]:
                cells.append("–")
            elif k not in used:
                cells.append("")
            else:
                cells.append("✅" if fid in meta.fields(k) else "⚠️ not on screen")
        out.append("| " + " | ".join(cells) + " |")
    cells = ["Story points"]
    for k in kinds:
        if k in ("story", "task") and meta.types[k]:
            pf = meta.points_field(k)
            name = next((f["name"] for f in meta.all_fields if f["id"] == pf), pf)
            cells.append(f"✅ {name}" if pf else "❌ not found")
            if k == "story" and not pf:
                ok = False
        else:
            cells.append("")
    out.append("| " + " | ".join(cells) + " |")
    for k in kinds:
        if meta.types[k]:
            req = [f.get("name") or fid for fid, f in meta.fields(k).items()
                   if f.get("required") and not f.get("hasDefaultValue")
                   and fid not in ("project", "issuetype", "summary", "reporter", "parent")
                   and (f.get("name") or "").lower() != "epic name"]
            if req:
                out.append(f"\n❌ {k} issues require fields the sync can't fill: {', '.join(req)}")
                ok = False
    lt = str(cfg.get("link_type") or "none")
    if lt.lower() != "none":
        types = [t["name"] for t in jira.get("/rest/api/3/issueLinkType").get("issueLinkTypes", [])]
        out.append("")
        out.append(f"✅ Link type **{lt}** exists" if lt.lower() in (t.lower() for t in types)
                   else f"❌ Link type **{lt}** not found. Available: {', '.join(types)}")
    ac = cfg.get("acceptance_criteria_field")
    if ac and str(ac).lower() != "none":
        out.append(f"✅ Acceptance criteria field **{ac}** found" if meta.ac_field()
                   else f"❌ Acceptance criteria field **{ac}** not on Story issues")
    out += ["", "**Team members** (.jira/team.yml)", ""]
    sy = Syncer(jira, meta, cfg, team)
    for h in team:
        acc = sy.account(h)
        out.append(f"- {'✅' if acc else '❌'} @{h} → {team[h]}")
    sy.warned.clear()
    out += ["", f"Epic files found: {len(epics)}"]
    write_report(report, "\n".join(out))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["validate", "sync", "doctor"])
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent), help="repository root")
    ap.add_argument("--report", help="also write the report to this file")
    ap.add_argument("--force", action="store_true", help="update issues even if nothing changed")
    a = ap.parse_args()
    root = Path(a.root)
    if a.command == "validate":
        sys.exit(cmd_validate(root, a.report))
    if a.command == "sync":
        sys.exit(cmd_sync(root, a.report, a.force))
    sys.exit(cmd_doctor(root, a.report))


if __name__ == "__main__":
    main()
