---
title: Evaluator Ensembles Under Reward Hacking: Covariance Geometry and Finite-Search Guarantees
published: 2026-08-08T08:28:55Z
authors: Fariya Afrin, Ibne Farabi Shihab
url: http://arxiv.org/abs/2608.08002v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluator Ensembles Under Reward Hacking: Covariance Geometry and Finite-Search Guarantees

## Abstract
Language-model judges and reward models enable scalable supervision, but finite optimization can exploit evaluator errors rather than improve response quality. We characterize this failure through the covariance geometry of evaluator ensembles. For calibrated judges, the ensemble mean retains common-mode error along the all-ones direction, whereas cross-judge disagreement captures only orthogonal error. Consequently, disagreement can be high despite robust aggregation, or low while shared response-dependent errors persist. We prove that common-mode error is not identifiable from internal judge scores alone. Under a joint sub-Gaussian model, we bound best-of-K selection overstatement and target-quality regret, extending the guarantees to predictably adaptive search under conditional calibration. The resulting search terms scale as the square root of log K and are asymptotically tight for Gaussian projected errors. We further show that noisy quality proxies introduce artificial rank-one covariance without changing disagreement, and propose a bounded two-anchor Bernstein certificate for finite-search error and regret. Fixed-seed Gaussian stress tests over 120 (J, rho, K) configurations and real-model audits validate the theory while revealing the limits of disagreement-based diagnostics under increasing search pressure.

## Metadata
- **Published**: 2026-08-08T08:28:55Z
- **Authors**: Fariya Afrin, Ibne Farabi Shihab
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08002v1)