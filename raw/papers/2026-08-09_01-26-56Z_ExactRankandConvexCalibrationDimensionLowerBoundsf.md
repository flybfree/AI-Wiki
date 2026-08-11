---
title: Exact Rank and Convex Calibration Dimension Lower Bounds for the Multi-Label F1 Loss
published: 2026-08-09T01:26:56Z
authors: Mingyuan Zhang
url: http://arxiv.org/abs/2608.08399v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Exact Rank and Convex Calibration Dimension Lower Bounds for the Multi-Label F1 Loss

## Abstract
The instance-wise $F_1$ measure is a central performance measure for multi-label classification. For a problem with $s$ labels, it defines a $2^s\times 2^s$ loss matrix. Previous work exhibited $s^2+1$-coordinate affine and shifted low-rank representations and used them to construct quadratic-dimensional convex calibrated surrogates. We determine the exact rank. Under the convention $F_1(\varnothing,\varnothing)=1$, the $F_1$ score matrix, the shifted loss matrix, and the unshifted loss matrix all have rank $s^2-s+2$, while the column-affine dimension of the loss is $s^2-s+1$. The proof factors the nonempty score matrix through subset-incidence matrices and a positive-definite Cauchy matrix.   Exact rank does not, by itself, lower-bound the dimension of an arbitrary convex calibrated surrogate. We therefore analyze the Bayes geometry of $F_1$ directly. We construct a distribution for which precisely all supersets of a fixed core label set are Bayes optimal, and show that the corresponding active loss columns, restricted to the witness support, have affine dimension $hn$, where $n=s-\lfloor s/3\rfloor$ and $h=\lceil(s\lfloor s/3\rfloor)^{1/2}\rceil-1$. Applying the feasible-subspace lower bound for convex calibration dimension gives \[   \operatorname{CCdim}(L^{F_1})   \ge \left(\frac{2}{3\sqrt{3}}-o(1)\right)s^2. \] Together with the quadratic upper bound, this establishes $\operatorname{CCdim}(L^{F_1})=Θ(s^2)$.

## Metadata
- **Published**: 2026-08-09T01:26:56Z
- **Authors**: Mingyuan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08399v1)