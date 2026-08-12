---
title: Dreamer-SAC: Off-Policy Learning in Latent World Models for Sample-Efficient Autonomous Driving
published: 2026-08-11T02:27:26Z
authors: Jiazhuo Li, Linjiang Cao, Qi Liu, Xi Xiong
url: http://arxiv.org/abs/2608.10386v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dreamer-SAC: Off-Policy Learning in Latent World Models for Sample-Efficient Autonomous Driving

## Abstract
Sample-efficient reinforcement learning for autonomous driving is often limited by the trade-off between data efficiency and model bias. While world models reduce the reliance on costly environment interactions, policy optimization over learned dynamics remains sensitive to prediction errors. This paper proposes the Dreamer-SAC framework, which integrates a recurrent state-space world model with an off-policy soft actor-critic algorithm trained directly in latent space. The framework uses a combination of real interactions and short-horizon generated trajectories with n-step target estimation and multi-objective supervision. Evaluated in autonomous driving scenarios with objectives encompassing driving efficiency and safety, the proposed framework consistently outperforms representative reinforcement learning baselines, including DreamerV3, SAC, and PPO, while achieving improved performance with substantially fewer real environment interactions. Experiments reveal an inverted-U relationship between rollout horizon and policy performance, where short-horizon latent rollouts achieve the best trade-off between additional training signals and accumulated model bias. Furthermore, n-step target estimation demonstrates more effectiveness over one-step temporal-difference targets in exploiting predicted experience for value learning.

## Metadata
- **Published**: 2026-08-11T02:27:26Z
- **Authors**: Jiazhuo Li, Linjiang Cao, Qi Liu, Xi Xiong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10386v1)