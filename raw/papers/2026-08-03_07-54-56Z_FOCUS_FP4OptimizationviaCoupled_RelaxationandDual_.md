---
title: FOCUS: FP4 Optimization via Coupled-Relaxation and Dual-Granularity Scaling
published: 2026-08-03T07:54:56Z
authors: Xianglong Yan, Hong Liu, Chengzhu Bao, Tianao Zhang, Guanghua Yu, Jianchen Zhu, Yulun Zhang
url: http://arxiv.org/abs/2608.01847v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FOCUS: FP4 Optimization via Coupled-Relaxation and Dual-Granularity Scaling

## Abstract
Large language models (LLMs) achieve remarkable performance but are expensive to deploy due to their enormous size. FP4 quantization, with formats such as MXFP4 and NVFP4, offers an appealing solution with native hardware support on modern accelerators. However, maintaining accuracy under FP4 precision remains difficult. A key bottleneck lies in scale optimization: existing methods tightly couple the quantization and dequantization scales, forcing both to conform to the discrete low-precision format required by hardware, such as E8M0 in MXFP4. Yet the quantization scale is never stored and need not obey this constraint, suggesting a significant untapped optimization space. In this work, we propose FOCUS, a post-training quantization framework with end-to-end scale learning for FP4 Optimization via Coupled-Relaxation and Dual-Granularity Scaling. Coupled-Relaxation Scaling (CRS) relaxes the tight coupling between quantization and dequantization scales with a learnable full-precision coefficient, enabling more effective optimization without breaking hardware compliance. Dual-Granularity Scaling (DGS) further refines the quantization scale at a finer sub-block granularity, allowing more precise adaptation to local weight distributions. Experiments across multiple LLM families and benchmarks show that FOCUS achieves state-of-the-art FP4 accuracy under both MXFP4 and NVFP4 formats, while introducing no additional inference overhead. Code and quantized models will be released at https://github.com/tencent/AngelSlim.

## Metadata
- **Published**: 2026-08-03T07:54:56Z
- **Authors**: Xianglong Yan, Hong Liu, Chengzhu Bao, Tianao Zhang, Guanghua Yu, Jianchen Zhu, Yulun Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01847v1)