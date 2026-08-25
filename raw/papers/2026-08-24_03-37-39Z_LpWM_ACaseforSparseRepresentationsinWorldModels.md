---
title: LpWM: A Case for Sparse Representations in World Models
published: 2026-08-24T03:37:39Z
authors: Yilun Kuang, Yash Dagade, Quentin Le Lidec, Lucas Maes, Randall Balestriero, Yann LeCun
url: http://arxiv.org/abs/2608.22764v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LpWM: A Case for Sparse Representations in World Models

## Abstract
Joint-embedding predictive architectures (JEPAs) learn latent dynamics for planning and avoid representation collapse by matching features to maximum-entropy distributions such as isotropic Gaussians, yielding dense representations. However, it is unclear whether dense representations are the most favorable geometry for modeling dynamics. In this work, we ask whether a different geometry, sparse representations, can make action-conditioned latent dynamics easier to model, and what dynamical structure emerges from such representations. We first show that nonlinear Lipschitz dynamics can be approximated arbitrarily well by action-conditioned linear dynamics in a sufficiently high-dimensional one-hot latent space, with rollout error vanishing as the dimension grows. This motivates distributed sparse representations as a practical relaxation of one-hot sparsity. We introduce LpWorldModel (LpWM), a JEPA model regularized with Rectified Distribution Matching Regularization (RDMReg) to match encoder features to a Rectified Generalized Gaussian distribution, yielding non-negative sparse codes. Empirically, sparsity lowers the predictor complexity required for successful planning: on PushT, sparse LpWM outperforms dense LeWM by up to 57% in planning success at intermediate predictor capacities. This advantage also extends beyond Gaussian distribution matching, with LpWM outperforming dense VICReg representations across multiple predictor families. We further find that the learned sparse representations are mode-factored, with support encoding discrete dynamical regimes and feature magnitudes capturing continuous within-regime state. Together, these results suggest that sparse representations can reduce the predictor complexity required for control while revealing interpretable structure.

## Metadata
- **Published**: 2026-08-24T03:37:39Z
- **Authors**: Yilun Kuang, Yash Dagade, Quentin Le Lidec, Lucas Maes, Randall Balestriero, Yann LeCun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22764v1)