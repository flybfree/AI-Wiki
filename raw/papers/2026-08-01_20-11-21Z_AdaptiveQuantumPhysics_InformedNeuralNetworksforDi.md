---
title: Adaptive Quantum Physics-Informed Neural Networks for Differential Equations with Applications to Fluid Dynamics
published: 2026-08-01T20:11:21Z
authors: Fabio Pereira dos Santos, Renato Portugal, Júlio de Castro Vargas Fernandes, Lucas Timotheo Sanches
url: http://arxiv.org/abs/2608.00850v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Quantum Physics-Informed Neural Networks for Differential Equations with Applications to Fluid Dynamics

## Abstract
Physics-informed neural networks (PINNs) have emerged as a versatile approach for solving nonlinear partial differential equations (PDEs), yet achieving high accuracy efficiently using these techniques remains challenging for high-dimensional or multiscale systems. Here, we present a hybrid quantum-classical framework that enhances Quantum PINNs (QPINNs) through adaptive collocation point sampling and loss-aware attention mechanisms. By dynamically prioritizing points in regions with large PDE residuals or steep solution gradients, our method mitigates the spectral bias inherent in conventional PINNs. Current Quantum Physics-Informed Neural Networks are commonly assumed to be limited by the expressive power of quantum circuits. In our work, we observed that, across diverse differential equations, optimization - not only expressivity - can be an important bottleneck. Furthermore, a trainable loss-weighting scheme balances contributions from physics residuals, boundary conditions, and data fidelity during training. Integrating these strategies with quantum computing techniques (including variational quantum circuits and quantum gradient estimation) can yield at least a 60% improvement in solution accuracy under specific regimes for benchmark fluid flows and reaction-diffusion systems. Finally, we argue that merely increasing model expressivity is insufficient for resolving complex PDEs via QPINNs, as they remain constrained by the structural optimization limitations of classical PINNs. This framework provides a scalable pathway for quantum-enhanced scientific machine learning, bridging physics-based modeling with emerging quantum computational capabilities.

## Metadata
- **Published**: 2026-08-01T20:11:21Z
- **Authors**: Fabio Pereira dos Santos, Renato Portugal, Júlio de Castro Vargas Fernandes, Lucas Timotheo Sanches
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00850v1)