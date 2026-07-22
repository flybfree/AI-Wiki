---
title: Thermodynamics-Informed Input Reparameterization for Neural Prediction of Real-Fluid Thermodynamic Properties in Supercritical Combustion
url: http://arxiv.org/abs/2607.19241v1
type: paper-summary
date: 2026-07-21
source_paper: 2026-07-21_16-12-30Z_Thermodynamics_InformedInputReparameterizationforN.md
generated_at: 2026-07-21 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a thermodynamics‑informed input reparameterization method called target‑aligned input reparameterization (TAIR) to improve the accuracy of neural networks that predict real‑fluid thermodynamic properties in supercritical combustion. By replacing raw enthalpy inputs with temperature, density, and compressibility estimates derived from ideal‑gas approximations, TAIR reduces prediction errors by factors up to 7.5 for compressibility and 3.6 for strain‑rate flames, outperforming both a raw‑input baseline and cross‑parameterized controls.

## Key Takeaways
- The method replaces the enthalpy coordinate with temperature estimates from an ideal‑gas mixture inversion, which directly captures the enthalpy‑temperature relation without solving the full closure.
- Density and compressibility networks use ideal‑gas density formulas, allowing the neural models to learn real‑fluid departures rather than reconstructing the entire equation‑of‑state.
- Experimental results show significant RMSE reductions (1.5× for temperature, 2.0× for density, 7.5× for compressibility) and even larger gains on unseen strain‑rate flames, indicating that thermodynamic alignment of inputs is crucial.

## Context
In AI‑driven surrogate modeling, input preprocessing often ignores the underlying physical relationships between variables, leading to suboptimal performance. This work demonstrates how aligning neural network inputs with thermodynamic targets can yield substantial accuracy improvements in high‑fidelity simulations where computational cost is prohibitive.

## Implications
For engineers and researchers working on supercritical combustion optimization, TAIR offers a practical way to reduce model training time while maintaining predictive fidelity. The approach can be extended to other real‑fluid systems, making AI surrogates more reliable for rapid design iterations in industrial applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19241v1)
