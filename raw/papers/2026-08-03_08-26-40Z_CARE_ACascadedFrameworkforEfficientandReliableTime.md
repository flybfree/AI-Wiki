---
title: CARE: A Cascaded Framework for Efficient and Reliable Time Series Anomaly Detection
published: 2026-08-03T08:26:40Z
authors: Zemin Chao, Qianhui Xu, Jianhe Cen, Guangzhi Ge, Xiao Chen, Hoangzhi Wang
url: http://arxiv.org/abs/2608.01885v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CARE: A Cascaded Framework for Efficient and Reliable Time Series Anomaly Detection

## Abstract
While deep learning models have achieved state-of-the-art performance in time series anomaly detection, their complex architectures incur substantial inference overhead. Existing methods typically apply a uniform inference strategy across all data points, which is inefficient given that anomalies are inherently scarce and the vast majority of temporal data consists of predictable normal patterns. To mitigate this bottleneck, we propose CARE, a model-agnostic cascaded inference framework that integrates a Lightweight Pre-filter Model (LPM) with an existing high-capacity Complex Detection Model (CDM). The LPM rapidly filters high-confidence normal samples using a Residual MLP AutoEncoder and a Normality-Conditioned Gating mechanism. Crucially, we introduce a Structure Attention module to explicitly capture channel-wise anomaly contributions, and optimize the gating network via a confidence-guided selective routing objective that learns reliable routing decisions to reduce unnecessary CDM invocations. Extensive experiments across eight real-world benchmarks demonstrate that CARE effectively isolates high-confidence normal samples. By routing only uncertain samples to the CDM, our framework achieves $2.7\times$ to $4.8\times$ inference speedup compared to the most accurate SOTA approaches, while still maintaining competitive detection quality.

## Metadata
- **Published**: 2026-08-03T08:26:40Z
- **Authors**: Zemin Chao, Qianhui Xu, Jianhe Cen, Guangzhi Ge, Xiao Chen, Hoangzhi Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01885v1)