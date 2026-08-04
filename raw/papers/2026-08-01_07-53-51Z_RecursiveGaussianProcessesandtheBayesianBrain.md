---
title: Recursive Gaussian Processes and the Bayesian Brain
published: 2026-08-01T07:53:51Z
authors: Moumita Das, Dipanjan Ray, Sourabh Bhattacharya
url: http://arxiv.org/abs/2608.00503v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Recursive Gaussian Processes and the Bayesian Brain

## Abstract
Predictive coding offers a powerful framework for cortical computation, yet scalable implementations that respect both Bayesian exactness and neurobiological constraints remain scarce. We bridge this gap by formally connecting predictive coding to Recursive Gaussian Processes (RGPs). RGPs employ a single Gaussian process \( g(t, \cdot) \) indexed by layer index and input value, preventing the representational collapse of standard deep Gaussian processes while allowing learnable cross-layer dependence via \( r_{1g} \). We demonstrate that RGPs intrinsically implement hierarchical Bayesian inference, uncertainty propagation, and precision-weighted prediction error. Critically, we map RGP components---the shared GP, spike-and-slab variable selection, and MCMC dynamics---onto the canonical cortical microcircuit, providing a neurobiological substrate for these computations. Drawing on the free energy principle, we show that RGP inference minimizes variational free energy, formally linking Bayesian mechanics to neuronal dynamics. Our synthesis positions RGPs as both a principled computational tool and a candidate model for the brain's predictive machinery, generating testable predictions for laminar-specific dynamics and spectral asymmetries between feedforward and feedback processing.

## Metadata
- **Published**: 2026-08-01T07:53:51Z
- **Authors**: Moumita Das, Dipanjan Ray, Sourabh Bhattacharya
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00503v1)