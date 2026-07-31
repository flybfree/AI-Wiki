---
title: Rethinking EEG-Based Disease Diagnosis: Decoupling Instance Representation Learning from Subject-Level Supervision
url: http://arxiv.org/abs/2607.27274v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_12-34-47Z_RethinkingEEG_BasedDiseaseDiagnosis_DecouplingInst.md
generated_at: 2026-07-30 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces BridgeMIL, a two‑stage framework that separates instance representation learning from subject‑level supervision in EEG disease diagnosis. By pretraining an encoder on temporally aligned windows without inherited labels and using variance and covariance regularization, the model learns robust representations. The second stage applies attention‑based multi‑instance learning only to subject predictions, achieving higher accuracy than baselines across multiple datasets.

## Key Takeaways
- BridgeMIL decouples instance representation from subject labels, pretraining the encoder on aligned windows while using variance and covariance regularization to avoid redundancy.
- The framework transfers a stable encoder to an attention aggregator that is supervised solely at the subject level, limiting representation drift through feature retention.
- Experiments show a 4.28‑percentage‑point gain in mean accuracy (76.57%) compared with the strongest baseline, highlighting sensitivity of performance to subject scarcity rather than instance scarcity.

## Context
EEG diagnosis traditionally relies on per‑subject predictions but suffers from label inheritance that can degrade representation quality. Multi‑instance learning offers a promising alternative yet is limited by few subjects relative to many instances. BridgeMIL addresses this imbalance by designing a two‑stage pipeline that learns strong, subject‑agnostic features before applying MIL.

## Implications
For researchers, BridgeMIL provides a practical method to leverage abundant EEG instances without contaminating them with disease labels. Clinically and industrially, the approach can improve diagnostic reliability in real‑world settings where subject numbers are limited but recordings are plentiful.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27274v1)
