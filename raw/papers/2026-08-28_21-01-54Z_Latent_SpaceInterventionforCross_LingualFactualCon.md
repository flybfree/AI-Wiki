---
title: Latent-Space Intervention for Cross-Lingual Factual Consistency: Consistency Improvements without Accuracy Drops
published: 2026-08-28T21:01:54Z
authors: Faeze Ghorbanpour, Constanza Fierro, Alexander Fraser, Anders Sogaard
url: http://arxiv.org/abs/2608.28860v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Latent-Space Intervention for Cross-Lingual Factual Consistency: Consistency Improvements without Accuracy Drops

## Abstract
Large Language Models (LLMs) often answer the same factual question differently across languages. We study whether cross-lingual latent-space intervention can reduce this inconsistency. We train layer-specific autoencoders on parallel multilingual representations and apply inference-time corrections to factual QA prompts. We find that latent intervention improves geometric alignment between languages, and that this improvement translates into consistent gains in cross-lingual consistency with English across both open-ended and multiple-choice QA formats, without degrading factual accuracy. In open-ended QA, Spearman's rank correlation between English and non-English languages improves substantially, with gains of 0.16 for English-Arabic and 0.20 for English-Russian pairs. In multiple-choice QA, answer agreement with English improves consistently across both KLAR and mParaRel. Ablations show that AE reconstruction yields consistent gains at no accuracy cost, while PCA projection contributes marginally, and mean-shift produces substantially larger consistency gains in open-ended QA at the cost of some accuracy.

## Metadata
- **Published**: 2026-08-28T21:01:54Z
- **Authors**: Faeze Ghorbanpour, Constanza Fierro, Alexander Fraser, Anders Sogaard
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28860v1)