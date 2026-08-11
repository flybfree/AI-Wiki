---
title: The Spectral Neuron
published: 2026-08-08T08:31:26Z
authors: Alex Shtoff
url: http://arxiv.org/abs/2608.08003v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Spectral Neuron

## Abstract
As machine learned models increase in complexity and expressive power, features of simpler models, such as interpretability and control over the shape of the modeled function are lost. On the one edge of the spectrum we have simple linear models are transparent and possess good interpretability and explainability properties, but have a limited expressive power. On the other edge we have neural networks, that have expressive power that improves with scaling, but are mostly opaque. In this work we develop the \emph{spectral neuron} concept: a scalar model given by $f(\vx)=λ_k \left(A_0+\sum_{i=1}^n x_i A_i\right)$, with learned real symmetric matrices \(A_0,\ldots,A_n\). The input enters the model through an affine matrix function, but the prediction is obtained by reading one of its eigenvalues. Thus, the model is nonlinear, but the source of nonlinearity is still mathematically explicit. This gives us a useful middle ground: the model can become more expressive as the matrix dimension grows, while retaining a degree of structural interpretability through the learned matrices. For example, extremal eigenvalues yield convex or concave functions, semidefinite constraints on the coefficient matrices impose monotonicity, and the associated eigenspaces characterize local feature sensitivity. We study the robustness, structural interpretability, and shape-control properties of this model family, and then test whether it can be learned and scaled in practice. We develop a systematic study of this model family, bringing together spectral results from several mathematical literatures to characterize its expressivity, robustness, interpretability, and shape-control properties.

## Metadata
- **Published**: 2026-08-08T08:31:26Z
- **Authors**: Alex Shtoff
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08003v1)