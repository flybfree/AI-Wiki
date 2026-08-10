---
title: Fast LapSum: Exact Differentiable Top-k at Million Scale
url: http://arxiv.org/abs/2608.06912v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_07-44-35Z_FastLapSum_ExactDifferentiableTop_katMillionScale.md
generated_at: 2026-08-09 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Fast LapSum, an exact-budget soft top‑k primitive that preserves the precise selection mass of k while remaining fully differentiable end‑to‑end. The GPU solver operates in linear time after sorting and achieves sub‑millisecond latency even for millions of scores, making it practical for large‑scale AI workloads.

## Key Takeaways
- Fast LapSum solves the soft top‑k problem exactly without relaxing the normalization constraint, unlike DFTopK which relaxes it.  
- The solver combines a linear‑time threshold computation with an analytical vector–Jacobian product and uses probabilistic bracketing to sort only uncertain middle scores, yielding negligible overhead.  
- Experiments show processing 10⁶, 10⁷, and 10⁸ scores in 0.41 ms, 1.15 ms, and 5.23 ms respectively, enabling exact soft top‑k at million scale.

## Context
In modern sparse AI systems, the top‑k operation is essential for routing, memory selection, and attention pruning, yet standard hard top‑k blocks gradients while continuous relaxations are computationally prohibitive for large models. Fast LapSum addresses this gap by delivering an exact soft solution that fits within training budgets without sacrificing efficiency.

## Implications
Fast LapSum enables precise gradient flow in sparse routing and retrieval tasks, improving model performance and stability. Practitioners can integrate it into training loops to generate high‑resolution adversarial examples or train fully differentiable image coders with minimal overhead, accelerating research and industry adoption of large‑scale sparse models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06912v1)
