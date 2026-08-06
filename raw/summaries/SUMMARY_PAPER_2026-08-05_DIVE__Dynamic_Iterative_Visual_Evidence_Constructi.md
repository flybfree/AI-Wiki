---
title: DIVE: Dynamic Iterative Visual Evidence Construction for Efficient Vision-Language Models
url: http://arxiv.org/abs/2608.04496v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_06-32-25Z_DIVE_DynamicIterativeVisualEvidenceConstructionfor.md
generated_at: 2026-08-05 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper DIVE proposes a training‑free framework that improves visual token pruning in vision‑language models by iteratively selecting tokens based on residual scores and updating residuals to exclude already explained evidence. Experiments across eight benchmarks show the method retains performance with an 88.9% reduction in visual tokens while keeping 98.2% of the uncompressed model’s average accuracy.

## Key Takeaways
- DIVE replaces one‑pass scoring with a dynamic iterative process that repeatedly picks the token with highest residual score, updates residuals to discount explained evidence, and re‑evaluates remaining tokens.
- The framework is training‑free, meaning it can be applied directly to existing models without additional fine‑tuning or extra data.
- With an 88.9% reduction in visual tokens DIVE retains 98.2% of the original model’s average performance across eight image‑understanding benchmarks.

## Context
Vision‑language models face a bottleneck because visual tokens are far longer than textual tokens, slowing inference and increasing memory usage. Traditional pruning methods rely on static scores that ignore how evidence accumulates during decoding, leading to suboptimal token selection. DIVE’s iterative approach addresses this by modeling the evolving relevance of each token as more evidence is retained.

## Implications
This work enables faster, lower‑resource deployment of vision‑language systems without sacrificing accuracy, which is crucial for real‑time applications such as mobile assistants and autonomous vehicles. Practitioners can adopt DIVE to compress models for edge devices while preserving performance, reducing latency and power consumption in the field.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04496v1)
