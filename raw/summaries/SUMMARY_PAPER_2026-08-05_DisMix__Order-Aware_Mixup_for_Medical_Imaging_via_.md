---
title: DisMix: Order-Aware Mixup for Medical Imaging via Disentangling Ordinal and Non-Ordinal Features
url: http://arxiv.org/abs/2608.04652v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_10-10-21Z_DisMix_Order_AwareMixupforMedicalImagingviaDisenta.md
generated_at: 2026-08-05 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DisMix, an order-aware mixup method for ordinal classification in medical imaging that separates ordinal disease severity cues from appearance-level variation. By using a dual-codebook VQ-VAE, it mixes each subspace independently, preserving the ordinal structure while adding diversity. Experiments on four datasets show DisMix outperforms six image mixup baselines with six ordinal classifiers.

## Key Takeaways
- DisMix uses a dual-codebook VQ‑VAE to disentangle ordinal and non‑ordinal features, allowing independent interpolation of severity codes without corrupting the rank ordering.
- Ordinal codes are interpolated to generate meaningful intermediate ranks while non‑ordinal codes remain varied for appearance diversity.
- The method achieves the best aggregate performance among six image mixup baselines paired with six ordinal classifiers across four medical imaging datasets.

## Context
Medical disease grading relies on ordinal labels that encode severity progression, yet standard data augmentation like mixup blurs this ordering. This creates samples unsuitable for ranking tasks and can mislead clinicians interpreting graded images. The need for order‑preserving augmentations is highlighted by the gap between generic image mixing and clinical relevance.

## Implications
Preserving ordinal structure in medical imaging data could improve diagnostic consistency and reduce false positives/negatives caused by corrupted severity cues. Practitioners adopting DisMix may achieve more reliable model predictions, supporting better patient outcomes and regulatory approvals for AI‑based grading tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04652v1)
