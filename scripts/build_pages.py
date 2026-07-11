#!/usr/bin/env python3
from __future__ import annotations

import html
import os
import shutil
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

try:
    import markdown
except ImportError:
    print("Missing dependency: markdown. Install it with 'python -m pip install markdown'.", file=sys.stderr)
    raise SystemExit(1)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs"
LANDING_SOURCE = Path("10_playbooks/operating_system.md")
HOME_PAGE = "index.html"
ALL_DOCS_PAGE = "all-docs.html"
SOURCE_DIRS = [
    "01_reporting_system",
    "03_campaign_analysis",
    "04_crm_management",
    "05_attribution",
    "06_dashboards",
    "07_ai_execution",
    "08_field_marketing",
    "09_referrals",
    "10_playbooks",
    "11_quality_control",
]

SITE_CSS = """
:root {
  color-scheme: light;
  --bg: #f4f7fb;
  --panel: #ffffff;
  --panel-border: #d9e2ec;
  --text: #14202b;
  --muted: #51606f;
  --link: #165dff;
  --link-hover: #0e49c7;
  --shadow: 0 12px 30px rgba(20, 32, 43, 0.08);
}

* {
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: Inter, "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
  line-height: 1.65;
}

a {
  color: var(--link);
}

a:hover {
  color: var(--link-hover);
}

.shell {
  min-height: 100vh;
}

.topbar {
  position: sticky;
  top: 0;
  z-index: 10;
  backdrop-filter: blur(12px);
  background: rgba(244, 247, 251, 0.92);
  border-bottom: 1px solid var(--panel-border);
}

.topbar-inner {
  max-width: 1080px;
  margin: 0 auto;
  padding: 0.9rem 1.25rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem 1.25rem;
  align-items: center;
  justify-content: space-between;
}

.brand {
  font-weight: 700;
  color: var(--text);
  text-decoration: none;
}

.brand:hover {
  color: var(--text);
}

.nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.9rem;
  align-items: center;
}

.nav a {
  text-decoration: none;
  font-weight: 600;
}

.meta {
  max-width: 1080px;
  margin: 0 auto;
  padding: 0.75rem 1.25rem 0;
  color: var(--muted);
  font-size: 0.95rem;
}

.page {
  max-width: 1080px;
  margin: 0 auto;
  padding: 1rem 1.25rem 3rem;
}

.card {
  background: var(--panel);
  border: 1px solid var(--panel-border);
  border-radius: 18px;
  box-shadow: var(--shadow);
  padding: 2rem;
}

article > :first-child {
  margin-top: 0;
}

h1, h2, h3, h4 {
  line-height: 1.2;
  margin-top: 1.8rem;
  margin-bottom: 0.8rem;
}

h1 {
  font-size: 2.1rem;
}

h2 {
  font-size: 1.45rem;
}

p, ul, ol, table, blockquote, pre {
  margin-top: 0;
  margin-bottom: 1rem;
}

ul, ol {
  padding-left: 1.3rem;
}

li + li {
  margin-top: 0.35rem;
}

code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  background: #edf2f7;
  border-radius: 6px;
  padding: 0.08rem 0.32rem;
  font-size: 0.92em;
}

pre {
  overflow-x: auto;
  padding: 1rem;
  background: #0f1720;
  color: #e6edf3;
  border-radius: 14px;
}

pre code {
  background: transparent;
  color: inherit;
  padding: 0;
}

blockquote {
  border-left: 4px solid #b7c4d3;
  margin-left: 0;
  padding: 0.25rem 0 0.25rem 1rem;
  color: var(--muted);
}

.table-wrap {
  overflow-x: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
  min-width: 560px;
}

th, td {
  border: 1px solid var(--panel-border);
  padding: 0.7rem 0.8rem;
  text-align: left;
  vertical-align: top;
}

th {
  background: #eef4fb;
}

.footer {
  max-width: 1080px;
  margin: 0 auto;
  padding: 0 1.25rem 2rem;
  color: var(--muted);
  font-size: 0.92rem;
}

.doc-list {
  display: grid;
  gap: 1rem;
}

.doc-group {
  border: 1px solid var(--panel-border);
  border-radius: 14px;
  padding: 1rem 1rem 0.25rem;
  background: #fbfdff;
}

.doc-group h2 {
  margin-top: 0;
}

.doc-group ul {
  margin-bottom: 0.9rem;
}

@media (max-width: 720px) {
  .card {
    padding: 1.25rem;
    border-radius: 14px;
  }

  h1 {
    font-size: 1.7rem;
  }
}
""".strip()


