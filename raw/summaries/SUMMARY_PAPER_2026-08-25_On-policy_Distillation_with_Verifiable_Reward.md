---
title: On-policy Distillation with Verifiable Reward
url: http://arxiv.org/abs/2608.24696v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_15-21-17Z_On_policyDistillationwithVerifiableReward.md
generated_at: 2026-08-25 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces On-policy Distillation with Verifiable Reward, a method that merges on-policy distillation and verifiable reward learning without extra hyperparameters. It reformulates the teacher’s sampled-token guidance using trajectory correctness and applies a ReLU gating to produce non‑negative rewards for correct paths and non‑positive ones otherwise. Experiments show OPDVR beats standard OPD across six reasoning benchmarks.

## Key Takeaways
- The paper demonstrates that implicit reward from sampled-token OPD can be aligned with task success by reformulating it based on trajectory correctness.
- A ReLU gating mechanism ensures correct trajectories receive non‑negative rewards while incorrect ones get non‑positive rewards, preserving teacher guidance without hyperparameters.
- This formulation turns sampled-token OPD into a proper RLVR signal that can be combined directly with policy gradient methods like GRPO.

## Context
Current RLVR and on-policy distillation approaches face complementary weaknesses: sparse task feedback versus dense token signals. Integrating them often requires manual weighting or heuristic switching, adding complexity. This work offers a principled, hyperparameter‑free integration that leverages both modalities for improved model training.

## Implications
For practitioners, OPDVR simplifies the deployment of teacher‑student distillation in RL settings, enabling consistent performance across diverse tasks. In industry, it reduces engineering effort and improves robustness, making large language models more reliable in reasoning applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24696v1)
