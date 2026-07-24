---
title: Fishing Out Free Riders: Shapley-Based Reward Attribution for Parallel Reasoning via Reinforcement Learning
url: http://arxiv.org/abs/2607.18979v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_11-14-33Z_FishingOutFreeRiders_Shapley_BasedRewardAttributio.md
generated_at: 2026-07-23 23:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Parallel Shapley, a reinforcement learning framework that attributes fine-grained contributions of individual reasoning paths in multi-path LLM tasks. By treating each path as a player and using Shapley values to measure marginal impact, the method replaces uniform rewards with proportional ones. Experiments on math benchmarks show improved performance and training stability.

## Key Takeaways
- The framework quantifies each path's marginal contribution using Shapley values, providing a principled way to distinguish valuable reasoning steps from redundant or harmful ones.
- Uniform outcome-level rewards are replaced by path-level utilities evaluated via a generative reward model, reducing ambiguous learning signals.
- Monte Carlo sampling enables efficient approximation of Shapley values, making the method scalable for large models.

## Context
Current LLM evaluation relies on final answer correctness, which masks internal reasoning quality. Parallel reasoning amplifies this issue as multiple paths converge to the same output, obscuring the true effort and risk. This paper addresses that gap by offering a transparent attribution mechanism.

## Implications
Practitioners can leverage Parallel Shapley to fine‑tune reward functions for complex tasks, leading to more robust models. The method also offers interpretable insights into which reasoning steps are essential, supporting research on model behavior and safety.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18979v1)
