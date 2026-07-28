---
title: Impute On-Demand: Adaptive Correlated Time Series Imputation for Changing Environments
url: http://arxiv.org/abs/2607.23503v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_07-08-00Z_ImputeOn_Demand_AdaptiveCorrelatedTimeSeriesImputa.md
generated_at: 2026-07-27 22:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AdaCTSi, an adaptive CTS imputer that improves accuracy while handling changing IoT environments. Experiments show it reduces MAE by 33.1% compared to the strongest baseline across multiple datasets and scenarios. The approach also reduces computational load compared to full‑graph attention methods.

## Key Takeaways
- The model uses a One-shot Temporal Convolutional Network combined with a learned time-sensor index table to generate sensor‑specific embeddings, allowing it to adapt when some sensors are missing or fail.
- Sparse spatial attention extracts dynamic spatial correlations while correlation‑weighted sensor selection chooses the most informative sensors for context.
- A single trained model can support both sensor‑subset and resource‑adaptive inference with a modest memory footprint suitable for deployment on commodity devices like MCUs.

## Context
IoT systems generate correlated time series data where missing values are common, yet most imputation methods assume static sensor configurations. This limitation hampers real‑time applications that must respond to intermittent failures or limited computing resources without retraining.

## Implications
The adaptive approach enables edge deployment of accurate imputation without heavy compute, supporting scalable IoT networks where sensors drift or fail unpredictably. Practitioners can rely on a single model to maintain performance across varying sensor subsets and resource constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23503v1)
