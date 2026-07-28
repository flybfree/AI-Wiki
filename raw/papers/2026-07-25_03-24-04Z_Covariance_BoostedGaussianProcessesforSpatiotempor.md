---
title: Covariance-Boosted Gaussian Processes for Spatiotemporal Irregularities
published: 2026-07-25T03:24:04Z
authors: Jeremy Ovadia
url: http://arxiv.org/abs/2607.23018v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Covariance-Boosted Gaussian Processes for Spatiotemporal Irregularities

## Abstract
Nonstationary Gaussian process (GP) models are powerful tools for capturing input-dependent variability by adapting to observed data. However, with limited sampling and highly parameterized covariance structure, they are often prone to overfitting and overconfident uncertainty estimates, potentially leading to misleading predictions in safety-critical applications. Motivated by ionospheric modeling for satellite-based augmentation systems (SBAS), this paper proposes a Covariance-Boosted Gaussian Process (CBGP) framework centered upon boosting covariance priors to discover nonstationary latent functions for signal and observation variation that capture irregularities in the input domain. An additional layer of GP modeling of "partially-whitened" observations guides latent function relative error estimation that is used to iteratively update weak priors in a gradient descent-like procedure. Following boosting, restrictions are imposed upon prior covariances to prevent overfitting while posterior uncertainties are inflated to prevent model overconfidence. CBGP model efficacy and robustness are demonstrated through out-of-sample testing of both simulated and real-world applications that meet a three-nines integrity standard. The modeling of an extensive ionospheric storm dataset over South America suggests accurate and reliable means to compute SBAS ionospheric corrections in the most challenging space weather environment using regional models that are more informed and responsive than local fitting performed by currently-operating SBAS.

## Metadata
- **Published**: 2026-07-25T03:24:04Z
- **Authors**: Jeremy Ovadia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23018v1)