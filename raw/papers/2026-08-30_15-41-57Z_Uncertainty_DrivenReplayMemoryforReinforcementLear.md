---
title: Uncertainty-Driven Replay Memory for Reinforcement Learning
published: 2026-08-30T15:41:57Z
authors: Sheeraja Rajakrishnan, Alexander G. Ororbia, Travis Desell, Daniel E. Krutz
url: http://arxiv.org/abs/2608.29860v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Uncertainty-Driven Replay Memory for Reinforcement Learning

## Abstract
Uncertainty estimation provides promising capabilities for reinforcement learning (RL) agents. Notably, estimating uncertainty can reduce the training time and enable agents to obtain greater rewards over time by exploiting information related to whether an action would facilitate exploration of portions of an environment that are well-known versus those that are relatively unknown. In this work, we propose a novel formulation of the experience replay buffer commonly used in RL that we call uncertainty-driven replay memory (UDRM), which entails an update scheme for internally stored memories based on uncertainty estimates obtained by an RL model during training. In contrast to existing forms of RL, which typically use temporal difference error or the distribution of transitions to update the replay memory buffer and train RL controllers, our scheme biases the memory buffer to store more uncertain transitions that will improve an RL agent's generalization throughout training. Experimental results demonstrate that our proposed uncertainty-aware replay buffer enables an RL agent to obtain higher rewards during training compared to other existing uncertainty-aware RL frameworks.

## Metadata
- **Published**: 2026-08-30T15:41:57Z
- **Authors**: Sheeraja Rajakrishnan, Alexander G. Ororbia, Travis Desell, Daniel E. Krutz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29860v1)