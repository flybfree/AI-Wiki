---
title: No Free Lunch in Flow Surrogates under Time-Varying Boundary Conditions: A Two-Regime Study
published: 2026-07-26T14:02:46Z
authors: Georg Winkler, Martin Stoll
url: http://arxiv.org/abs/2607.23667v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# No Free Lunch in Flow Surrogates under Time-Varying Boundary Conditions: A Two-Regime Study

## Abstract
A flow surrogate validated on a simple regime is often taken as evidence that the approach will carry to a richer one. We test this assumption on two transient flows under time-varying boundary conditions emulating the process startup: the three-dimensional slurry film in chemical-mechanical planarisation (CMP), a core semiconductor-manufacturing process, and the two-dimensional Karman vortex street (KVS) behind a cylinder. Eight surrogate models are compared on one shared evaluation pipeline, differing in whether they learn the full field or a latent representation, and whether they predict trajectories in one shot or step by step. No single architecture wins both regimes. On the film, a one-shot full-field model reconstructs the process-relevant cumulative wall shear stress to 3.2% relative error. On the wake, a latent autoregressive DeepONet retains 96% of the shedding power that direct and one-shot models damp to almost zero. The deciding axis is the treatment of time. The self-sustained wake requires the phase memory that autoregressive feedback provides, while the boundary-driven film rewards a direct map. Pointwise RMSE picks the wrong model in both regimes, so the evaluation scores five physical questions instead, the field, its structure, invented motion, amplitude, and timing. The trained surrogates answer queries $10^3$ to $10^4$ times faster than the finite-element solver, but the offline cost of the training simulations means they pay off from the first query beyond the training set for CMP and the third for the KVS. The choice of surrogate should follow the dynamical character of the target flow, and its validation should use failure-mode-resolved metrics, since neither the winning architecture nor its validation transfers.

## Metadata
- **Published**: 2026-07-26T14:02:46Z
- **Authors**: Georg Winkler, Martin Stoll
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23667v1)