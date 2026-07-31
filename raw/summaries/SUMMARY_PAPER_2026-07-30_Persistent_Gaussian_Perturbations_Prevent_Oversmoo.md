---
title: Persistent Gaussian Perturbations Prevent Oversmoothing in Recurrent Graph Neural Networks
url: http://arxiv.org/abs/2607.28185v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_13-21-18Z_PersistentGaussianPerturbationsPreventOversmoothin.md
generated_at: 2026-07-30 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how injecting independent Gaussian noise into a recurrent graph neural network prevents oversmoothing. It proves that the stochastic dynamics form a geometrically ergodic Markov chain with positive Dirichlet energy. The analysis shows asymptotic representation diversity is maintained under standard contraction assumptions.

## Key Takeaways
- Independent Gaussian perturbations after each propagation step create a stochastic dynamical system whose stationary state has non‑zero Dirichlet energy, preventing collapse to constant representations.
- A lower bound on the expected stationary Dirichlet energy is derived that scales with noise variance and graph spectral gap, guaranteeing oversmoothing avoidance.
- Numerical experiments confirm that both linear and nonlinear recurrent GNNs exhibit a stationary distribution matching theoretical predictions.

## Context
Oversmoothing limits deep GNN performance by reducing representation diversity. Existing deterministic fixes such as residual connections or normalization are often insufficient for long‑range dynamics. This work introduces stochastic regularization as an alternative mechanism to maintain expressive power.

## Implications
For practitioners, the result offers a simple yet effective way to stabilize recurrent GNNs without redesigning architectures. It may inspire hybrid models that combine noise injection with deterministic shortcuts, improving robustness in real‑world graph tasks like node classification and link prediction.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28185v1)
