---
title: Coarse Indexing, Fine Evidence: Decoupling Temporal Granularity in Long-Video RAG
url: http://arxiv.org/abs/2608.23011v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_09-12-06Z_CoarseIndexing_FineEvidence_DecouplingTemporalGran.md
generated_at: 2026-08-24 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents Density-Aware Graph Construction (DAGC), a training-free method that separates coarse retrieval indexing from fine-grained video evidence in long-video RAG. It shows that by merging visually redundant chunks, the index can be reduced to 40-50% of original nodes while still achieving near‑original QA performance and delivering 1.3–1.7× speedup.

## Key Takeaways
- DAGC decouples coarse retrieval granularity from fine evidence granularity by constructing a density‑adaptive graph that merges redundant video chunks, allowing the index to retain only about half of the original nodes.
- The method preserves mappings to the original temporal units so retrieved coarse regions can be expanded back to full‑resolution evidence for downstream reasoning.
- Experiments on MLVU, VideoMME, and LongVideoBench demonstrate a 1.3–1.7× end‑to‑end wall‑clock acceleration without sacrificing QA accuracy (≈99% of baseline).

## Context
Long‑video retrieval‑augmented generation systems often suffer from computational bottlenecks because they index every video chunk, leading to large and slow graphs. Existing solutions treat indexing granularity as fixed, limiting flexibility in model capacity and inference speed.

## Implications
This decoupling enables more efficient deployment of long‑video RAG pipelines across diverse LLMs, reducing memory usage and latency for real‑time applications such as autonomous driving or content summarization. Practitioners can adopt DAGC without retraining models, making large video datasets more accessible.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23011v1)
