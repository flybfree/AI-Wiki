---
title: Routed Graph Handoff: Adaptive Format Selection for Multi-Agent LLM Delegation
published: 2026-08-26T01:24:34Z
authors: Pratyay Banerjee, Ankit Chadha
url: http://arxiv.org/abs/2608.25277v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Routed Graph Handoff: Adaptive Format Selection for Multi-Agent LLM Delegation

## Abstract
Multi-agent LLM systems coordinate through natural-language messages that consume 40--60\% of their token budget. Replacing these with structured graphs reduces cost but fails on tasks requiring adaptive reasoning. We propose \textbf{Routed Graph Handoff}, where a lightweight LLM router (155 tokens, 0.15\% overhead) selects between a typed dependency graph and natural language for each delegation. On four benchmarks (1,050+ trajectories), the routed system matches or exceeds NL-only on every task: \textbf{+12.7\,pp} on $τ$-retail at 3.2$\times$ compression ($p{<}0.01$), \textbf{+8.7\,pp} on BrowseComp at 2.2$\times$ compression ($p{<}0.05$), and parity on BFCL and AppWorld. Without the router, graph-only delegation regresses 14.6\,pp on AppWorld; the router eliminates this at near-zero cost. A graph-aware executor prompt is required: the same schema without interpretation guidance yields no gain. An oracle analysis reveals 8.6\,pp of additional headroom, motivating execution-time adaptive routing as future work.

## Metadata
- **Published**: 2026-08-26T01:24:34Z
- **Authors**: Pratyay Banerjee, Ankit Chadha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25277v1)