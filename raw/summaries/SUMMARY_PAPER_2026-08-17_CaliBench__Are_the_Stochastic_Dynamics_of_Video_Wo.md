---
title: CaliBench: Are the Stochastic Dynamics of Video World Models Physically Calibrated?
url: http://arxiv.org/abs/2608.16829v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_17-14-50Z_CaliBench_AretheStochasticDynamicsofVideoWorldMode.md
generated_at: 2026-08-17 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
CaliBench evaluates whether video world models generate stochastic outcomes that are physically calibrated to known reference distributions. The study shows that most image‑to‑video models concentrate probability mass on a few outcomes, often collapsing to a single result, and that their performance varies across different scenes and model families.

## Key Takeaways
- CaliBench scores individual generations using interpretable discrete bins (e.g., die faces) rather than learned feature spaces, allowing direct measurement of total variation distance from the reference.  
- The benchmark reveals that many models exhibit severe miscalibration, producing distributions that are far from uniform or the known physical law, with some collapsing entirely to one outcome.  
- Significance is detected only for large deviations (N=32 per cell) via a chi‑squared test, indicating that small errors may not be statistically significant.

## Context
Video world models aim to approximate the true stochastic nature of physical processes, yet existing evaluation methods often treat uncertainty as a learned latent variable without grounding it in physics. CaliBench bridges this gap by using closed‑form reference distributions and discrete scoring, providing a more interpretable benchmark for assessing aleatoric uncertainty.

## Implications
For practitioners developing generative video systems, CaliBench highlights the need to prioritize uniform probability across outcomes rather than merely improving feature fidelity. The metric mnTV offers a clear, physics‑aware way to compare new models against established physical laws, guiding responsible AI design in domains where stochasticity matters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16829v1)
