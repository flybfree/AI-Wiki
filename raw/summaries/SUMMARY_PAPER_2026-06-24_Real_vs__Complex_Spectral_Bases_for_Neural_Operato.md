---
title: Real vs. Complex Spectral Bases for Neural Operators: The Role of Green's Function Alignment
url: http://arxiv.org/abs/2606.24851v1
type: paper-summary
date: 2026-06-24
source_paper: 2026-06-23_17-29-15Z_Realvs_ComplexSpectralBasesforNeuralOperators_TheR.md
generated_at: 2026-06-24 00:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper compares Fourier Neural Operators (FNO) and Hartley Neural Operators (HNO), two real‑valued alternatives that learn solution operators of PDEs using spectral bases in the complex versus purely real frequency domain. The authors show that HNO, which uses a real Discrete Hartley Transform, retains twice as many spectral corners because its spectrum is not halved by conjugate symmetry, while FNO carries only half due to symmetry constraints. Experiments across various PDE classes reveal that the optimal basis aligns with the Green’s‑function structure: self‑adjoint elliptic operators favor HNO, whereas time‑dependent operators with phase content favor FNO.

## Key Takeaways
- The real Hartley Transform provides a spectral basis that doubles the number of retained frequency corners compared to the complex FFT, preserving more information for certain PDEs.  
- Training HNO is advantageous for self‑adjoint elliptic operators because its Green’s functions are symmetric and diagonalized by a single real multiplier, whereas FNO cannot represent this symmetry efficiently.  
- For time‑dependent operators that involve oscillatory or transport phenomena, the complex phase content of solutions makes FNO more suitable than HNO.

## Context
The field of neural operators seeks to learn global solution maps for partial differential equations with minimal data and computational cost. Spectral methods are attractive because they can capture long‑range interactions efficiently, but the choice between complex and real frequency bases is often overlooked in favor of a single universal approach.

## Implications
Practitioners should select HNO when dealing with symmetric, time‑invariant problems where Green’s functions are real, and FNO for problems involving explicit phase or advection effects. This rule can improve training stability and reduce overfitting, leading to more accurate and efficient neural operator implementations in scientific computing and AI‑driven simulation pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.24851v1)
