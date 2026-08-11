---
title: No Unique Minimizer, No Problem: On the Consistency of Robust Neural Classifiers
published: 2026-08-09T05:21:08Z
authors: Subhabrata Majumdar, Anand Deo, Partha Pratim Saha, Abhik Ghosh
url: http://arxiv.org/abs/2608.08489v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# No Unique Minimizer, No Problem: On the Consistency of Robust Neural Classifiers

## Abstract
Neural network classifiers trained by cross-entropy minimization are highly sensitive to label noise and adversarial contamination. While robust alternatives offer bounded influence and resistance to corruption, their statistical foundations in the deep learning setting are insufficient due to a fundamental difficulty: neural parameterizations are non-identifiable, so the population loss minimizer is an equivalence class of parameters, not a unique point. We develop a consistency theory for robust neural classifiers based on the S-divergence family that requires no identifiability assumption. Casting training as stochastic optimization over a non-identifiable parameter space, we prove that empirical S-divergence minimizers converge to the population-optimal equivalence class under mild regularity conditions, and verify these conditions for three architecture choices. We further establish that limit points of the robust training algorithm are stationary points of the empirical objective. Experiments on vision and language benchmark datasets confirm that S-divergence training maintains clean-data accuracy while exhibiting performance competitive with existing robust methods.

## Metadata
- **Published**: 2026-08-09T05:21:08Z
- **Authors**: Subhabrata Majumdar, Anand Deo, Partha Pratim Saha, Abhik Ghosh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08489v1)