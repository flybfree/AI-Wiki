---
title: DynG-Diff: A State-Aware Dynamic Guidance Diffusion Framework for Probabilistic Time Series Forecasting
published: 2026-09-02T03:50:39Z
authors: Zhente Zhang, Zhengwei Ni, Wei Fan
url: http://arxiv.org/abs/2609.02068v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DynG-Diff: A State-Aware Dynamic Guidance Diffusion Framework for Probabilistic Time Series Forecasting

## Abstract
Probabilistic multivariate time series (MTS) forecasting is crucial for modeling complex dynamical systems. However, existing diffusion-based methods rely on task-specific conditional paradigms that lack flexibility and struggle with inherent "information heterogeneity"--the significantly varying noise levels and evolutionary patterns across variables. To address this, we propose DynG-Diff, a variable-sensitive dynamic guidance diffusion framework for probabilistic multivariate time-series forecasting: (1) DynG-Diff adopts a two-stage separated training strategy and uses an unconditional diffusion backbone to model the joint distribution of multivariate time series. (2) DynG-Diff introduces a lightweight state-aware policy network that adaptively infers variable reliability from real-time noisy states and one-step denoising estimates, outputting a dynamic guidance strength matrix. (3) DynG-Diff mathematically formulates this dynamic weight as the local precision of the observation distribution, enabling precise guidance for high-confidence variables during inference while filtering out interference from anomalous noise. Extensive experiments on real-world benchmarks demonstrate competitive probabilistic forecasting performance against state-of-the-art conditional diffusion models and improved robustness under severe observation corruption.The implementation code is available at: https://github.com/TT-20011031/DynG-Diff

## Metadata
- **Published**: 2026-09-02T03:50:39Z
- **Authors**: Zhente Zhang, Zhengwei Ni, Wei Fan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02068v1)