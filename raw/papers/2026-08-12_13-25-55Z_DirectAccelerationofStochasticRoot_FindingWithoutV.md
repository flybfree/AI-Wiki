---
title: Direct Acceleration of Stochastic Root-Finding Without Variance Reduction and Regularization
published: 2026-08-12T13:25:55Z
authors: TaeHo Yoon, Nicolas Loizou
url: http://arxiv.org/abs/2608.12043v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Direct Acceleration of Stochastic Root-Finding Without Variance Reduction and Regularization

## Abstract
Acceleration for deterministic root-finding problems has been extensively studied in recent years; specifically, the anchor-based, or Halpern-type methods achieve optimal convergence rates with respect to the operator norm. However, acceleration via these methods does not directly carry over to stochastic setting due to accumulation of errors, unless one enforces diminishing variance via increasing batch sizes or variance reduction techniques. In this work, we show that another class of acceleration, namely the dual-anchor mechanism, extends to the stochastic setting without such error accumulation, in contrast to anchor-based algorithms. Consequently, we cleanly achieve $O(ε^{-3})$ complexity with iteration-independent batch size, without any variance reduction or double-loop recursive regularization, for stochastic root-finding (resp. fixed-point) problems with cocoercivity (resp. square-nonexpansivity) in expectation. For strongly monotone operators, the same algorithm attains a sharper $\widetilde{O} (ε^{-2})$ complexity, nearly matching the lower bound in terms of $ε$-dependence.

## Metadata
- **Published**: 2026-08-12T13:25:55Z
- **Authors**: TaeHo Yoon, Nicolas Loizou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12043v1)