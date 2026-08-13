---
title: A Factor Graph Approach to Scalable Multi-Output Gaussian Process Regression
published: 2026-08-12T10:52:13Z
authors: Wouter W. L. Nuijten, Esther G. van Pelt, Albert Podusenko, İsmail Şenöz, Wouter M. Kouw
url: http://arxiv.org/abs/2608.11917v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Factor Graph Approach to Scalable Multi-Output Gaussian Process Regression

## Abstract
Multi-output Gaussian process regression scales cubically in the number of observations times outputs, and dense kernel-matrix methods need bespoke handling whenever different outputs are observed at different inputs. We express multi-output Gaussian process regression as a Forney-style factor graph in which a nearest-neighbor chain orders a fixed candidate set of $C$ inputs into a one-dimensional sequence. Along this chain, latent Matérn processes evolve through linear-Gaussian transition factors, while the linear model of coregionalization mixes $L$ latent processes into $D$ outputs through a deterministic mixing factor and per-output scalar observation factors. Posterior computation reduces to exact Gaussian message passing on the chain at cost $\mathcal{O}(C(DL^2 + L^3))$ after chain construction, and missing observations omit their local factor without any covariance-matrix restructuring. The formulation therefore scales in the number of data samples and in the rate of missing observations, while remaining best suited to candidate sets in low input dimension.We compare the factor-graph formulation against an exact kernel-matrix baseline, a sparse-variational inducing-point baseline, and a nearest-neighbor baseline on a synthetic input-dimension sweep and on electricity time series forecasting. At low input dimension the factor-graph posterior tracks the exact kernel-matrix posterior closely, and the gap grows gradually as input dimension increases while staying competitive with both approximate baselines. On the electricity time series our factor-graph formulation matches all three baselines in forecast accuracy while scaling linearly in the number of data points, where the exact kernel-matrix method becomes infeasible and the inducing-point baseline remains substantially slower.

## Metadata
- **Published**: 2026-08-12T10:52:13Z
- **Authors**: Wouter W. L. Nuijten, Esther G. van Pelt, Albert Podusenko, İsmail Şenöz, Wouter M. Kouw
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11917v1)