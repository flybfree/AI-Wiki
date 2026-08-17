---
title: High-dimensional nonparametric changepoint detection via low-rank degree-two density projection
published: 2026-08-14T03:48:29Z
authors: Guoqing Zhang, Zhaixin Chen
url: http://arxiv.org/abs/2608.13922v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# High-dimensional nonparametric changepoint detection via low-rank degree-two density projection

## Abstract
Detecting distributional changes in high dimension is difficult when neither the pre-change nor post-change density is parametrically specified. We introduce a representation-based approach that retains all degree-at-most-two density information while replacing density estimation by matrix mean estimation. For observations in $[-1,1]^d$, a symmetric feature matrix $H_2(X)\in\R^{(d+1)\times(d+1)}$ is constructed so that $M(f)=\E_f H_2(X)$ is an isometric encoding of the degree-two orthogonal projection of the density. We scan matrix CUSUMs after rank-$r$ truncation, exploiting the low rank of the projected jump rather than sparsity of individual coordinates. The resulting \LRD{} estimator has a tent-shaped population objective and a nonasymptotic operator-norm analysis whose leading stochastic term scales as $\sqrt{rd\log(nd)}$. For multiple changes, we give a seeded narrowest-over-threshold procedure and prove exact recovery by an induction that preserves an isolating interval for every undetected change. A cross-fitted scalar refinement learns the changing low-rank direction on one fold and localizes on the other, attaining $\widetilde O_{\Pp}(κ^{-2})$ error; a matching Le Cam lower bound shows optimality up to logarithms. A geometrically $β$-mixing extension follows from a dependent matrix Bernstein inequality. Experiments with ambient dimension up to $200$, a three-change $d=100$ sequence, and a $128$-feature human-activity benchmark show that the method remains computationally practical and accurately detects pure dependence changes that are invisible to mean CUSUMs.

## Metadata
- **Published**: 2026-08-14T03:48:29Z
- **Authors**: Guoqing Zhang, Zhaixin Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13922v1)