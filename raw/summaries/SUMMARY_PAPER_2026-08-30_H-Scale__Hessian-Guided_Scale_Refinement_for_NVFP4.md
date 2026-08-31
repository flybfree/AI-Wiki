---
title: H-Scale: Hessian-Guided Scale Refinement for NVFP4 Sub-Byte LLM Inference
url: http://arxiv.org/abs/2608.28113v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_09-22-17Z_H_Scale_Hessian_GuidedScaleRefinementforNVFP4Sub_B.md
generated_at: 2026-08-30 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces H-Scale a lightweight post‑processing method for NVFP4 per‑group scale refinement that improves LLM inference on the Blackwell architecture. Experiments show it generally boosts performance of existing NVFP4 baselines and moves several variants closer to BF16 reference accuracy.

## Key Takeaways
- H-Scale selects hardware‑valid group scales using a diagonal second‑order proxy derived from calibration activations instead of minimizing plain weight reconstruction error.
- The method is designed as a drop‑in replacement for RTN‑style scale selection and works across diverse NVFP4 pipelines with only modest offline calibration.
- It introduces strictly zero overhead at inference time while still refining per‑group scaling factors to target layer output perturbation.

## Context
The rapid adoption of the NVIDIA Blackwell GPU architecture enables ultra‑fine‑grained quantization formats such as NVFP4 which can reduce memory bandwidth and improve energy efficiency. However, the fine‑grained design creates a large space of per‑group scaling factors that are sensitive to calibration, making scale selection a critical yet underexplored bottleneck in PTQ pipelines.

## Implications
For practitioners deploying LLM inference on Blackwell hardware H-Scale offers a simple way to extract extra performance without redesigning quantization pipelines. The zero‑inference‑time cost makes it attractive for production systems where latency and power are paramount, potentially widening the gap between quantized models and their near‑native BF16 counterparts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28113v1)
