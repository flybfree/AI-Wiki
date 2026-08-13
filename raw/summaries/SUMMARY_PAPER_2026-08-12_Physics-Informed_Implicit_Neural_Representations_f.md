---
title: Physics-Informed Implicit Neural Representations for Improved Myocardial Perfusion MRI Quantification
url: http://arxiv.org/abs/2608.11282v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_11-25-22Z_Physics_InformedImplicitNeuralRepresentationsforIm.md
generated_at: 2026-08-12 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes an extension of physics‑informed neural networks (PINNs) that incorporate spatiotemporal implicit neural representations (INRs) to model cardiac magnetic resonance signals. By representing the MR signal as a continuous function, the method achieves smoother and more physically consistent parameter estimates compared with conventional non‑linear least squares fitting. In simulated datasets the new PINN‑INR framework demonstrates higher robustness and more accurate extraction of myocardial perfusion parameters.

## Key Takeaways
- The INR extension adds spatiotemporal continuity to PINNs, reducing sensitivity to noise and acquisition variability in tracer‑kinetic models.
- Simulation results show improved parameter estimation accuracy and smoother output curves across the cardiac cycle compared with baseline PINN methods.
- The framework maintains physical consistency by embedding known hemodynamic equations directly into the neural representation.

## Context
Implicit neural representations aim to solve inverse problems without explicit model fitting, offering a data‑driven alternative in medical imaging. This work advances that goal by integrating physics constraints at both spatial and temporal scales, highlighting how AI can complement traditional quantitative MRI protocols.

## Implications
Clinicians could rely on more reliable perfusion maps generated automatically from CMR scans, reducing inter‑observer variability. The method also supports rapid prototyping for new tracer‑kinetic models without extensive computational tuning, accelerating research and commercialization of advanced perfusion quantification tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11282v1)
