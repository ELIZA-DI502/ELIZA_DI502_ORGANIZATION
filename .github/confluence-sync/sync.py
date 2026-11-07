#!/usr/bin/env python3
"""Publish the Markdown pages in this repository to a Confluence Cloud space.

How the repository maps onto Confluence
---------------------------------------
* Every ``.md`` file is one Confluence page. Its title is the file's first
  ``# Heading`` (falling back to the file name).
* A folder is a parent page. Its content is the folder's ``README.md``, and
  the other files and folders inside it are its children. A folder without a
  ``README.md`` becomes a page that just lists its children.
* The ``README.md`` at the top of the docs directory is the root page: it
  updates the page CONFLUENCE_PARENT_ID, or the space homepage when that is not
  set, and every top-level page goes under it.
* Pages are matched by title inside the space: an existing page with the same
  title is updated (and moved under the right parent); otherwise a new page is
  created. Nothing is ever deleted.
* Relative links between Markdown files (and to folders) become Confluence
  page links.
* Relative links to any other file in the repository (for example a CSV, a
  PDF or a Markdown file outside the docs directory) become links to that file
  on GitHub, because Confluence does not have the file.
* Images with a relative path are shown from the repository (raw file on
  GitHub), and every image is shown at page width.
* Links to a heading on the same page (``#heading``) jump to that heading:
  every heading gets a Confluence anchor with the name GitHub gives it.
* A ``mermaid`` code block is put in a collapsed "Diagram source (Mermaid)"
  section, because Confluence does not draw Mermaid. Add the diagram as an
  image next to the block so that Confluence readers see it.

Usage
-----
    python sync.py --all                 # every page
    python sync.py --since <git-sha>     # only files changed since that commit
    python sync.py --all --dry-run --out preview/   # no network; writes XHTML

Environment
-----------
    CONFLUENCE_BASE_URL    https://<site>.atlassian.net
    CONFLUENCE_SPACE_KEY   key of the existing space, e.g. DI502
    CONFLUENCE_EMAIL       Atlassian account e-mail
    CONFLUENCE_API_TOKEN   API token for that account
    CONFLUENCE_PARENT_ID   optional: page id to put top-level pages under
    DOCS_DIR               optional: folder holding the Markdown (default ".")
    CONFLUENCE_IGNORE      optional: comma-separated globs to skip
    GITHUB_REPOSITORY      set by GitHub Actions (owner/repo); taken from the
                           git remote "origin" when not set
    GITHUB_REF_NAME        set by GitHub Actions; the branch the file links use
                           (default "main")
"""
from __future__ import annotations

import argparse
import fnmatch
import html
import os
import re
import struct
import subprocess
import sys
import time
from pathlib import Path, PurePosixPath
from urllib.parse import quote, unquote, urlsplit

import markdown
import requests
from lxml import etree
from lxml import html as lhtml

ZERO_SHA = "0" * 40
ROOT = PurePosixPath(".")
H1 = re.compile(r"^#[ \t]+(.+?)[ \t#]*$", re.MULTILINE)
VOID = {"br", "hr", "img", "col"}


def log(msg: str) -> None:
    print(msg, flush=True)


