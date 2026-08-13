---
title: Temperature-Driven Sequential Modeling for the Prediction of Annual Power Conversion Efficiency Profiles of Organic Photovoltaic Materials: Douala Case Study
url: http://arxiv.org/abs/2608.11261v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-09_16-24-18Z_Temperature_DrivenSequentialModelingforthePredicti.md
generated_at: 2026-08-12 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a climate‑native computational framework that predicts the annual power conversion efficiency of organic photovoltaic donor molecules under real tropical operating conditions. Using a combination of GFN2‑xTB molecular dynamics and an equivariant graph neural network surrogate, it trains sequential deep learning models on NASA POWER climate data for Douala, Cameroon, and validates them with zero‑shot transfer to Yaoundé and Maroua. The framework outperforms static baselines by 35–48 % relative MAE improvement.

## Key Takeaways
- The sequential model captures temperature‑driven conformational changes that static PCE values ignore, leading to a 35–48 % lower mean absolute error than time‑averaged baselines.  
- Validation across three Cameroonian cities demonstrates zero‑shot transfer capability, showing the framework’s geographic robustness beyond its training location.  
- A seasonal stability score ranks molecules by performance consistency under tropical conditions, revealing deployment suitability that diverges from static PCE rankings.

## Context
This work advances AI‑driven materials discovery for photovoltaics by integrating physics‑based molecular dynamics with deep learning to model time‑dependent device behavior. It exemplifies how sequential models can replace simpler averaging techniques in climate‑sensitive applications.

## Implications
For solar developers, the seasonal stability score offers a practical metric to prioritize OPV candidates that retain efficiency under heat and humidity. Practitioners can use the framework to screen thousands of molecules efficiently, accelerating deployment planning in tropical markets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11261v1)
