---
title: DivOPD: Spread Wide, Look Close for Asynchronous On-Policy Distillation of Multi-turn Agents
url: http://arxiv.org/abs/2609.34838v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_10-35-39Z_DivOPD_SpreadWide_LookCloseforAsynchronousOn_Polic.md
generated_at: 2026-09-28 23:11
model: qwen3.6-35b-a3b
---

## Summary
DivOPD addresses critical inefficiencies in asynchronous multi-turn on-policy distillation where arrival-order batching allows early or long rollouts to dominate updates while other valid interactions become stale and wasted. The authors introduce a learner-side batch-selection method that distributes a fixed turn budget across more diverse rollouts and prioritizes turns with high cumulative teacher-student disagreement, effectively maximizing the utility of generated experience without modifying the underlying loss functions or optimizers.

## Key Takeaways
- DivOPD implements a batch-selection strategy that spreads a fixed turn budget across a broader set of rollouts to prevent dominance by early sequences, while explicitly filtering out turns lacking usable teacher feedback to ensure only high-quality interactions contribute to updates.
- Within each rollout, the method prioritizes training on turns exhibiting the largest cumulative disagreement between student and teacher actions, focusing optimization on areas of divergence without altering the per-turn loss or optimizer configuration.
- Across six settings on ALFWorld, ScienceWorld, and WebShop benchmarks with 1.5B-7B students, DivOPD increases mean peak success rates from 77.4 to 84.4 and achieves geometric-mean speedups of 1.84x in training tokens and 1.87x in learner GPU time compared to vanilla OPD, with optional teacher intervention further raising performance while retaining substantial efficiency gains.

## Context
Asynchronous multi-turn reinforcement learning is essential for scaling capable language agents but often suffers from compute waste due to variable rollout lengths and data staleness in distributed training environments. This research contributes

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34838v1)