# --------------------------------------------------------------------------- repository model
class Docs:
    def __init__(self, root: Path, ignore: list[str]):
        self.root = root.resolve()
        self.nodes: dict[PurePosixPath, Path | None] = {}
        self.skipped: dict[str, str] = {}
        files = sorted(
            p for p in self.root.rglob("*.md")
            if not any(part.startswith(".") or part == "node_modules"
                       for part in p.relative_to(self.root).parts)
        )
        for f in files:
            rel = f.relative_to(self.root).as_posix()
            if any(fnmatch.fnmatch(rel, g) for g in ignore):
                self.skipped[rel] = "matches CONFLUENCE_IGNORE"
                continue
            self.nodes[self.node_of(rel)] = f
        # folders without their own file still need a page
        for node in list(self.nodes):
            for anc in self.ancestors(node):
                self.nodes.setdefault(anc, None)
        self._titles: dict[PurePosixPath, str] = {}
        self.repo = Repo(self.root)

    @staticmethod
    def node_of(rel: str) -> PurePosixPath:
        """A README.md stands for its folder; any other file stands for itself."""
        p = PurePosixPath(rel)
        return p.parent if p.name == "README.md" else p

    @staticmethod
    def ancestors(node: PurePosixPath) -> list[PurePosixPath]:
        """Ancestors from the top down, excluding the root and the node itself."""
        return [a for a in reversed(node.parents) if a != ROOT]

    def title(self, node: PurePosixPath) -> str:
        if node not in self._titles:
            src = self.nodes.get(node)
            m = H1.search(src.read_text(encoding="utf-8")) if src else None
            if m:
                t = m.group(1).strip()
            else:
                name = node.name.removesuffix(".md") or "Home"
                t = re.sub(r"^\d+[-_ ]+", "", name).replace("-", " ").replace("_", " ")
                t = t[:1].upper() + t[1:]
            self._titles[node] = t
        return self._titles[node]

    def resolve_link(self, src: Path, href: str) -> PurePosixPath | None:
        """The page a relative link to a Markdown file or a folder points to."""
        parts = urlsplit(href)
        if parts.scheme or parts.netloc or not parts.path:
            return None
        target = (src.parent / unquote(parts.path)).resolve()
        if not (parts.path.lower().endswith(".md") or target.is_dir()):
            return None
        try:
            rel = target.relative_to(self.root).as_posix()
        except ValueError:
            return None
        node = self.node_of(rel) if rel.lower().endswith(".md") else PurePosixPath(rel)
        return node if node in self.nodes else None

    def check_titles(self) -> None:
        seen: dict[str, PurePosixPath] = {}
        for node in sorted(self.nodes):
            t = self.title(node)
            if t in seen:
                sys.exit(f"ERROR: '{seen[t]}' and '{node}' both have the title '{t}'. "
                         "Confluence needs unique page titles in a space; rename one heading.")
            seen[t] = node


# --------------------------------------------------------------------------- links to files on GitHub
class Repo:
    """Where the repository's files can be opened on GitHub."""

    def __init__(self, docs_root: Path):
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=docs_root,
                             capture_output=True, text=True)
        self.root = Path(out.stdout.strip()).resolve() if out.returncode == 0 else docs_root
        self.server = os.environ.get("GITHUB_SERVER_URL", "https://github.com").rstrip("/")
        self.ref = os.environ.get("GITHUB_REF_NAME") or "main"
        self.name = os.environ.get("GITHUB_REPOSITORY") or self._from_remote()

    def _from_remote(self) -> str | None:
        out = subprocess.run(["git", "remote", "get-url", "origin"], cwd=self.root,
                             capture_output=True, text=True)
        m = re.search(r"github\.com[:/]+([^/]+/[^/]+?)(?:\.git)?/?$", out.stdout.strip())
        return m.group(1) if m else None

    def rel(self, path: Path) -> str | None:
        try:
            return path.resolve().relative_to(self.root).as_posix()
        except ValueError:
            return None

    def page_url(self, path: Path) -> str | None:
        """The GitHub page of a file or folder in the repository."""
        rel = self.rel(path)
        if not self.name or rel is None or not path.exists():
            return None
        kind = "tree" if path.is_dir() else "blob"
        return f"{self.server}/{self.name}/{kind}/{quote(self.ref)}/{quote(rel)}"

    def raw_url(self, path: Path) -> str | None:
        """The raw file of an image in the repository, which Confluence can show."""
        rel = self.rel(path)
        if not self.name or rel is None or not path.is_file() or self.server != "https://github.com":
            return None
        return f"https://raw.githubusercontent.com/{self.name}/{quote(self.ref)}/{quote(rel)}"

    def local_file(self, url: str) -> Path | None:
        """The repository file behind a raw.githubusercontent.com URL of this repository."""
        prefix = f"https://raw.githubusercontent.com/{self.name}/{self.ref}/"
        if not self.name or not url.startswith(prefix):
            return None
        path = self.root / unquote(url[len(prefix):])
        return path if path.is_file() else None


def png_size(path: Path | None) -> tuple[int, int] | None:
    """Width and height of a PNG file, or None."""
    if path is None or path.suffix.lower() != ".png":
        return None
    with path.open("rb") as f:
        head = f.read(24)
    if len(head) < 24 or head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", head[16:24])


def github_slug(text: str, seen: dict[str, int]) -> str:
    """The anchor GitHub gives a heading, so that '#...' links keep working."""
    slug = re.sub(r"[^\w\- ]", "", text.strip().lower()).replace(" ", "-")
    n = seen.get(slug, 0)
    seen[slug] = n + 1
    return slug if n == 0 else f"{slug}-{n}"


def cdata(text: str) -> str:
    return "<![CDATA[" + text.replace("]]>", "]]]]><![CDATA[>") + "]]>"


