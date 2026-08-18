---
title: ENAF: A Multi-Exit Network with an Adaptive Patch Fusion for Large Image Super Resolution
url: http://arxiv.org/abs/2608.15349v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_18-06-28Z_ENAF_AMulti_ExitNetworkwithanAdaptivePatchFusionfo.md
generated_at: 2026-08-17 21:36
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ENAF, a dynamic network for large image super-resolution that uses early exits and an adaptive patch fusion to balance quality and computational cost. It replaces handcrafted edge scores with a tiny PSNR estimator at each exit, enabling efficient routing of patches. Experiments on 2K-8K images show improved performance relative to static networks.

## Key Takeaways
- ENAF employs multiple early exits that estimate PSNR locally to assign patches based on texture hardness rather than relying solely on edge detection.
- The adaptive fusion mechanism merges patch outputs only when necessary, reducing redundant computation while preserving image quality.
- Benchmarks demonstrate that ENAF achieves higher PSNR and faster inference compared to baseline SISR models across diverse datasets.

## Context
Large image super-resolution remains a bottleneck for real-time applications due to high computational demands. Dynamic networks aim to alleviate this by selectively processing easier patches, yet most rely on simplistic texture metrics that ignore fine-grained quality differences.

## Implications
This approach offers a scalable template for other vision tasks where early exit strategies can be combined with lightweight quality estimators. Practitioners may adopt ENAF's fusion logic to create cost‑effective pipelines for high‑resolution image generation and medical imaging analysis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15349v1)
