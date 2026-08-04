---
title: Rethinking Video Token Compression with a Global Codebook: Learning Once, Compressing Everywhere
url: http://arxiv.org/abs/2608.01271v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_14-24-13Z_RethinkingVideoTokenCompressionwithaGlobalCodebook.md
generated_at: 2026-08-03 23:38
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes ONCE, a framework that compresses video tokens offline using a global codebook and applies the result online to reduce repeated computation. It learns a frequency‑aware codebook once in visual feature space and then uses lightweight lookups for each video input. Experiments show that ONCE achieves lower inference latency while maintaining competitive accuracy compared with pruning or merging methods.

## Key Takeaways
- The framework shifts compression from an on‑line operation to an offline learning phase, eliminating repeated per‑video computation.
- A global codebook is built once in the visual feature space and reused across all videos, providing a reusable lookup table for token aggregation.
- ONCE reduces inference latency among compared methods while preserving strong accuracy‑efficiency trade‑offs.

## Context
Video large language models face challenges because their token sequences grow with video length, creating redundant visual patterns that inflate computational cost. Traditional compression techniques apply per‑video processing, which is inefficient and model specific. This work addresses those inefficiencies by decoupling learning from inference.

## Implications
The approach enables more scalable video understanding systems with minimal latency impact, benefiting real‑time applications such as autonomous driving and content recommendation. Practitioners can adopt ONCE without redesigning their models, making it a practical upgrade for existing Video‑LLM pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01271v1)
