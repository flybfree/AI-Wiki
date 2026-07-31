---
title: HealthCAT: An Interpretable Encoder-only Transformer Framework for Health Indicator Prediction and Temporal Interpretation of Wearable Sensor Data
published: 2026-07-30T03:45:38Z
authors: Xiaotong Yu, Joshua Y. Kim, HaeJin Lee, Kalina Yacef
url: http://arxiv.org/abs/2607.27635v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HealthCAT: An Interpretable Encoder-only Transformer Framework for Health Indicator Prediction and Temporal Interpretation of Wearable Sensor Data

## Abstract
Wearable sensors continuously capture fine-grained multivariate time-series data, providing opportunities to model behavioural patterns associated with health outcomes. However, existing deep learning methods prioritise predictive accuracy over interpretability, limiting their application in health research. In this study, we present HealthCAT, a flexible framework that integrates an Encoder-only Transformer with an Attentive Class Activation Token (AttentiveCAT) to generate class-specific, time-step-level interpretations. These interpretations can be mapped back onto behavioural cycles that are relevant to the domain (e.g., time-of-day), supporting individual-level analysis of wearable sensor data. We evaluated HealthCAT using two real-world wearable sensor datasets (306 participants in total). HealthCAT outperformed deep learning baselines by up to 17\% in F1-score and 12\% in accuracy on both datasets ($p<0.05$). In masking experiments, the time steps identified by HealthCAT carried significantly more predictive value than random selection across all masking conditions ($p<0.05$), indicating that the identified time steps are predictively informative. By coupling predictive performance with validated time-step-level interpretability, HealthCAT moves wearable sensor analysis beyond aggregated metrics towards temporal patterns that support health monitoring, behavioural pattern analysis, and intervention design in health research. The significance of this work is that it enables accurate prediction of health indicators from wearable sensor data while providing insights into when and how physical activity patterns occur, rather than relying solely on aggregated summary measures.

## Metadata
- **Published**: 2026-07-30T03:45:38Z
- **Authors**: Xiaotong Yu, Joshua Y. Kim, HaeJin Lee, Kalina Yacef
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27635v1)