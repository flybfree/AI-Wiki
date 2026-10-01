---
title: RATIO: Reasoning Analysis and Token-level Inference Optimization for Quantized Reasoning Models
published: 2026-09-30T14:14:24Z
authors: Chengzhu Bao, Xianglong Yan, Tianao Zhang, Jiaqi Chen, Shaoqiu Zhang, Yulun Zhang
url: http://arxiv.org/abs/2609.39801v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RATIO: Reasoning Analysis and Token-level Inference Optimization for Quantized Reasoning Models

## Abstract
Post-training quantization (PTQ) has become a widely adopted technique for reducing the memory footprint and inference cost of large language models (LLMs). However, recent studies reveal that when applied to reasoning models, PTQ not only degrades reasoning performance but also exacerbates overthinking, leading to longer reasoning trajectories. These issues may offset the efficiency gains expected from lower-precision inference. Existing approaches mainly rely on complex optimization procedures. More recent lightweight inference strategies instead use predefined overthinking markers, limiting their adaptability across quantized models. To address these issues, we propose Reasoning Analysis and Token-level Inference Optimization (RATIO), a framework that identifies model-specific overthinking tokens and assigns each a tailored penalty. RATIO first introduces Quantization-aware Reasoning Behavior Analysis (QRBA) to identify overthinking tokens by analyzing discrepancies between full-precision and quantized models. It then adopts Token-Specific Penalty Determination (TSPD), which leverages full-precision guidance to derive token-specific penalties without additional training. Extensive experiments show that RATIO achieves a better accuracy-efficiency trade-off than existing token-level interventions. Specifically, RATIO achieves up to 9.8 points accuracy improvement and reduces chain-of-thought (CoT) length by up to 51.3% compared with quantized baselines. The code will be available at https://github.com/steven-bao1/RATIO.

## Metadata
- **Published**: 2026-09-30T14:14:24Z
- **Authors**: Chengzhu Bao, Xianglong Yan, Tianao Zhang, Jiaqi Chen, Shaoqiu Zhang, Yulun Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39801v1)