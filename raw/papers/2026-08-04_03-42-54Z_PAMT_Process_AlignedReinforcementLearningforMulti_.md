---
title: PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation
published: 2026-08-04T03:42:54Z
authors: Yongshi Ye, Biao Fu, Chongxuan Huang, Yidong Chen, Xiaodong Shi
url: http://arxiv.org/abs/2608.03077v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation

## Abstract
Multi-domain machine translation (MDMT) requires more than fluent generation: it demands domain-sensitive translation decisions such as domain disambiguation, terminology control, and stylistic adaptation. Large reasoning models (LRMs) make such decisions explicit through intermediate translation steps, but our analysis across 15 domains and four translation directions shows that this explicit reasoning is double-edged: it improves long-form and high-difficulty translation, yet often drifts in terminology-intensive and stylistically constrained settings. We trace this failure to a credit-assignment bottleneck: existing methods optimize final outputs or coarse trajectories, but cannot identify which translation steps actually help the final translation. To address this, we propose PAMT, a process-aligned training framework that combines cold-start domain-aware Long-CoT supervision with reinforcement learning. PAMT uses sequence-level format and outcome rewards for the final translation, together with a step-level process reward that measures how much each explicit translation step increases the likelihood of the reference translation. Across two backbones, PAMT improves over base models, outperforms MT-specialized baselines on average, and remains competitive with strong LLMs/LRMs across in-domain, OOD, and multilingual settings.

## Metadata
- **Published**: 2026-08-04T03:42:54Z
- **Authors**: Yongshi Ye, Biao Fu, Chongxuan Huang, Yidong Chen, Xiaodong Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03077v1)