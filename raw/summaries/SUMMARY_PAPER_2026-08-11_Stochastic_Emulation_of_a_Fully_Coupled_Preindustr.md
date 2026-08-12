---
title: Stochastic Emulation of a Fully Coupled Preindustrial E3SMv3 Simulation
url: http://arxiv.org/abs/2608.10277v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_22-19-59Z_StochasticEmulationofaFullyCoupledPreindustrialE3S.md
generated_at: 2026-08-11 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a stochastic emulator for E3SMv3 that couples ACE2S with Samudra to capture internal variability. Trained on 105 years of preindustrial data it reproduces mean climate while preserving variability across timescales, though rare extremes are underestimated.

## Key Takeaways
- The stochastic training preserves the ENSO power spectrum and eddy-rich SST anomalies, demonstrating that internal variability is retained in the emulator.
- Daily precipitation up to the 99.99th percentile is reproduced accurately, showing high fidelity for common events.
- The emulator underestimates the rarest tropical extremes, indicating a limitation when modeling extreme weather.

## Context
In AI-driven climate science, stochastic emulators reduce computational cost while maintaining physical realism. This work exemplifies how machine learning can emulate complex Earth system dynamics with minimal data, highlighting the potential of probabilistic models to replace expensive simulations for routine analysis.

## Implications
These results suggest that stochastic coupled emulators could become standard tools for operational climate projections and risk assessment. Practitioners may adopt them to generate diverse ensembles without full model runs, though caution is needed when extrapolating to extreme events.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10277v1)
