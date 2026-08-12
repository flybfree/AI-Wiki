---
title: CRHT: A Continuous Regression Hybrid Transformer for Vessel Trajectory Prediction with Online Cluster Sampling
published: 2026-08-10T21:42:40Z
authors: Alexander Schiøtz, Bertram Hage, Christian Rand, Felix Thomsen, Peder Heiselberg
url: http://arxiv.org/abs/2608.10256v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CRHT: A Continuous Regression Hybrid Transformer for Vessel Trajectory Prediction with Online Cluster Sampling

## Abstract
Accurate vessel trajectory prediction is critical for maritime safety and anomaly detection, yet existing models often struggle with geographic bias and navigational realism. We propose the Continuous Regression Hybrid Transformer (CRHT), a deep learning framework designed to forecast vessel motion using Automatic Identification System (AIS) data. To mitigate spatial data imbalance, we introduce an online K-means cluster sampling strategy that ensures diverse exposure to rare maneuvers during training. Our hybrid architecture integrates 1D convolutional layers for local kinematic feature extraction with a multi-head attention mechanism for global temporal context. CRHT demonstrates superior performance in short-term forecasting, achieving the lowest errors at the 1-hour horizon. The results demonstrate that while discrete models provide high navigational stability over long horizons, CRHT offers an optimal balance of precision and maneuver tracking for real-time maritime surveillance.

## Metadata
- **Published**: 2026-08-10T21:42:40Z
- **Authors**: Alexander Schiøtz, Bertram Hage, Christian Rand, Felix Thomsen, Peder Heiselberg
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10256v1)