---
title: AGQ: Action-Guided Ultra-Low-Bit Quantization for Vision-Language-Action Models
published: 2026-10-21T06:22:51Z
authors: Xuhong Qiu, Zhuoyu Wu, Qiawei Zheng, Wenhui Ou, Wenqi Fang, Raphaël C. -W. Phan
url: http://arxiv.org/abs/2610.33074v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AGQ: Action-Guided Ultra-Low-Bit Quantization for Vision-Language-Action Models

## Abstract
Vision-language-action (VLA) models enable robots to perform tasks specified through natural-language instructions, but their large weight footprint challenges deployment on memory-constrained onboard platforms. Ultra-low-bit quantization reduces this footprint, yet preserving task performance and controlling weight recovery costs remain challenging. We propose Action-Guided Quantization, which combines action sensitivity with a measured proxy for weight recovery cost to allocate matrix bitwidths under storage budgets. Per-channel calibration compensates for quantization error, while a uniform bitwidth within each matrix preserves regular layouts. Bit-dependent grouped lossless coding reduces resident weight storage, and block-wise recovery limits temporary buffers. On LIBERO, AGQ achieves 92.7% task success at W3, exceeding AWQ and GPTQ by 1.2 and 3.7 percentage points, respectively, and retains 70.5% success at W2.5. An asymmetric configuration, denoted W1.5$^{*}$, uses W4 vision weights and a parameter-weighted average of 1.5 bits for language weights. With lossless coding, it achieves $6.10\times$ complete-model compression relative to BF16 while retaining 25.5% task success. Code and experimental results are available at https://github.com/Qiuxu00/AGQ

## Metadata
- **Published**: 2026-10-21T06:22:51Z
- **Authors**: Xuhong Qiu, Zhuoyu Wu, Qiawei Zheng, Wenhui Ou, Wenqi Fang, Raphaël C. -W. Phan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.33074v1)