---
title: Universal Thermodynamic Interatomic Potentials for Crystalline Materials
url: http://arxiv.org/abs/2608.14502v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_17-16-27Z_UniversalThermodynamicInteratomicPotentialsforCrys.md
generated_at: 2026-08-16 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents the thermodynamic interatomic potential (TIP) that converts a static interatomic potential into a thermodynamically consistent Gibbs free energy model. By training on free energies from quasi‑harmonic to molecular dynamics calculations and calibrating to higher‑resolution data, TIP provides an equation of state and phase transition identification from a single evaluation. The approach enables finite‑temperature phase stability for high‑throughput discovery.

## Key Takeaways
- TIP extends interatomic potentials to include Gibbs free energy with automatic differentiation linking temperature and pressure responses.
- A single model return both the equation of state and locates all competing phases, including dynamically stabilized ones.
- Fine‑tuning of TIP can predict alloy solubility limits and miscibility gaps beyond simple phase boundaries.

## Context
The integration of free energies into materials modeling is essential for accurate phase stability predictions but has been limited by computational cost. This work bridges that gap by offering a scalable thermodynamic potential, aligning with AI’s role in accelerating material discovery through data‑driven models.

## Implications
High‑throughput screening can now incorporate temperature and pressure effects without expensive simulations, reducing development timelines for new materials. Industries ranging from batteries to aerospace will benefit from faster, reliable phase stability assessments enabled by TIP.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14502v1)
