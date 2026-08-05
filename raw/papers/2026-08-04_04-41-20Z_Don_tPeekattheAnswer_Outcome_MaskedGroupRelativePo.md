---
title: Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR
published: 2026-08-04T04:41:20Z
authors: Yongshi Ye, Liang Zhang, Yidong Chen, Xiaodong Shi, Biao Fu
url: http://arxiv.org/abs/2608.03119v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR

## Abstract
Reinforcement Learning with Verifiable Rewards (RLVR) improves LLM reasoning but typically relies on ground-truth (GT) answers, limiting scalability. Voting-based label-free RLVR replace gold supervision with answer-level consensus from model samples. However, collapse arises when the same answer-level signal is used both to estimate rewards and to drive token-level policy optimization, encouraging the model to directly reinforce answer tokens rather than improve reasoning. We propose OM-GRPO, a label-free RLVR framework that decouples reward estimation from policy optimization. OM-GRPO masks gradients on the answer span while retaining answer-level rewards through a soft consensus signal, shifting optimization pressure away from answer tokens. We further introduce Contrast-Augmented Reward, which refines reward estimation via low-cost pairwise comparisons over existing trajectories without additional rollouts. Across diverse reasoning benchmarks and three LLM backbones, OM-GRPO consistently outperforms existing label-free RLVR methods and matches supervised GT-reward training with stable optimization. This stability is particularly beneficial in the Test-Time Training setting, where OM-GRPO surpasses majority voting by 4.24 points.

## Metadata
- **Published**: 2026-08-04T04:41:20Z
- **Authors**: Yongshi Ye, Liang Zhang, Yidong Chen, Xiaodong Shi, Biao Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03119v1)