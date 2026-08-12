---
title: Pair-Centric Graph Rewiring for Over-Squashing via Optimal Transport-Guided Communication Alignment
url: http://arxiv.org/abs/2608.10619v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_08-05-32Z_Pair_CentricGraphRewiringforOver_SquashingviaOptim.md
generated_at: 2026-08-11 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PairAlign, a framework that rewires graphs to reduce over-squashing in message-passing networks by focusing on pairwise communication demands. It defines a shortage score as the ratio of demand to support and shows it aligns with Jacobian-based measures. Experiments confirm its effectiveness across benchmarks.

## Key Takeaways
- The shortage score quantifies how poorly distant pairs are supported relative to their communication need, providing a pair-level measure of over-squashing.
- PairAlign optimizes edge additions to maximize this ratio improvement, prioritizing rewiring where the deficit is largest.
- Optimal transport guides the allocation of a limited edge budget to cover shortage targets more broadly than greedy local choices.

## Context
Message-passing networks rely on graph topology to propagate information efficiently; when graphs are too dense or sparse, signals can be over-squashed. This work addresses a key bottleneck in designing such networks by making structural support explicit at the pair level.

## Implications
By offering a principled way to repair graph structures at the pair level, PairAlign can improve model performance without retraining. Practitioners may apply it to accelerate training of large-scale graph neural networks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10619v1)
