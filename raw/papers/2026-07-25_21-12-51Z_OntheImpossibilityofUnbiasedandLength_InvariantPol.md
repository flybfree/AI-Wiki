---
title: On the Impossibility of Unbiased and Length-Invariant Policy Optimization with Outcome Rewards
published: 2026-07-25T21:12:51Z
authors: Fei Ding, Yongkang Zhang, Yuhao Liao, Zijian Zeng, Huiming Yang
url: http://arxiv.org/abs/2607.23364v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Impossibility of Unbiased and Length-Invariant Policy Optimization with Outcome Rewards

## Abstract
Group Relative Policy Optimization (GRPO) is the dominant reinforcement learning algorithm for training reasoning capabilities in large language models, notably adopted by DeepSeek-R1. The recent improvement Dr. GRPO (COLM 2025) identifies the response-level length bias caused by per-trajectory length normalization in GRPO and proposes removing this normalization, claiming the resulting optimizer is "unbiased." We show that this claim is incomplete. Specifically, we establish an impossibility theorem: under the standard outcome reward + GRPO setting, no length-based weighting scheme can simultaneously achieve the following two properties. (P1) Gradient unbiasedness: the gradient estimator is an unbiased estimate of the true policy gradient. (P2) Length invariance: each trajectory's effective contribution to the gradient is independent of its token length. GRPO approximately satisfies P2 but violates P1; Dr. GRPO satisfies P1 but violates P2. We characterize the complete tradeoff spectrum via the parametric family f_alpha(L) = L^{alpha - 1}, where alpha = 0 recovers GRPO, alpha = 1 recovers Dr. GRPO, and provide quantitative analysis showing that Dr. GRPO's length bias can cause longer trajectories to dominate gradient updates by a factor proportional to the length ratio. Our results reveal that neither algorithm is universally "done right"; they occupy opposite ends of a fundamental and unavoidable tradeoff.

## Metadata
- **Published**: 2026-07-25T21:12:51Z
- **Authors**: Fei Ding, Yongkang Zhang, Yuhao Liao, Zijian Zeng, Huiming Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23364v1)