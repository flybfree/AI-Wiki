---
title: JAPE: Joint Anomaly Prediction and Intrinsic Explanation in Multivariate Time Series
published: 2026-08-12T08:44:14Z
authors: Yian Wei, Yuanyuan Yao, Lu Chen, Xiangmin Zhou, Tianyi Li
url: http://arxiv.org/abs/2608.11801v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# JAPE: Joint Anomaly Prediction and Intrinsic Explanation in Multivariate Time Series

## Abstract
Multivariate time-series anomaly prediction aims to identify whether and when anomalies will occur over a future horizon from historical observations. Existing methods primarily characterize anomalies as deviations in future numerical values, which may overlook subtle dependency changes induced by weak anomaly precursors and provide no native variable-level explanation together with the alert. To bridge these gaps, we propose JAPE, a Joint Anomaly Prediction and Explanation framework that lifts anomaly prediction from numerical-deviation modeling to dependency-structure modeling. JAPE is the first anomaly prediction framework to explicitly model evolving dependency structures for both point-wise alerting and native variable-level explanation. Specifically, JAPE (i) proposes a Decoupled Spatio-Temporal Representation (DSTR) backbone that decouples temporal and spatial modeling and captures lag-aware dependencies via learnable lag aggregation, thereby perceiving structural precursors before numerical deviations emerge; (ii) designs a dual-view alerting mechanism that fuses numerical forecasts with evolving dependency graphs for point-wise anomaly prediction, capturing structural evidence even under subtle numerical deviations; and (iii) presents Native Predictive Explanation (NPE), which directly reuses the predicted dependency graphs to rank variables by structural deviations without additional models or training. Extensive experiments on five real-world benchmarks across three prediction horizons demonstrate that JAPE improves average F1 and AUC-PR by 19.7% and 41.3%, respectively, while improving explainability with 26.6% gain in MRR.

## Metadata
- **Published**: 2026-08-12T08:44:14Z
- **Authors**: Yian Wei, Yuanyuan Yao, Lu Chen, Xiangmin Zhou, Tianyi Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11801v1)