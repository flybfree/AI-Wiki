---
title: Dependency-Aware Revocable Decoding for Efficient Diffusion Large Language Model Inference
published: 2026-08-27T03:34:47Z
authors: Wooje Park, Insu Lee, Minyoung Noh, Jaeyun Jang, Sungmin Lee, Kyuhong Shim, Byonghyo Shim
url: http://arxiv.org/abs/2608.26574v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dependency-Aware Revocable Decoding for Efficient Diffusion Large Language Model Inference

## Abstract
Diffusion large language models (dLLMs) offer a promising alternative to autoregressive generation by decoding multiple tokens in parallel through iterative denoising. However, increasing decoding parallelism often degrades generation quality, as early errors can contaminate later contexts. Revocable decoding mitigates this issue by re-evaluating decoded tokens and remasking unreliable ones, but existing methods overlook that unreliable tokens may also corrupt the verification context itself. We identify this failure mode and propose Dependency-Aware Revocable Decoding (DARD), a training-free framework that separates tokens into masked, candidate, and unmasked states. DARD verifies candidate tokens using a selective context that excludes less reliable tokens and adaptively regulates their influence on subsequent decoding. Experiments across 12 textual and multimodal benchmarks on 3 open-source dLLMs show that DARD consistently improves the speed-quality Pareto frontier over recent revocable decoding methods, achieving a 2.71$\times$ speedup and a 4.35-point CIDEr score gain over Saber on Flickr30K.

## Metadata
- **Published**: 2026-08-27T03:34:47Z
- **Authors**: Wooje Park, Insu Lee, Minyoung Noh, Jaeyun Jang, Sungmin Lee, Kyuhong Shim, Byonghyo Shim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26574v1)