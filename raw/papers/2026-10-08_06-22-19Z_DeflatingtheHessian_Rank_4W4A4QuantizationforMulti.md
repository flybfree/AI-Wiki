---
title: Deflating the Hessian: Rank-4 W4A4 Quantization for Multimodal Diffusion Transformers
published: 2026-10-08T06:22:19Z
authors: Shiwen Wang, Pengxiang Zhao, Xiaoming Yuan
url: http://arxiv.org/abs/2610.11315v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Deflating the Hessian: Rank-4 W4A4 Quantization for Multimodal Diffusion Transformers

## Abstract
In diffusion transformers, low-rank branches can mitigate 4-bit weight--activation (W4A4) post-training quantization (PTQ) loss by decomposing each weight into a low-bit residual and a high-precision low-rank component. Existing low-rank PTQ approaches, however, either optimize low-rank compensation and residual quantization separately, often requiring higher ranks, or rely on second-order weight updates without explicitly modeling activation quantization error, which becomes particularly pronounced under 4-bit quantization. To address these limitations, we present \method{}, a unified framework modeling low-rank-assisted W4A4 PTQ as a coupled calibration problem and deriving optimization-based solvers from the joint objective. Eliminating the output-side low-rank factor yields a \emph{deflated Hessian} that discounts residual errors already captured by the low-rank component, while an activation-noise surrogate is incorporated to suppress activation quantization error. Across five diffusion backbones, rank-4 \method{} consistently outperforms rank-4 SVDQuant in PSNR and LPIPS. It further surpasses rank-32 SVDQuant on SANA-1.6B, FLUX.1-schnell, and FLUX.1-dev with an $8\times$ smaller rank and up to $6.25\times$ faster quantization. Furthermore, on the Qwen3-8B LLM, rank-4 \method{} improves MMLU accuracy from 61.50\% to 68.17\% over rank-32 SVDQuant. Overall, \method{} achieves better W4A4 performance with substantially lower rank and quantization cost.

## Metadata
- **Published**: 2026-10-08T06:22:19Z
- **Authors**: Shiwen Wang, Pengxiang Zhao, Xiaoming Yuan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11315v1)