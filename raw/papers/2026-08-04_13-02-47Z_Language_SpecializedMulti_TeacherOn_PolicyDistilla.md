---
title: Language-Specialized Multi-Teacher On-Policy Distillation for Multilingual LLM-Based ASR
published: 2026-08-04T13:02:47Z
authors: Yuan Xie, Jiaqi Song, Xianliang Wang, Ming Lei, Jie Gao, Jie Wu
url: http://arxiv.org/abs/2608.03610v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Language-Specialized Multi-Teacher On-Policy Distillation for Multilingual LLM-Based ASR

## Abstract
Modern LLM-based ASR systems have established multilingual capability as a standard feature, leveraging large-scale multilingual corpora and LLMs' cross-lingual knowledge to achieve competitive performance across multilingual benchmarks. However, joint modeling of languages with heterogeneous acoustic, phonological, and lexical characteristics inevitably introduces optimization conflicts, undermining language-wise specialization. To address this challenge, we propose Language-Specialized Multi-Teacher On-Policy Distillation (LS-MOPD), which decouples language-specific knowledge acquisition from multilingual capability integration: language-specialized teachers are independently optimized via reinforcement learning (RL), after which their expertise is integrated into a generalist multilingual student through language routing and token-level multi-teacher distillation, thereby reducing direct cross-lingual optimization conflicts. We further explore two acoustic-prefix configurations, static and dynamic, to examine how teacher--student prefix consistency influences the efficacy of on-policy distillation. Experiments on benchmarks covering Mandarin, Mandarin subdialects, Cantonese, and English demonstrate that LS-MOPD substantially outperforms RL baselines and consistently surpasses the empirical performance envelope defined by best-performing RL teachers, revealing its potential to generalize beyond all teachers in multilingual ASR.

## Metadata
- **Published**: 2026-08-04T13:02:47Z
- **Authors**: Yuan Xie, Jiaqi Song, Xianliang Wang, Ming Lei, Jie Gao, Jie Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03610v1)