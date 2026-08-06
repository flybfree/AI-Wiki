---
title: Predict, Then Retrieve: Cross-Instance Future-State Retrieval from Video Prefixes
published: 2026-08-05T04:12:00Z
authors: Quynh Vo, Thong Nguyen, Vinh-Hien Do, Cong-Duy Nguyen, Anh-Tuan Luu
url: http://arxiv.org/abs/2608.04426v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Predict, Then Retrieve: Cross-Instance Future-State Retrieval from Video Prefixes

## Abstract
We introduce Predictive State Retrieval (PSR), a task in which a model observes a short video prefix and a temporal question about an object's future state, then retrieves instances from other videos or images that depict that state. Unlike action anticipation, which predicts a label, moment retrieval, which localizes an observed event within a video, or video generation, which synthesizes pixels, PSR combines anticipation with cross-instance retrieval across multiple temporal horizons. We construct a benchmark from four datasets with graded, human-validated ground truth, difficulty tiers, and an oracle ceiling. We also propose LFTR, a lightweight retriever with frozen encoders that predicts a question- and horizon-conditioned future latent and matches it in complementary semantic and visual spaces. A ceiling decomposition reveals a clear bottleneck: the true future state is highly retrievable once specified, whereas every predictor we evaluate, including a large multimodal language model with access to the prefix frames, remains far below the oracle. Thus, forecasting rather than perception is the central learnable challenge. LFTR narrows this gap at substantially lower inference cost, and ablations attribute its gains to cross-space fusion and hard-negative training rather than latent rollout. We release the benchmark, code, and evaluation scripts.

## Metadata
- **Published**: 2026-08-05T04:12:00Z
- **Authors**: Quynh Vo, Thong Nguyen, Vinh-Hien Do, Cong-Duy Nguyen, Anh-Tuan Luu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04426v1)