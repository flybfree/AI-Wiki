---
title: "Wiki Usage Cheat Sheet"
created: 2026-07-15
updated: 2026-07-15
type: concept
tags: [wiki, logseq, knowledge-management, navigation]
sources: ["https://github.com/flybfree/AI-Wiki/wiki"]
confidence: high
---

# Wiki Usage Cheat Sheet

**Source**: [GitHub Wiki](https://github.com/flybfree/AI-Wiki/wiki)

## What goes where

| Page type | Folder | Use for | Rules |
|---|---|---|---|
| Concepts | `concepts/` | Durable explanations of ideas | Write for reuse, not one-off source notes |
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
| Local logseq-brain `~/logseq-brain/pages/ai-research/` | Graph mirror for Logseq and assistant retrieval |
| SMB backup | Safety copy / recovery mirror |
| PRISM `~/logseq-brain` | Fast-access Logseq mirror |

## Practical rule of thumb

- **Need to write or fix content?** → local wiki
- **Need to browse the graph?** → local logseq-brain or PRISM logseq-brain
- **Need the published version?** → GitHub wiki
- **Need backup?** → SMB
- **Need PRISM fast access?** → PRISM logseq-brain only

## One-line rule

**Author in the local wiki, publish to GitHub, mirror to logseq-brain for graph use, back up via SMB, and use PRISM only as a fast Logseq mirror.**
