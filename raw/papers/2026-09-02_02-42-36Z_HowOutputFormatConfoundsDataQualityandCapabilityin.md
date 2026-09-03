---
title: How Output Format Confounds Data Quality and Capability in Instruction Tuning
published: 2026-09-02T02:42:36Z
authors: Chengguang Gan, Hanjun Wei, Yunhao Liang, Qinghao Zhang, Shiwen Ni, Zhixi Cai
url: http://arxiv.org/abs/2609.02015v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Output Format Confounds Data Quality and Capability in Instruction Tuning

## Abstract
Instruction-tuning data are judged by quality metrics, and tuned models are judged by benchmarks, but both judgments pass through an output interface: the surface format in which an answer is written. Using gradient signatures across 12 tasks, four semantically equivalent interfaces, three model families, and controlled corruptions, we show that this interface confounds both measurements. Spectral statistics such as effective rank are provably invariant to interface rotation and empirically blind to semantic corruption, while the direction of the update carries the quality signal. The interface-varying residual is not noise: it identifies each unit's own target task perfectly across all three families. Capability itself is stored relative to the training interface: a skill that raises accuracy by more than 40 points under the training format can be nearly invisible under every other, and correcting a single generation budget flips the measured effect of fine-tuning on GSM8K from a gain into a large loss. Pre-registered interventions delimit where this geometry stops short of control. Data quality and model capability are interface-conditioned quantities, and current practice often reports the interface instead of the content.

## Metadata
- **Published**: 2026-09-02T02:42:36Z
- **Authors**: Chengguang Gan, Hanjun Wei, Yunhao Liang, Qinghao Zhang, Shiwen Ni, Zhixi Cai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02015v1)