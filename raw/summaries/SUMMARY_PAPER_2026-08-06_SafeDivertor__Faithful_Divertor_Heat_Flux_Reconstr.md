---
title: SafeDivertor: Faithful Divertor Heat Flux Reconstruction from Macroscopic Plasma State Signals via Time-Frequency Prior Exploitation
url: http://arxiv.org/abs/2608.05669v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_07-05-58Z_SafeDivertor_FaithfulDivertorHeatFluxReconstructio.md
generated_at: 2026-08-06 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SafeDivertor, a framework that reconstructs time-resolved radial heat-flux profiles from macroscopic plasma-state signals during discharge without needing infrared inversion or detailed material models. It achieves the best performance across five evaluation metrics on the DivMPS2HF dataset compared to baselines. The method combines prior-aware initialization, input perturbation, spectral optimization and progressive training.

## Key Takeaways
- SafeDivertor reconstructs heat-flux directly from plasma signals, eliminating reliance on infrared measurements or device-specific conduction models.
- The framework uses a multi-source discharge dataset DivMPS2HF to provide realistic benchmark data for signal‑based reconstruction.
- By integrating time-frequency priors and progressive training, the method stabilizes optimization while preserving transient dynamics.

## Context
This work advances AI applications in plasma physics by demonstrating that deep learning can replace traditional inverse heat-conduction simulations. It shows how prior knowledge can be encoded into neural architectures to improve reliability and speed of diagnostics in magnetic confinement fusion devices.

## Implications
For industry, SafeDivertor offers a real-time solution for monitoring divertor performance, reducing downtime and maintenance costs. Practitioners can adopt the framework to integrate heat-flux data directly into control loops without costly hardware upgrades.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05669v1)
