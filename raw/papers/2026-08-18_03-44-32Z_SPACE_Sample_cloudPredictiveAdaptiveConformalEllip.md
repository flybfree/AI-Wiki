---
title: SPACE: Sample-cloud Predictive Adaptive Conformal Ellipsoids for Multivariate Time-Series Forecasting
published: 2026-08-18T03:44:32Z
authors: Baishi Li, Kelvin J. L. Koa, Ke-Wei Huang
url: http://arxiv.org/abs/2608.17333v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPACE: Sample-cloud Predictive Adaptive Conformal Ellipsoids for Multivariate Time-Series Forecasting

## Abstract
Modern probabilistic time-series forecasters often express uncertainty through forecast samples. While typically converted into nominal prediction regions using empirical quantiles, these model-implied sets lack formal coverage guarantees and frequently deviate from nominal targets under distribution shift. Existing multivariate conformal methods can calibrate these regions online, but they typically estimate geometry from historical residuals using fixed or accumulating look-back windows. This reliance on the past limits their ability to exploit the instantaneous dependence structure of current predictions and leaves them vulnerable to stale-regime contamination. To address this, we propose SPACE, a conformal wrapper for sample-generating multivariate forecasters. SPACE constructs ellipsoidal joint prediction regions by estimating time-local covariance geometry directly from the current forecast sample cloud, calibrating the region's radius via a dynamic backward window-selection scheme. Across diverse multivariate datasets, probabilistic forecasters, and conformal baselines, SPACE consistently brings realized joint and rolling coverage closer to the nominal target, achieving superior coverage-efficiency tradeoffs relative to competing wrappers.

## Metadata
- **Published**: 2026-08-18T03:44:32Z
- **Authors**: Baishi Li, Kelvin J. L. Koa, Ke-Wei Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17333v1)