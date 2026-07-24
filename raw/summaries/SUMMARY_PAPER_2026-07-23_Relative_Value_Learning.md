---
title: Relative Value Learning
url: http://arxiv.org/abs/2607.21120v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_09-55-45Z_RelativeValueLearning.md
generated_at: 2026-07-23 22:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Relative Value Learning RV which learns value differences between states using an antisymmetric function Δ(s_i,s_j)=V(s_i)-V(s_j) instead of absolute state values. It proves that the pairwise Bellman operator is a γ‑contraction guaranteeing convergence to true value differences and derives unbiased policy‑gradient estimators such as R‑GAE. Experiments on 49 Atari games show RV combined with PPO matches or exceeds standard PPO performance.

## Key Takeaways
- The framework learns only relative state values Δ(s_i,s_j) which are the relevant quantities for control decisions.
- It proves that the pairwise Bellman operator is a γ‑contraction leading to a unique fixed point equal to true value differences.
- This enables unbiased policy‑gradient estimators like R‑GAE and competitive performance on Atari benchmarks.

## Context
Relative value estimation addresses a limitation of traditional absolute critics in reinforcement learning where only differences matter for action selection. By focusing on pairwise differences the method aligns with theoretical guarantees that depend on contraction properties of Bellman operators.

## Implications
Practitioners can adopt RV to build more stable and unbiased policy‑gradient methods without retraining full value networks. This could improve sample efficiency and reliability in robotics, game AI, and any domain where relative state perception is key.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21120v1)
