---
title: AnchorFold: A Focus-Then-Fold Framework via Recursive Attention Propagation for Efficient Multi-Vector Visual Document Retrieval
url: http://arxiv.org/abs/2608.08732v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_14-23-08Z_AnchorFold_AFocus_Then_FoldFrameworkviaRecursiveAt.md
generated_at: 2026-08-10 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
AnchorFold introduces a training-free focus-then-fold framework that compresses multi-vector visual document retrieval indexes by recursively propagating attention scores within each head and integrating across heads and layers. The method selects high-centrality tokens as anchors, then folds remaining tokens into nearest anchor groups using centrality-weighted aggregation. Across multiple benchmarks it achieves near-lossless compression while maintaining high retrieval quality.

## Key Takeaways
- AnchorFold uses recursive attention propagation to compute multi-step scores within each visual attention head and merges them across heads and layers for a unified representation.
- It selects the highest-centrality tokens as anchors, preserving their importance while delegating other tokens to nearest anchor groups in normalized retrieval space.
- The framework retains 98.3% of full-index NDCG@5 at fivefold compression and 92.4% at twentyfold compression on ViDoRe v1/v2.

## Context
Multi-vector vision-language retrievers are essential for fine-grained document search but suffer from high storage and scoring costs due to dense visual patch embeddings. Training-free methods often sacrifice quality through aggressive pruning or merging, highlighting a need for approaches that balance efficiency with relevance preservation.

## Implications
AnchorFold demonstrates that structural attention can guide compression without explicit training, offering a scalable solution for large-scale document indexing in AI systems. Practitioners can adopt this framework to reduce memory footprints while maintaining high retrieval performance across diverse backbones and retrieval settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08732v1)
