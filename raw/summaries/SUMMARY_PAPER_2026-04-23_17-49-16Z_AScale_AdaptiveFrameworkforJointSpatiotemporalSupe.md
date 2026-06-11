---
title: A Scale-Adaptive Framework for Joint Spatiotemporal Super-Resolution with Diffusion Models
url: http://arxiv.org/abs/2604.21903v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-04-23_17-49-16Z_AScale_AdaptiveFrameworkforJointSpatiotemporalSupe.md
generated_at: 2026-06-11 10:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a scale‑adaptive framework for joint spatiotemporal super‑resolution that can be reused across different upscaling factors. By separating the conditional mean, attention, and diffusion residual, the model adapts hyperparameters to larger factors while preserving mass conservation. Experiments on French precipitation data show a single architecture works from 1 to 25 spatial and 1 to 6 temporal scales.

## Key Takeaways
- The framework decouples the deterministic prediction of the conditional mean with attention and a residual diffusion model, allowing separate tuning for each super‑resolution factor.
- Hyperparameter adaptation includes increasing diffusion noise amplitude beta for larger factors, setting temporal context length L to keep attention horizons comparable across cadences, and optionally applying a mass‑conservation function f that tapers extreme amplification.
- The same architecture spans spatial upscaling from 1 to 25 and temporal up to 6 frames, providing a reusable tuning recipe across scales.

## Context
Joint spatiotemporal super‑resolution remains challenging because most models are fixed to a single pair of factors, limiting flexibility for climate data where both space and time vary. This work demonstrates that adaptable architectures can handle diverse factors without redesigning the model structure.

## Implications
For meteorologists and remote‑sensing analysts, this approach enables efficient generation of high‑resolution precipitation maps across multiple temporal resolutions, supporting better climate modeling and early warning systems. Practitioners can adopt a single model pipeline with minimal retraining effort for new scale combinations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2604.21903v1)
