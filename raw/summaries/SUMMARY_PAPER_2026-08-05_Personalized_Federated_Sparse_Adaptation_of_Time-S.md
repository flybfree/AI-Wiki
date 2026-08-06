---
title: Personalized Federated Sparse Adaptation of Time-Series Foundation Models
url: http://arxiv.org/abs/2608.04695v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_11-01-47Z_PersonalizedFederatedSparseAdaptationofTime_Series.md
generated_at: 2026-08-05 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a personalized federated sparse adaptation framework for time‑series foundation models (TSFMs) to improve energy forecasting while respecting privacy and non‑identical data across buildings. The proposed heterogeneous MoE adapter, routed at the sequence level, consistently outperforms global FL‑MoE and local MoE approaches, demonstrating that client‑aware and backbone‑aware adaptation yields better performance.

## Key Takeaways
- Fully shared adapters suppress building‑specific temporal behavior because they cannot capture unique patterns in each site.  
- Fully local adaptation discards cross‑building transfer, limiting the reuse of knowledge across buildings.  
- The personalized federated MoE strategy consistently outperforms both global FL‑MoE and local MoE variants, with the optimal sparse‑adaptation method varying by TSFM backbone and evaluation metric.

## Context
Federated learning enables collaborative model training without sharing raw data, a crucial requirement for private sensor streams like smart meter readings. Time‑series forecasting models benefit from adaptation to capture site‑specific dynamics while preserving global knowledge, making efficient personalization a key research challenge in AI for energy management.

## Implications
This work provides a scalable template for deploying personalized federated models across distributed infrastructure, reducing data transfer costs and enhancing forecast accuracy. Practitioners can adopt the MoE routing concept to tailor large foundation models to specific use cases without retraining entire networks, accelerating innovation in smart building systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04695v1)
