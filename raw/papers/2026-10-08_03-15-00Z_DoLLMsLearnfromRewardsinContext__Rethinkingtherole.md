---
title: Do LLMs Learn from Rewards in Context? : Rethinking the role of reward in In-Context Reinforcement Learning
published: 2026-10-08T03:15:00Z
authors: Minchan Kwon, Seunghee Koh, Sunghyun Baek, Minsung Bae, Junmo Kim
url: http://arxiv.org/abs/2610.11152v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do LLMs Learn from Rewards in Context? : Rethinking the role of reward in In-Context Reinforcement Learning

## Abstract
LLM agents increasingly improve at inference time by accumulating experience in context rather than by updating parameters. This process is often described as in-context reinforcement learning (ICRL). Whether in-context learning (ICL) can actually play the role of RL, however, has not been tested. We study this question in its simplest form, direct ICRL, where the model conditions directly on raw trajectory-reward pairs, and ask whether the reward acts as a learning signal. Through controlled experiments on four benchmarks across six models, we find that the reward is read, but its effect is small: flipping, randomizing, or removing the reward leaves the improvement curve almost unchanged, and this holds even under meta-prompts that explicitly instruct the model to explore, exploit, or reason over rewards. Trajectories drive improvement, but not through their semantic content: shuffled or corrupted trajectories work as well as real ones. These patterns closely mirror those known in ICL, suggesting that direct ICRL is better understood as a special case of ICL than as inference-time RL. This reframing has implications for agent memory design: ICL factors such as input distribution and demonstrations may matter more than RL elements such as reward shaping and exploration.

## Metadata
- **Published**: 2026-10-08T03:15:00Z
- **Authors**: Minchan Kwon, Seunghee Koh, Sunghyun Baek, Minsung Bae, Junmo Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11152v1)