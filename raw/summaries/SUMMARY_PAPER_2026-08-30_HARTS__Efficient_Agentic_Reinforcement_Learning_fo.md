---
title: HARTS: Efficient Agentic Reinforcement Learning for Hybrid-Attention Models over Arbitrary Rollout Trees
url: http://arxiv.org/abs/2608.28158v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_10-18-54Z_HARTS_EfficientAgenticReinforcementLearningforHybr.md
generated_at: 2026-08-30 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
HARTS is a system that enables efficient agentic reinforcement learning for hybrid‑attention models operating on arbitrary rollout trees. By compressing shared prefixes and reusing them across microbatches, HARTS achieves large speedups in forward, backward, and gradient computation while preserving the original RL interface.

## Key Takeaways
- HARTS jointly plans microbatches, data‑parallel replica assignments, and microbatch‑slot schedules using non‑replay compact‑token work after prefix compression.  
- For chunkwise linear attention, a linear‑time algorithm coordinates chunk‑boundary state recovery and replay to produce the minimum number of sequential linear‑attention calls under its packed execution model.  
- HARTS preserves chunkwise state partitioning: it avoids repeating projections, MLP/MoE computation, or final outputs, performing only bounded state replay for numerical alignment; each round batches all branches into one packed call, propagates gradients through differentiable state handoffs, supports activation recomputation, and restores per‑token log‑probabilities.

## Context
Agentic reinforcement learning often generates irregular rollout trees with shared histories, causing costly recomputation of prefixes. Existing RL frameworks target full‑attention models and lack dense, differentiable hybrid‑attention execution compatible with activation recomputation. This gap limits the scalability of large hybrid‑attention agents in practice.

## Implications
HARTS demonstrates that arbitrary‑rollout‑tree prefix sharing can be applied to real hybrid‑attention models, delivering up to 4.8× speedup across multiple configurations without sacrificing reward trends. Practitioners can now train and deploy RL agents using MoE or other hybrid attention architectures at reduced computational cost, opening new possibilities for large‑scale AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28158v1)
