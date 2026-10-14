---
title: Failure Recovery via Belief Updates and World Modeling for Long-Horizon Agents
published: 2026-10-13T10:05:06Z
authors: Xiyang Wu, Zhichao Liu, Shengxin zhang, Zongxia Li, Ming Li, Tianyi Zhou, Dinesh Manocha
url: http://arxiv.org/abs/2610.18082v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Failure Recovery via Belief Updates and World Modeling for Long-Horizon Agents

## Abstract
Long-horizon agents often struggle to recover from failures whose causes lie several steps earlier, beyond what local reflection or backtracking can resolve. We introduce BELIEFWEAVER, a framework that combines persistent evidence across attempts with prospective reasoning over repair directions. It maintains a relational belief state over frontiers, attempts, observations, and checkpoints. Execution evidence updates related frontier priorities across attempts and rollback, while diagnostic evidence gates execution. An implicit world model (IWM) evaluates repair hypotheses, predicts progress, and identifies relations among frontiers to guide exploration. We further distill these recurring IWM reasoning components into a 9B student through supervised fine-tuning and on-policy distillation (OPD). Across three terminal-based benchmarks, BELIEFWEAVER improves aggregate final score by 5.1 percentage points over native Terminus-2 continuation, with positive trends in exploration efficiency. The distilled 9B student improves final score by 9.8 percentage points over the reported native baseline while reducing estimated teacher API cost by 54.8% relative to the matched teacher. These results show that persistent evidence and prospective reasoning can improve recovery in long-horizon agent tasks while substantially reducing reliance on teacher-model inference.

## Metadata
- **Published**: 2026-10-13T10:05:06Z
- **Authors**: Xiyang Wu, Zhichao Liu, Shengxin zhang, Zongxia Li, Ming Li, Tianyi Zhou, Dinesh Manocha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.18082v1)