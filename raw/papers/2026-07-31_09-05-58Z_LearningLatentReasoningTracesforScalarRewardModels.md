---
title: Learning Latent Reasoning Traces for Scalar Reward Models End-to-End
published: 2026-07-31T09:05:58Z
authors: Sanwoo Lee, Clive Bai, Hsiu-Yuan Huang, Kun Liang, Weijie Liu, Yunfang Wu
url: http://arxiv.org/abs/2607.29185v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Latent Reasoning Traces for Scalar Reward Models End-to-End

## Abstract
Reward models (RMs) are central to aligning large language models with human preferences via reinforcement learning. Although traditional scalar RMs enable efficient and probabilistic reward modeling, they rely on superficial cues that fail to generalize to complex or out-of-distribution (OOD) tasks. Conversely, generative RMs leverage extensive reasoning to improve robustness on challenging tasks, but their natural language-based scores lack the numerical flexibility and probabilistic interpretability that scalar RMs offer. While recent approaches combine both paradigms through off-policy multi-task learning, such parallel optimization does not guarantee that generated reasoning traces actively align with or benefit downstream scalar reward prediction. To address this mismatch, we propose LatentRM, a reward modeling framework that learns intermediate reasoning traces as discrete latent variables to explicitly maximize the likelihood of downstream scalar rewards. Through on-policy optimization of the latent reasoning space end-to-end, LatentRM tightly couples deep reasoning-based evaluation with precise scoring. Extensive validations on in-distribution and OOD datasets and RLHF show that LatentRM outperforms scalar, generative, and hybrid RMs on preference modeling and policy alignment across tasks ranging from open-ended conversation to complex reasoning.

## Metadata
- **Published**: 2026-07-31T09:05:58Z
- **Authors**: Sanwoo Lee, Clive Bai, Hsiu-Yuan Huang, Kun Liang, Weijie Liu, Yunfang Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29185v1)