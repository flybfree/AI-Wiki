---
title: Mitigating Exploration Bias in RL for Multi-Instruction Following
published: 2026-08-24T21:19:46Z
authors: Mian Zhang, Yueqin Yin, Kaiyu He, Peilin Wu, Xinlu Zhang, Mingyuan Zhou, Zhiyu Zoey Chen
url: http://arxiv.org/abs/2608.23830v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mitigating Exploration Bias in RL for Multi-Instruction Following

## Abstract
RL has emerged as a powerful paradigm for enhancing the instruction following capabilities of LLMs. While existing training recipes achieve substantial gains, we find that they suffer from exploration bias towards easy instructions when the training data has multiple instructions in a prompt. This bias is caused by two main reasons: 1) the policy model's initial ability to satisfy hard instructions is too low to trigger successful exploration during RL training, so the optimization is biased towards easy instructions; and 2) canonical RL training recipes typically employ a cumulative reward (the number of instructions fulfilled), treating all instructions equally, which biases the policy model towards fulfilling easy instructions to obtain the same amount of reward. To address these issues, we first propose two metrics to measure the exploration bias in instruction following and then introduce a two-stage framework to alleviate it: 1) Behavioral Bootstrapping, a lightweight rejection sampling fine-tuning stage before RL to activate hard instructions; and 2) Scarcity-Aware Rewards, a new RL reward function that assigns rewards to instructions based on their empirical scarcity. Experiments show that the proposed metrics are highly correlated with model performance, and our methods unleash the potential of RL training: our best models outperform the baselines by a significant margin across three verifiable instruction following benchmarks. We release codes at https://github.com/mianzhang/MulIF.

## Metadata
- **Published**: 2026-08-24T21:19:46Z
- **Authors**: Mian Zhang, Yueqin Yin, Kaiyu He, Peilin Wu, Xinlu Zhang, Mingyuan Zhou, Zhiyu Zoey Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23830v1)