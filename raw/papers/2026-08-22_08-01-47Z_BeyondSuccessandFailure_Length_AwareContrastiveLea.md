---
title: Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents
published: 2026-08-22T08:01:47Z
authors: Chengyang Gu, Le Zhang, Jingbo Zhou, Yize Chen, Yu Shi, Siqi Bao, Zheng-Fan Wu, Hua Wu, Hui Xiong
url: http://arxiv.org/abs/2608.21830v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents

## Abstract
Graphical User Interface (GUI) agents powered by Multimodal Large Language Models (MLLMs) have shown strong potential for automating tasks across diverse digital environments, where reinforcement learning (RL) has become a dominant training paradigm. However, widely used methods such as Group Relative Policy Optimization (GRPO) suffer from reward-gradient misalignment, leading to inefficient and unstable optimization. Recent work addresses this issue by reformulating RL with verifiable rewards (RLVR) as contrastive or classification-based objectives, which improve stability by eliminating problematic gradient behaviors. Despite this progress, existing contrastive RLVR methods rely primarily on outcome-level supervision and fail to capture fine-grained differences in trajectory quality within the same outcome category. In this paper, we propose Length-Aware Contrastive Learning for GUI Agents (LACL-GUI), a contrastive RLVR framework that incorporates trajectory-level quality signals into policy optimization. LACL-GUI introduces structured preferences within both successful and failed trajectories, encouraging concise successful executions and differentiating failure quality based on divergence from successful trajectories, while preserving optimization stability. Experiments on GUI agent benchmarks show that LACL-GUI provides more effective learning signals and consistently improves agent performance over prior methods, highlighting the value of trajectory-level supervision in contrastive RLVR.

## Metadata
- **Published**: 2026-08-22T08:01:47Z
- **Authors**: Chengyang Gu, Le Zhang, Jingbo Zhou, Yize Chen, Yu Shi, Siqi Bao, Zheng-Fan Wu, Hua Wu, Hui Xiong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21830v1)