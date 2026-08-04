---
title: HindSearch: Trajectory-Level Hindsight Critique for Search-Augmented Reinforcement Learning
published: 2026-08-03T02:06:29Z
authors: Haowei Liu, Jiamian Wang, Hsin-Tai Wu, Zhiqiang Tao, Yi Fang
url: http://arxiv.org/abs/2608.01597v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HindSearch: Trajectory-Level Hindsight Critique for Search-Augmented Reinforcement Learning

## Abstract
Search-augmented LM agents are typically trained with a binary exact-match reward, which throws away most of what a failed trajectory tells us about why it failed. We introduce HindSearch, a hindsight self-distillation procedure for GRPO: after each rollout, a frozen judge writes a short critique of every failed trajectory using the gold answer, and the critique supplies an auxiliary on-policy distillation signal on the student's search actions. On the standard seven-benchmark suite with Qwen2.5-3B-Instruct, HindSearch reaches 39.4% average EM, outperforming prior search-RL baselines. Removing the judge's access to the gold answer erases most of the gain, isolating hindsight as the source of the improvement.

## Metadata
- **Published**: 2026-08-03T02:06:29Z
- **Authors**: Haowei Liu, Jiamian Wang, Hsin-Tai Wu, Zhiqiang Tao, Yi Fang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01597v1)