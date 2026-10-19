---
title: From Memory Hits to Answerable Evidence: Query-Conditioned Memory Compilation for Long-Term Agent Memory
published: 2026-10-16T11:15:29Z
authors: Shangze Li, Yanyu Yao, Derong Xu, Zhi Zheng, Tong Xu
url: http://arxiv.org/abs/2610.23313v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Memory Hits to Answerable Evidence: Query-Conditioned Memory Compilation for Long-Term Agent Memory

## Abstract
Long-term agent memory requires recovering answer-relevant evidence dispersed across turns and sessions. Existing systems increasingly use structured memories and adaptive retrieval, yet often pass retrieved or expanded units directly to the reader, coupling memory addressing with evidence presentation and leaving the final context redundant or incomplete. To address this gap, we propose MemCompile, a query-conditioned evidence compilation framework for long-term conversational memory. Given a query, the Address Plane locates relevant support through compact source-linked descriptors and capacity-aware Cells, while a normalization boundary resolves heterogeneous retrieval hits to stable SourcePacket identities. Its Evidence Plane then allocates a bounded evidence budget across complementary packets, admits limited additional support, and renders the retained claims associated with each selected packet into an answer-ready context. MemCompile achieves 80.52% Judge Accuracy on LoCoMo and extends the empirical quality-cost Pareto frontier to a higher-quality regime. Its strong performance on LongMemEval-S further suggests that the benefits of query-conditioned compilation generalize across long-term conversational-memory benchmarks.

## Metadata
- **Published**: 2026-10-16T11:15:29Z
- **Authors**: Shangze Li, Yanyu Yao, Derong Xu, Zhi Zheng, Tong Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.23313v1)