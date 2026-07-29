---
title: Physics-Informed Neural Operator for Warm-Starting Background-Decomposed and Preconditioned PSFD: Enabling Scalable 3-D EUV Mask Simulation
url: http://arxiv.org/abs/2607.25330v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_06-31-21Z_Physics_InformedNeuralOperatorforWarm_StartingBack.md
generated_at: 2026-07-28 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a physics‑informed neural operator that solves EUV scattering problems using pseudo‑spectral frequency‑domain equations. It factorizes the Fourier operator into lateral and axial branches while preserving full vector coupling without the Born approximation. The model is trained on 16,000 randomly sampled mask designs from LithoBench and achieves a mean absolute error of about 7×10⁻³ for scattered intensity predictions.

## Key Takeaways
- The PINO reduces computational cost by factorizing the Fourier neural operator into lateral and axial branches while retaining full vector coupling without Born approximation.  
- Training uses random sampling of 16,000 mask designs from LithoBench each iteration avoiding precomputed EM fields.  
- Warm‑start initialization with spectral damping accelerates background‑decomposed PSFD solver on finer discretizations.

## Context
This work advances AI‑driven surrogate modeling for high‑dimensional physics problems in semiconductor manufacturing. By integrating neural operators with Fourier analysis, it bridges deep learning and rigorous electromagnetic simulation.

## Implications
The approach enables faster design iterations that are critical for EUV lithography equipment optimization. Practitioners can leverage the model to reduce simulation time and improve mask performance without sacrificing accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25330v1)
