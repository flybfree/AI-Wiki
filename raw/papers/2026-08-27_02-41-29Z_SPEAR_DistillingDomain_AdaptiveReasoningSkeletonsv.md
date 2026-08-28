---
title: SPEAR: Distilling Domain-Adaptive Reasoning Skeletons via Sequential Symbolic Alignment in Reinforcement Learning
published: 2026-08-27T02:41:29Z
authors: Zhuochun Li, Yuelyu Ji, Yiming Zeng, Daqing He
url: http://arxiv.org/abs/2608.26550v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPEAR: Distilling Domain-Adaptive Reasoning Skeletons via Sequential Symbolic Alignment in Reinforcement Learning

## Abstract
Reinforcement learning-based knowledge distillation has the potential to transfer complex reasoning from teacher to student models, yet it currently faces a critical dilemma: researchers must choose between sparse outcome-based rewards, which provide insufficient logical guidance, or expensive neural Process Reward Models (PRMs) for dense signals. We resolve this by introducing SPEAR (Symbolic Process Evaluation and Alignment Reward), a training-free and plug-and-play process reward method for sequence-level on-policy distillation. SPEAR projects natural-language reasoning traces into domain-adaptive symbolic milestones, providing an efficient proxy for process-level reasoning alignment. By utilizing the longest common subsequence (LCS) to align student explorations with teacher milestones, SPEAR provides a dense, order-aware reward signal that enforces logical consistency without the need for an external neural verifier. Our experiments across math, science, and commonsense reasoning tasks demonstrate that SPEAR effectively bridges the reasoning gap between student and teacher models via sequence-level distillation with efficient dense process rewards. Our code and data are available at: https://github.com/zhuochunli/SPEAR.

## Metadata
- **Published**: 2026-08-27T02:41:29Z
- **Authors**: Zhuochun Li, Yuelyu Ji, Yiming Zeng, Daqing He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26550v1)