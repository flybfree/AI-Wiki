---
title: BayesSeg: A Bayesian Optimization Framework for State Segmentation of Electricity Consumption Time Series
published: 2026-08-01T08:22:49Z
authors: Zhenya Zhang, Wendi Zhu, Ping Wang, Hongmei Cheng, Shuguang Zhang
url: http://arxiv.org/abs/2608.00513v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BayesSeg: A Bayesian Optimization Framework for State Segmentation of Electricity Consumption Time Series

## Abstract
In Non-Intrusive Load Monitoring (NILM), adaptive segmentation of electricity consumption time series is critical for appliance recognition. However, prevailing methods face challenges including heuristic parameter tuning, boundary sensitivity, and metric saturation. This paper proposes BayesSeg, a unified framework integrating time-series segmentation, multidimensional evaluation, and automatic parameter optimization. The segmentation layer employs a dual steady-state criterion based on the tail value and mean of preceding subsequences, combined with a sequential extraction and complement-set parsing strategy, to achieve precise unsupervised partitioning of steady-state and transition-state segments. The evaluation layer maps segmentation results to binary state sequences and formulates a composite metric integrating an event-level F1 score (event_F1) with Normalized Mutual Information (NMI). The event_F1 quantifies switching-event precision and recall via tolerance matching, while NMI captures global structural consistency, jointly overcoming the boundary sensitivity and limited discriminability of point-wise metrics. In the optimization layer, the composite score serves as the objective function for Bayesian optimization, which constructs a TPE surrogate model for efficient global parameter-space exploration. Experiments on the SustDataED2 dataset demonstrate that Bayesian optimization requires only ~100 objective evaluations to locate a parameter region within 0.35% deviation of the exhaustive grid-search optimum. The framework achieves a weighted composite score of 0.7149 and an event_F1 of 0.9340 while reducing optimization latency from ~5300 seconds to under 1 second, a speedup exceeding 5700x. BayesSeg automates segmentation configuration and provides a scalable, efficient solution for time-series analysis in NILM and related domains.

## Metadata
- **Published**: 2026-08-01T08:22:49Z
- **Authors**: Zhenya Zhang, Wendi Zhu, Ping Wang, Hongmei Cheng, Shuguang Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00513v1)