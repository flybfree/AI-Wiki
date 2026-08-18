---
title: $S^3$: A Smooth Simulation Surrogate for Optimizing Discrete Abstractions of Dynamical Systems
published: 2026-08-16T20:31:04Z
authors: Jordan Peper, James Mathias Gast, Vignesh Nanduri, Tanmayee Maram, Ethan Howes, Ivan Ruchkin
url: http://arxiv.org/abs/2608.15920v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# $S^3$: A Smooth Simulation Surrogate for Optimizing Discrete Abstractions of Dynamical Systems

## Abstract
Intelligent systems are increasingly deployed in safety-critical settings with black-box controllers, including neural networks. The properties and behaviors of these end-to-end systems can be studied with abstraction-based methods that replace them with simpler finite models. Constructing such abstractions requires balancing the soundness of over-approximating the dynamical system against conservatism, which manifests as spurious or excessive nondeterministic behaviors. Bi-simulation theory provides principled metrics for characterizing these relationships, but does not prescribe how to construct sound abstractions with minimal conservatism. We fill this gap with a smooth simulation surrogate ($S^3$) --- a differentiable objective that approximates the reverse simulation metric used to quantify conservatism. Combined with Taylor model-based reachability, $S^3$ enables gradient-based optimization of abstraction parameters while preserving soundness by construction. We evaluate this optimization pipeline on three case studies. Our results show that $S^3$ is strongly correlated with the reverse simulation metric, is computationally faster, and serves as an effective objective for reducing abstraction conservatism.

## Metadata
- **Published**: 2026-08-16T20:31:04Z
- **Authors**: Jordan Peper, James Mathias Gast, Vignesh Nanduri, Tanmayee Maram, Ethan Howes, Ivan Ruchkin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15920v1)