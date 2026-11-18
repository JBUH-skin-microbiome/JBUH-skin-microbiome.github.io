from __future__ import annotations

import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BIB_PATH = ROOT / "_bibliography" / "papers.bib"
OUTPUT_DIR = ROOT / "_includes" / "publications"
MEMBER_OUTPUT_DIR = ROOT / "_includes" / "member-publications"
MEMBER_DIR = ROOT / "_members"
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


def load_member_aliases() -> tuple[dict[str, dict[str, str]], dict[str, list[str]]]:
    """Load exact BibTeX author aliases from member front matter."""
    alias_map: dict[str, dict[str, str]] = {}
    aliases_by_slug: dict[str, list[str]] = {}
    for path in sorted(MEMBER_DIR.glob("*.md")):
        source = path.read_text(encoding="utf-8")
        front_matter = source.split("---", 2)[1] if source.startswith("---") else ""
        names_match = re.search(r"^publication_names:\s*(\[.*\])\s*$", front_matter, re.M)
        if not names_match:
            continue
        aliases = json.loads(names_match.group(1))
        name_match = re.search(r"^name_en:\s*(.+?)\s*$", front_matter, re.M)
        member = {
            "slug": path.stem,
            "name": name_match.group(1).strip() if name_match else path.stem,
            "url": f"/members/{path.stem}/",
        }
        aliases_by_slug[path.stem] = aliases
        for alias in aliases:
            if alias in alias_map:
                raise ValueError(f"Duplicate publication alias: {alias}")
            alias_map[alias] = member
    return alias_map, aliases_by_slug


def display_authors(value: str, alias_map: dict[str, dict[str, str]]) -> str:
    names = []
    for author in value.split(" and "):
        canonical = author.strip()
        if "," in canonical:
            last, first = [part.strip() for part in canonical.split(",", 1)]
            label = f"{first} {last}"
        else:
            label = canonical
        escaped = html.escape(label)
        member = alias_map.get(canonical)
        if member:
            url = html.escape(member["url"], quote=True)
            member_name = html.escape(member["name"], quote=True)
            escaped = (
                f'<a class="member-author-link" href="{url}" '
                f'aria-label="{member_name} member profile"><strong>{escaped}</strong></a>'
            )
        names.append(escaped)
    return ", ".join(names)


def render_entry(entry: dict[str, str], alias_map: dict[str, dict[str, str]]) -> str:
    title = html.escape(entry.get("title", ""))
    authors = display_authors(entry.get("author", ""), alias_map)
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
    alias_map, aliases_by_slug = load_member_aliases()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for year in YEARS:
        selected = [entry for entry in entries if entry.get("year") == str(year)]
        rendered = ["<!-- Generated from _bibliography/papers.bib. -->", '<ol class="bibliography">']
        rendered.extend(render_entry(entry, alias_map) for entry in selected)
        rendered.append("</ol>")
        (OUTPUT_DIR / f"articles-{year}.html").write_text("\n".join(rendered) + "\n", encoding="utf-8")

    MEMBER_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for slug, aliases in aliases_by_slug.items():
        selected = [
            entry
            for entry in entries
            if any(author.strip() in aliases for author in entry.get("author", "").split(" and "))
        ]
        rendered = [
            "<!-- Generated from _bibliography/papers.bib and member publication_names. -->",
            '<section class="member-publications publication-catalog">',
            "  <h2>Publications</h2>",
        ]
        for year in YEARS:
            year_entries = [entry for entry in selected if entry.get("year") == str(year)]
            if not year_entries:
                continue
            rendered.extend([f'  <h3 class="publication-year">{year}</h3>', '  <ol class="bibliography">'])
            rendered.extend(render_entry(entry, alias_map) for entry in year_entries)
            rendered.append("  </ol>")
        rendered.extend(
            [
                '  <p class="member-publications-all"><a href="/publications/">View all publications →</a></p>',
                "</section>",
            ]
        )
        (MEMBER_OUTPUT_DIR / f"{slug}.html").write_text("\n".join(rendered) + "\n", encoding="utf-8")

    print(
        f"Generated {len(entries)} publication entries across {len(YEARS)} year files "
        f"and {len(aliases_by_slug)} member files."
    )


if __name__ == "__main__":
    main()
