---
title: Quantum Speedups for Stochastic Optimization with Heavy-Tailed Noise
published: 2026-07-28T09:29:37Z
authors: Bin Luo, Chengchang Liu, Jonathan Allcock, Shengyu Zhang, John C. S. Lui
url: http://arxiv.org/abs/2607.25492v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Quantum Speedups for Stochastic Optimization with Heavy-Tailed Noise

## Abstract
We study stochastic optimization with heavy-tailed gradient noise. We first propose a novel quantum mean estimator for multivariate heavy-tailed random variables that achieves lower query complexity than optimal classical estimators in the low-dimensional regime. We further develop an unbiased quantum mean estimator by applying a generalized multi-level Monte Carlo technique. We prove quantum lower bounds showing that, when the dimension $d$ of the random vector is small and can be viewed as a constant, our quantum estimators are optimal up to logarithmic factors. We further derive stronger dimension-dependent lower bounds for tail index $p>4/3$, showing that a nontrivial dependence on the dimension is unavoidable in the low-dimensional regime. Based on these estimators, we propose a quantum normalized stochastic gradient descent method ($\texttt{QNSGD}$), which finds an $ε$-stationary point using $\tilde{\mathcal{O}}\big(\sqrt d\,ε^{-\frac{5p-4}{2p-2}}\big)$ queries to the quantum stochastic gradient oracle. For a convex objective function, we propose a quantum projected stochastic gradient descent method ($\texttt{QPSGD}$), which computes a solution with $ε$-optimal solution using $\tilde{\mathcal{O}}\big(\sqrt d\,ε^{-\frac{3p-2}{2p-2}}+ε^{-2}\big)$ queries in expectation. These sharper bounds improve upon the classical lower bounds $Ω\big(ε^{-\frac{3p-2}{p-1}}\big)$ for nonconvex problems and $Ω\big(ε^{-\frac{p}{p-1}}\big)$ for convex problems in the low-dimensional regimes $d\lesssimε^{-\frac{p}{p-1}}$ and $d\lesssimε^{-\frac{2-p}{p-1}}$, respectively.

## Metadata
- **Published**: 2026-07-28T09:29:37Z
- **Authors**: Bin Luo, Chengchang Liu, Jonathan Allcock, Shengyu Zhang, John C. S. Lui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25492v1)