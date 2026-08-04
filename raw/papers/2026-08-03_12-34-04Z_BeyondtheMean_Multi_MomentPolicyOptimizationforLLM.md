---
title: Beyond the Mean: Multi-Moment Policy Optimization for LLM Reasoning
published: 2026-08-03T12:34:04Z
authors: Yijun Zhang, Yule Xie, Jiaxin Ding, Xin Ding, Fan Xu, Haoxiang Zhang, Luoyi Fu
url: http://arxiv.org/abs/2608.02149v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond the Mean: Multi-Moment Policy Optimization for LLM Reasoning

## Abstract
Reinforcement learning has become a central paradigm for improving the reasoning capabilities of large language models. Existing methods generally aim to reduce the failure probabilities induced across problems. In this paper, we introduce a moment-based perspective on policy optimization for LLM reasoning by treating the failure probability of a randomly sampled problem as a random variable and characterizing optimization objectives through its moments. Under this perspective, many existing methods optimize only a single moment of the failure-probability distribution, leaving its broader distributional structure largely uncharacterized. We propose \textbf{M}ulti-\textbf{M}oment \textbf{P}olicy \textbf{O}ptimization (MMPO), a novel policy optimization framework that jointly minimizes multiple moments of the failure-probability distribution. MMPO admits a direct operational interpretation as minimizing the expected truncated time required to obtain the first successful response. Beyond MMPO, we further develop a general moment-transformation framework that systematically induces different moment profiles and provides a unified view of a broader family of policy optimization objectives. Experiments across five mathematical reasoning benchmarks and models of different scales demonstrate that MMPO consistently outperforms strong baselines. We hope this moment-based perspective offers new insights into the design of policy optimization objectives for LLM reasoning.

## Metadata
- **Published**: 2026-08-03T12:34:04Z
- **Authors**: Yijun Zhang, Yule Xie, Jiaxin Ding, Xin Ding, Fan Xu, Haoxiang Zhang, Luoyi Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02149v1)