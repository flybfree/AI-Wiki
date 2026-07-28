---
title: Adaptive Multi-Scale Forecasting and Gate-Localized Conformal Prediction for Multivariate Nonstationary Time Series
published: 2026-07-25T11:46:38Z
authors: Ziling Ma, Junshu Jiang, Ángel López-Oriona, Ying Sun, Hernando Ombao
url: http://arxiv.org/abs/2607.23165v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Multi-Scale Forecasting and Gate-Localized Conformal Prediction for Multivariate Nonstationary Time Series

## Abstract
We propose ABF-T-GLCP, a model-agnostic framework for forecasting and uncertainty quantification in nonstationary multivariate time series. The central idea is to learn an adaptive predictive state representation for point forecasting and reuse it for conformal calibration. The forecasting module combines horizon-specific temporal experts through a learned gate and refines predictions using sparse predictive transfer across related series. The uncertainty module, Gate-Localized Conformal Prediction (GLCP), uses the learned gate state, together with temporal recency, to select locally relevant calibration residuals, thereby coupling uncertainty calibration to the predictive regimes used by the forecasting model. This shared representation allows point forecasts and prediction intervals to adapt consistently under evolving temporal dynamics while retaining the model-agnostic nature of conformal prediction and yielding approximate local coverage under mild stability conditions. Experiments on a large-scale high-frequency commodity forecasting benchmark show consistent gains in point forecasting accuracy and substantially narrower prediction intervals with empirical coverage close to the nominal level. Additional results indicate that the framework extends beyond the motivating financial application.

## Metadata
- **Published**: 2026-07-25T11:46:38Z
- **Authors**: Ziling Ma, Junshu Jiang, Ángel López-Oriona, Ying Sun, Hernando Ombao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23165v1)