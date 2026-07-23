---
title: PG-KINN: A Physics-Informed Petrov-Galerkin Kolmogorov-Arnold Network for Solving Forward and Inverse PDEs
url: http://arxiv.org/abs/2607.20378v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_17-08-29Z_PG_KINN_APhysics_InformedPetrov_GalerkinKolmogorov.md
generated_at: 2026-07-23 00:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PG-KINN, a physics‑informed Kolmogorov‑Arnold network that employs a Petrov‑Galerkin formulation to solve forward and inverse PDEs. It demonstrates superior performance over MLP baselines and existing KAN methods on diverse mechanical benchmarks by mitigating spectral bias and improving conditioning.

## Key Takeaways
- The loss functional is built from weak residuals using independent compactly supported test functions, which lowers differentiation order and avoids trivial solutions in parameter identification.
- Integration by parts enables the method to handle non‑self‑adjoint operators while retaining accuracy for nonlinear problems.
- Localized test functions transform global residual into element‑wise weak terms with favorable conditioning.

## Context
Physics‑informed neural networks have struggled with spectral bias and dense weight matrices, limiting both performance and interpretability. KANs offer a better structural alignment but suffer from similar issues when the loss is not well conditioned.

## Implications
PG-KINN provides a robust framework for AI‑driven computational mechanics that can be applied to crack analysis, hyperelasticity, and inverse material characterization, offering higher accuracy with fewer parameters than traditional MLP approaches. This could accelerate design cycles in aerospace and manufacturing industries where rapid inverse solutions are critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20378v1)
