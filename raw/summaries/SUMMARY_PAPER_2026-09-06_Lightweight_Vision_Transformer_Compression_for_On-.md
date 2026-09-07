---
title: Lightweight Vision Transformer Compression for On-Device Plant Disease Detection in Resource-Constrained Agricultural Field Conditions
url: http://arxiv.org/abs/2609.05334v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_16-40-06Z_LightweightVisionTransformerCompressionforOn_Devic.md
generated_at: 2026-09-06 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a unified compression framework for Vision Transformers that combines Hessian‑Balanced Adaptive Block Pruning, quantization, and attention‑based knowledge distillation to reduce model size while preserving accuracy. On a chilli disease detection dataset the integrated pipeline achieves 95.13 % accuracy with a 6.01 MB INT8 footprint—a 54.5× reduction from the original 327.42 MB model—matching or exceeding the FP32 baseline.

## Key Takeaways
- The H‑BAC pruning method, guided by second‑order sensitivity estimates, removes low‑impact blocks without harming classification performance.  
- Quantization to INT8 further shrinks the model size while maintaining accuracy within a narrow margin of the full‑precision result.  
- Knowledge distillation transfers knowledge from the large FP32 teacher to the compressed student, enabling high accuracy at a tiny footprint.

## Context
Vision Transformers dominate image classification but their memory and compute demands limit deployment on low‑power agricultural sensors. Existing compression techniques are often applied separately, making it hard to know which combination yields the best trade‑off for real‑world constraints.

## Implications
The results show that pruning and distillation can be combined effectively to create compact models suitable for edge devices in field settings. Practitioners can adopt this pipeline to deliver reliable disease detection without expensive hardware upgrades or large data centers.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.05334v1)
