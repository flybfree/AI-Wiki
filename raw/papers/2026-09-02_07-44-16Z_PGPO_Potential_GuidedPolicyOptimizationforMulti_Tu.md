---
title: PGPO: Potential-Guided Policy Optimization for Multi-Turn Agentic Tasks
published: 2026-09-02T07:44:16Z
authors: Yuyao Zheng, Haipeng Sun, Junwei Bao, Lemao Liu, Hongfei Jiang, Yang Song, Dejing Dou
url: http://arxiv.org/abs/2609.02236v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PGPO: Potential-Guided Policy Optimization for Multi-Turn Agentic Tasks

## Abstract
Group-based reinforcement learning (RL) has become an effective paradigm for LLM post-training, but in multi-turn agentic tasks with sparse terminal rewards, it often provides coarse credit for intermediate actions. To obtain more fine-grained credit assignment, recent work such as GiGPO introduces step-level advantages for intermediate actions. However, these step-level signals still rely on the final outcome of each individual trajectory. As a result, actions within failed trajectories can remain poorly differentiated, so effective actions can receive the same unfavorable credit as erroneous ones. In this work, we propose Potential-Guided Policy Optimization (PGPO) for multi-turn agentic tasks. PGPO estimates empirical state potentials from anchor-state-group return statistics within each rollout group. It then derives action advantages from potential differences between adjacent states, enabling cross-trajectory credit propagation. This provides finer-grained step-level credit assignment, especially within failed trajectories. Experiments on ALFWorld and WebShop show strong overall performance relative to recent group-based RL methods. Further analysis provides evidence that PGPO yields more informative failure-side credit signals with negligible training overhead.

## Metadata
- **Published**: 2026-09-02T07:44:16Z
- **Authors**: Yuyao Zheng, Haipeng Sun, Junwei Bao, Lemao Liu, Hongfei Jiang, Yang Song, Dejing Dou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02236v1)