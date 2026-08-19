---
title: PlanPO: Group Planning-Aware Policy Optimization for Multi-Turn Agentic LLMs
url: http://arxiv.org/abs/2608.17289v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_02-39-53Z_PlanPO_GroupPlanning_AwarePolicyOptimizationforMul.md
generated_at: 2026-08-18 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Group Planning-aware Policy Optimization (PlanPO), a reinforcement learning method that addresses the problem of collapsing advantages in multi-turn agentic LLMs. By using coarse-to-fine advantage signals, PlanPO learns generalizable planning abilities across tasks while avoiding simple length minimization. Experiments show it outperforms GRPO by 27.2 % on average across ALFWorld, WebShop, and SciWorld.

## Key Takeaways
- PlanPO distinguishes between successful trajectories that differ in interaction efficiency by assigning advantage signals based on trajectory length and turn‑level response length.  
- The coarse‑to‑fine signal captures relative differences among group‑relative samples, preventing advantage collapse.  
- Despite negligible extra training cost, PlanPO improves performance significantly over GRPO on challenging benchmarks.

## Context
Group‑relative policy optimization aims to align agent behavior across diverse tasks without task‑specific fine‑tuning. Current methods often treat all successful rollouts equally, leading to loss of useful information and suboptimal learning. This work advances the field by providing a principled way to encode trajectory diversity into reward shaping.

## Implications
PlanPO offers practitioners a scalable technique for training LLMs that can plan across conversations without sacrificing efficiency. The method could be integrated into commercial agents to enhance user interaction quality while keeping training resources low, benefiting both research and industry deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17289v1)
