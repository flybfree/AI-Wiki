---
title: Recurrent Residual Quantization: A Progressive Multi-Precision Representation for LLMs
published: 2026-08-04T08:32:05Z
authors: Yu Luo, Bo Dong, Wenhua Cheng, Haihao Shen
url: http://arxiv.org/abs/2608.04048v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Recurrent Residual Quantization: A Progressive Multi-Precision Representation for LLMs

## Abstract
Serving large language models (LLMs) under diverse deployment constraints requires flexible trade-offs between accuracy, memory footprint, and throughput. However, conventional quantization methods typically require a separate checkpoint for each target bit-width. We introduce Recurrent Residual Quantization (RRQ), a post-training quantization (PTQ) framework that represents weights as a low-bit quantized base together with a sequence of quantized residual corrections, enabling multiple effective precisions from a single checkpoint. Starting from a 2-bit model obtained via post-training quantization (PTQ) or round-to-nearest (RTN), RRQ progressively adds lightweight 2-bit residuals generated via RTN to construct 4-, 6-, and 8-bit representations. The method is calibration-free and avoids joint multi-bit optimization. In our Qwen3-8B setup, the full all-RTN 2-/4-/6-/8-bit package is constructed in 1,293 seconds, 3.3 times faster than the measured MatGPTQ construction. Experiments on six recent LLMs show competitive accuracy at 6 and 8 bits, with model-dependent behavior at 4 bits. The code will be made publicly available upon publication.

## Metadata
- **Published**: 2026-08-04T08:32:05Z
- **Authors**: Yu Luo, Bo Dong, Wenhua Cheng, Haihao Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04048v1)