@dataclass(frozen=True)
class Page:
    source: Path
    relative_source: Path
    output: Path
    title: str


def collect_sources() -> list[Path]:
    sources: list[Path] = []
    for directory in SOURCE_DIRS:
        base = ROOT / directory
        if not base.exists():
            continue
        sources.extend(sorted(base.rglob("*.md")))
    return sources


def extract_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback.replace("_", " ").replace("-", " ").title()


def to_output_path(relative_source: Path) -> Path:
    return OUTPUT / relative_source.with_suffix(".html")


def rel_href(current_output: Path, target_output: Path) -> str:
    return Path(os.path.relpath(target_output, start=current_output.parent)).as_posix()


def resolve_markdown_link(source_rel: Path, href_path: str) -> Path:
    if href_path.startswith("/"):
        return Path(href_path.lstrip("/"))
    normalized = os.path.normpath(str(source_rel.parent / href_path))
    return Path(normalized)


def find_markdown_link(text: str, cursor: int) -> tuple[int, int, str, str, str] | None:
    start = text.find("[", cursor)
    while start != -1:
        if start > 0 and text[start - 1] == "!":
            start = text.find("[", start + 1)
            continue

        label_end = text.find("](", start)
        if label_end == -1:
            return None

        href_end = text.find(")", label_end + 2)
        if href_end == -1:
            return None

        label = text[start + 1 : label_end]
        href = text[label_end + 2 : href_end].strip()
        original = text[start : href_end + 1]
        return start, href_end + 1, label, href, original

    return None


def rewrite_markdown_links(text: str, source_rel: Path, current_output: Path) -> str:
    def rewrite_candidate(label: str, href: str, original: str) -> str:
        parts = urlsplit(href)

        if parts.scheme or parts.netloc or not parts.path or parts.path.startswith("#"):
            return original

        if not parts.path.endswith(".md"):
            return original

        target_source = resolve_markdown_link(source_rel, parts.path)
        target_output = to_output_path(target_source)
        new_path = rel_href(current_output, target_output)
        rewritten = urlunsplit(("", "", new_path, parts.query, parts.fragment))
        return f"[{label}]({rewritten})"

    chunks: list[str] = []
    cursor = 0

    while cursor < len(text):
        match = find_markdown_link(text, cursor)
        if match is None:
            chunks.append(text[cursor:])
            break

        start, cursor_end, label, href, original = match
        chunks.append(text[cursor:start])
        if any(char in label for char in "\r\n") or any(char in href for char in "\r\n"):
            chunks.append(original)
        else:
            chunks.append(rewrite_candidate(label, href, original))
        cursor = cursor_end

    return "".join(chunks)


def render_markdown(text: str) -> str:
    html_output = markdown.markdown(
        text,
        extensions=["extra", "sane_lists", "toc"],
        output_format="html5",
    )
    return html_output.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")


def render_shell(title: str, body_html: str, current_output: Path, source_label: str) -> str:
    css_href = rel_href(current_output, OUTPUT / "assets" / "site.css")
    home_href = rel_href(current_output, OUTPUT / HOME_PAGE)
    all_docs_href = rel_href(current_output, OUTPUT / ALL_DOCS_PAGE)
    title_html = html.escape(title)
    source_html = html.escape(source_label)

    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title_html} | Evo MKT OS</title>
    <link rel="stylesheet" href="{css_href}">
  </head>
  <body>
    <div class="shell">
      <header class="topbar">
        <div class="topbar-inner">
          <a class="brand" href="{home_href}">OS Index</a>
          <nav class="nav">
            <a href="{all_docs_href}">All docs</a>
          </nav>
        </div>
      </header>
      <div class="meta">{source_html}</div>
      <main class="page">
        <section class="card">
          <article>
{body_html}
          </article>
        </section>
      </main>
      <footer class="footer">
        Published from the repo markdown in <code>mktg-context</code>.
      </footer>
    </div>
  </body>
