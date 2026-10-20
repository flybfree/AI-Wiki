---
title: PACT: NVFP4 Data-Flow LoRA Fine-Tuning on Consumer GPUs
published: 2026-10-18T06:14:14Z
authors: Lei Gao, Hossein Entezari Zarch, Chaoyi Jiang, Murali Annavaram
url: http://arxiv.org/abs/2610.25048v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PACT: NVFP4 Data-Flow LoRA Fine-Tuning on Consumer GPUs

## Abstract
Fine-tuning language models on consumer GPUs is constrained by computation and memory. Although LoRA reduces trainable parameters and optimizer state, frozen projections remain expensive, and activations retained for backward can dominate memory usage. We present PACT, a LoRA fine-tuning system that accelerates frozen projections with native NVFP4 GEMMs while reducing quantization and dequantization overhead and limiting quantization error. To reduce activation memory, PACT reuses quantized RMSNorm outputs and saves gate/up activations in NVFP4 for backward. To limit numerical error, it preserves BF16 inputs for forward nonlinear operations and calibrates frozen weights offline using GPTQ adapted to NVFP4 scales and quantized activations. Fused nonlinear kernels and cached forward and backward weight layouts reduce quantization and dequantization overhead. Evaluations across multiple models and tasks on a 16\,GB RTX~5080 show lower memory usage and faster LoRA fine-tuning with competitive accuracy, enabling model adaptation on resource-constrained consumer hardware.

## Metadata
- **Published**: 2026-10-18T06:14:14Z
- **Authors**: Lei Gao, Hossein Entezari Zarch, Chaoyi Jiang, Murali Annavaram
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25048v1)