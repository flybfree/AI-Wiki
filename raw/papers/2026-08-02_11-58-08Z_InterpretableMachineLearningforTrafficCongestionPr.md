---
title: Interpretable Machine Learning for Traffic Congestion Prediction: Unveiling the Impact of Different COVID-19 Periods
published: 2026-08-02T11:58:08Z
authors: Dan Zhu, Chi Sin Ng, Litian Xie, Yang Liu
url: http://arxiv.org/abs/2608.01180v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Interpretable Machine Learning for Traffic Congestion Prediction: Unveiling the Impact of Different COVID-19 Periods

## Abstract
Traffic congestion prediction is essential for congestion mitigation, but the COVID-19 pandemic and related control measures altered travel behavior and increased prediction complexity. This study predicts congestion in Alameda County, California, during pre-lockdown, lockdown, and post-lockdown periods. Weather, seasonality, and COVID-19 variables are incorporated, and Recursive Feature Elimination with Cross-Validation is used to select important features and reduce overfitting. Support vector regression, multiple linear regression, recurrent neural networks, and long short-term memory networks are trained and optimized. Because LSTM is more sensitive to hyperparameter settings, an adaptive parameter selection approach is used, while SVR and RNN are manually tuned. Performance is evaluated using Normalized Root Mean Square Error. Bidirectional LSTM consistently performs best across all periods because it captures temporal dependence in both directions. Integrated Gradients is used to interpret Bi-LSTM predictions, and SHapley Additive exPlanations is applied to SVR. New COVID-19 cases have a mainly negative effect on congestion during lockdown and post-lockdown, likely due to greater risk awareness, voluntary travel reduction, and compliance with mobility restrictions. In the post-pandemic period, higher hospitalization reduces travel and congestion, while higher fuel prices do not prevent a shift toward private vehicles and therefore increase congestion.

## Metadata
- **Published**: 2026-08-02T11:58:08Z
- **Authors**: Dan Zhu, Chi Sin Ng, Litian Xie, Yang Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01180v1)