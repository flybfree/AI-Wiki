---
title: Minimax Optimal Early-Stopped Gradient Descent for Gaussian Mixture Classification
published: 2026-08-06T16:41:00Z
authors: Alex Buna, Shirley Xiaoqi Liu, Patrick Rebeschini
url: http://arxiv.org/abs/2608.06250v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Minimax Optimal Early-Stopped Gradient Descent for Gaussian Mixture Classification

## Abstract
In overparameterised classification, training data can be linearly separable even when the underlying distribution is not. In this setting, gradient descent (GD) on the logistic loss diverges in norm while converging in direction to a max-margin interpolating classifier, whose implicit bias can be statistically suboptimal. In this work, we show that early stopping can overcome this suboptimality: in a Gaussian mixture model with label-flipping noise, GD stopped at an appropriate oracle time achieves minimax-optimal excess zero-one risk for covariance spectra with fast and continuous decay, including polynomial and exponential spectral decays. Our analysis combines a sharp upper bound for the early-stopped iterate with a matching statistical lower bound over arbitrary classifiers, yielding optimal rates that are validated by experiments. A central technical contribution is a new calibration result that converts excess logistic risk into excess zero-one risk; it handles the model misspecification induced by the label-flipping noise, and removes the square-root rate in standard bounds. We also establish a lower bound for linear interpolators, showing that interpolation can require exponentially more samples than early stopping to achieve the same excess risk.

## Metadata
- **Published**: 2026-08-06T16:41:00Z
- **Authors**: Alex Buna, Shirley Xiaoqi Liu, Patrick Rebeschini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06250v1)