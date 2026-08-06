---
title: Adaptive Finite-Budget Training for CVaR Risk-Aware Q-Learning
published: 2026-08-05T00:26:22Z
authors: Yifan Wu, Junjie Lei, Wenjie Huang
url: http://arxiv.org/abs/2608.04305v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Finite-Budget Training for CVaR Risk-Aware Q-Learning

## Abstract
Risk-aware Q-learning (RaQL) provides a model-free, two-timescale estimator for dynamic risk objectives, but its finite-budget behavior remains fragile: fixed inner-loop hyperparameters can produce unstable value estimates, persistent Bellman residuals, and inefficient sample reuse. This paper proposes an adaptive training controller for Conditional Value-at-Risk (CVaR) RaQL and evaluates it on a daily Bitcoin trading task. The controller preserves the original CVaR estimator and Bellman fixed point; instead, it redesigns the training procedure through six coordinated mechanisms: per-cell inner-step sizing, outer-rate-matched decay synchronization, a short early correction for the VaR-like inner variable, a coverage-first-then-greedy sample allocation rule, progressive suffix aggregation of mature inner estimates, and data-driven calibration of key scales from online-observable quantities. Across 20 random seeds and 856,000 inner-transition samples, the controller reduces the mean empirical CVaR Bellman residual by approximately 85% relative to the fixed-parameter baseline (MeanBEQ: 1.2202 to 0.1854; MeanBEV: 1.1624 to 0.0535) and maintains stability across CVaR levels, discount factors, and training budgets. On the chronological out-of-sample test set, the learned policy attains a Sharpe ratio of 0.9281 with a maximum drawdown of 6.46% after transaction costs. Although buy-and-hold yields a higher cumulative return (35.43% vs. 23.61%), the adaptive policy achieves far lower volatility (9.57% vs. 47.93%), drawdown, and CVaR loss. These results demonstrate that adaptive finite-budget training design, applied solely to the training procedure without altering the risk objective, can materially improve the reliability and risk-adjusted performance of risk-aware Q-learning in financial applications.

## Metadata
- **Published**: 2026-08-05T00:26:22Z
- **Authors**: Yifan Wu, Junjie Lei, Wenjie Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04305v1)