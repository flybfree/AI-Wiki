---
title: Low-Rank Dependence Decomposition via Accelerated Symmetric Non-negative Matrix Factorization
published: 2026-07-27T14:56:00Z
authors: Lavinia Ghita, Dhruv Desai, Jake Goldberg, Roman Yokunda Enzmann
url: http://arxiv.org/abs/2607.24518v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Low-Rank Dependence Decomposition via Accelerated Symmetric Non-negative Matrix Factorization

## Abstract
Symmetric non-negative matrix factorization (SymNMF) recovers latent group structure from a dependence matrix, but its dense, quadratic-memory objective has confined prior work to moderate sizes. We present a large-scale GPU study of seven algorithm families (over 30 configurations) on absolute Pearson correlation and tail pairwise dependence matrices from Extreme Value Theory, two proxies for empirical risk-factor estimation on large portfolios. A trace-identity reformulation eliminates all $n \times n$ intermediates, so a single GPU reaches $n \approx 10^5$ and multi-node distribution scales to $n = 10^6$ and beyond. Under a two-phase protocol, eleven methods converge at moderate scale; six remain efficient enough at $n = 10^5$ (five AdaGrad-family plus ADMM), and five AdaGrad-family methods still converge at $n = 10^6$: AdaGrad, RMSprop, and three we introduce (Piecewise AdaGrad, Row-Stochastic SVRG, Block-SVRG AdaptGrow). At $n = 10^6$ the fastest solver tracks the matrix spectrum: Block-SVRG AdaptGrow wins on the flat, ill-conditioned tail-dependence spectrum, where its lower per-iteration cost decides a long factorization, and full-batch AdaGrad wins on the dominant-low-rank correlation spectrum, where the run is short. We also benchmark spherical K-means as a hard-label baseline: cheaper when angular cluster structure is present, yet provably degenerate once the matrix collapses toward a single common factor, where the soft factorization remains necessary.

## Metadata
- **Published**: 2026-07-27T14:56:00Z
- **Authors**: Lavinia Ghita, Dhruv Desai, Jake Goldberg, Roman Yokunda Enzmann
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24518v1)