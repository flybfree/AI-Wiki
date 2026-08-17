---
title: GeoCache: Training-Free Acceleration of Multi-View Texture Diffusion via Geometric Delta Transport
url: http://arxiv.org/abs/2608.13255v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_13-57-35Z_GeoCache_Training_FreeAccelerationofMulti_ViewText.md
generated_at: 2026-08-16 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a training‑free accelerator called gc that speeds up multi‑view texture diffusion by reusing geometry‑aligned updates across views without retraining or architectural changes. By evaluating a rotating subset of anchor views and transporting their per‑step xz updates to the remaining views, gc reduces denoiser evaluations while preserving visual fidelity. On test datasets it achieves 2.21× speedup with MV‑LPIPS 0.0293 and MV‑PSNR 33.60 dB, outperforming temporal caches above a step factor of two.

## Key Takeaways
- It evaluates a rotating subset of anchor views and transports per‑step xz updates to the remaining views, dramatically cutting per‑view denoiser evaluations.
- Periodic full‑view computation controls accumulated error while preserving the denoising trajectory across all steps.
- On Hunyuan3D‑2.1 it delivers 2.21× speedup with MV‑LPIPS 0.0293 and MV‑PSNR 33.60 dB, providing the best fidelity among accelerated methods above step factor two.

## Context
In AI‑generated textures, high‑quality multi‑view outputs are essential for realistic rendering pipelines. The approach aligns with trends toward training‑free optimization of diffusion models to reduce inference latency and computational cost.

## Implications
This method offers a practical way to accelerate texture generation in real‑time applications without costly retraining or hardware changes. It enables faster deployment of high‑fidelity multi‑view textures across diverse platforms, supporting broader adoption of diffusion‑based rendering tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13255v1)
