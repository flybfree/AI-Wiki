---
title: LayerRAG-Bench: A Cross-Layer Reliability Benchmark for Agentic Retrieval-Augmented Generation
published: 2026-07-29T18:09:17Z
authors: Musa Shams
url: http://arxiv.org/abs/2607.27353v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LayerRAG-Bench: A Cross-Layer Reliability Benchmark for Agentic Retrieval-Augmented Generation

## Abstract
Agentic retrieval-augmented generation systems can produce answers that appear grounded while failing at the evidence, tool-contract, authorization, or session-state layer. We introduce LayerRAG-Bench, a controlled cross-layer reliability benchmark with 8 enterprise domains, 240 tasks, 9 fault scenarios, 2 contract modes, and 38,880 live task-level records across nine models from OpenAI, Anthropic, and Gemini. Schema normalization raises schema-drift success from 0.000 to 0.913, but stale evidence, missing tool output, denied permissions, and wrong-session context are not recovered by schema normalization. Groundedness-only evaluation also produces substantial false positives under stale and wrong-session evidence. These results support a layer-specific evaluation principle: a reliability intervention should be credited for repairing its target layer without being mistaken for a universal fix.

## Metadata
- **Published**: 2026-07-29T18:09:17Z
- **Authors**: Musa Shams
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27353v1)