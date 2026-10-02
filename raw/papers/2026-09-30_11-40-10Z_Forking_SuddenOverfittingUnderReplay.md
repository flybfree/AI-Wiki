---
title: Forking: Sudden Overfitting Under Replay
published: 2026-09-30T11:40:10Z
authors: Shanbin Yu, Shaoyang Guo, Haoran Zhao, Danni Yu, Ziming Liu
url: http://arxiv.org/abs/2610.00394v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Forking: Sudden Overfitting Under Replay

## Abstract
This paper studies forking, a generalization failure discovered in NanoGPT autoresearch. Under data replay, models with an over-encoding n-gram memory branch show a sharp separation of training and validation loss at epoch boundaries, resembling the shape of forks. We study this phenomenon in a controlled vanilla NanoGPT setting and reproduce it in a DeepSeek-style model with Engram. Mechanistically, repeated updates sharpen the continuations observed in training while suppressing the probability of unseen continuations, whose loss grows with each pass. The n-gram module creates weakly interacting context-specific subspaces, amplifying this effect. Low-frequency contexts contribute most of the gap, whereas larger training budgets and heavily crowded tables suppress it. We also observe forking in short-budget, heavily repeated SFT and RL-like regimes. The contributions of this paper are twofold: (1) Forking reveals yet another curious phenomenon in deep learning, in addition to grokking and double descent. (2) Forking is an unexpected and unpleasant by-product of tricks proposed by autoresearch agents. While these agents produce an enormous number of results that seem useful, we should always be careful with their results.

## Metadata
- **Published**: 2026-09-30T11:40:10Z
- **Authors**: Shanbin Yu, Shaoyang Guo, Haoran Zhao, Danni Yu, Ziming Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00394v1)