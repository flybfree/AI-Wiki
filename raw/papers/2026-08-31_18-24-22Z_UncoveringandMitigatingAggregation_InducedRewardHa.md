---
title: Uncovering and Mitigating Aggregation-Induced Reward Hacking in Multi-Reward Reinforcement Learning
published: 2026-08-31T18:24:22Z
authors: Yu Yuan, Yaoyou Fan, Lili Zhao, Guangting Zheng, Kai Zhang, Lu Pan, Ke Zeng, Qi Liu
url: http://arxiv.org/abs/2609.00213v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Uncovering and Mitigating Aggregation-Induced Reward Hacking in Multi-Reward Reinforcement Learning

## Abstract
Reinforcement learning fine-tuning of large language models increasingly adopts multiple reward dimensions, including verifiable rules, task-specific evaluators, and learned reward models, to provide richer supervision across diverse capabilities. These dimensions are commonly scalarized with fixed aggregation weights. We identify a failure mode in which aggregation itself induces reward hacking: static projection aliases qualitatively different reward profiles into a single scalar, steering optimization toward whichever dimensions are easiest, densest, or systematically favored by the reward signal. Over training, this traps the policy in suboptimal profiles and prevents convergence to better-balanced ones that would yield higher task performance. To address this, we propose Adaptive Multi-Reward Projection (AMRP), a lightweight online method that reallocates aggregation weights using three signals, relative shortfall, reward volatility, and recent progress, increasing pressure on lagging, unstable, or stagnant dimensions while relieving saturated ones. Across structured reasoning, citation-grounded generation, and open-ended alignment under GRPO, AMRP consistently improves reward-profile balance and downstream performance over fixed and dynamic weighting baselines; it also remains effective with GDPO and PPO, supporting compatibility across RL algorithms. Our code is available at https://github.com/yyhappier/AMRP.git.

## Metadata
- **Published**: 2026-08-31T18:24:22Z
- **Authors**: Yu Yuan, Yaoyou Fan, Lili Zhao, Guangting Zheng, Kai Zhang, Lu Pan, Ke Zeng, Qi Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00213v1)