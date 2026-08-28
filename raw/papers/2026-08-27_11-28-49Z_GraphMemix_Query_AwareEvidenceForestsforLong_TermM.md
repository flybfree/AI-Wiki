---
title: GraphMemix: Query-Aware Evidence Forests for Long-Term Multimodal Agent Memory
published: 2026-08-27T11:28:49Z
authors: Geng Li, Yuhao Wang, Dong Li, Jianye Hao, Yuxin Peng
url: http://arxiv.org/abs/2608.26983v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GraphMemix: Query-Aware Evidence Forests for Long-Term Multimodal Agent Memory

## Abstract
Organizing long-term memory for multimodal agents remains challenging because existing methods either suffer from expensive question-agnostic offline summaries or naive embedding similarity matching that introduces incomplete and redundant context. To address these issues, we propose GraphMemix, a combinatorial-optimization graph memory framework that models memory organization as query-aware evidence-forest construction. Specifically, our method consists of three key components:(1) candidate graph construction, which expands multi-view seed memories through schema and semantic relations to acquire query-aware original context; (2) evidence utility and activation costs, which decouples direct memory support from anchor-conditioned relation verification to suppress redundant or conflicting information; and (3) forest optimization, which jointly selects a forest-format memory context under a maximum evidence budget and its reliable relational structure. By organizing memory into a query-relevant subgraph, the method avoids substantial lifecycle cost and recovers low-similarity complementary evidence. Experimental results across four long-term multimodal memory benchmarks demonstrate significant improvements with different foundation models and establish a new Pareto frontier between accuracy and lifecycle cost.

## Metadata
- **Published**: 2026-08-27T11:28:49Z
- **Authors**: Geng Li, Yuhao Wang, Dong Li, Jianye Hao, Yuxin Peng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26983v1)