---
title: Collaborative Weighting with Pessimistic Critic for Mitigating Overestimation in Off-Policy Reinforcement Learning
published: 2026-07-29T06:18:19Z
authors: Gong Gao, Xiao Lai, Ziqi Xie, Guojie Chen, Xianhui Liu, Weidong Zhao
url: http://arxiv.org/abs/2607.26509v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Collaborative Weighting with Pessimistic Critic for Mitigating Overestimation in Off-Policy Reinforcement Learning

## Abstract
Deep off-policy reinforcement learning algorithms for continuous control typically rely on neural value function approximation to guide policy improvement. However, temporal-difference (TD) learning introduces noisy targets, resulting in non-stationary optimization, while greedy policy updates amplify early-stage estimation errors. The recursive propagation of such errors leads to persistent overestimation bias and degraded training stability in actor-critic methods. Existing approaches attempt to alleviate this issue via prioritized sampling or modified value learning objectives, but often overemphasize high-uncertainty transitions caused by limited data coverage or bootstrapping errors, thereby further amplifying bias.In this paper, we propose Collaborative Weighting Actor-Critic (CWAC), a unified framework that explicitly accounts for predictive uncertainty in value estimation. CWAC employs distributional critic to model return uncertainty and introduces a collaborative weighting mechanism that jointly reweights TD-errors and uncertainty, enabling robust learning from reliable samples while suppressing noisy updates. In addition, we incorporate a stochastic pessimistic value estimation scheme via sampling from the return distribution, which effectively mitigates error propagation during policy improvement. CWAC can be seamlessly integrated into existing off-policy algorithm frameworks such as SAC, TD3, and DDPG with minimal overhead. Empirical results demonstrate that our proposed method significantly enhances performance across a diverse range of simulated tasks. Our code is publicly available at https://anonymous.4open.science/r/CWAC-348E.

## Metadata
- **Published**: 2026-07-29T06:18:19Z
- **Authors**: Gong Gao, Xiao Lai, Ziqi Xie, Guojie Chen, Xianhui Liu, Weidong Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26509v1)