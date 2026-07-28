---
title: MixQuant: Adaptive Mixed-Precision Quantization for Large Language Models
published: 2026-07-25T05:10:01Z
authors: Ashitabh Misra, Madhav Agrawal, Arham Jain, Tarek Abdelzaher
url: http://arxiv.org/abs/2607.23047v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MixQuant: Adaptive Mixed-Precision Quantization for Large Language Models

## Abstract
Mixed-precision quantization improves the accuracy of post-training quantization by allocating higher bitwidths to sensitive layers, but existing methods solve the allocation for a single fixed memory budget. In practice the budget varies across deployments and is unknown at calibration time. Adaptive quantization addresses this with one offline calibration that serves any budget, yet current methods score layer sensitivity in a manner that does not consider its dependency on quantization levels of other layers. We show that a layer's sensitivity depends strongly on the bitwidths of its upstream layers and that this dependence shifts the resulting preferred bit allocation. We propose MixQuant, a technique-agnostic adaptive framework that wraps any base quantizer. MixQuant marginalizes each layer's distortion over random quantized upstream configurations to obtain budget-agnostic scores, calibrates the quantizer's parameters on plans the allocator itself produces, and penalizes allocations that leave layers at the lowest bitwidths. A single greedy pass then serves any budget at deployment. Across Llama-3.2-3B, Llama-2-7B, and Mistral-7B under AWQ and GPTQ, MixQuant outperforms adaptive and mixed-precision baselines in every setting, improving average accuracy by up to 8 points and reducing perplexity from 12.43 to 10.70 at the tightest budget, while matching an ILP solver at negligible deployment cost.

## Metadata
- **Published**: 2026-07-25T05:10:01Z
- **Authors**: Ashitabh Misra, Madhav Agrawal, Arham Jain, Tarek Abdelzaher
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23047v1)