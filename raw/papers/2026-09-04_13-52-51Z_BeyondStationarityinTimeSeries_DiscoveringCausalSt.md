---
title: Beyond Stationarity in Time Series: Discovering Causal Structures and Latent Regimes via Markov Blankets
published: 2026-09-04T13:52:51Z
authors: Lei Zan, Charles K. Assaad, Emilie Devijver, Eric Gaussier
url: http://arxiv.org/abs/2609.05150v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Stationarity in Time Series: Discovering Causal Structures and Latent Regimes via Markov Blankets

## Abstract
This paper introduces Regime-aware Constraint-Based and Noise-Based causal discovery with Markov Blankets (RCBNB-MB), a novel causal discovery algorithm for time series that relaxes the common assumption of a single, time-consistent causal structure. Time series are typically observed at discrete time points and often exhibit regime changes that challenge the assumption of a static causal structure, a limitation in many real-world dynamic systems. To address this challenge, RCBNB-MB identifies latent causal regimes, defined as subsets of time points within which a stable causal structure holds. The algorithm follows an iterative strategy that segments the time series into regimes and discovers the causal graph within each regime. By leveraging the Markov blanket rather than direct parents, RCBNB-MB gains robustness to errors in causal discovery and preserves predictive information. We provide theoretical guarantees for RCBNB-MB's ability to recover both regime transitions and causal graphs under reasonable assumptions. Furthermore, we validate its effectiveness through extensive experiments on simulated datasets with known ground truth and real-world IT monitoring data, where taking into account regime shifts is critical. Empirical results show that RCBNB-MB systematically outperforms baseline approaches in accurately detecting regime changes and their associated causal graphs, positioning it as a robust and versatile framework for non-stationary time series analysis.

## Metadata
- **Published**: 2026-09-04T13:52:51Z
- **Authors**: Lei Zan, Charles K. Assaad, Emilie Devijver, Eric Gaussier
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05150v1)