def swap(el, token: str) -> None:
    """Replace an element with a text token, keeping the text that follows it."""
    parent, prev = el.getparent(), el.getprevious()
    filler = token + (el.tail or "")
    if prev is not None:
        prev.tail = (prev.tail or "") + filler
    else:
        parent.text = (parent.text or "") + filler
    parent.remove(el)


PAGE_WIDTH = 760  # width of a Confluence page in the default (fixed-width) layout


# --------------------------------------------------------------------------- Markdown -> storage format
def to_storage(docs: Docs, node: PurePosixPath) -> str:
    src = docs.nodes[node]
    if src is None:  # folder with no content file: show its children
        return '<ac:structured-macro ac:name="children" ac:schema-version="2" />'

    text = src.read_text(encoding="utf-8")
    text = H1.sub("", text, count=1)  # the H1 becomes the page title
    body = markdown.markdown(text, extensions=["tables", "sane_lists", "fenced_code"],
                             output_format="xhtml")
    if not body.strip():
        return ""

    tree = lhtml.fragment_fromstring(body, create_parent="div")

    # Confluence expects header rows inside <tbody>
    for thead in tree.iter("thead"):
        table = thead.getparent()
        tbody = table.find("tbody")
        if tbody is None:
            tbody = etree.SubElement(table, "tbody")
        for i, row in enumerate(list(thead)):
            tbody.insert(i, row)
        table.remove(thead)

    # Confluence markup is swapped in for these tokens after serialising
    links: dict[str, str] = {}

    def token_for(value: str) -> str:
        token = f"@@CFLINK{len(links)}@@"
        links[token] = value
        return token

    repo = docs.repo

    # mermaid blocks -> collapsed "Diagram source" section (Confluence cannot draw them)
    for code in list(tree.iter("code")):
        pre = code.getparent()
        if pre is None or pre.tag != "pre" or "language-mermaid" not in (code.get("class") or ""):
            continue
        swap(pre, token_for(
            '<ac:structured-macro ac:name="expand">'
            '<ac:parameter ac:name="title">Diagram source (Mermaid)</ac:parameter>'
            '<ac:rich-text-body><ac:structured-macro ac:name="code">'
            f"<ac:plain-text-body>{cdata(code.text_content())}</ac:plain-text-body>"
            "</ac:structured-macro></ac:rich-text-body></ac:structured-macro>"))

    # every heading gets an anchor with the name GitHub gives it
    seen: dict[str, int] = {}
    for h in tree.iter("h1", "h2", "h3", "h4", "h5", "h6"):
        slug = github_slug(h.text_content(), seen)
        h.text = token_for(
            '<ac:structured-macro ac:name="anchor">'
            f'<ac:parameter ac:name="">{html.escape(slug)}</ac:parameter>'
            "</ac:structured-macro>") + (h.text or "")

    # images: shown from the repository when the path is relative, at page width
    for img in list(tree.iter("img")):
        url = img.get("src", "")
        parts = urlsplit(url)
        if not parts.scheme and not parts.netloc and parts.path:
            local = (src.parent / unquote(parts.path)).resolve()
            url = repo.raw_url(local) or url
            if url == img.get("src"):
                log(f"  warning: {src.relative_to(docs.root)}: image not found: {img.get('src')}")
        else:
            local = repo.local_file(url)
        size = png_size(local) if local else None
        width = PAGE_WIDTH if size is None else min(PAGE_WIDTH, size[0])
        alt = html.escape(img.get("alt") or "", quote=True)
        swap(img, token_for(
            f'<ac:image ac:align="center" ac:layout="center" ac:width="{width}" ac:alt="{alt}">'
            f'<ri:url ri:value="{html.escape(url, quote=True)}" /></ac:image>'))

    # links
    for a in list(tree.iter("a")):
        href = a.get("href", "")
        parts = urlsplit(href)
        if parts.scheme or parts.netloc or not href:
            continue
        label = cdata(a.text_content())
        if not parts.path and parts.fragment:  # a heading on the same page
            swap(a, token_for(
                f'<ac:link ac:anchor="{html.escape(unquote(parts.fragment), quote=True)}">'
                f"<ac:plain-text-link-body>{label}</ac:plain-text-link-body></ac:link>"))
            continue
        node_t = docs.resolve_link(src, href)
        if node_t is not None:  # another page in Confluence
            swap(a, token_for(
                f'<ac:link><ri:page ri:content-title="{html.escape(docs.title(node_t), quote=True)}" />'
                f"<ac:plain-text-link-body>{label}</ac:plain-text-link-body></ac:link>"))
            continue
        url = repo.page_url(src.parent / unquote(parts.path))  # any other file: open it on GitHub
        if url:
            a.set("href", url + (f"#{parts.fragment}" if parts.fragment else ""))
        else:
            log(f"  warning: {src.relative_to(docs.root)}: link target not found: {href}")

    # keep empty cells as <td></td> rather than <td/>
    for el in tree.iter():
        if isinstance(el.tag, str) and el.tag not in VOID and el.text is None and len(el) == 0:
            el.text = ""

    xml = etree.tostring(tree, method="xml", encoding="unicode")
    xml = re.sub(r"^<div>|</div>$", "", xml)
    for token, value in links.items():
        xml = xml.replace(token, value)
    return xml


