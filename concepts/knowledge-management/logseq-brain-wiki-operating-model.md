---
title: "Logseq Brain & Wiki Operating Model"
created: 2026-07-14
updated: 2026-07-14
type: concept
tags: [wiki, logseq, knowledge-management, navigation, infrastructure]
sources: ["https://github.com/flybfree/AI-Wiki/wiki"]
confidence: high
---

# Logseq Brain & Wiki Operating Model

**Source**: [GitHub Wiki](https://github.com/flybfree/AI-Wiki/wiki)

This page defines how the AI Research wiki and the Logseq brain should work together:
- the **wiki** is the curated, user-facing reference system
- the **Logseq brain** is the assistant-facing mirror for fast retrieval and graph use
- the **GitHub wiki** is the canonical copy Rich actually uses
- the local copy under `/home/rich/wiki/ai-research/` is the working clone Hermes edits

## Core principle

If the GitHub wiki and the local mirror disagree, the **GitHub wiki wins** for user-facing content.
The local Logseq mirror exists so Hermes and Logseq can read and navigate the same material quickly.

## Storage map

| Component | Canonical location | What belongs there |
|---|---|---|
| GitHub wiki | `https://github.com/flybfree/AI-Wiki/wiki` | The published wiki Rich actually uses |
| Local wiki working copy | `/home/rich/wiki/ai-research/` | Source files Hermes edits before pushing |
| Logseq mirror | `/home/rich/logseq-brain/pages/ai-research/` | Synced copy for Logseq graph use and assistant retrieval |
| SMB mirror / backup | `192.168.3.62/share` | Shared mirror for accessibility and backup workflows |
| Raw articles | `raw/articles/` | Immutable article captures |
| Raw papers | `raw/papers/` | Immutable paper captures |
| Raw summaries | `raw/summaries/` | Historical summary outputs and legacy summary files |
| Curated article entities | `entities/article/` | Clean summary pages for article-style sources |
| Curated concepts | `concepts/` | Durable concept pages and topic explainers |
| Comparisons | `comparisons/` | Side-by-side analyses and tradeoff pages |
| Navigation pages | `index.md`, `wiki-topic-index.md`, `wiki-landing-page.md` | Curated entry points and browse maps |
| Activity log | `log.md` | Append-only record of ingest, update, and maintenance actions |
| Processing state | `processed_files.log`, `summarized_files.log`, `analyzed_files.log` | Deduplication and pipeline bookkeeping |
| Lookup/index data | `wiki_search_data.json`, `wiki_log_data.json` | Search and catalog support data |

## What each layer is for

### 1. Raw source layer
Raw pages are the evidence store.
They should be treated as immutable once captured.

Examples:
- article snapshots in `raw/articles/`
- paper snapshots in `raw/papers/`
- older summary captures in `raw/summaries/`

### 2. Curated knowledge layer
Curated pages explain, connect, and interpret.
They should be rewritten when the understanding improves.

Examples:
- concept pages for durable ideas
- entity/article summary pages for source-specific takeaways
- comparison pages for tradeoff analysis

### 3. Navigation layer
Navigation pages should help a human or assistant find the right page quickly.
They should stay concise and should not become dumping grounds.

Examples:
- `index.md`
- `wiki-topic-index.md`
- `wiki-landing-page.md`

### 4. Operational layer
Operational files track how content moves through the system.
They are useful for debugging and maintenance, but they are not reference content.

Examples:
- `log.md`
- `processed_files.log`
- `summarized_files.log`
- `analyzed_files.log`
- maintenance scripts and audit reports

## How data should flow

1. Capture or ingest source material into the raw layer.
2. Create or update a curated page with a visible source link.
3. Add cross-links from related concept and navigation pages.
4. Push the local wiki working copy to GitHub.
5. Sync the wiki into the Logseq mirror.
6. Reindex / refresh Logseq if needed.
7. Run maintenance checks for duplicates, broken links, and missing summaries.

## Design rules for the wiki

- Keep source material separate from interpretation.
- Use concept pages for durable ideas, not just source summaries.
- Put visible source links in the rendered page body, not only in frontmatter.
- Prefer one canonical page per idea.
- Use navigation pages only for curated discovery.
- If a page is for learning, make it explain the idea plainly.
- If a page is for reference, make it easy to scan and cite.

## Design rules for the Logseq mirror

- Treat it as a synced working graph, not the canonical publication layer.
- Keep titles unique enough to avoid Logseq collisions.
- Preserve the same content structure as the source wiki where possible.
- Use the mirror for fast graph navigation and assistant retrieval.

## What I should optimize for

When Hermes answers questions from this system, it should:

- prefer the GitHub wiki as the authoritative user-facing copy
- use the local working copy for edits and verification
- rely on curated pages for synthesis
- fall back to raw pages only for provenance or source checking
- avoid inventing new pages when a concept already exists
- keep navigation pages clean and short

## Good page shape

A strong knowledge page usually has:

- a clear title
- a short summary at the top
- visible source links
- definitions for first-use terms
- concrete examples
- tradeoffs or caveats
- related pages
- a stable place in the navigation graph

## Related pages

- [[wiki-landing-page.md|AI Research Wiki — Landing Page]]
- [[wiki-topic-index.md|AI Research Wiki — Topic Index]]
- [[index.md|AI Research Wiki Index]]
- [[SCHEMA.md|Wiki Schema: AI Research]]
