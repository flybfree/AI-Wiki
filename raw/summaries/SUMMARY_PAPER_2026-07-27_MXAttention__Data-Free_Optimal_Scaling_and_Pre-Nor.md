---
title: MXAttention: Data-Free Optimal Scaling and Pre-Normalization Quantization for MXFP4 Attention
url: http://arxiv.org/abs/2607.24377v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_12-53-22Z_MXAttention_Data_FreeOptimalScalingandPre_Normaliz.md
generated_at: 2026-07-27 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MXAttention, a data‑free post‑training quantization method that tackles the quadratic cost of attention in diffusion video generation. By combining Universal Optimal Scaling (UOS) and Pre‑Normalization Quantization (PNQ), MXAttention eliminates calibration needs while preserving high‑quality image generation with minimal degradation.

## Key Takeaways
- UOS determines a distribution‑independent scaling boundary Qmax=7.25 using the periodic nature of power‑of‑two microscaling, eliminating the need for search or calibration and thus avoiding clipping‑underflow issues.
- PNQ quantizes unnormalized softmax exponentials before row‑wise summation, which prevents normalization errors that arise from post‑quantization rounding in standard MXFP4 approaches.
- Experiments on Wan2.2 and HunyuanVideo show that MXAttention reduces the VBench Imaging Quality gap to less than 5% compared with OCP MXFP4 while maintaining FP16‑level generation quality, achieving a degradation of under 0.01 absolute points across all VBench metrics.

## Context
The attention mechanism’s quadratic complexity limits the scalability of diffusion models for video synthesis, prompting research into lightweight quantization techniques that do not compromise fidelity. This work advances the field by providing a practical, calibration‑free solution that integrates seamlessly with existing attention pipelines without sacrificing performance.

## Implications
For practitioners developing real‑time video generation systems, MXAttention offers a viable path to lower memory and compute demands while preserving visual quality, potentially enabling deployment on edge devices. The method’s compatibility with strong NVFP4 baselines suggests broader applicability across diverse diffusion architectures, encouraging industry adoption of efficient quantization strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24377v1)
