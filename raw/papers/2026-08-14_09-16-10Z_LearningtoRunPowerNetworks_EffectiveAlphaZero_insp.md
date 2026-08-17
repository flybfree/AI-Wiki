---
title: Learning to Run Power Networks: Effective AlphaZero-inspired Topological Control
published: 2026-08-14T09:16:10Z
authors: Lukas Zetto, Benjamin Schäfer, Qiong Huang
url: http://arxiv.org/abs/2608.14114v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Run Power Networks: Effective AlphaZero-inspired Topological Control

## Abstract
As the integration of volatile renewable energy sources increases the strain on modern power grids, the use of Reinforcement Learning (RL) for autonomous topological reconfiguration has emerged as a promising research field to keep strained grids stable and operational. Compared to traditional redispatching measures, topological actions offer a cheaper and more cost-effective way to manage grid congestion. However, their implementation is hindered by a vast combinatorial action space and strict operational constraints. This paper investigates the effectiveness of model-based AlphaZero-inspired approaches that utilize Monte Carlo Tree Search (MCTS) for proactive grid management. We systematically evaluate how reward functions, observation density, and search guidance influence an agent's survivability. Our results demonstrate that the optimized AlphaZero approach achieves a peak survivability of 98.43%, significantly outperforming the proximal policy optimization (PPO) variant. We find that conducting the MCTS without guidance from a prior learned policy or value function can enhance training efficiency, and that a straightforward binary survival reward provides more effective search guidance than complex, multi-objective functions. Our findings demonstrate that while AlphaZero is a powerful framework for topological control, pure reinforcement learning is not sufficient; rather, an effective and reliable system requires a 'minimalist' integration of domain-specific heuristics, binary rewards, and a restricted observation space of line loads.

## Metadata
- **Published**: 2026-08-14T09:16:10Z
- **Authors**: Lukas Zetto, Benjamin Schäfer, Qiong Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14114v1)