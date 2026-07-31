---
title: TAPO: Transition-Aware Policy Optimization for LLM Agents
published: 2026-07-30T10:17:55Z
authors: Cong Li, Peixi Peng, Yisen Zhao, Xinyu Hu, Shudong Liu, Zhan Su, Zhuojian Li
url: http://arxiv.org/abs/2607.27973v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TAPO: Transition-Aware Policy Optimization for LLM Agents

## Abstract
Recently, Reinforcement Learning (RL) has emerged as a crucial paradigm for the post-training of Large Language Model (LLM) agents. However, existing methods predominantly rely on sparse task rewards for policy optimization, failing to fully exploit another class of inherently dense supervisory signals naturally present during online interaction: environmental feedback following action execution. Recent theoretical studies suggest that generalization in multi-step, goal-oriented tasks hinges on predictive knowledge of environmental consequences. Inspired by this, we propose TAPO: Transition-Aware Policy Optimization for LLM Agents, a unified training framework that alternates between policy optimization and transition supervision. Beyond standard RL updates, TAPO repurposes rollout data to apply action-conditioned next-observation prediction supervision on a shared backbone model. This approach enhances the model's sensitivity to environmental transition dynamics and action consequences while concurrently optimizing the policy. It serves as a computationally lightweight, plug-and-play enhancement module for existing agent RL algorithms, requiring no additional expert data, extra sampling costs, or inference-time overhead. We conduct systematic experiments on WebShop and ALFWorld, integrating foundation models of various scales with different policy optimization algorithms. Empirical results demonstrate that TAPO consistently improves task performance over pure policy optimization baselines.

## Metadata
- **Published**: 2026-07-30T10:17:55Z
- **Authors**: Cong Li, Peixi Peng, Yisen Zhao, Xinyu Hu, Shudong Liu, Zhan Su, Zhuojian Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27973v1)