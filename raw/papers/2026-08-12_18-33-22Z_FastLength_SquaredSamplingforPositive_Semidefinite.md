---
title: Fast Length-Squared Sampling for Positive-Semidefinite Matrices
published: 2026-08-12T18:33:22Z
authors: Rajarshi Bhattacharjee, Ethan N. Epperly, Cameron Musco, Aaron Tian
url: http://arxiv.org/abs/2608.12503v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fast Length-Squared Sampling for Positive-Semidefinite Matrices

## Abstract
We describe a simple rejection-sampling-based algorithm to perform length-squared sampling on an $n \times n$ positive-semidefinite (psd) matrix: that is, to sample a column with probability proportional to its squared $\ell_2$-norm. The algorithm runs in just $O(n)$ expected time, which is significantly sublinear in the input matrix size. The runtime is optimal, even when the input is assumed to be diagonal.   Our result has several applications. Length-squared sampling is used by a number of sublinear time algorithms for matrix problems, like low-rank approximation and eigenvalue approximation. Often, it is assumed that the algorithm is given access to the matrix column norms, and thus can perform length-squared sampling efficiently. Our result shows that, at least for psd matrices, we can remove this assumption. We also discuss an application to an asymptotically optimal algorithm for estimating the Frobenius norm of a psd matrix to relative error. Finally, we show that our sampling algorithm yields a very simple sublinear time algorithm for the robust psd low-rank approximation problem introduced by Bakshi et al. (FOCS, 2020), which nearly matches the more complex method developed there.

## Metadata
- **Published**: 2026-08-12T18:33:22Z
- **Authors**: Rajarshi Bhattacharjee, Ethan N. Epperly, Cameron Musco, Aaron Tian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12503v1)