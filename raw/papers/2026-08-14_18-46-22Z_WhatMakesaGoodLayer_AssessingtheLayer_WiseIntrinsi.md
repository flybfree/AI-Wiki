---
title: What Makes a Good Layer? Assessing the Layer-Wise Intrinsic Properties of Music Foundation Models
published: 2026-08-14T18:46:22Z
authors: Angelos-Nikolaos Kanatas, Yuexuan Kong, Pablo Alonso-Jiménez, Xavier Serra, Dmitry Bogdanov
url: http://arxiv.org/abs/2608.14819v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Makes a Good Layer? Assessing the Layer-Wise Intrinsic Properties of Music Foundation Models

## Abstract
Music foundation models are commonly used as frozen audio feature extractors, yet selecting which layer to extract from remains largely heuristic. Current practice defaults to fixed depths or multi-layer fusion, with limited understanding of why certain layers transfer better across downstream tasks or how representation quality varies with depth and pre-training paradigm. We conduct a systematic layer-wise analysis of 12 music foundation models spanning three pre-training paradigms (masked modeling, autoregressive modeling, and contrastive learning), characterizing their hidden representations through intrinsic geometric and transformation-based properties. Correlating label-free representation-quality metrics with layer-wise performance across 15 downstream tasks, we find that several metrics track layer quality for genre classification, emotion recognition, automatic tagging, and beat tracking, albeit with varying strength across tasks and pre-training paradigms. However, all metrics fail on tonal tasks such as key estimation and chord recognition, indicating that no single property serves as a general proxy for representation quality across music information retrieval tasks. To address this gap, we introduce a pitch-transposition equivariance measure that captures properties missed by these standard metrics, providing a consistent indicator of tonal quality across model families. Finally, we show that intrinsic metrics can serve as effective proxies for layer selection, matching or outperforming trainable multi-layer fusion methods, particularly in limited-data settings.

## Metadata
- **Published**: 2026-08-14T18:46:22Z
- **Authors**: Angelos-Nikolaos Kanatas, Yuexuan Kong, Pablo Alonso-Jiménez, Xavier Serra, Dmitry Bogdanov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14819v1)