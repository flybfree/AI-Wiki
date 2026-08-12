---
title: Self-Normalized Inference for Constant-Stepsize Temporal-Difference Learning under Markovian Sampling
published: 2026-08-11T13:19:28Z
authors: Min Zeng, Yichen Zhang, Xiaofeng Shao
url: http://arxiv.org/abs/2608.10896v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Normalized Inference for Constant-Stepsize Temporal-Difference Learning under Markovian Sampling

## Abstract
Constant-stepsize temporal-difference (TD) learning is attractive for policy evaluation, but inference from a single Markov trajectory must account for serial dependence and a stepsize-dependent stationary target. For fixed-stepsize linear TD, we establish a functional central limit theorem whose covariance retains the multiplicative component induced by the random TD matrix and the stationary iterate error. We then derive a joint functional limit for parallel Richardson--Romberg (RR) recursions driven by the same trajectory. A Brownian-bridge self-normalizer yields asymptotically pivotal confidence regions for prespecified state-value contrasts without estimating the long-run covariance or selecting a bandwidth or batch length. For such a contrast, the procedure admits a one-pass implementation whose memory does not grow with the trajectory length. At a fixed stepsize, the inferential center is the RR stationary target. We also study horizon-indexed designs in which the stepsize remains constant within each run and decreases across longer horizons. Under an explicit RR-dependent rate window, the residual RR target shift, multiplicative remainder, and initialization effect are negligible at the root-$n$ scale, yielding inference for the projected Bellman solution. Experiments on FrozenLake and Garnet illustrate stationary-target coverage, RR target correction, and the finite-sample behavior of the horizon-indexed design.

## Metadata
- **Published**: 2026-08-11T13:19:28Z
- **Authors**: Min Zeng, Yichen Zhang, Xiaofeng Shao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10896v1)