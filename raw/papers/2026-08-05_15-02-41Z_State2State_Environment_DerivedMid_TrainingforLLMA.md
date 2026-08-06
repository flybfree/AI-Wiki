---
title: State2State: Environment-Derived Mid-Training for LLM Agents
published: 2026-08-05T15:02:41Z
authors: Xuanyu Lei, Yiqi Zhu, Chenliang Li, Kaiming Liu, Peng Li, Ming Yan, Jieping Ye, Ya-Qin Zhang, Yang Liu
url: http://arxiv.org/abs/2608.04934v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# State2State: Environment-Derived Mid-Training for LLM Agents

## Abstract
Training LLM agents commonly relies on supervised fine-tuning from expert trajectories or online reinforcement learning over human-specified tasks with handcrafted verifiers. Though effective, both remain bottlenecked by externally specified tasks and supervision signals, limiting the scalability and diversity of agent training. We study an environment learning paradigm in which agents acquire interaction and manipulation capabilities solely through environment interaction, without externally specified tasks. We propose State2State, an environment-derived mid-training method that converts explored environment states into training objectives, challenging agents to reach a specified target state. By deriving tasks from environment exploration and verifying success through rule-based state matching, State2State provides scalable and verifiable training objectives without expert supervision or manual task design. Experiments on ALFWorld and ScienceWorld show that State2State improves agent performance as a standalone environment-learning stage in most settings. As initialization for downstream RL, it further improves final performance and learning efficiency, with promising evidence of cross-environment generalization.

## Metadata
- **Published**: 2026-08-05T15:02:41Z
- **Authors**: Xuanyu Lei, Yiqi Zhu, Chenliang Li, Kaiming Liu, Peng Li, Ming Yan, Jieping Ye, Ya-Qin Zhang, Yang Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04934v1)