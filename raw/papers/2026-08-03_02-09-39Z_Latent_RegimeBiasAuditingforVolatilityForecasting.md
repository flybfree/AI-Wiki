---
title: Latent-Regime Bias Auditing for Volatility Forecasting
published: 2026-08-03T02:09:39Z
authors: Arthur Chagas, Pedro Bento, Yan Aquino, Arthur Buzelin, Wagner Meira, Cristiano Arbex Valle
url: http://arxiv.org/abs/2608.01599v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Latent-Regime Bias Auditing for Volatility Forecasting

## Abstract
Volatility forecasts are commonly evaluated with aggregate accuracy metrics such as RMSE and MAE, but these metrics can hide conditional failures that matter for risk management. This paper proposes a model-agnostic audit framework for evaluating whether volatility forecasts remain reliable across latent market regimes. We learn time-series representations of market-state windows, cluster them into regimes using only training information, assign regimes out of sample, and compare aggregate forecast behavior with regime-conditional bias, tail-underprediction, and underprediction-sensitive economic losses. Applied to daily volatility forecasting across cryptocurrency and ETF assets, the audit shows that models with competitive aggregate accuracy can still exhibit substantial regime-specific bias and severe tail underprediction. The results suggest that volatility forecasting should be evaluated not only by average error, but also by where and how forecasts become unreliable. Our framework shifts forecast evaluation from asking which model is most accurate on average to identifying the market regimes in which apparently accurate forecasts fail conditionally. Reproducibility: https://github.com/arthurchagas1/Latent-Regime-Bias-Auditing-for-Volatility-Forecasting

## Metadata
- **Published**: 2026-08-03T02:09:39Z
- **Authors**: Arthur Chagas, Pedro Bento, Yan Aquino, Arthur Buzelin, Wagner Meira, Cristiano Arbex Valle
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01599v1)