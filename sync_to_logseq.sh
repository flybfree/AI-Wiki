#!/bin/bash
# sync_to_logseq.sh - Mirror AI Research wiki to Logseq pages
# This script COPIES (never moves/deletes) files from wiki to logseq
# Wiki remains source of truth
# Duplicate page titles are de-duped by keeping one canonical file per title.

set -euo pipefail

# Paths
WIKI_SOURCE="/home/rich/wiki/ai-research/raw"
LOGSEQ_TARGET="/home/rich/logseq-brain/pages/ai-research"

export WIKI_SOURCE LOGSEQ_TARGET

python3 - <<'PY'
from pathlib import Path
from collections import defaultdict
import os
import re
import shutil

WIKI_ROOT = Path("/home/rich/wiki/ai-research")
WIKI_SOURCE = WIKI_ROOT / "raw"
LOGSEQ_TARGET = Path(os.environ["LOGSEQ_TARGET"])


def get_wiki_dir(section: str) -> Path:
    """Return the wiki directory to scan for a given section name.

    'comparisons', 'concepts', 'entities' live as subdirectories of
    WIKI_ROOT (not inside raw/). Everything else lives under
    WIKI_SOURCE/section.
    """
    non_raw = {"comparisons", "concepts", "entities"}
    if section in non_raw:
        return WIKI_ROOT / section
    return WIKI_SOURCE / section


SECTIONS = ["articles", "comparisons", "concepts", "entities", "papers", "summaries", "transcripts"]

# Top-level wiki files that should be synced to Logseq root
WIKI_ROOT_PAGES = [
    "ilya-sutskever-reading-list.md",
    "ilya-sutskever-reading-list-study-order.md",
    "wiki-landing-page.md",
    "wiki-topic-index.md",
    "ai-ml-foundations-landing-page.md",
    "ai-ml-foundations-syllabus.md",
    "ai-ml-foundations-course-map.md",
    "ai-ml-foundations-edit-plan.md",
]

# Course lesson files (glob pattern, synced separately)
def get_lesson_files():
    """Return list of ai-ml-foundations-lesson-*.md files from wiki root."""
    root = Path("/home/rich/wiki/ai-research")
    return sorted([f.name for f in root.glob("ai-ml-foundations-lesson-*.md") if f.is_file()])


def extract_title(path: Path) -> str:
    text = path.read_text(errors="ignore").splitlines()
    if text and text[0].strip() == "---":
        for i in range(1, min(len(text), 80)):
            line = text[i]
            if line.strip() == "---":
                break
            m = re.match(r"^title:\s*(.*)$", line.strip())
            if m:
                return m.group(1).strip().strip('"\'')
    for line in text[:60]:
        m = re.match(r"^#\s+(.+?)\s*$", line)
        if m:
            return m.group(1).strip()
    return path.stem


def date_key(path: Path):
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", path.name)
    if m:
        return tuple(map(int, m.groups()))
    return (0, 0, 0)


def canonical_choice(paths):
    return max(paths, key=lambda p: (date_key(p), p.stat().st_mtime_ns, p.name))


def prune_empty_dirs(base: Path):
    if not base.exists():
        return
    for path in sorted((p for p in base.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
        try:
            path.rmdir()
        except OSError:
            pass


def sync_section(section: str):
    src_dir = get_wiki_dir(section)
    dst_dir = LOGSEQ_TARGET / section

    if not src_dir.exists():
        print(f"SKIP: {section} directory not found at {src_dir}")
        return

    print(f"Syncing {section}: {src_dir} -> {dst_dir}")
    src_files = [p for p in src_dir.rglob("*.md") if p.is_file()]
    by_title = defaultdict(list)
    for path in src_files:
        by_title[extract_title(path)].append(path)

    canonical = {canonical_choice(paths) for paths in by_title.values()}
    canonical_rels = {p.relative_to(src_dir) for p in canonical}

    dst_dir.mkdir(parents=True, exist_ok=True)

    deleted = 0
    new_count = 0
    updated_count = 0
    unchanged_count = 0
    skipped_duplicates = len(src_files) - len(canonical)

    if dst_dir.exists():
        for dst_file in sorted(dst_dir.rglob("*.md")):
            rel = dst_file.relative_to(dst_dir)
            if rel not in canonical_rels:
                dst_file.unlink()
                deleted += 1
                print(f"  DELETED: {rel}")

    for src_file in sorted(canonical):
        rel_path = src_file.relative_to(src_dir)
        dst_file = dst_dir / rel_path
        dst_file.parent.mkdir(parents=True, exist_ok=True)

        if not dst_file.exists():
            shutil.copy2(src_file, dst_file)
            new_count += 1
            print(f"  NEW: {rel_path}")
            continue

        if src_file.read_bytes() != dst_file.read_bytes():
            shutil.copy2(src_file, dst_file)
            updated_count += 1
            print(f"  UPDATED: {rel_path}")
        else:
            unchanged_count += 1

    prune_empty_dirs(dst_dir)
    print(f"  canonical files: {len(canonical)}")
    print(f"  skipped duplicates: {skipped_duplicates}")
    print(f"  deleted stale: {deleted}")
    print(f"  {new_count} new, {updated_count} updated, {unchanged_count} unchanged\n")


for section in SECTIONS:
    sync_section(section)

# Sync top-level wiki pages to Logseq root
print("Syncing wiki root pages to Logseq:")
wiki_root = WIKI_ROOT
logseq_root = LOGSEQ_TARGET
root_synced = 0
for fname in WIKI_ROOT_PAGES + get_lesson_files():
    src = wiki_root / fname
    dst = logseq_root / fname
    if src.exists():
        if not dst.exists() or src.read_bytes() != dst.read_bytes():
            shutil.copy2(src, dst)
            root_synced += 1
            print(f"  {'UPDATED' if dst.exists() else 'NEW'}: {fname}")
        else:
            print(f"  unchanged: {fname}")
    else:
        print(f"  MISSING: {fname}")
print(f"  root pages synced: {root_synced}\n")

print("\n=== Sync complete ===")
PY
