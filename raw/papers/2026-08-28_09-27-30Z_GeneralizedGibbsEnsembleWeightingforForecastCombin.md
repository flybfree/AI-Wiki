---
title: Generalized Gibbs Ensemble Weighting for Forecast Combination
published: 2026-08-28T09:27:30Z
authors: Prasen R. Nuthanakaluva, Nava K. Gaddam
url: http://arxiv.org/abs/2608.28116v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Generalized Gibbs Ensemble Weighting for Forecast Combination

## Abstract
Forecast combination is a reliable way to improve predictive performance when several forecasting models are available. Simple aggregation rules such as the mean, median, trimmed mean, inverse-loss weighting, and exponential weighting are often strong baselines, but their relative performance can vary across datasets, forecast horizons, deployment settings, and levels of disagreement among base forecasters. We develop Generalized Gibbs Ensemble Weighting (GGEW), a probabilistic framework that treats forecasting models as experts and assigns ensemble weights using a Gibbs-style exponential transformation of normalized predictive loss. The framework extends this basic weighting rule through numerical stabilization, diversity-aware score corrections, and online hyperparameter adaptation. GGEW produces a family of related methods, including Stable Gibbs weighting, Directional Gibbs-NCL, and Symmetric Gibbs-NCL. These variants share one core algorithm and differ only in the score used inside the exponential weighting rule. For sequential deployment, we adopt a UCB-style bandit mechanism, called online Local-UCB, to adapt the learning rate, diversity strength, and Gibbs variant without evaluating the full hyperparameter grid at every prediction step. We evaluate GGEW on official M4 competition forecast submissions and external rolling-origin deployment experiments using Monash Traffic Hourly, Electricity Hourly, and Solar Weekly datasets. Results suggest that Gibbs-style adaptive weighting is a useful and competitive tool across several benchmark settings, although its relative performance varies across datasets, forecast horizons, deployment protocols, and forecast disagreement groups. The contribution is not a universal dominance claim, but a framework and empirical study motivating further investigation of when adaptive Gibbs-style forecast combination is useful.

## Metadata
- **Published**: 2026-08-28T09:27:30Z
- **Authors**: Prasen R. Nuthanakaluva, Nava K. Gaddam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28116v1)