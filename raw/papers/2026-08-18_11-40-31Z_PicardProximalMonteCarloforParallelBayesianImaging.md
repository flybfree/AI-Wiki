---
title: Picard Proximal Monte Carlo for Parallel Bayesian Imaging with Score-Based Generative Priors
published: 2026-08-18T11:40:31Z
authors: Deliang Wei, Evan Bell, Wenhan Guo, Yifan Chen, Yu Sun
url: http://arxiv.org/abs/2608.17666v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Picard Proximal Monte Carlo for Parallel Bayesian Imaging with Score-Based Generative Priors

## Abstract
Bayesian imaging inverse problems often require sampling from high-dimensional posterior distributions. While recent score-based and diffusion models provide expressive Bayesian priors, their sampling procedures remain inherently sequential and computationally expensive for large-scale imaging applications. We propose PiX-MC, a time-parallel posterior sampling framework based on proximal Langevin dynamics and Picard iteration. The proximal-likelihood formulation exploits the fact that many imaging likelihoods admit efficient, problem-specific proximal operators, while Picard refinement exposes parallelism across discretization nodes and naturally supports multi-GPU implementation. To further improve practical scalability and sampling performance, we develop multi-block and annealed variants of the proposed framework. We establish convergence guarantees under transparent assumptions, accommodating non-log-concave posteriors, imperfect learned score models, multi-block implementations, and annealing schedules. Experiments on a diverse collection of imaging inverse problems demonstrate that PiX-MC substantially reduces wall-clock time while preserving reconstruction quality. On a $512\times512\times80$ sparse-view computed tomography (CT) problem, annealed multi-block PiX-MC achieves up to a $50\times$ runtime speedup over the standard Langevin sampler using eight GPUs.

## Metadata
- **Published**: 2026-08-18T11:40:31Z
- **Authors**: Deliang Wei, Evan Bell, Wenhan Guo, Yifan Chen, Yu Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17666v1)