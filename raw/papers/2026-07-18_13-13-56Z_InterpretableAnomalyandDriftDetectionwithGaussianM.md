---
title: Interpretable Anomaly and Drift Detection with Gaussian Mixture Models
published: 2026-07-18T13:13:56Z
authors: Behnam Asadi
url: http://arxiv.org/abs/2607.16811v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Interpretable Anomaly and Drift Detection with Gaussian Mixture Models

## Abstract
We revisit Gaussian Mixture Models (GMMs) as a lightweight, interpretable tool for anomaly detection and, in particular, for detecting distributional drift in data streams. We make three practical choices explicit and evaluate them on seven public benchmarks. First, the number of mixture components is selected automatically by the Bayesian Information Criterion, initialised by k-means, removing the need to fix it in advance. Second, individual observations are scored by their negative log-likelihood under a GMM fitted to normal data, with thresholds set at a target false-alarm rate using Extreme Value Theory. Third, the same interpretable model extends to distributional drift: each Gaussian component is a named "regime," and the fraction of a stream window that matches no regime -- its unexplained mass -- is a drift signal that is itself the explanation. We benchmark this against a model-free kernel two-sample test (Maximum Mean Discrepancy, MMD) and against two GMM-to-GMM divergences (a closed-form Cauchy-Schwarz divergence and a matching-based KL surrogate). Across seven benchmarks ranging from 3 to 64 dimensions and five random splits, the GMM point detector is competitive with -- though rarely more accurate than -- Isolation Forest, Local Outlier Factor, one-class SVM, ECOD, COPOD and an autoencoder, while uniquely yielding an interpretable model. For drift, MMD is the strongest pure detector, but the interpretable unexplained-mass statistic matches it when anomalies form novel regimes (and honestly fails, as MMD does not, when drift is a pure re-weighting of existing regimes). Every alarm is explainable: anomalies lie a median of 3-10 sigma outside their nearest regime vs. about 1 sigma for normal points, and a drift alarm reports the fraction of the window matching no known regime. All code and experiments are released.

## Metadata
- **Published**: 2026-07-18T13:13:56Z
- **Authors**: Behnam Asadi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.16811v1)