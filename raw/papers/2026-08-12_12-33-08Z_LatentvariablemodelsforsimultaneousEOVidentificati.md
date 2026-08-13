---
title: Latent variable models for simultaneous EOV identification and removal in population-based SHM
published: 2026-08-12T12:33:08Z
authors: M. D. Champneys, M. R. Jones, A. J. Hughes, T. J. Rogers, E. J. Cross, K. Worden
url: http://arxiv.org/abs/2608.11995v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Latent variable models for simultaneous EOV identification and removal in population-based SHM

## Abstract
The robust treatment of environmental and operational variability (EOV) is an open challenge in population-based structural health monitoring (PBSHM). The difficulty is compounded in the case that the EOV signals are unmeasured. A common approach in conventional SHM is to apply \emph{projection-based} methods that discard subspaces of healthy feature data, reasoning that the EOV signal dominates the variance of the measured features. However, a common pitfall of projection-based approaches is that when damage acts close to the same variance-dominant direction, damage sensitivity is removed along with the EOV. An alternative identifying assumption for the removal of particular unmeasured EOVs is slowness; the latent EOV process is characterised by its long temporal correlation. In this paper, the latent EOV is cast as a state-space Gaussian process, enabling tractable $\mathcal{O}(T)$ inference via a Kalman filter. A robust hierarchical Bayesian identification framework is developed that enables population-level identification of latent EOVs and EOV-free residual features, using a Laplace approximation. The approach is first validated on a single laboratory-scale benchmark structure from the literature, subject to thermal EOVs, demonstrating robust damage detection and EOV recovery. The method is then applied to a simulated nine-turbine offshore wind farm with staggered deployment and damage, where it delivers a substantial true-positive uplift over projection and cointegration-based baselines at matched false-positive rates.

## Metadata
- **Published**: 2026-08-12T12:33:08Z
- **Authors**: M. D. Champneys, M. R. Jones, A. J. Hughes, T. J. Rogers, E. J. Cross, K. Worden
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11995v1)