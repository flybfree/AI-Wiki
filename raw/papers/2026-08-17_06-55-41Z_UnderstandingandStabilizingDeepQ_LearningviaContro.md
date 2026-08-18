---
title: Understanding and Stabilizing Deep Q-Learning via Controlled Bootstrapping and Regulated Value Dynamics
published: 2026-08-17T06:55:41Z
authors: Bozhou Chen, Yongyi Wang, Hanyu Liu, Xionghui Yang, Wenxin Li
url: http://arxiv.org/abs/2608.16182v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding and Stabilizing Deep Q-Learning via Controlled Bootstrapping and Regulated Value Dynamics

## Abstract
Deep Q-learning (DQL) has achieved remarkable empirical success in reinforcement learning, yet its training process remains notoriously unstable. Existing studies often attribute instability to isolated factors such as overestimation bias or representation learning issues, lacking a unified understanding of how different sources of instability interact during recursive value estimation. In this work, we provide a systematic analysis of instability in deep Q-learning from three complementary perspectives: operator-level bias in Bellman bootstrapping, estimator-level sensitivity of greedy action selection to regression noise, and parameter-dynamics imbalance under aggressive data reuse. We identify a reward-triggered self-reinforcing trap and characteristic parameter spike dynamics, then derive stabilization principles for controlled bootstrapping, ensemble quantile estimation, and spike-based parameter regulation. Experiments on Atari-100K and Procgen demonstrate competitive performance and improved training stability.

## Metadata
- **Published**: 2026-08-17T06:55:41Z
- **Authors**: Bozhou Chen, Yongyi Wang, Hanyu Liu, Xionghui Yang, Wenxin Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16182v1)