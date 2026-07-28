---
title: Impute On-Demand: Adaptive Correlated Time Series Imputation for Changing Environments
published: 2026-07-26T07:08:00Z
authors: Zhichen Lai, Huan Li, Dalin Zhang, Dong Gong, Lina Yao, Christian S. Jensen
url: http://arxiv.org/abs/2607.23503v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Impute On-Demand: Adaptive Correlated Time Series Imputation for Changing Environments

## Abstract
Internet of Things (IoT) applications generate vast amounts of Correlated Time Series (CTS) data that often contain missing values and require imputation. Existing methods emphasize accuracy but often lack adaptability to changing IoT environments: they are vulnerable to sensor failures, cannot selectively impute only incomplete sensors, and use static architectures that do not adapt to resource availability. To address these limitations, we propose AdaCTSi, an adaptive CTS imputer for changing environments. AdaCTSi combines a One-shot Temporal Convolutional Network with a Learned Time-Sensor Index Table to extract and decouple complex spatio-temporal features into sensor-wise embeddings, enabling adaptation to varying sensor subsets. Sparse Spatial Attention efficiently extracts dynamic spatial correlations, while Correlation-Weighted Sensor Selection selects informative sensors to provide sufficient spatial context. Experiments with twelve baseline methods, three adaptability scenarios, and five benchmark datasets covering traffic, air quality, and trajectory data show that AdaCTSi reduces MAE by an average of 33.1% relative to the strongest baseline on each dataset. A single trained model supports sensor-subset and resource-adaptive inference, and its modest memory footprint enables deployment on commodity computing devices, including MCUs.

## Metadata
- **Published**: 2026-07-26T07:08:00Z
- **Authors**: Zhichen Lai, Huan Li, Dalin Zhang, Dong Gong, Lina Yao, Christian S. Jensen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23503v1)