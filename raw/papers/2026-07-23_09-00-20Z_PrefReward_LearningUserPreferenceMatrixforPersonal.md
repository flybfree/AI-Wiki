---
title: PrefReward: Learning User Preference Matrix for Personalized Text Generation
published: 2026-07-23T09:00:20Z
authors: Yue Wu, Chengbing Wang, Yimeng Bai, Xiaoyan Zhao, Yang Zhang, Fuli Feng
url: http://arxiv.org/abs/2607.21067v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PrefReward: Learning User Preference Matrix for Personalized Text Generation

## Abstract
Large Language Models (LLMs) have demonstrated remarkable ability in generating personalized content by leveraging user histories and contextual cues. However, most existing personalization approaches rely on implicit representations within model parameters, making it difficult to interpret user-specific preferences or effectively handle long-context dependencies. To address these challenges, we propose PrefReward, a novel preference-aware generative framework that explicitly models user styles through a structured preference matrix and integrates it into the decoding process as a reward signal. PrefReward consists of two stages: (1) extracting a user-specific preference matrix that summarizes individual stylistic tendencies, and (2) using the matrix to guide generation via a KL-divergence-based reward function. Experiments on the LongLaMP dataset show that PrefReward outperforms non-personalized and retrieval-based baselines in both generation quality and personalization interpretability.

## Metadata
- **Published**: 2026-07-23T09:00:20Z
- **Authors**: Yue Wu, Chengbing Wang, Yimeng Bai, Xiaoyan Zhao, Yang Zhang, Fuli Feng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21067v1)