---
title: WHALE: A Simple Recipe for Joint Harness-Weight Optimization
url: http://arxiv.org/abs/2609.00196v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_18-12-55Z_WHALE_ASimpleRecipeforJointHarness_WeightOptimizat.md
generated_at: 2026-09-01 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces WHALE, a joint optimization recipe that alternates model fine‑tuning under the current harness with harness search using Meta‑Harness and online rejection sampling. It demonstrates that alternating updates improve accuracy across multiple tasks compared to methods that optimize only one component.

## Key Takeaways
- Joint optimization is necessary because updating weights can change which harness is effective, while updating a harness can expose or hide model capabilities.
- The adaptive patience rule allows the system to separate genuine improvements from noise and avoid over‑optimizing against a changing counterpart by monitoring training signals.
- Small interleaved updates outperform stagewise weight‑then‑harness optimization in both accuracy gains and rollout cost, showing that frequent low‑impact changes are beneficial.

## Context
In large language model deployment the executable harness determines how prompts and control flow are managed yet most joint adaptation methods treat it as static. This limitation hampers real‑world performance where both components evolve together.

## Implications
For practitioners WHALE offers a practical framework to balance computational cost and accuracy, enabling cheaper rollouts while still achieving state‑of‑the‑art results across search QA math reasoning and chess puzzles.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00196v1)
