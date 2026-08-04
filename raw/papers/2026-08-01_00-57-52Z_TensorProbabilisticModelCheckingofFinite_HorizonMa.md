---
title: Tensor Probabilistic Model Checking of Finite-Horizon Markov Chains (Extended Version)
published: 2026-08-01T00:57:52Z
authors: Jianlin Li, Nick Guo, Peter Ye, Yizhou Zhang
url: http://arxiv.org/abs/2608.00374v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tensor Probabilistic Model Checking of Finite-Horizon Markov Chains (Extended Version)

## Abstract
We reexamine the problem of verifying Markov chains with respect to step-bounded reachability probabilities. Prevailing approaches rely on encoding the state-transition matrix using either explicit or symbolic representations. While these approaches are effective for sparse transition dynamics, they scale less favorably in the dense regime.   Our insight is to cast probabilistic model checking of Markov chains as computations over dense tensors. This methodology enables the use of off-the-shelf compiler toolchains for optimized execution of these tensor computations on hardware accelerators. We prove the soundness of the methodology of mapping probabilistic model checking to tensor computations. We implement our approach in a tool called Tessa . Empirical evaluation shows that Tessa unlocks massive speedups over state-of-theart methods on selected benchmarks from the literature.

## Metadata
- **Published**: 2026-08-01T00:57:52Z
- **Authors**: Jianlin Li, Nick Guo, Peter Ye, Yizhou Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00374v1)