---
title: LoRA-GA$^2$: Low Rank Adaptation with Multi-step Gradient Adaptive Alignment
published: 2026-08-20T08:55:05Z
authors: Haonan He, Xinyue Fan
url: http://arxiv.org/abs/2608.19800v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LoRA-GA$^2$: Low Rank Adaptation with Multi-step Gradient Adaptive Alignment

## Abstract
Low-Rank Adaptation (LoRA) is a prominent fine-tuning method for large models, achieving competitive performance with reduced memory overhead. However, a persistent performance gap remains between LoRA and full fine-tuning. Recent studies have sought to narrow this gap by employing one-step gradient approximations of pretrained weights to align LoRA updates with the principal directions or intrinsic dimensionalities of full fine-tuning updates. Nevertheless, these approaches fail to capture the full dynamics of the gradients. In this paper, we propose LoRA-GA$^2$, an effective fine-tuning algorithm that fully leverages multi-step gradient information. Specifically, we introduce a lightweight probe for multi-step gradients of pretrained weights that incurs no additional GPU memory cost and only marginal time overhead. We further employ a spectrum-aware, importance-based rank allocation and optimal initialization derived from multi-step gradients. Extensive experimental results demonstrate that LoRA-GA$^2$ consistently outperforms existing LoRA variants while preserving the efficiency advantages of vanilla LoRA. For instance, LoRA-GA$^2$ surpasses the leading baseline by an average of 0.66 points on the GLUE benchmark, and outperforms the strongest baseline by 1.03 points on GSM8K and 0.87 points on HumanEval, respectively.

## Metadata
- **Published**: 2026-08-20T08:55:05Z
- **Authors**: Haonan He, Xinyue Fan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19800v1)