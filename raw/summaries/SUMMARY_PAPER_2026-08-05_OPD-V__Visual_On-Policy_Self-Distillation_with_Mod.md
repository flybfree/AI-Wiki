---
title: OPD-V: Visual On-Policy Self-Distillation with Modality Balance
url: http://arxiv.org/abs/2608.05131v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_17-53-06Z_OPD_V_VisualOn_PolicySelf_DistillationwithModality.md
generated_at: 2026-08-05 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the limitation of on‑policy self‑distillation (OPSD) in multimodal large language models by showing that modality imbalance can hinder reasoning improvement. The authors propose OPD-V, a visual OPSD framework that uses positive and negative teachers with varying modality balance to guide distillation. Experiments across multiple benchmarks demonstrate consistent gains in reasoning while lowering training cost.

## Key Takeaways
- Modality imbalance causes the model to ignore multimodal cues, leaving privileged information underused during self‑distillation.
- The Positive Teacher’s Zoom‑In image and Negative Teacher’s Mask image create distinct levels of modality balance that act as trusted signals for token selection.
- OPD-V selects on‑policy tokens within a modality‑balance trust region, leading to better reasoning performance across six benchmarks with reduced training effort.

## Context
Multimodal large language models aim to fuse text and visual inputs seamlessly, yet current post‑training methods often treat modalities as independent. The imbalance between dominant textual and visual information can degrade model behavior without explicit handling. This work highlights a nuanced source of privileged data that is currently overlooked in OPSD pipelines.

## Implications
Practitioners can adopt OPD-V to fine‑tune MLLMs with minimal compute, preserving the benefits of self‑distillation while mitigating modality bias. The approach offers a scalable way to improve reasoning accuracy without extensive dataset augmentation or costly training cycles.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05131v1)
