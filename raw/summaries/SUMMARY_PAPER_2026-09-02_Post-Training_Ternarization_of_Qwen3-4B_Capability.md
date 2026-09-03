---
title: Post-Training Ternarization of Qwen3-4B Capability, Effective Bit Budget, Storage Compression, and Deployment
url: http://arxiv.org/abs/2609.01962v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_00-42-54Z_Post_TrainingTernarizationofQwen3_4BCapability_Eff.md
generated_at: 2026-09-02 20:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents an end-to-end post-training conversion of Qwen3-4B using KOTMS rotation and E2M-ATQ ternarization with GPTQ error compensation, achieving 1.641 effective bits per weight while keeping activations in FP16; it reduces model size to ~3.96 GiB without significant loss of task performance.

## Key Takeaways
- Effective bit accounting shows 1.641 bits per weight for quantized linear weights, targeting 81.62% of parameters.
- Capability retention is uneven: BoolQ keeps 84.6% teacher accuracy while ARC‑Challenge drops to 43.8%, indicating model-specific sensitivity.
- Perplexity increases on benchmark corpora (WikiText‑2 from 13.639 to 18.748, PTB from 24.700 to 31.992), reflecting compression trade-offs.

## Context
Ultra-low-bit quantization is a key driver for deploying large language models on edge devices where memory and bandwidth are limited; this work demonstrates that such compression can be applied without major quality loss, supporting broader accessibility.

## Implications
Practitioners can adopt similar post-training ternarization pipelines to shrink model footprints while maintaining usable performance, though inference speed may suffer due to slower GEMV kernels. The findings encourage careful evaluation of per-task degradation rather than a single “1.58-bit” label.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01962v1)
