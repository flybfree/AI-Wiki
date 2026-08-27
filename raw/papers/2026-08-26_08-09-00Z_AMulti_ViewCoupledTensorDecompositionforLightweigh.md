---
title: A Multi-View Coupled Tensor Decomposition for Lightweight Online Adaptive Traffic Prediction
published: 2026-08-26T08:09:00Z
authors: Quan Yu, Jie Ni, Yu-Hong Dai, Xiongjun Zhang
url: http://arxiv.org/abs/2608.25498v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Multi-View Coupled Tensor Decomposition for Lightweight Online Adaptive Traffic Prediction

## Abstract
Accurate online traffic prediction is essential for intelligent transportation systems, where forecasting must be performed continuously under imperfect sensing conditions. Missing observations and anomalous disturbances make this task challenging, particularly when prediction relies on a single traffic view. This paper proposes a Multi-View Coupled Tensor Decomposition (MVCTD) model for online traffic prediction from imperfect multi-view observations, such as speed, flow, and occupancy. The proposed model uses coupled tensor decomposition to build a structured latent forecasting space, in which shared spatial structures across traffic views and view-specific temporal dynamics are jointly modeled. A group sparse regularization is further introduced to capture correlated abnormal responses induced by real traffic anomalies and thus reduce their influence on forecasts. For streaming deployment, MVCTD performs iterative refinement only on the current latent tensor, while the remaining model variables are updated by lightweight closed-form steps based on summarized historical information, thereby avoiding repeated optimization over the full historical sequence. Experiments on real-world traffic datasets demonstrate that MVCTD achieves accurate forecasts with favorable runtime under severe missingness, confirming its suitability for online traffic prediction.

## Metadata
- **Published**: 2026-08-26T08:09:00Z
- **Authors**: Quan Yu, Jie Ni, Yu-Hong Dai, Xiongjun Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25498v1)