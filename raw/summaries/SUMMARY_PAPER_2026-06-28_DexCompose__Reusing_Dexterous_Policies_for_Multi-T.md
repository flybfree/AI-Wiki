---
title: DexCompose: Reusing Dexterous Policies for Multi-Task Manipulation with a Single Hand
url: http://arxiv.org/abs/2606.28323v1
type: paper-summary
date: 2026-06-28
source_paper: 2026-06-26_17-59-57Z_DexCompose_ReusingDexterousPoliciesforMulti_TaskMa.md
generated_at: 2026-06-28 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DexCompose, a framework for composing pretrained dexterous manipulation policies into multi‑task sequences using a single hand. It achieves a 77.4% average success rate across 16 composite tasks by preserving existing skill states while adding new actions. The method relies on finger‑level action ownership and dual residual modules.

## Key Takeaways
- DexCompose identifies which fingers must remain active to maintain the outcome of the first task through release tests over candidate finger masks, preventing destructive interference.
- It trains two asymmetric residuals: a bounded stabilizer that limits changes to the preserved skill state, and a context‑aware residual that adapts only the downstream policy within its assigned action subspace.
- The framework composes up to four object‑retention skills with four downstream interactions without retraining full policies.

## Context
Dexterous manipulation remains limited by the need for separate policies per task, leading to inefficiency and failure when tasks overlap. This work addresses that bottleneck by reusing existing models while preserving skill integrity, aligning with trends toward modular AI agents.

## Implications
Practitioners can deploy a single pretrained hand controller across diverse manipulation scenarios, reducing development time and hardware complexity. The approach also offers a blueprint for integrating residual learning in robotics, potentially enabling more flexible and robust humanoid robots.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.28323v1)
