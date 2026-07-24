---
title: Self-Improving is Often Sudden: Enlightenment-style Finetuning for Large-Scale Models
published: 2026-07-15T02:43:34Z
authors: Jing-Xiao Liao, Tianwei Zhang, Yu-Hao Jiang, Feifei Zhang, Hang-Cheng Dong, Feng-Lei Fan
url: http://arxiv.org/abs/2607.13395v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Improving is Often Sudden: Enlightenment-style Finetuning for Large-Scale Models

## Abstract
The pursuit of autonomously self-improving models has attracted growing interest in the era of large-scale foundation models. Drawing inspiration from the concept of "enlightenment" or "aha moment" in human brain, we hypothesize that large models exhibit an analogous enlightenment phenomenon-a latent capacity for sudden capability boost. Then, we propose Enlightenment, a novel training-free post-tuning paradigm for large-scale models. Our approach modifies shortcuts for key modules/layers without weight updates, while existing training-free ones predominantly manipulate attention weights. We introduce two architecture-specific instantiations: i) For large language models, we propose attention head-mixing shortcuts that recalibrate attention weights by linking the initial attention head's output to all other target heads, modulated by an adaptive scaling factor initialization strategy. ii) For vision-language models, we apply a lightweight scalar-modulated factor to residual connections in the decoder layers, regulating information flow. Extensive experiments show that Enlightenment efficiently unlocks the latent potential of pre-trained networks, yielding remarkable performance improvements across diverse benchmarks and models.

## Metadata
- **Published**: 2026-07-15T02:43:34Z
- **Authors**: Jing-Xiao Liao, Tianwei Zhang, Yu-Hao Jiang, Feifei Zhang, Hang-Cheng Dong, Feng-Lei Fan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.13395v1)