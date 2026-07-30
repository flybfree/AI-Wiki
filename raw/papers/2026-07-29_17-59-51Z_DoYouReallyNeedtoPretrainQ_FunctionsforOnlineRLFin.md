---
title: Do You Really Need to Pretrain Q-Functions for Online RL Fine-Tuning?
published: 2026-07-29T17:59:51Z
authors: Perry Dong, Ron Polonsky, Dorsa Sadigh, Chelsea Fin
url: http://arxiv.org/abs/2607.27203v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do You Really Need to Pretrain Q-Functions for Online RL Fine-Tuning?

## Abstract
Pre-training followed by fine-tuning has become the dominant recipe for learning performant policies, and in value-based reinforcement learning (RL) this raises a natural question: given a pretrained policy, should the Q-function be pretrained on offline data too? Conventional wisdom suggests it should, but recent results show that online RL with a randomly-initialized Q-function can result in highly performant and reliable policies without needing to pretrain the Q-function. In this paper, we systematically study whether pretraining the Q-function actually helps when fine-tuning on top of a pretrained base policy. We find, surprisingly, that naive Q-function pretraining often provides little benefit over random initialization. We show this stems from a fundamental mismatch: the Q-function learned during pretraining targets the pretrained policy's Q-function, not the Q-function that online fine-tuning converges to, and this gap persists even after offline value maximization. Motivated by this finding, we propose Initialization via Policy Ensemble (IPE), a simple method that trains multiple diverse policies and uses their pooled rollouts to bootstrap the Q-function learning in online RL. Across a suite of challenging continuous control benchmarks, IPE yields an average 1.26x improvement in fine-tuning performance over naive Q-function pre-training.

## Metadata
- **Published**: 2026-07-29T17:59:51Z
- **Authors**: Perry Dong, Ron Polonsky, Dorsa Sadigh, Chelsea Fin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27203v1)