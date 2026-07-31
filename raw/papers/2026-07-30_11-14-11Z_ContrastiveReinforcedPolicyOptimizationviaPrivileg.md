---
title: Contrastive Reinforced Policy Optimization via Privileged Self-Distillation
published: 2026-07-30T11:14:11Z
authors: Xingjian Wu, Junlin Liu, Xingchen Liu, Xuhang Zhu, Jianing Wang, Linsen Guo, Xiaoyu Li, Xuezhi Cao, Xunliang Cai
url: http://arxiv.org/abs/2607.28026v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Contrastive Reinforced Policy Optimization via Privileged Self-Distillation

## Abstract
Recent advances in post-training Large Language Models (LLMs) increasingly rely on Reinforcement Learning with Verifiable Rewards (RLVR) or On-Policy Self-Distillation (OPSD). While OPSD provides dense, logit-level supervision, it inherently suffers from exposure bias due to the privileged information of the self-teacher. In multi-turn agentic settings, this leads to reasoning route convergence and the loss of clear optimization directions. To tackle these challenges, we introduce Contrastive Reinforced Policy Optimization (CRPO), which reformulates agentic OPSD from a contrastive learning perspective. By leveraging predictive entropy to distinguish between positive positions (reflective exploration) and negative positions (exposure bias), CRPO conducts group-wise contrast to preserve reliable, fine-grained optimization signals. Extensive evaluations across 13 challenging reasoning and deep-search benchmarks demonstrate that CRPO consistently outperforms existing reinforcement learning and self-distillation baselines, significantly enhancing training stability and generalization in long-horizon interactions.

## Metadata
- **Published**: 2026-07-30T11:14:11Z
- **Authors**: Xingjian Wu, Junlin Liu, Xingchen Liu, Xuhang Zhu, Jianing Wang, Linsen Guo, Xiaoyu Li, Xuezhi Cao, Xunliang Cai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28026v1)