---
title: SOMTab: Set-Order Mamba for Efficient Tabular In-Context Learning
published: 2026-08-28T03:43:08Z
authors: Hao Wang, Siyu Zhang, Wei Ma
url: http://arxiv.org/abs/2608.27882v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SOMTab: Set-Order Mamba for Efficient Tabular In-Context Learning

## Abstract
Tabular foundation models based on in-context learning have recently emerged as strong alternatives to task-specific model fitting. However, the current performance frontier remains dominated by attention-heavy architectures, where attention is used throughout the modeling pipeline. This raises a natural question: is attention necessary at every stage of tabular in-context learning? We introduce SOMTab, a Set-Order Mamba architecture for efficient tabular in-context learning. SOMTab separates representation construction from query-conditioned retrieval. For row and column representations, it maps unordered table tokens into stable latent slots and applies Mamba-based state-space mixing to construct compact representations. For final prediction, it retains attention-based in-context learning to preserve query-conditioned retrieval from labeled context examples. We further introduce DCH-TailMix, a synthetic prior that combines degree-corrected graph heterogeneity with mixed heavy-tailed regimes to diversify synthetic dependency structures. Across tabular benchmarks, SOMTab approaches the performance of strong Transformer-based tabular foundation models while achieving faster inference and lower GPU memory usage, yielding a favorable efficiency--accuracy trade-off.

## Metadata
- **Published**: 2026-08-28T03:43:08Z
- **Authors**: Hao Wang, Siyu Zhang, Wei Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27882v1)