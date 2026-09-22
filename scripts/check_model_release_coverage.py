#!/usr/bin/env python3
"""Check whether high-signal model releases appear in recent AI briefings."""
from __future__ import annotations

import argparse
import json
import re
from datetime import date, timedelta
from pathlib import Path


def briefing_text(text: str) -> str:
    """Ignore the QA checklist itself; it must not satisfy its own gate."""
    return re.split(r"\n## Model Release Coverage Check\n", text, maxsplit=1)[0]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wiki", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--days", type=int, default=10)
    args = parser.parse_args()

    config = json.loads((args.wiki / "config/model-release-watchlist.json").read_text())
    today = date.today()
    corpus = []
    for day_delta in range(args.days):
        day = today - timedelta(days=day_delta)
        for pattern in (
            f"concepts/ai-trends/daily-ai-intelligence-summary-{day}.md",
            f"concepts/ai-trends/daily-ai-intelligence-blog-{day}.md",
        ):
            path = args.wiki / pattern
            if path.exists():
                corpus.append((path, path.read_text(encoding="utf-8", errors="replace")))

    print(f"Corpus files: {len(corpus)}")
    failures = 0
    for release in config["releases"]:
        aliases = release["aliases"]
        found = [str(path.relative_to(args.wiki)) for path, text in corpus
                 if any(re.search(re.escape(alias), briefing_text(text), flags=re.IGNORECASE) for alias in aliases)]
        status = "covered" if found else "MISSING"
        if not found:
            failures += 1
        print(f"{status:8} | {release['name']:18} | released {release['release_date']} | {', '.join(found[:3])}")

    print(f"Missing releases: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
