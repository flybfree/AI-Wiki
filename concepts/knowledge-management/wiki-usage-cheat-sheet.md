---
title: "Wiki Usage Cheat Sheet"
created: 2026-07-15
updated: 2026-07-27
type: concept
tags: [wiki, logseq, knowledge-management, navigation]
sources: ["https://github.com/flybfree/AI-Wiki/wiki"]
confidence: high
---

# Wiki Usage Cheat Sheet

**Source**: [GitHub Wiki](https://github.com/flybfree/AI-Wiki/wiki)

## Semantic links
- [[concepts/knowledge-management/logseq-brain-wiki-operating-model.md|Logseq Brain & Wiki Operating Model]] — 1 title term overlap; shared tags: knowledgemanagement, logseq, navigation; 4 backlinks
- [[concepts/knowledge-management/page-templates.md|Page Templates for the AI Research Wiki]] — 1 title term overlap; shared tags: knowledgemanagement, logseq, navigation; 4 backlinks
- [[concepts/knowledge-management/ai-research-concept-map.md|AI Research Concept Map]] — shared tags: navigation; 3 backlinks; 1 summary/topic term overlap

## What goes where

| Page type | Folder | Use for | Rules |
|---|---|---|---|
| Concepts | `concepts/` | Durable explanations of ideas | Write for reuse, not one-off source notes | Semantic links should point here first |
| Article summaries | `entities/article/` | Source-specific article takeaways | Include a visible **Source** link in the body |
| Paper notes | `papers/` | Academic paper analysis | Include a visible **Original Paper** link |
| Summary pages | `summaries/` or `_summary.md` | Generated or derived summaries | Prefix visible titles with `Summary:` when needed |
| Comparisons | `comparisons/` | Side-by-side tradeoff pages | Make the comparison explicit in the title |
| Tutorials | `tutorials/` | Step-by-step workflows | Optimize for action, not theory |
| Raw sources | `raw/` | Immutable captures | Do not hand-edit raw files |
| Navigation pages | `index.md`, `wiki-topic-index.md`, `wiki-landing-page.md`, `SCHEMA.md` | Browse maps and conventions | Keep short and curated |

## Where each system is for

| System | Purpose |
|---|---|
| Local wiki `~/wiki/ai-research/` | Edit working copy for wiki content |
| GitHub wiki | Published user-facing version |
| Local logseq-brain `~/logseq-brain/pages/ai-research/` | Curated graph mirror for Logseq and assistant retrieval |
| SMB backup | Safety copy / recovery mirror |
| PRISM `~/logseq-brain` | Fast-access Logseq mirror |

## Practical rule of thumb

- **Need to write or fix content?** → local wiki
- **Need to browse the graph?** → local logseq-brain or PRISM logseq-brain
- **Need the published version?** → GitHub wiki
- **Need backup?** → SMB
- **Need PRISM fast access?** → PRISM logseq-brain only
- **Need provenance?** → raw wiki pages, not duplicated Logseq copies

## One-line rule

**Author in the local wiki, publish to GitHub, mirror curated pages to logseq-brain for graph use, back up via SMB, and use PRISM only as a fast Logseq mirror. Semantic links should identify concepts first; structural links should follow.**
