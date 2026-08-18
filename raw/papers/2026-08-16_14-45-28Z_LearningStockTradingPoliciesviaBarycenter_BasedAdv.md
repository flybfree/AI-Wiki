---
title: Learning Stock Trading Policies via Barycenter-Based Adversarial Inverse Reinforcement Learning
published: 2026-08-16T14:45:28Z
authors: Arishi Orra, Himanshu Choudhary, Manoj Thakur
url: http://arxiv.org/abs/2608.15770v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Stock Trading Policies via Barycenter-Based Adversarial Inverse Reinforcement Learning

## Abstract
Designing effective trading strategies using reinforcement learning remains challenging due to delayed and noisy rewards, poor exploration, and the difficulty of enforcing explicit risk constraints. In this work, we propose BRaG, a barycenter-based adversarial inverse reinforcement learning framework for stock trading that learns trading behavior from multiple heterogeneous expert strategies. BRaG aggregates expert demonstrations using a performance-weighted Wasserstein barycenter, yielding a stable pseudo-expert representation that captures shared structure across diverse trading styles. This representation is used to pretrain a trading policy via adversarial imitation learning, which alleviates unstable exploration during reinforcement learning. The pretrained policy is subsequently refined using reinforcement learning with true market rewards. To ensure risk-aware decision-making, BRaG incorporates control barrier functions that constrain action execution and regularize policy learning to satisfy drawdown limits. We evaluate the proposed approach on four major global equity markets, including the US, UK, Indian, and Taiwanese indices. Across all the markets, the proposed approach achieves stronger performance than both classical trading rules and recent deep reinforcement learning methods, while exhibiting more stable risk characteristics.

## Metadata
- **Published**: 2026-08-16T14:45:28Z
- **Authors**: Arishi Orra, Himanshu Choudhary, Manoj Thakur
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15770v1)