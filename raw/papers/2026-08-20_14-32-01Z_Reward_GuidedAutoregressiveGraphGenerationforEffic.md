---
title: Reward-Guided Autoregressive Graph Generation for Efficient Multi-Agent Communication Topology Design
published: 2026-08-20T14:32:01Z
authors: Poomphob Suwannapichat, Boonyarit Changaival, Caesar Wu, Pascal Bouvry
url: http://arxiv.org/abs/2608.20099v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reward-Guided Autoregressive Graph Generation for Efficient Multi-Agent Communication Topology Design

## Abstract
LLM-based Multi-Agent Systems (MAS) achieve strong performance on complex reasoning tasks by coordinating multiple agents, but at the cost of substantial token consumption. Recent work on automatic topology design, ARG-Designer, has reframed this problem as autoregressive graph generation. However, its training objective provides no explicit incentive for the model to generate sparse and efficient topologies. We address this limitation by introducing a Reward-Guided Autoregressive Graph Generation (RGA-Designer) inspired by Reinforcement Learning from Human Feedback (RLHF). We train a reward model that jointly captures task correctness and structural compactness, and then fine-tune the pretrained graph generator using the reward model as feedback. Our method preserves task accuracy at the level of ARG-Designer while reducing token consumption by an average of 20.5%.

## Metadata
- **Published**: 2026-08-20T14:32:01Z
- **Authors**: Poomphob Suwannapichat, Boonyarit Changaival, Caesar Wu, Pascal Bouvry
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20099v1)