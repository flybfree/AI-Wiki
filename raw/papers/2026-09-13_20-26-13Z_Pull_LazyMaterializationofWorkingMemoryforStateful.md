---
title: Pull: Lazy Materialization of Working Memory for Stateful LLM Conversations
published: 2026-09-13T20:26:13Z
authors: Jiangang Chen
url: http://arxiv.org/abs/2609.14773v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Pull: Lazy Materialization of Working Memory for Stateful LLM Conversations

## Abstract
As LLM conversations grow to hundreds of turns, full-context injection incurs $O(N^2)$ cumulative token costs, while lossy summarization or hard truncation irreversibly discards historical state. We propose Pull, a session router that maintains an addressable metadata directory via a local, deterministic Purifier (zero LLM calls, millisecond-level latency). At query time, the LLM lazily materializes only the turns it needs; unmaterialized turns remain accessible but collapsed. Unlike irreversible compression, Pull's materialization is reversible; subsequent queries can expand any collapsed turn. On LoCoEval (128 conversations, 12,780 turns), Pull reduces per-query context tokens (Phase 2) by 75.1 percent on single-hop tasks with equivalent quality ($Δ= -0.002$, n.s.) and by 72.0 percent on multi-hop tasks with no quality loss ($Δ= +0.017$). A controlled routing benchmark (7,831 queries x 10 methods) shows that entity lifecycle tracking is empirically a prerequisite for distance-independent routing. On BEAM 1M (14 conversations, 263 questions), Pull improves F1 by +55.2 percent over a truncation baseline.

## Metadata
- **Published**: 2026-09-13T20:26:13Z
- **Authors**: Jiangang Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14773v1)