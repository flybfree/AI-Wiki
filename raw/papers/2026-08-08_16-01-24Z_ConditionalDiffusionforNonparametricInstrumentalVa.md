---
title: Conditional Diffusion for Nonparametric Instrumental Variable Quantile Regression
published: 2026-08-08T16:01:24Z
authors: Xingdong Feng, Xinhong Jiang, Yuling Jiao, Lican Kang, Junwei Liu
url: http://arxiv.org/abs/2608.08204v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conditional Diffusion for Nonparametric Instrumental Variable Quantile Regression

## Abstract
This work proposes deep nonparametric Instrumental variable quantile regression (IVQR), a two-stage estimator that combines conditional diffusion modeling with a kernel-smoothed conditional moment formulation. In the first stage, we estimate the joint conditional distribution of the outcome and endogenous covariates given the instrument using a variance-preserving conditional diffusion model. In the second stage, we approximate the conditional moment operator through Monte Carlo sampling and a kernel-smoothed surrogate for the indicator function, and then estimate the structural quantile function by empirical risk minimization over deep neural networks. We establish an excess-risk bound for the proposed estimator and derive end-to-end total variation guarantees for the conditional diffusion model under unbounded support, explicitly accounting for score estimation, early stopping, and discretization errors. Our theory is developed under a polynomial-tail envelope on the data distribution and degenerates continuously to the exponential setting: as the tail index grows, the obtained excess-risk rate converges to the minimax-optimal rate of nonparametric regression, thus our heavy-tailed theory covers the classical light-tailed nonparametric guarantees as a limiting case. Simulation studies and a real-data application demonstrate that the proposed method outperforms existing nonparametric IVQR approaches, with gains that become increasingly pronounced as the dimensionality of the covariates and instruments increases.

## Metadata
- **Published**: 2026-08-08T16:01:24Z
- **Authors**: Xingdong Feng, Xinhong Jiang, Yuling Jiao, Lican Kang, Junwei Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08204v1)