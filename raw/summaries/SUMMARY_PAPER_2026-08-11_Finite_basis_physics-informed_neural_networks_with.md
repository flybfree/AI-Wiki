---
title: Finite basis physics-informed neural networks with hard constraints for viscous fluid flow in highly perforated domains
url: http://arxiv.org/abs/2608.08114v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-08_12-54-16Z_Finitebasisphysics_informedneuralnetworkswithhardc.md
generated_at: 2026-08-11 13:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes finite basis physics-informed neural networks with hard constraints to solve viscous flow in highly perforated domains using Stokes equations. It shows that FBPINNs combined with exact boundary encoding improve accuracy and convergence despite many perforations. The method reduces spectral bias and is parallelizable.

## Key Takeaways
- Conventional PINNs lose accuracy when perforation count rises because penalty terms become stiff and cause gradient conflicts near boundaries.
- Hard constraints enforce boundary conditions exactly but can create non‑local effects due to global network approximation.
- Finite basis PINNs with localisation mitigate these issues, yielding weak dependence of convergence on the number of perforations.

## Context
Physics-informed neural networks aim to embed governing equations directly into loss functions, reducing data requirements for complex fluid flows. Recent advances focus on improving robustness to high‑dimensional geometry and avoiding overfitting through better constraint handling.

## Implications
This framework offers a scalable solution for engineering simulations where microstructures dictate flow behavior, enabling faster design iterations without sacrificing fidelity. Practitioners can rely on neural models that remain stable across extreme perforations, supporting real‑world applications in microfluidics and porous media.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08114v1)
