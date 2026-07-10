#!/usr/bin/env python3
"""Find the newest model article, generate its release block, and append it to the tracker.

Usage:
  python3 tools/append_latest_llm_release.py
  python3 tools/append_latest_llm_release.py --dry-run
  python3 tools/append_latest_llm_release.py --tracker concepts/llm-models/2026-07-10_LLMReleaseTracker.md
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from llm_release_block import build_article_data, render_template

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TRACKER = ROOT / "concepts" / "llm-models" / "2026-07-10_LLMReleaseTracker.md"
ARTICLE_DIRS = [ROOT / "raw" / "articles", ROOT / "articles"]
SUMMARY_DIRS = [ROOT / "entities" / "article", ROOT / "raw" / "summaries"]
MODEL_HINTS = (
    "llm",
    "model",
    "models",
    "release",
    "releases",
    "benchmark",
    "reasoning",
    "coding",
    "multimodal",
    "openai",
    "anthropic",
    "google",
    "deepseek",
    "qwen",
    "llama",
    "gemini",
    "mistral",
    "gemma",
    "glm",
    "kimi",
    "phi",
    "aiupdates",
)

DATE_BLOCK_RE = re.compile(r"^###\s+\d{4}-\d{2}-\d{2}\s+-\s+", re.M)


def iter_articles() -> list[Path]:
    files: list[Path] = []
    for base in ARTICLE_DIRS:
        if base.exists():
            files.extend(p for p in base.glob("*.md") if p.is_file())
    files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return files


def article_score(path: Path) -> tuple[int, str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    haystack = f"{path.name}\n{text[:3000]}".lower()
    score = sum(1 for hint in MODEL_HINTS if hint in haystack)
    # Prefer actual model-release style titles when scores tie.
    title_bias = 1 if re.search(r"(?i)(llm|model|release|benchmark|multimodal|reasoning|coding)", haystack) else 0
    return score + title_bias, haystack


def choose_newest_model_article() -> Path:
    best_path: Path | None = None
    best_key: tuple[int, float] | None = None

    for path in iter_articles():
        try:
            score, _ = article_score(path)
        except OSError:
            continue
        if score <= 0:
            continue
        key = (score, path.stat().st_mtime)
        if best_key is None or key > best_key:
            best_key = key
            best_path = path

    if best_path is None:
        raise FileNotFoundError("No model-related article found in raw/articles or articles")
    return best_path


def find_summary(article_path: Path) -> Path | None:
    stem = article_path.stem
    candidates = [
        *[d / f"{stem}_summary.md" for d in SUMMARY_DIRS],
        *[d / f"Summary_{stem}.md" for d in SUMMARY_DIRS],
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def insert_block(tracker_text: str, block: str) -> str:
    match = DATE_BLOCK_RE.search(tracker_text)
    if match:
        insert_at = match.start()
        return tracker_text[:insert_at] + block.rstrip() + "\n\n" + tracker_text[insert_at:]

    marker = "## Practical shortlist"
    idx = tracker_text.find(marker)
    if idx != -1:
        return tracker_text[:idx] + block.rstrip() + "\n\n" + tracker_text[idx:]

    return tracker_text.rstrip() + "\n\n" + block.rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Append the newest model article to the LLM Release Tracker.")
    parser.add_argument("--tracker", default=str(DEFAULT_TRACKER), help="Tracker file to update")
    parser.add_argument("--dry-run", action="store_true", help="Print the generated block and do not edit files")
    args = parser.parse_args()

    tracker = Path(args.tracker)
    if not tracker.exists():
        print(f"ERROR: tracker not found: {tracker}", file=sys.stderr)
        return 1

    article = choose_newest_model_article()
    summary = find_summary(article)
    data = build_article_data(str(article), str(summary) if summary else None)
    block = render_template(data)

    if args.dry_run:
        sys.stdout.write(f"# Selected article: {article}\n")
        if summary:
            sys.stdout.write(f"# Summary: {summary}\n")
        sys.stdout.write(block)
        if not block.endswith("\n"):
            sys.stdout.write("\n")
        return 0

    original = tracker.read_text(encoding="utf-8")
    updated = insert_block(original, block)
    if updated == original:
        print("No change made; tracker already appears up to date.", file=sys.stderr)
        return 2

    tracker.write_text(updated, encoding="utf-8")
    print(f"Appended {article.name} to {tracker}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
