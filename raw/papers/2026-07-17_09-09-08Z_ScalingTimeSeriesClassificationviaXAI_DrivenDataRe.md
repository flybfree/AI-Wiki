---
title: Scaling Time Series Classification via XAI-Driven Data Reduction
published: 2026-07-17T09:09:08Z
authors: Davide Italo Serramazza, Thach Le Nguyen, Georgiana Ifrim
url: http://arxiv.org/abs/2607.15774v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scaling Time Series Classification via XAI-Driven Data Reduction

## Abstract
Explainable AI (XAI) for time series has seen significant algorithmic growth, but its utility in providing measurable performance gains for downstream tasks remains under-explored. This paper bridges this gap by introducing drXAI, a novel methodology that repurposes XAI attribution methods for effective data reduction in Time Series Classification (TSC). The core challenge in modern TSC is scalability; state-of-the-art models, such as Transformers, exhibit quadratic complexity relative to sequence length and linear complexity relative to the number of channels. This renders them computationally prohibitive for massive datasets. drXAI addresses this by using a fast, GPU-accelerated classifier (Hydra) to generate local attributions. We aggregate these into global feature importance scores and employ an automated elbow-cut heuristic to select the most salient features without requiring manual thresholds.   We evaluate our approach on both synthetic and real-world univariate and multivariate datasets. On synthetic benchmarks, drXAI successfully recovers ground-truth features where traditional baselines fail. On real-world data, drXAI achieves between 80% and 90% data reduction while maintaining classification accuracy comparable to models trained on the full dataset. Most importantly, we show that drXAI allows resource-intensive models like ConvTran to scale to datasets that were previously inaccessible due to memory constraints. Our results show the benefits of using XAI not just for interpretability, but as a robust tool for feature selection and scalability in time series analysis. All our code and data are openly available.

## Metadata
- **Published**: 2026-07-17T09:09:08Z
- **Authors**: Davide Italo Serramazza, Thach Le Nguyen, Georgiana Ifrim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.15774v2)