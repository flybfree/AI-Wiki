---
title: Distributional Split Criteria for Random Forests: Extensions, Shrinkage, and the Robustness of Mean Splitting
published: 2026-07-26T15:37:30Z
authors: Silas Koemen
url: http://arxiv.org/abs/2607.23721v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distributional Split Criteria for Random Forests: Extensions, Shrinkage, and the Robustness of Mean Splitting

## Abstract
Distributional random forests replace mean-based CART splitting with criteria that compare the full conditional response distribution in candidate children. We implement and systematically study a family of such criteria inside a single honest-forest implementation: isotropic random-Fourier-feature maximum mean discrepancy (MMD), an anisotropic diagonal-bandwidth variant, an adaptive per-split frequency-selection variant, and a non-kernel sliced-Wasserstein criterion, together with post-hoc kernel-mean shrinkage of the forest weights. Using paired-seed comparisons across synthetic quantile mechanisms, real univariate benchmarks, a California-housing subsample curve, and multivariate synthetic and real responses, we characterize where each extension pays. Three findings recur. First, among distributional criteria ordinary isotropic MMD is already close to best in class: the anisotropic, adaptive-frequency, and sliced-Wasserstein extensions, and post-hoc shrinkage, do not systematically improve on it. Second, on scalar tabular regression mean-based CART splitting remains the robust default and wins many cells. Third, multivariate responses are the regime where distributional splitting clearly earns its keep, most sharply on a pure-dependence copula where the energy score separates the criteria even though marginal CRPS does not. The evidence supports a simple allocation story: distributional splitting helps only when non-location structure is both present and estimable; otherwise it dilutes split-selection power away from the mean. All criteria, the honest forest, and the paired-comparison harness are implemented in the open-source \texttt{drforest} library, whose Rust-backed split search makes broad criterion sweeps inexpensive.

## Metadata
- **Published**: 2026-07-26T15:37:30Z
- **Authors**: Silas Koemen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23721v1)