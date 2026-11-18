from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BIB_PATH = ROOT / "_bibliography" / "papers.bib"
OUTPUT_DIR = ROOT / "_includes" / "publications"
YEARS = (2026, 2025, 2024, 2023, 2022, 2021)


def parse_entries(source: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for match in re.finditer(r"@(?P<kind>\w+)\{(?P<key>[^,]+),(?P<body>.*?)(?=\n\}\s*(?:\n@|\Z))", source, re.S):
        entry = {"kind": match.group("kind"), "key": match.group("key").strip()}
        body = match.group("body")
        for field in re.finditer(r"^\s*(\w+)\s*=\s*\{(.*?)\}\s*,?\s*$", body, re.M):
            entry[field.group(1).lower()] = field.group(2).strip()
        entries.append(entry)
    return entries


def display_authors(value: str) -> str:
    names = []
    for author in value.split(" and "):
        if "," in author:
            last, first = [part.strip() for part in author.split(",", 1)]
            label = f"{first} {last}"
        else:
            label = author.strip()
        escaped = html.escape(label)
        if label in {"J Park", "J. Park", "KH Nam", "K.H. Nam", "SY Kim", "S.Y. Kim"}:
            escaped = f"<strong>{escaped}</strong>"
        names.append(escaped)
    return ", ".join(names)


def render_entry(entry: dict[str, str]) -> str:
    title = html.escape(entry.get("title", ""))
    authors = display_authors(entry.get("author", ""))
    journal = html.escape(entry.get("journal", ""))
    year = html.escape(entry.get("year", ""))
    note = html.escape(entry.get("note", ""))
    abbr = html.escape(entry.get("abbr", "Article"))
    doi = entry.get("doi", "")
    web = entry.get("html", "")
    citation = ", ".join(part for part in (f"<em>{journal}</em>" if journal else "", year) if part)
    bib = html.escape(
        "@{kind}{{{key},\n  title = {{{title}}},\n  author = {{{author}}},\n  journal = {{{journal}}},\n  year = {{{year}}}\n}}".format(
            kind=entry.get("kind", "article"),
            key=entry.get("key", "reference"),
            title=entry.get("title", ""),
            author=entry.get("author", ""),
            journal=entry.get("journal", ""),
            year=entry.get("year", ""),
        )
    )
    links = []
    if doi:
        links.append(f'<a class="btn btn-sm z-depth-0" href="https://doi.org/{html.escape(doi, quote=True)}">DOI</a>')
    elif web:
        links.append(f'<a class="btn btn-sm z-depth-0" href="{html.escape(web, quote=True)}">Website</a>')
    links.append(
        '<details class="bibtex-details"><summary class="btn btn-sm z-depth-0">Bib</summary>'
        f'<pre>{bib}</pre></details>'
    )
    note_html = f'<div class="periodical publication-note">{note}</div>' if note else ""
    return "\n".join(
        [
            "  <li>",
            '    <div class="row">',
            f'      <div class="col-sm-2 abbr"><abbr class="badge">{abbr}</abbr></div>',
            '      <div class="col-sm-10">',
            f'        <div class="title">{title}</div>',
            f'        <div class="author">{authors}</div>',
            f'        <div class="periodical">{citation}</div>',
            f"        {note_html}" if note_html else "",
            f'        <div class="links">{" ".join(links)}</div>',
            "      </div>",
            "    </div>",
            "  </li>",
        ]
    ).replace("\n\n", "\n")


def main() -> None:
    entries = parse_entries(BIB_PATH.read_text(encoding="utf-8"))
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for year in YEARS:
        selected = [entry for entry in entries if entry.get("year") == str(year)]
        rendered = ["<!-- Generated from _bibliography/papers.bib. -->", '<ol class="bibliography">']
        rendered.extend(render_entry(entry) for entry in selected)
        rendered.append("</ol>")
        (OUTPUT_DIR / f"articles-{year}.html").write_text("\n".join(rendered) + "\n", encoding="utf-8")
    print(f"Generated {len(entries)} publication entries across {len(YEARS)} year files.")


if __name__ == "__main__":
    main()
