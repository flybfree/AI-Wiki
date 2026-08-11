---
title: Particle-Based Conformal Prediction for Contact-Aware Uncertainty Calibration in Stratified Configuration Spaces
url: http://arxiv.org/abs/2608.09166v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_06-22-10Z_Particle_BasedConformalPredictionforContact_AwareU.md
generated_at: 2026-08-11 12:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CaPTURe, a particle-based conformal prediction method that accounts for contacts between robots and obstacles in planning. It generates calibrated uncertainty regions by calibrating motion models from transition data, ensuring coverage even when the true configuration space is multimodal or low‑dimensional. Experiments on marble navigation and peg‑in‑hole insertion show up to 30% higher success rates than baselines.

## Key Takeaways
- CaPTURe uses a calibration dataset of system transitions to locally adjust motion uncertainty, producing regions that contain the future configuration with user‑set probability even when contacts cause multimodal or low‑dimensional configurations.
- The method’s particle representation captures both stochastic and model‑mismatch sources of uncertainty, providing geometrically valid prediction sets for arbitrary fidelity models.
- In simulations, CaPTURe meets coverage requirements both in contact and out of contact scenarios, improving task success rates compared to state‑of‑the‑art baselines.

## Context
Uncertainty quantification is crucial for safe autonomous robotics where motion models often deviate from reality due to limited data or simplifications. Conformal prediction offers principled ways to bound predictions but typically assumes a fixed distribution that may not reflect contact effects, leading to under‑coverage in real deployments.

## Implications
This work demonstrates that calibration can reconcile conformal guarantees with the complexities of physical interaction, offering practitioners a tool for more reliable planning and higher task success. The approach could be extended to real‑world manipulators and multi‑robot systems where safety margins are paramount.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09166v1)
