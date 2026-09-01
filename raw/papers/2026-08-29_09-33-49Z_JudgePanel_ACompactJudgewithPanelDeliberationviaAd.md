---
title: JudgePanel: A Compact Judge with Panel Deliberation via Adaptive Multi-Reward Reinforcement Learning
published: 2026-08-29T09:33:49Z
authors: Yiyue Qian, Shinan Zhang, Huan Song, Hannah Marlowe
url: http://arxiv.org/abs/2608.29168v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# JudgePanel: A Compact Judge with Panel Deliberation via Adaptive Multi-Reward Reinforcement Learning

## Abstract
The LLM-as-a-Judge paradigm has emerged as a scalable alternative to human evaluation. However, single-model judges are limited by their inherent model biases, while multi-agent evaluation protocols that mitigate this through diverse deliberation are prohibitively expensive at inference time. To this end, we propose \textbf{\modelname}, which equips a compact \underline{Judge} model with multi-agent \underline{Panel} deliberation capability. Specifically, we first train on panel deliberation traces from an ensemble of strong evaluators, capturing structured patterns of discussion, disagreement, and resolution. To further improve judgment quality beyond SFT, we introduce \textit{AdaReward}, an adaptive multi-reward RL algorithm that dynamically rebalances reward component weights as different objectives saturate at different rates during RL training. For practical deployment, we further design a lightweight domain specialization module for rapid adaptation to new evaluation domains with few hundred labeled samples. As a result, (i) \textit{Novel}: the first framework to equip a single compact judge with multi-agent panel deliberation capability at single-model inference cost; (ii) \textit{Effective \& Reliable}: JudgePanel with a 14B backbone outperforms judge-specialized models up to 70B across four evaluation benchmarks, demonstrates strong position consistency, and rapidly specializes to new domains with few hundred samples.

## Metadata
- **Published**: 2026-08-29T09:33:49Z
- **Authors**: Yiyue Qian, Shinan Zhang, Huan Song, Hannah Marlowe
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29168v1)