# --------------------------------------------------------------------------- Confluence Cloud client
class Confluence:
    def __init__(self, base_url: str, email: str, token: str, space_key: str):
        self.site = re.sub(r"/wiki/?$", "", base_url.rstrip("/"))
        self.api = f"{self.site}/wiki/api/v2"
        self.s = requests.Session()
        self.s.auth = (email, token)
        self.s.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
        space = self._req("GET", f"{self.api}/spaces", params={"keys": space_key})["results"]
        if not space:
            sys.exit(f"ERROR: space '{space_key}' not found, or this account cannot see it.")
        self.space_id = space[0]["id"]
        self.homepage_id = space[0].get("homepageId")

    def _req(self, method: str, url: str, **kw):
        for attempt in range(6):
            r = self.s.request(method, url, timeout=60, **kw)
            if r.status_code == 429 or r.status_code >= 500:
                wait = int(r.headers.get("Retry-After", 2 ** attempt))
                log(f"  … {r.status_code} from Confluence, retrying in {wait}s")
                time.sleep(wait)
                continue
            if not r.ok:
                raise RuntimeError(f"{method} {url} -> {r.status_code}: {r.text[:800]}")
            return r.json() if r.content else {}
        raise RuntimeError(f"{method} {url} kept failing; giving up")

    def get(self, page_id: str) -> dict:
        return self._req("GET", f"{self.api}/pages/{page_id}")

    def find(self, title: str) -> dict | None:
        wanted = title.strip().casefold()
        params = {"space-id": self.space_id, "status": "current", "limit": 250}
        url = f"{self.api}/pages"

        while url:
            res = self._req("GET", url, params=params)
            params = {}
            for page in res.get("results", []):
                if page["title"].strip().casefold() == wanted:
                    return page

            next_url = res.get("_links", {}).get("next")
            if next_url:
                from urllib.parse import urljoin
                url = urljoin(self.site, next_url)
            else:
                url = None

        return None

    def create(self, title: str, parent_id: str, body: str) -> dict:
        return self._req("POST", f"{self.api}/pages", json={
            "spaceId": self.space_id, "status": "current", "title": title, "parentId": parent_id,
            "body": {"representation": "storage", "value": body}})

    def update(self, page: dict, title: str, parent_id: str | None, body: str, message: str) -> dict:
        payload = {
            "id": page["id"], "status": "current", "title": title,
            "body": {"representation": "storage", "value": body},
            "version": {"number": page["version"]["number"] + 1, "message": message}}
        if parent_id:
            payload["parentId"] = parent_id
        res = self._req("PUT", f"{self.api}/pages/{page['id']}", json=payload)
        if parent_id and str(res.get("parentId")) != str(parent_id):
            self._req("PUT", f"{self.site}/wiki/rest/api/content/{page['id']}/move/append/{parent_id}")
        return res


