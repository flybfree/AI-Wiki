---
title: Rewriting or Reweighting? A Geometric Account in Language Models
published: 2026-08-03T07:46:28Z
authors: Juntong Wang, Shengkun Yang, Xiyuan Wang, Muhan Zhang
url: http://arxiv.org/abs/2608.01835v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rewriting or Reweighting? A Geometric Account in Language Models

## Abstract
Post-training can substantially alter language-model behavior, yet aggregate behavior rates do not reveal whether training removes an existing mechanism, creates a new one, or changes how an inherited mechanism is used. We study this question through two mechanistically distinct failures, repetition as a decoding-attractor pathology and sycophancy as a preference-related alignment failure. We introduce behavioral manifold analysis, which isolates behavior-specific geometry by selecting sparse behavior-associated coordinates and lifting them into low-dimensional local charts. We construct these charts in two complementary spaces. ACT captures runtime activation states, while NOC quantifies how strongly the model routes functional information flow through the shared behavior-associated subspace. Across multiple model families, the resulting charts are highly compressed and partially alignable across architectures. Contribution-space charts expose a more architecture-robust shared core, whereas activation-space charts retain stronger family-specific structure. Tracking these charts through controlled post-training reveals a consistent asymmetry. Supervised fine-tuning substantially alters the inherited behavioral geometry, whereas reward optimization changes behavior while largely preserving the underlying chart. This geometric perspective provides a unified framework for understanding the mechanistic distinction between the two objectives. SFT tends to rewrite behavioral geometry, whereas reward optimization primarily reweights it. Code is available at https://github.com/ronglingze/Manifold-Analysis

## Metadata
- **Published**: 2026-08-03T07:46:28Z
- **Authors**: Juntong Wang, Shengkun Yang, Xiyuan Wang, Muhan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01835v1)