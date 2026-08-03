---
title: Don't Mix Rewards, Mix Policies: Policy Decomposition and Optimization for Multi-Reward RL
published: 2026-07-31T10:19:41Z
authors: Ruiming Liang, Yi Zhong, Yizhen Yuan, Yinan Zheng, Tianyi Tan, Tianyue Wang, Haiyun Guo, Jinqiao Wang, Xianyuan Zhan
url: http://arxiv.org/abs/2607.29246v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Don't Mix Rewards, Mix Policies: Policy Decomposition and Optimization for Multi-Reward RL

## Abstract
Modern large language models (LLMs) are expected not just to answer correctly, but to adapt their behavior to different human values and use cases. As a result, multi-reward reinforcement learning (RL) has become an increasingly important problem for LLMs, where each reward captures a different aspect of desired behavior. However, optimizing with multiple rewards suffers from a more severe alignment tax issue, where different optimization objectives can trade off or even conflict with each other, leading to unstable and inefficient post-training. In this work, we propose PRISM, a new multi-reward RL framework built upon the idea of policy-space decomposition and composition. Instead of compositing different rewards, PRISM optimizes a set of standalone positive policies and a global negative policy. This alleviates the potential conflict during multi-reward policy optimization, while enabling controllability during inference by flexible policy composition. Experiments on scientific reasoning, tool-use reasoning, and helpfulness-safety alignment show that PRISM consistently outperforms existing multi-reward RL baselines, with extra controllability for inference-time preference control.

## Metadata
- **Published**: 2026-07-31T10:19:41Z
- **Authors**: Ruiming Liang, Yi Zhong, Yizhen Yuan, Yinan Zheng, Tianyi Tan, Tianyue Wang, Haiyun Guo, Jinqiao Wang, Xianyuan Zhan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29246v1)