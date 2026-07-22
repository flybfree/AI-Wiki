---
title: Thermodynamics-Informed Input Reparameterization for Neural Prediction of Real-Fluid Thermodynamic Properties in Supercritical Combustion
published: 2026-07-21T16:12:30Z
authors: Haoze Zhang, Han Li, Ke Xiao, Yangchen Xu, Runze Mao, Zhi X. Chen
url: http://arxiv.org/abs/2607.19241v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Thermodynamics-Informed Input Reparameterization for Neural Prediction of Real-Fluid Thermodynamic Properties in Supercritical Combustion

## Abstract
Real-fluid thermodynamic property evaluation is a major computational cost in supercritical combustion simulations. In the enthalpy-based pressure-correction formulation, the closure evaluates temperature T, density $ρ$, and compressibility coefficient $ψ$ from the solver state (h,p,Y) through enthalpy-temperature inversion and repeated real-fluid equation-of-state evaluations. Neural-network surrogates offer fixed-cost inference, but direct mapping from (h,p,Y) to $(T,ρ,ψ)$ must capture the enthalpy-temperature relation and non-ideal equation-of-state response, resulting in a complex regression problem. This work introduces a thermodynamics-informed input reparameterization strategy, termed target-aligned input reparameterization (TAIR). TAIR replaces the raw enthalpy coordinate of each property network with a target-matched thermodynamic coordinate: the temperature network uses a temperature estimate obtained by inverting a constant-$c_p$ ideal-gas mixture enthalpy approximation, whereas the density and compressibility networks use an ideal-gas density estimate. These algebraic transformations use only solver-available variables and species constants, guiding the networks to learn real-fluid departures from ideal-gas baselines rather than reconstructing the full closure from raw enthalpy. The method is assessed using supercritical methane-oxygen counterflow flame data against a raw-input baseline and target-inconsistent cross-reparameterization controls. TAIR reduces held-out RMSE by factors of about 1.5, 2.0, and 7.5 for T, $ρ$, and $ψ$, respectively. For an unseen strain-rate flame within the augmented thermodynamic envelope, the corresponding factors are 3.6, 14.5, and 6.0. The target-inconsistent controls perform worse, indicating that the gains arise from thermodynamically matched input design rather than generic preprocessing.

## Metadata
- **Published**: 2026-07-21T16:12:30Z
- **Authors**: Haoze Zhang, Han Li, Ke Xiao, Yangchen Xu, Runze Mao, Zhi X. Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19241v1)