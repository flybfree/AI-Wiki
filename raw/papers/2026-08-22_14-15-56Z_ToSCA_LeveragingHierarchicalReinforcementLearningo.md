---
title: ToSCA: Leveraging Hierarchical Reinforcement Learning on Temporal and Strategic Abstractions of Conversational Agents
published: 2026-08-22T14:15:56Z
authors: Xiaoyu Wang, Qingqing Gu, Yue Zhao, Teng Chen, Yuqi Cao, Xiaokai Chen, Hongyan Li, Luo Ji
url: http://arxiv.org/abs/2608.21969v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ToSCA: Leveraging Hierarchical Reinforcement Learning on Temporal and Strategic Abstractions of Conversational Agents

## Abstract
Humans have multiple levels of temporal abstractions on daily interaction and thinking, such as concept perception and strategic planning. Inspired by this nature, we propose a two-level hierarchical reinforcement learning (RL) framework for conversational agents, bridging the gap between previous token-level or utterance-level RL methods. Developed on a two-level MDP, the token-level response decoding is conditioned on the utterance-level action, the explicit textual strategies. Based on theoretical derivation and efficiency consideration, we use DQN to solve the high-level critic and PPO to solve the low-level actor-critic. To further alleviate the reward sparsity and facilitate the convergence, we also design the dual-granularity reward mechanism, in which the utterance-level satisfaction score is integrated with token-level intrinsic motivation and K-L penalty. Experiments on both daily and emotional support conversations show that our method outperforms versatile baselines in strategy determination and response quality. Our implementation is available at https://github.com/AaronJi/ToSCA.

## Metadata
- **Published**: 2026-08-22T14:15:56Z
- **Authors**: Xiaoyu Wang, Qingqing Gu, Yue Zhao, Teng Chen, Yuqi Cao, Xiaokai Chen, Hongyan Li, Luo Ji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21969v1)