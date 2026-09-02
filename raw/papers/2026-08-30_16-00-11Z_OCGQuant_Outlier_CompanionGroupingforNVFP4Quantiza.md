---
title: OCGQuant: Outlier-Companion Grouping for NVFP4 Quantization
published: 2026-08-30T16:00:11Z
authors: Yishan Yao, Binjun Li, Hanling Yi, Pengyu Li, Xiaoqing Liu, Zihan Yang, Xiaotian Yu, Zhiwen Yu
url: http://arxiv.org/abs/2609.00066v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OCGQuant: Outlier-Companion Grouping for NVFP4 Quantization

## Abstract
NVFP4 is an efficient microscaling format for low-bit inference, but activation outliers can still degrade quantization accuracy within NVFP4 blocks. Within each quantization block, large activations can dominate the block scale, increasing the quantization error of the remaining values sharing the same scale. Existing post-training quantization (PTQ) methods mitigate outlier errors through strategies such as mixed precision, rotation, or residual compensation, but these approaches are either not specifically tailored to NVFP4 or introduce additional computation. In this work, we revisit NVFP4 from a channel-grouping perspective and define the reducible error incurred by remaining block values under the scale set by the block maximum as Collateral Quantization Error. Based on this insight, we propose OCGQuant, a post-training quantization method centered on Outlier-Companion Grouping (OCG), which adaptively pairs outlier channels with low-magnitude companion channels to improve NVFP4 activation block composition. Experiments on Llama3 and Qwen3 show that OCGQuant achieves the lowest WikiText-2 perplexity and highest average downstream accuracy among evaluated PTQ methods, while maintaining prefill speedup close to RTN and matching its peak decoding memory. Code is available at https://github.com/Eshamont/OCGQuant.

## Metadata
- **Published**: 2026-08-30T16:00:11Z
- **Authors**: Yishan Yao, Binjun Li, Hanling Yi, Pengyu Li, Xiaoqing Liu, Zihan Yang, Xiaotian Yu, Zhiwen Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00066v1)