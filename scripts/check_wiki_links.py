#!/usr/bin/env python3
"""Audit source-wiki wikilinks without counting the Logseq mirror or metadata examples."""
from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
TITLE_RE = re.compile(r"^title:\s*[\"']?(.+?)[\"']?\s*$", re.M)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)


def page_title(text: str, path: Path) -> str:
    match = TITLE_RE.search(text)
    if match:
        return match.group(1).strip("\"'").strip().lower()
    match = H1_RE.search(text)
    return match.group(1).strip().lower() if match else path.stem.lower()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wiki", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--sample", type=int, default=25)
    args = parser.parse_args()
    root = args.wiki.resolve()
    pages = [p for p in root.rglob("*.md") if "logseq-brain" not in p.parts and ".git" not in p.parts]

    titles: dict[str, list[Path]] = defaultdict(list)
    for path in pages:
        title = page_title(path.read_text(encoding="utf-8", errors="replace"), path)
        titles[title].append(path)
        if title.startswith("summary: "):
            titles[title.removeprefix("summary: ").strip()].append(path)

    unresolved_path: list[tuple[Path, str]] = []
    unresolved_title: list[tuple[Path, str]] = []
    ambiguous: list[tuple[Path, str, int]] = []
    links = 0

    for path in pages:
        text = path.read_text(encoding="utf-8", errors="replace")
        if path.name == "SCHEMA.md":
            continue
        for raw in WIKILINK_RE.findall(text):
            target = raw.split("|", 1)[0].strip()
            if path.name == "page-templates.md" or target.startswith(("<", "http://", "https://")):
                continue
            if re.fullmatch(r"[0-9≤, ]+", target) or target == "prototype":
                continue
            links += 1
            candidates = [
                (path.parent / target).resolve(),
                (path.parent / f"{target}.md").resolve(),
                (root / target).resolve(),
                (root / f"{target}.md").resolve(),
            ]
            if any(candidate.is_file() for candidate in candidates):
                continue
            matches = titles.get(target.lower(), [])
            if not matches and target.lower().endswith(".md"):
                matches = titles.get(Path(target).stem.lower(), [])
            if len(matches) == 1:
                continue
            if len(matches) > 1:
                ambiguous.append((path, target, len(matches)))
            elif "/" in target or target.endswith(".md") or target.startswith("/"):
                unresolved_path.append((path, target))
            else:
                unresolved_title.append((path, target))

    print(f"Pages scanned: {len(pages)}")
    print(f"Wikilinks scanned: {links}")
    print(f"Unresolved path-like links: {len(unresolved_path)}")
    print(f"Unresolved title-like links: {len(unresolved_title)}")
    print(f"Ambiguous title links: {len(ambiguous)}")
    for label, rows in (("PATH", unresolved_path), ("TITLE", unresolved_title)):
        print(f"\n{label} samples:")
        for source, target in rows[: args.sample]:
            print(f"- {source.relative_to(root)} -> {target}")
    print("\nAMBIGUOUS samples:")
    for source, target, count in ambiguous[: args.sample]:
        print(f"- {source.relative_to(root)} -> {target} ({count} matches)")
    return 1 if unresolved_path or unresolved_title or ambiguous else 0


if __name__ == "__main__":
    raise SystemExit(main())
