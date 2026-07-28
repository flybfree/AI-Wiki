---
title: Covariance Last-Layer Ensembles: Function-Space Diversity for Efficient Uncertainty Quantification
published: 2026-07-26T21:56:02Z
authors: H. Martin Gillis, Isaac Xu, Gabriel Spadon, Thomas Trappenberg
url: http://arxiv.org/abs/2607.23856v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Covariance Last-Layer Ensembles: Function-Space Diversity for Efficient Uncertainty Quantification

## Abstract
A Last-Layer Ensemble (LLE), $K$ linear units on one shared frozen feature map, is an efficient single-pass approach to the disagreement-based epistemic uncertainty for out-of-distribution (OOD) detection. Its weakness is that members share the backbone gradient and can converge toward the same function, collapsing the inter-member diversity the signal depends on. Whether last-layer diversity can be restored, and what mitigates the collapse, is an open question. The weight-orthonormality defining Orthonormal Certificates (OC), the weight-orthonormal special case of the LLE, is only an indirect correction; it decorrelates the weights of the members, not their predictions. Here, we instead target the collapse directly in function space, with a Covariance Last-Layer Ensemble (cov-LLE) that places a direct covariance penalty on member activations. Cov-LLE restores the function-space diversity that weight-orthonormality cannot, and at matched $K$ recovers much of the diversity and calibration of a deep ensemble at $1\times$ backbone cost (in-distribution prediction variance $0.05\!\to\!9.3$ vs.\ $22.1$ ($\times10^{-3}$), and ECE $0.135\!\to\!0.090$ vs.\ $0.035$, for a $K\times$-cost deep ensemble), at no cost to accuracy. Viewing OC as a last-layer ensemble also organizes detectors into a two-axis taxonomy (by how their units are trained and how their outputs are scored) and exposes the OC score as a magnitude, motivating a scale-invariant, label-free direction score that repairs its near-OOD failure, adding $+0.16$ to $+0.18$ ROC AUC on every backbone.

## Metadata
- **Published**: 2026-07-26T21:56:02Z
- **Authors**: H. Martin Gillis, Isaac Xu, Gabriel Spadon, Thomas Trappenberg
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23856v1)