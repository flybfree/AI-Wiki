---
title: H-Scale: Hessian-Guided Scale Refinement for NVFP4 Sub-Byte LLM Inference
published: 2026-08-28T09:22:17Z
authors: Hao Yu, Zheng Li, Dayiheng Liu, Jianwei Zhang
url: http://arxiv.org/abs/2608.28113v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# H-Scale: Hessian-Guided Scale Refinement for NVFP4 Sub-Byte LLM Inference

## Abstract
The NVIDIA Blackwell architecture, with native support for the ultra-fine-grained NVFP4 format, opens new opportunities for accelerating large language model (LLM) inference. NVFP4's micro-block design, such as a group size of 16, offers strong representational flexibility for capturing local weight distributions and isolating outliers, but it also introduces a large and highly sensitive space of per-group scaling factors. Existing post-training quantization (PTQ) methods primarily focus on refining quantized weight values, leaving this scale-selection step underexplored. To address this gap, we propose \textbf{H-Scale}, a lightweight post-processing method for NVFP4 per-group scale refinement. Instead of minimizing plain weight reconstruction error, H-Scale selects hardware-valid group scales using a diagonal second-order proxy derived from calibration activations, thereby targeting layer output perturbation more directly. It is designed as a drop-in replacement for RTN-style scale selection in diverse NVFP4 pipelines, requires only modest offline calibration, and introduces strictly zero overhead at inference time. Under a fixed evaluation protocol, experiments on mainstream LLMs show that H-Scale generally improves a broad range of NVFP4 baselines and brings several variants closer to the BF16 reference.

## Metadata
- **Published**: 2026-08-28T09:22:17Z
- **Authors**: Hao Yu, Zheng Li, Dayiheng Liu, Jianwei Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28113v1)