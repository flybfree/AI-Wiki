---
title: Memory Depth and Reconstructed Context Width: A Controlled Evaluation of Hierarchical Retrieval
published: 2026-10-06T13:04:43Z
authors: Michael Andreev
url: http://arxiv.org/abs/2610.08300v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memory Depth and Reconstructed Context Width: A Controlled Evaluation of Hierarchical Retrieval

## Abstract
Long-term conversational memory is becoming an integral component of modern LLM systems. Proposed architectures group records by topics and events, construct hierarchies and graphs, and connect facts through causal and temporal relations. We experimentally study the interaction between two memory parameters: structural depth and the width of context supplied to the answer model. Using EverMemBench, we evaluate depths D1-D4, core budgets of 1,024/2,048/4,096 tokens, and additional Production and Oracle conditions up to the full archive. Increasing width from 1K to 4K improves Accuracy by 10.11-17.98 percentage points, whereas increasing depth provides no monotonic gain. Beyond 8-16K, Production performance reaches a plateau while tokens per correct answer continue to increase; Oracle preserves quality on full archives of 68-71K tokens. These results motivate further investigation of large, coherent context blocks instead of progressively deeper memory structures.

## Metadata
- **Published**: 2026-10-06T13:04:43Z
- **Authors**: Michael Andreev
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.08300v1)