---
title: Stress-Testing EEG Foundation Models for Clinical Decoding: Dataset Identity and Targeted Negative Controls
url: http://arxiv.org/abs/2607.24519v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_14-59-42Z_Stress_TestingEEGFoundationModelsforClinicalDecodi.md
generated_at: 2026-07-27 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper evaluates six pretrained EEG foundation models on clinical decoding tasks using frozen linear probes and various split strategies across five datasets. It finds that model performance varies with dataset identity, evaluation unit, and comparator strength, showing both robust positive results and surprising negative controls.

## Key Takeaways
- Frozen REVE embeddings achieve 0.568 AUROC on Korean dementia while classical features reach 0.769, indicating strong domain shift that is not mitigated by simple projection.
- Dataset identity can be decoded from frozen embeddings with near‑perfect accuracy (AUROC 1.000 at PCA‑50), yet the same pipeline yields only 0.528 for diagnosis, highlighting limited diagnostic utility beyond classification.
- A randomly initialised encoder outperforms pretrained REVE on dementia detection (0.659 vs 0.570), showing that model initialization matters more than architecture.

## Context
EEG foundation models aim to reduce reliance on handcrafted features by learning complex representations from raw electrophysiological signals, a trend driven by advances in deep learning and the need for scalable clinical AI tools. This work contributes empirical evidence about how such models behave under realistic clinical deployment conditions, where data heterogeneity is common.

## Implications
Clinicians and developers must treat pretrained EEG embeddings as context‑specific rather than universally transferable, requiring dataset‑aware evaluation protocols. Ignoring these nuances could lead to overconfidence in model predictions when applied across populations or with limited negative controls.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24519v1)
