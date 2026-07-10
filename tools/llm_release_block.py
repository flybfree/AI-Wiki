#!/usr/bin/env python3
"""Generate the next dated release block for the LLM Release Tracker.

Usage examples:
  python3 tools/llm_release_block.py path/to/raw/article.md
  python3 tools/llm_release_block.py https://example.com/article
  python3 tools/llm_release_block.py path/to/raw/article.md --summary path/to/summary.md

The script prints a markdown block that can be pasted into the tracker.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.error import URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "templates" / "llm_release_block.md"
DEFAULT_FOLLOW_UP = "Add the next dated block when a newer article lands."

MODEL_PATTERNS = [
    r"GPT-5(?:\.5)?(?:\s+Thinking|\s+Pro)?",
    r"Claude Opus\s+4(?:\.7)?",
    r"Gemini\s+3(?:\.5)?\s+Flash",
    r"Gemini\s+3\.1\s+Pro",
    r"DeepSeek\s+V4(?:\s+Pro|\s+Flash)?",
    r"Qwen\s+3(?:\.7|\.6)?(?:-Plus|\s+Max)?",
    r"Llama\s+4\s+(?:Scout|Maverick)",
    r"Gemma\s+4(?:\s+\d+B(?:\s+(?:MoE|Dense|Unified))?)?",
    r"GLM-5(?:\.1)?",
    r"Mistral\s+Large\s+3",
    r"Kimi\s+K2\.6",
    r"Arcee\s+Trinity",
    r"Phi-4\s+Mini",
    r"DiffusionGemma\s+26B-A4B-it",
    r"Harness-1",
]


@dataclass
class ArticleData:
    title: str
    source_url: str
    date: str
    summary_text: str = ""
    article_text: str = ""


def read_text_source(source: str) -> str:
    path = Path(source)
    if path.exists():
        return path.read_text(encoding="utf-8")

    req = Request(source, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=20) as resp:
        raw = resp.read()
        charset = resp.headers.get_content_charset() or "utf-8"
    return raw.decode(charset, errors="replace")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    lines = text.splitlines()
    data: dict[str, str] = {}
    in_frontmatter = False
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip().lower()
        value = value.strip().strip('"').strip("'")
        data[key] = value
    return data


def html_title(text: str) -> str | None:
    m = re.search(r"<meta[^>]+property=['\"]og:title['\"][^>]+content=['\"]([^'\"]+)['\"]", text, re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip()
    return None


def slug_to_title(source: str) -> str:
    base = source.rstrip("/").split("/")[-1]
    base = re.sub(r"\.(md|html?|php)$", "", base, flags=re.I)
    base = base.replace("-", " ").replace("_", " ")
    base = re.sub(r"\s+", " ", base).strip()
    return base.title() or "Untitled"


def extract_summary_text(text: str) -> str:
    if not text:
        return ""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            body = parts[2]
        else:
            body = text
    else:
        body = text

    # Prefer explicit summary-ish sections.
    section_markers = [
        r"(?im)^##+\s*Summary\s*$",
        r"(?im)^Summary\s*$",
        r"(?im)^##+\s*Overview\s*$",
        r"(?im)^Overview\s*$",
        r"(?im)^##+\s*What Changed in 2026\s*$",
        r"(?im)^What Changed in 2026\s*$",
        r"(?im)^##+\s*Quick answer\s*$",
        r"(?im)^Quick answer\s*$",
        r"(?im)^##+\s*Quick Reference.*$",
        r"(?im)^Quick Reference.*$",
    ]
    for marker in section_markers:
        m = re.search(marker, body)
        if m:
            tail = body[m.end():]
            paragraphs = [p.strip() for p in re.split(r"\n\s*\n", tail) if p.strip()]
            for para in paragraphs:
                candidate = clean_candidate(para)
                if candidate:
                    return candidate

    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    for para in paragraphs:
        candidate = clean_candidate(para)
        if candidate:
            return candidate
    return ""


def clean_candidate(text: str) -> str:
    if not text:
        return ""
    stripped = re.sub(r"<[^>]+>", "", text)
    stripped = re.sub(r"\s+", " ", stripped).strip()
    if not stripped:
        return ""
    if stripped.startswith(("#", "-", "---", "ERROR", "Log in", "Sign Up", "Compare")):
        return ""
    if len(stripped) < 60 and stripped.count(".") == 0:
        return ""
    return squeeze_sentences(stripped)


def squeeze_sentences(text: str, max_sentences: int = 2) -> str:
    cleaned = re.sub(r"\[[^\]]*\]\([^)]*\)", "", text)
    cleaned = re.sub(r"<[^>]+>", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    parts = re.split(r"(?<=[.!?])\s+", cleaned)
    result = " ".join(parts[:max_sentences]).strip()
    return result


def infer_models(text: str) -> str:
    found: list[str] = []
    for pattern in MODEL_PATTERNS:
        for match in re.finditer(pattern, text, flags=re.I):
            candidate = re.sub(r"\s+", " ", match.group(0)).strip()
            if candidate.lower() not in {x.lower() for x in found}:
                found.append(candidate)
    return ", ".join(found) if found else "TBD"


def choose_title(meta: dict[str, str], fallback_source: str, text: str) -> str:
    for key in ("title", "og:title", "headline"):
        if key in meta and meta[key].strip():
            return meta[key].strip()
    html = html_title(text)
    if html:
        return html
    return slug_to_title(fallback_source)


def choose_source_url(source_arg: str, meta: dict[str, str]) -> str:
    for key in ("source_url", "source", "url"):
        value = meta.get(key, "").strip()
        if value:
            return value
    return source_arg


def choose_date(meta: dict[str, str]) -> str:
    for key in ("date", "updated", "published", "scraped"):
        value = meta.get(key, "").strip()
        if value:
            return value.split()[0].strip('"')
    return "YYYY-MM-DD"


def render_template(data: ArticleData) -> str:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    summary = data.summary_text or ""
    why = squeeze_sentences(summary, 1) if summary else "TBD"
    current_take = squeeze_sentences(summary, 2) if summary else "TBD"
    follow_up = DEFAULT_FOLLOW_UP
    rendered = (
        template
        .replace("{{DATE}}", data.date)
        .replace("{{LABEL}}", data.title)
        .replace("{{TITLE}}", data.title)
        .replace("{{SOURCE_URL}}", data.source_url)
        .replace("{{MODELS}}", infer_models(" ".join(filter(None, [data.title, data.summary_text, data.article_text]))))
        .replace("{{WHY}}", why)
        .replace("{{CURRENT_TAKE}}", current_take)
        .replace("{{FOLLOW_UP}}", follow_up)
    )
    return rendered


def build_article_data(source: str, summary_source: str | None = None) -> ArticleData:
    article_text = read_text_source(source)
    article_meta = parse_frontmatter(article_text)
    title = choose_title(article_meta, source, article_text)
    source_url = choose_source_url(source, article_meta)
    date = choose_date(article_meta)

    summary_text = ""
    if summary_source:
        try:
            summary_text = extract_summary_text(read_text_source(summary_source))
        except Exception:
            summary_text = ""
    if not summary_text:
        summary_text = extract_summary_text(article_text)

    return ArticleData(title=title, source_url=source_url, date=date, summary_text=summary_text, article_text=article_text)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a dated LLM release log block from an article file or URL.")
    parser.add_argument("article", help="Path or URL to the new article")
    parser.add_argument("--summary", help="Optional path or URL to a companion summary")
    args = parser.parse_args(argv)

    try:
        data = build_article_data(args.article, args.summary)
        sys.stdout.write(render_template(data))
        if not sys.stdout.isatty():
            sys.stdout.write("\n")
        return 0
    except (OSError, URLError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
