---
title: PAC-Bayes Beyond Parameter Space: Behavioral Equivalence, Z-Information, and Exact Complexity Decomposition
published: 2026-08-11T22:09:17Z
authors: Vasant G. Honavar, Satish Kumar Keshri, Neil Ashtekar, Zehao Liu
url: http://arxiv.org/abs/2608.11465v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PAC-Bayes Beyond Parameter Space: Behavioral Equivalence, Z-Information, and Exact Complexity Decomposition

## Abstract
PAC-Bayes theory provides generalization guarantees by controlling the Kullback--Leibler (KL) divergence between posterior and prior distributions over a chosen hypothesis representation. However, predictive risk depends only on the predictive behavior induced by a hypothesis, not on the particular internal realization that implements that behavior. In over-parameterized systems, many distinct configurations induce identical predictive behavior, yet the classical PAC-Bayes KL divergence does not distinguish uncertainty over predictive behavior from variation among behaviorally equivalent realizations.   We show that this distinction induces an exact structural decomposition of classical PAC-Bayes complexity. We formalize behavioral equivalence through a measurable behavior map and use measure disintegration to decompose probability measures on the configuration space into a distribution over predictive behaviors and conditional distributions over behavioral fibers. This yields an exact decomposition of the classical PAC-Bayes KL divergence into a behavior-selection term and a realization-level term given by an expected conditional KL within fibers.   We define Z-information as the negative of this realization-level contribution: the exact gap between the KL divergence and the complexity of uncertainty over predictive behavior alone. We further show that the behavior-selection term admits an exact variational characterization: it is the minimum KL divergence among all posteriors inducing the same distribution over predictive behaviors, attained by a canonical fiber-symmetrized representative.   Finally, we show that symmetry, behavior-preserving directions, fiber geometry, and invariance under fiber-preserving perturbations arise naturally from the same behavior-map structure. Together, these results identify predictive behavior as the natural object of PAC-Bayes complexity.

## Metadata
- **Published**: 2026-08-11T22:09:17Z
- **Authors**: Vasant G. Honavar, Satish Kumar Keshri, Neil Ashtekar, Zehao Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11465v1)