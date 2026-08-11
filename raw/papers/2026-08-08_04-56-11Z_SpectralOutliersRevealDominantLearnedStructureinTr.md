---
title: Spectral Outliers Reveal Dominant Learned Structure in Transformer Attention
published: 2026-08-08T04:56:11Z
authors: Kasun Dewage, Marianna Pensky, Suranadi De Silva, T. H. Bandara
url: http://arxiv.org/abs/2608.07921v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Spectral Outliers Reveal Dominant Learned Structure in Transformer Attention

## Abstract
We apply Marchenko-Pastur (MP) random matrix theory to pre-trained attention weights in order to separate each projection matrix into a random-like bulk and a set of spectral outliers. We validate this decomposition causally: zeroing the MP-identified outliers (signal) in Mistral-7B drives HellaSwag, MMLU, and PIQA close to random-chance performance, whereas zeroing a count-matched subset of bulk singular values causes smaller but non-negligible degradation. Across 11 pre-trained transformers we identify five recurring patterns: spectral outliers encode a dominant component of the learned structure; Q projections carry the most outliers; V projections under grouped-query attention lack a clean signal/noise separation; entry-level outliers form structured row-bands in Q and column-bands in O; and specific residual-stream dimensions persist as band outliers across layers in K and O. We close by outlining how these observations could inform parameter-efficient fine-tuning and structured pruning.

## Metadata
- **Published**: 2026-08-08T04:56:11Z
- **Authors**: Kasun Dewage, Marianna Pensky, Suranadi De Silva, T. H. Bandara
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07921v1)