</html>
"""


def build_page(page: Page) -> None:
    source_text = page.source.read_text(encoding="utf-8")
    rewritten = rewrite_markdown_links(source_text, page.relative_source, page.output)
    body_html = render_markdown(rewritten)
    page_html = render_shell(page.title, body_html, page.output, page.relative_source.as_posix())
    page.output.parent.mkdir(parents=True, exist_ok=True)
    page.output.write_text(page_html, encoding="utf-8")


def build_landing_page(landing_source: Path) -> None:
    source_file = ROOT / landing_source
    output_file = OUTPUT / HOME_PAGE
    source_text = source_file.read_text(encoding="utf-8")
    title = extract_title(source_text, "Operating system index")
    rewritten = rewrite_markdown_links(source_text, landing_source, output_file)
    body_html = render_markdown(rewritten)
    output_file.write_text(render_shell(title, body_html, output_file, landing_source.as_posix()), encoding="utf-8")


def build_all_docs_page(pages: list[Page]) -> None:
    output_file = OUTPUT / ALL_DOCS_PAGE
    grouped: dict[str, list[Page]] = defaultdict(list)
    for page in pages:
        grouped[page.relative_source.parts[0]].append(page)

    chunks = ['<h1>All docs</h1>', "<p>Browsable HTML mirror of the operating system docs.</p>", '<div class="doc-list">']
    for group in sorted(grouped):
        chunks.append(f'<section class="doc-group"><h2>{html.escape(group)}</h2><ul>')
        for page in sorted(grouped[group], key=lambda item: item.relative_source.as_posix()):
            href = rel_href(output_file, page.output)
            title = html.escape(page.title)
            source = html.escape(page.relative_source.as_posix())
            chunks.append(f'<li><a href="{href}">{title}</a><br><code>{source}</code></li>')
        chunks.append("</ul></section>")
    chunks.append("</div>")

    body_html = "\n".join(chunks)
    output_file.write_text(render_shell("All docs", body_html, output_file, "Generated navigation"), encoding="utf-8")


def build_404_page() -> None:
    output_file = OUTPUT / "404.html"
    home_href = rel_href(output_file, OUTPUT / HOME_PAGE)
    all_docs_href = rel_href(output_file, OUTPUT / ALL_DOCS_PAGE)
    body_html = f"""
<h1>Page not found</h1>
<p>This page does not exist in the current Pages build.</p>
<p><a href="{home_href}">Go back to the OS Index</a> or <a href="{all_docs_href}">browse all docs</a>.</p>
""".strip()
    output_file.write_text(render_shell("Page not found", body_html, output_file, "Generated fallback"), encoding="utf-8")


def main() -> None:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)

    OUTPUT.mkdir(parents=True)
    (OUTPUT / "assets").mkdir(parents=True, exist_ok=True)
    (OUTPUT / ".nojekyll").write_text("", encoding="utf-8")
    (OUTPUT / "assets" / "site.css").write_text(SITE_CSS + "\n", encoding="utf-8")

    sources = collect_sources()
    pages = [
        Page(
            source=source,
            relative_source=source.relative_to(ROOT),
            output=to_output_path(source.relative_to(ROOT)),
            title=extract_title(source.read_text(encoding="utf-8"), source.stem),
        )
        for source in sources
    ]

    for page in pages:
        build_page(page)

    build_landing_page(LANDING_SOURCE)
    build_all_docs_page(pages)
    build_404_page()

    print(f"Built {len(pages)} pages into {OUTPUT}")


if __name__ == "__main__":
    main()
