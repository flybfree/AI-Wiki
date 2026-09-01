---
title: ButterMamba: Butterworth-Enhanced Spatial-Temporal Mamba for Efficient Traffic Flow Prediction
published: 2026-08-30T08:46:11Z
authors: Limiao Zhang, Yuhui Lu, Jie Gao, Hao Jiang, Haiping Ma, Xingyi Zhang
url: http://arxiv.org/abs/2608.29658v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ButterMamba: Butterworth-Enhanced Spatial-Temporal Mamba for Efficient Traffic Flow Prediction

## Abstract
Accurate traffic flow prediction is fundamental to intelligent transportation systems, playing a pivotal role in urban mobility optimization and smart city development. While Graph Neural Networks (GNNs) integrated with time series forecasting have emerged as promising solutions, two critical limitations persist: (1) the quadratic complexity of attention-based architectures hinders real-time deployment in large-scale networks, and (2) high-frequency noise in sensor data significantly degrades prediction reliability. These challenges are particularly acute in metropolitan scenarios where both computational efficiency and noise robustness are paramount. To address these limitations, we introduce \textbf{ButterMamba}, a novel and efficient framework based on State Space Models (SSMs). ButterMamba consists of two key components: (1) a Butterworth Spectral Filtering module that preprocesses the data by removing high-frequency noise, allowing the model to focus on significant underlying trends, and (2) a Spatial-Temporal State Mixer that uses a parallel Mamba architecture to efficiently capture both long-range temporal dependencies and complex spatial correlations across the road network. By decoupling noise filtering from spatial-temporal modeling, ButterMamba achieves superior predictive accuracy with linear computational complexity. Extensive experiments on three public datasets demonstrate that ButterMamba not only outperforms existing state-of-the-art models in terms of prediction accuracy but also considerably reduces training time and memory usage.

## Metadata
- **Published**: 2026-08-30T08:46:11Z
- **Authors**: Limiao Zhang, Yuhui Lu, Jie Gao, Hao Jiang, Haiping Ma, Xingyi Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29658v1)