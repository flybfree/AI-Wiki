---
title: Susceptible Reservoir Architectures for Regime-Conditional Volatility Forecasting
published: 2026-07-24T17:03:08Z
authors: Aliaksei Kaliutau
url: http://arxiv.org/abs/2607.22491v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Susceptible Reservoir Architectures for Regime-Conditional Volatility Forecasting

## Abstract
Volatility forecasting is dominated by persistence and measurement noise, leaving limited residual structure for nonlinear models to exploit. We introduce Susceptible Architectures (SUSA), a reservoir-design principle for volatility forecasting, and its two concrete implementations, based on complex-valued open-chain and periodic reservoirs and regime-conditioned experts to interpret reservoir features across calm, onset, recovery, and persistent-stress states. We also implement open-system $q$-qubit counterparts in Qiskit while retaining a common AR-Ridge anchor and a bounded residual correction trained under QLIKE. We evaluate models on 16 U.S. equity and exchange-traded-fund series using three disjoint chronological training, validation, and test folds, a 12-observation input window, and a five-observation forecast horizon. The proposed models perform competitively with GARCH, achieving statistically significant QLIKE improvements for specific assets (IWM, XLP). Also models' forecasts complement HARQ-style predictions: a stacked ensemble improves mean QLIKE by 0.0116 over its strongest constituent and wins in 75% of test scenarios.

## Metadata
- **Published**: 2026-07-24T17:03:08Z
- **Authors**: Aliaksei Kaliutau
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22491v1)