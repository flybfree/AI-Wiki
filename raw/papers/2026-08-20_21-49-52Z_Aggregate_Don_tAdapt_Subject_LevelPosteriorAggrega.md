---
title: Aggregate, Don't Adapt: Subject-Level Posterior Aggregation and Transductive Calibration for Cross-Site Parkinsonian Gait Severity
published: 2026-08-20T21:49:52Z
authors: Junlong Shen
url: http://arxiv.org/abs/2608.20587v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Aggregate, Don't Adapt: Subject-Level Posterior Aggregation and Transductive Calibration for Cross-Site Parkinsonian Gait Severity

## Abstract
We describe the winning entry to the MoCha 2026 Benchmark and Challenge on Parkinsonian Gait, which predicts MDS-UPDRS gait severity from canonicalized SMPL motion recorded at clinical sites unseen during training. The system reaches 0.6945 macro-F1 on the hidden test and ranked first of 58 entries, ahead of the runner-up at 0.5807 and the organizers' baseline at 0.4289, on a frozen public motion encoder with a single $4\times512$ linear layer. Nearly all of the margin comes from three stages usually treated as bookkeeping: reproducing the reference benchmark's exact head recipe, averaging per-walk posteriors within the subject grouping the organizers ship, and a label-free transductive calibration of the feature mean and the decision operating point. Fine-tuning the encoder lost in four distinct forms, and ten alternative encoders were worse. Every ablation number is a paid read on the hidden test, because our own leave-two-cohort-out cross-validation proved anti-correlated with the deciding score over eleven configurations. We give the negative record in full, and identify our largest gain, subject-level aggregation, as the binding ceiling on this benchmark.

## Metadata
- **Published**: 2026-08-20T21:49:52Z
- **Authors**: Junlong Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20587v1)