# --------------------------------------------------------------------------- sync
def changed_nodes(docs: Docs, since: str | None) -> list[PurePosixPath] | None:
    """Nodes whose file changed since `since`; None means 'sync everything'."""
    if not since or since == ZERO_SHA:
        log("No previous commit to compare with: syncing every page.")
        return None
    top = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                       cwd=docs.root, text=True).strip())
    if subprocess.run(["git", "cat-file", "-e", f"{since}^{{commit}}"], cwd=top,
                      capture_output=True).returncode != 0:
        log(f"Commit {since[:12]} is not in the history (force push?): syncing every page.")
        return None
    out = subprocess.check_output(
        ["git", "diff", "--name-only", "--diff-filter=AMR", since, "HEAD", "--", "*.md"],
        cwd=top, text=True)
    nodes = []
    for line in filter(None, out.splitlines()):
        path = (top / line).resolve()
        try:
            rel = path.relative_to(docs.root).as_posix()
        except ValueError:
            continue
        if rel in docs.skipped:
            log(f"skip {rel}: {docs.skipped[rel]}")
            continue
        node = docs.node_of(rel)
        if docs.nodes.get(node) is not None and docs.nodes[node].resolve() == path:
            nodes.append(node)
    return nodes


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--all", action="store_true", help="sync every page")
    mode.add_argument("--since", metavar="SHA", help="sync files changed since this commit")
    ap.add_argument("--dry-run", action="store_true", help="convert only; do not call Confluence")
    ap.add_argument("--out", type=Path, help="with --dry-run: write the converted XHTML here")
    args = ap.parse_args()

    docs = Docs(Path(os.environ.get("DOCS_DIR") or "."),
                [g.strip() for g in os.environ.get("CONFLUENCE_IGNORE", "").split(",") if g.strip()])
    for rel, why in docs.skipped.items():
        log(f"skip {rel}: {why}")
    docs.check_titles()

    targets = None if args.all else changed_nodes(docs, args.since)
    if targets is None:
        targets = [n for n in docs.nodes if docs.nodes[n] is not None]
    targets = sorted(set(targets), key=lambda n: (n != ROOT, n.as_posix()))
    if not targets:
        log("No Markdown pages changed. Nothing to do.")
        return

    # parents first, so every page has somewhere to go
    order: list[PurePosixPath] = []
    for node in targets:
        for n in docs.ancestors(node) + [node]:
            if n not in order:
                order.append(n)
    update = set(targets)

    if args.dry_run:
        for n in order:
            action = "create/update" if n in update else "ensure exists"
            if n == ROOT:
                action, parent = "update root", "(CONFLUENCE_PARENT_ID or space homepage)"
            else:
                parent = n.parent if n.parent != ROOT else "(root page)"
            log(f"[dry-run] {action:13} '{docs.title(n)}'  <- {docs.nodes[n] and docs.nodes[n].relative_to(docs.root)}  parent: {parent}")
            if args.out and n in update:
                dest = args.out / docs.nodes[n].relative_to(docs.root).with_suffix(".xhtml")
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(to_storage(docs, n), encoding="utf-8")
        return

    need = ["CONFLUENCE_BASE_URL", "CONFLUENCE_SPACE_KEY", "CONFLUENCE_EMAIL", "CONFLUENCE_API_TOKEN"]
    missing = [v for v in need if not os.environ.get(v)]
    if missing:
        sys.exit("ERROR: missing settings: " + ", ".join(missing))

    cf = Confluence(os.environ["CONFLUENCE_BASE_URL"], os.environ["CONFLUENCE_EMAIL"],
                    os.environ["CONFLUENCE_API_TOKEN"], os.environ["CONFLUENCE_SPACE_KEY"])
    root_id = os.environ.get("CONFLUENCE_PARENT_ID") or cf.homepage_id
    if not root_id:
        sys.exit("ERROR: the space has no homepage; set CONFLUENCE_PARENT_ID.")
    sha = os.environ.get("GITHUB_SHA", "")[:7]
    message = f"Synced from git {sha}".strip()

    ids: dict[PurePosixPath, str] = {ROOT: str(root_id)}
    failures = 0
    for n in order:
        title, parent_id = docs.title(n), ids[n.parent]
        try:
            if n == ROOT:  # top-level README.md -> the root page itself
                cf.update(cf.get(ids[ROOT]), title, None, to_storage(docs, n), message)
                log(f"updated  '{title}' (root page)")
                continue
            page = cf.find(title)
            if page and str(page["id"]) == ids[ROOT]:
                raise RuntimeError(f"'{title}' is the title of the root page; rename this heading")
            if page and n not in update:
                ids[n] = page["id"]
                continue
            body = to_storage(docs, n)
            if page:
                cf.update(page, title, parent_id, body, message)
                ids[n] = page["id"]
                log(f"updated  '{title}'")
            else:
                ids[n] = cf.create(title, parent_id, body)["id"]
                log(f"created  '{title}'")
        except RuntimeError as e:
            failures += 1
            log(f"FAILED   '{title}': {e}")
            if n not in ids:  # its children cannot be placed either
                ids[n] = parent_id
    if failures:
        sys.exit(f"{failures} page(s) failed; see the log above.")
    log(f"Done: {len(update)} page(s) synced.")


if __name__ == "__main__":
    main()
