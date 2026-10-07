---
title: OSFP4: Joint Optimization of Diagonal Smoothing and Block Scales for NVFP4 Quantization
published: 2026-10-06T12:17:52Z
authors: Neriah Ben David, Ori Meir, Or Ordentlich
url: http://arxiv.org/abs/2610.08231v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OSFP4: Joint Optimization of Diagonal Smoothing and Block Scales for NVFP4 Quantization

## Abstract
NVFP4 is an attractive datatype for large language model (LLM) inference, offering compact storage and native tensor-core acceleration. However, preserving accuracy using NVFP4 requires careful quantization. In this work we develop a novel quantization scheme called Optimized Smoothing and Scaling for NVFP4 (OSFP4). For each linear projection it uses a diagonal smoothing matrix whose entries are optimized to minimize the squared matrix-product quantization error under NVFP4, taking into account the rounding procedure that is used (either round-to-nearest, or GPTQ-style successive interference cancellation). This requires performing joint optimization on the smoothing entries as well as the block scales, which is facilitated by analyzing a multiplicative-dither FP4 quantizer instead of the fixed deterministic one. Experiments show that OSFP4 achieves the highest average accuracy among the evaluated competitors in the corresponding quantization settings, while retaining approximately 94-97\% of vendor NVFP4 prefill throughput on the measured workloads. Our code is available in https://github.com/neriahbd/OSFP4

## Metadata
- **Published**: 2026-10-06T12:17:52Z
- **Authors**: Neriah Ben David, Ori Meir, Or Ordentlich
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.08231v1)