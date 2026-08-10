---
title: Limit Points of Reflow with Minibatch Optimal Transport
published: 2026-08-07T09:51:33Z
authors: Antonin Chambolle, Johannes Hertrich
url: http://arxiv.org/abs/2608.07042v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Limit Points of Reflow with Minibatch Optimal Transport

## Abstract
Rectified flows, also called flow matching or stochastic interpolants, are generative models that learn a time-dependent vector field steering a probability curve between two probability distributions, usually referred to as latent and target distributions. Reflow accelerates inference by iteratively straightening the trajectories induced by this vector field. We study the asymptotic behavior of this iteration and characterize its limit points. First, we define weak rectified couplings which always exist. Next, when rectified flow updates are alternated with minibatch optimal transport steps of fixed batch size, we show that any limit is $N$-cyclically monotone, where $N$ is the batch size. Such $N$-cyclically monotone couplings enjoy favorable structural and stability properties such as rectifiability and straightness. Finally, restricting velocities to gradient fields and assuming additional support conditions, we prove that reflow limits coincide with the optimal transport map between the endpoint distributions.

## Metadata
- **Published**: 2026-08-07T09:51:33Z
- **Authors**: Antonin Chambolle, Johannes Hertrich
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07042v1)