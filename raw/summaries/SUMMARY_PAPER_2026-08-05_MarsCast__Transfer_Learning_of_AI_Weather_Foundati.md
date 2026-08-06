---
title: MarsCast: Transfer Learning of AI Weather Foundation Models to Planetary Atmospheres
url: http://arxiv.org/abs/2608.05054v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_17-03-13Z_MarsCast_TransferLearningofAIWeatherFoundationMode.md
generated_at: 2026-08-05 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper adapts the Earth‑trained GraphCast model to forecast Martian temperature and wind fields using the Mars Climate Database. Zero‑shot predictions capture current conditions but miss diurnal cycles, while fine‑tuned models learn variability within a few epochs. The study shows rapid adaptation yields accurate 10‑day forecasts.

## Key Takeaways
- Fine‑tuning GraphCast with Martian solar radiation and MCD variables enables the model to learn Martian thermal variability within as few as ten training epochs.
- Zero‑shot forecasts remain surprisingly accurate for present conditions but fail to reproduce diurnal cycles and rapid decay toward climatological means.
- Prediction quality improves with larger training samples and is sensitive to how seasonal initialization is set.

## Context
Transfer learning of Earth‑based AI weather models to alien atmospheres illustrates the potential of domain‑agnostic foundation models beyond terrestrial use. This work demonstrates that a single architecture can be repurposed for planetary science, expanding the scope of rapid climate simulation.

## Implications
These results provide a practical pathway for mission operators to generate fast, reliable Martian forecasts without extensive ground data. The approach could reduce reliance on costly experiments and support dust‑storm risk assessment, enhancing future human exploration planning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05054v1)
