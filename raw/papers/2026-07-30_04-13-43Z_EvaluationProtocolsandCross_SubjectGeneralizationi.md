---
title: Evaluation Protocols and Cross-Subject Generalization in EEG Emotion Recognition
published: 2026-07-30T04:13:43Z
authors: Hanting Suo, Yuwen Li
url: http://arxiv.org/abs/2607.27655v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluation Protocols and Cross-Subject Generalization in EEG Emotion Recognition

## Abstract
Reported accuracy in electroencephalography (EEG) emotion recognition depends on the complete evaluation procedure, not only the classifier. We separate the target quantity, development procedure, and reporting rule, then use one archived dynamical graph convolutional neural network (DGCNN) pathway on SEED and SEED-IV as an illustrative case. In a protocol-matched subject-dependent check, the SEED result was within 1.47 percentage points of the public reference value; the 3.40-point SEED-IV difference remained unresolved. Across 30 matched SEED subject-session trajectories, checkpoint selection based on repeated test-set evaluation increased mean window accuracy from 0.7855 at epoch 80 to 0.8892. Under five-fold subject-disjoint evaluation, validation-selected checkpoints achieved training-participant trial accuracies of 0.9990 on SEED and 0.9920 on SEED-IV. Accuracy for entirely held-out participants was 0.5348 (95% conditional subject-level bias-corrected and accelerated [BCa] interval [0.4667, 0.5985]) on SEED. The SEED-IV estimate was 0.3954 ([0.3343, 0.4648]) and is reported only as secondary sensitivity evidence because its protocol-matched compatibility check remained unresolved. The observed train-to-held-out-subject gaps are inconsistent with simple optimization underfitting, but they do not isolate subject identity from implementation, preprocessing, representation, or distributional factors. Supporting analyses further showed that participant rankings depended on representation and time scale, while a development-selected tail-risk ensemble did not establish a positive gain in a separate final evaluation. Subject-dependent, subject-disjoint, and cross-session results should therefore be reported as answers to different questions.

## Metadata
- **Published**: 2026-07-30T04:13:43Z
- **Authors**: Hanting Suo, Yuwen Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27655v1)