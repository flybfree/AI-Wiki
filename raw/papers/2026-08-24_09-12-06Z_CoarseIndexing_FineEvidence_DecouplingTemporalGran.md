---
title: Coarse Indexing, Fine Evidence: Decoupling Temporal Granularity in Long-Video RAG
published: 2026-08-24T09:12:06Z
authors: Zhe Jin, Zhimin Lin, Bin Zheng, Junhua Fang, Huihua Yang
url: http://arxiv.org/abs/2608.23011v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Coarse Indexing, Fine Evidence: Decoupling Temporal Granularity in Long-Video RAG

## Abstract
Graph-based retrieval-augmented generation (RAG) provides a scalable paradigm for long-video understanding, but existing systems typically inherit a fixed temporal granularity from video segmentation when constructing their retrieval index. We argue that this design unnecessarily couples indexing granularity with evidence granularity: coarse representations can often suffice for locating relevant temporal regions, while fine-grained evidence remains important for downstream reasoning. We propose \textbf{Density-Aware Graph Construction (DAGC)}, a training-free approach that decouples a query-independent coarse retrieval index from the original fine-grained evidence space. DAGC constructs a compact, density-adaptive graph index by merging visually redundant neighboring chunks, while preserving mappings to the original temporal units. Retrieved coarse regions are subsequently expanded back to the original chunk granularity for fine-grained evidence refinement and answer generation. Experiments on MLVU, VideoMME, and LongVideoBench show that DAGC retains only about 40--50\% of the original graph nodes and achieves $1.3$--$1.7\times$ end-to-end wall-clock acceleration while preserving approximately 99\% of the original QA performance. The gains transfer across different LVLM backbones and video RAG pipelines, suggesting that long-video RAG need not maintain the same temporal granularity for indexing and evidence reasoning.

## Metadata
- **Published**: 2026-08-24T09:12:06Z
- **Authors**: Zhe Jin, Zhimin Lin, Bin Zheng, Junhua Fang, Huihua Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23011v1)