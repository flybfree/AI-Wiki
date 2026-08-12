---
title: Critic-Free Pretraining for Efficient Online Reinforcement Learning Fine-Tuning
published: 2026-08-11T04:38:32Z
authors: Daoyi Li, Yixian Zhang, Chao Yu, Wenbo Ding, Yu Wang
url: http://arxiv.org/abs/2608.10473v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Critic-Free Pretraining for Efficient Online Reinforcement Learning Fine-Tuning

## Abstract
Offline-to-online (O2O) reinforcement learning aims to leverage policies pretrained on static datasets while improving them through online interaction. However, directly reusing an offline-trained critic can hinder online fine-tuning: as the policy and data distribution change rapidly, value estimates inherited from offline training may become misaligned with the online environment, leading to inaccurate policy improvement and inefficient exploration. To address this problem, we introduce \textbf{C}ritic-\textbf{F}ree \textbf{P}retraining: an efficient paradigm that completely abandons the approach of offline critic training, allowing a freshly initialized critic to adapt without inheriting biased estimates. CFP is compatible with various mainstream O2O algorithms and consistently matches or improves upon conventional O2O algorithms across a diverse set of tasks, with particularly pronounced gains on several challenging tasks.

## Metadata
- **Published**: 2026-08-11T04:38:32Z
- **Authors**: Daoyi Li, Yixian Zhang, Chao Yu, Wenbo Ding, Yu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10473v1)