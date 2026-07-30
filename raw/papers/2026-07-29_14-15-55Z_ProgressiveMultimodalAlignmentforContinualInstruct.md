---
title: Progressive Multimodal Alignment for Continual Instruction Tuning
published: 2026-07-29T14:15:55Z
authors: Duzhen Zhang, Yahan Yu, Qiaoyi Su, Jiahua Dong, Tielin Zhang
url: http://arxiv.org/abs/2607.26947v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Progressive Multimodal Alignment for Continual Instruction Tuning

## Abstract
Multimodal Large Language Models (MLLMs) rely on a projector to align visual representations with the language embedding space, making it central to cross-modal understanding. In Multimodal Continual Instruction Tuning (MCIT), however, shifting visual distributions and evolving instruction semantics cause this shared projector to drift, leading to projector-level forgetting, an issue largely overlooked by methods that focus primarily on the LLM backbone. We introduce Progressive Multimodal Alignment (PMA), a framework that enables the projector to adapt continually while preserving previously learned alignment. PMA detects multimodal distribution shifts via a lightweight representation descriptor and progressively expands projector experts only when needed. An expandable router integrates expert outputs based on multimodal features, while the original pretrained projector is retained as a stable alignment anchor. This progressive mechanism balances stability and plasticity with sub-linear parameter growth and serves as a method-agnostic add-on to existing MCIT approaches. Extensive experiments on two recent MCIT benchmarks demonstrate that mitigating projector-level forgetting yields consistent gains over prior state-of-the-art methods when combined with PMA. Moreover, PMA scales across diverse MLLM backbones, demonstrating robust and broadly applicable MCIT performance.

## Metadata
- **Published**: 2026-07-29T14:15:55Z
- **Authors**: Duzhen Zhang, Yahan Yu, Qiaoyi Su, Jiahua Dong, Tielin Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26947v1)