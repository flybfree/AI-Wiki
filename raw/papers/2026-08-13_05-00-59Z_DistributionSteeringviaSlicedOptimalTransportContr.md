---
title: Distribution Steering via Sliced Optimal Transport Control
published: 2026-08-13T05:00:59Z
authors: Kaito Ito, Anqi Dong
url: http://arxiv.org/abs/2608.12828v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distribution Steering via Sliced Optimal Transport Control

## Abstract
Distribution steering seeks feedback laws that drive the state law of a dynamical system between prescribed initial and terminal distributions. Optimal transport provides a natural geometric approach, but its implementation generally requires a transport map or coupling in the full state space. Sliced optimal transport avoids this full-dimensional construction through one-dimensional projections. Yet, the resulting projected maps specify only directional displacements and do not by themselves prescribe a realizable feedback law. To this end, we develop a finite-horizon control framework based on sliced optimal transport. At each sampling instant, a projected optimal transport map defines a directional terminal condition, whose minimum-energy realization yields a randomized single-direction controller. Averaging over projection directions gives a deterministic sliced feedback. For the single-integrator dynamics, the averaged feedback makes the sliced Wasserstein distance to the target non-increasing. For Gaussian endpoint laws, it is affine, preserves Gaussianity, and steers the mean and covariance to their prescribed terminal values. We further identify a law-dependent gain that yields linear decay of the sliced Wasserstein distance together with an explicit characterization of the control energy. We also prove that the randomized controller converges to the averaged sliced flow as the sampling period vanishes. Finally, we extend the construction to linear dynamical systems. Reachability-normalized coordinates allow instantaneous realization of the sliced velocity for uniformly fully actuated systems, while local controllability Gramians provide exact finite-step realization for general controllable systems. Numerical examples illustrate the resulting distributional flows.

## Metadata
- **Published**: 2026-08-13T05:00:59Z
- **Authors**: Kaito Ito, Anqi Dong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12828v1)