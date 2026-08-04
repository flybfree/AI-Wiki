---
title: PGMem: Tightly Coupled Persona-Memory Graph for Lifelong Personalized Agents
published: 2026-08-03T05:14:59Z
authors: Wonjun Choi, Yerim Kim, Yukyung Lee, Susik Yoon
url: http://arxiv.org/abs/2608.01708v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PGMem: Tightly Coupled Persona-Memory Graph for Lifelong Personalized Agents

## Abstract
Long-term personalized dialogue agents must track user preferences as their personas evolve. Existing memory systems organize past events well, but store personas as flat profiles detached from the events that justify them. This loose coupling leads to the memory-persona validity gap and the persona-aware retrieval gap. We propose PGMem, a heterogeneous persona-memory graph that connects event and persona nodes through typed provenance and evidence edges, keeping each persona signal traceable to the events that support or revise it. At retrieval time, PGMem expands from query-relevant seeds and ranks signals by evidential validity. Across three benchmarks with small language model backbones, PGMem consistently outperforms summary-based, persona-aware, graph-structured, and agentic memory baselines, and improves performance as the context grows. The source code of PGMem is available at https://github.com/wonjunchoi23/pgmem/

## Metadata
- **Published**: 2026-08-03T05:14:59Z
- **Authors**: Wonjun Choi, Yerim Kim, Yukyung Lee, Susik Yoon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01708v1)