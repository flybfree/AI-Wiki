---
title: Dynamical and Optimization Trade-offs of Levi--Civita Coordinates for Learned Close-Encounter Dynamics
url: http://arxiv.org/abs/2607.20235v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_14-56-15Z_DynamicalandOptimizationTrade_offsofLevi__CivitaCo.md
generated_at: 2026-07-23 23:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the dynamical and optimization trade‑offs of Levi–Civita coordinates versus Cartesian coordinates when learning Hamiltonian dynamics for a perturbed Kepler problem with a smooth quadrupole potential. The authors find that the regularized Levi–Civita formulation achieves a relative energy error near \(2.1\times10^{-5}\) across high eccentricities, while the Cartesian splitting becomes unstable and incurs errors up to eight orders of magnitude larger. Neural residual learning fails to match the analytic baseline despite attempts at exact‑feature controls.

## Key Takeaways
- The regularized Levi–Civita Hamiltonian splitting maintains a maximum relative energy error of \(2.1\times10^{-5}\) even when eccentricity reaches 0.99, whereas Cartesian splitting loses stability and yields errors up to eight orders of magnitude higher.
- In matched physical horizon and force‑evaluation budgets the regularized model’s baseline error is \(3\times10^{-5}\), which is four to eight orders of magnitude lower than that of the Cartesian arm depending on eccentricity.
- Neural residual models, even with exact‑feature controls, cannot close the gap beyond \(\mathcal{O}(1)\) rollout error because raw‑basis ill‑conditioning prevents optimal least‑squares fitting.

## Context
The study addresses a core challenge in AI‑driven Hamiltonian dynamics: how to balance accurate representation of physical constraints with efficient optimization of learning algorithms. By comparing two coordinate systems within the same regularization framework, the paper highlights that coordinate choice influences both dynamical stability and computational conditioning, a nuance rarely explored in prior work.

## Implications
For practitioners developing neural solvers for celestial mechanics or any high‑precision physics simulation, this research underscores the importance of selecting coordinate representations that preserve low energy error while avoiding severe optimization difficulties. The findings suggest that while Levi–Civita coordinates improve dynamical conditioning, they introduce raw‑basis challenges that must be mitigated through preprocessing such as orthogonalization to achieve reliable learned dynamics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20235v1)
