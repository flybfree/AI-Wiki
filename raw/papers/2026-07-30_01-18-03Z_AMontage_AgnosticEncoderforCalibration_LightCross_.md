---
title: A Montage-Agnostic Encoder for Calibration-Light Cross-User Gesture Recognition from Surface Electromyography
published: 2026-07-30T01:18:03Z
authors: Jethro Odeyemi, W. J. Zhang
url: http://arxiv.org/abs/2607.27565v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Montage-Agnostic Encoder for Calibration-Light Cross-User Gesture Recognition from Surface Electromyography

## Abstract
Pattern-recognition control promises a myoelectric prosthesis that responds to many intended gestures rather than one or two, but the promise has stayed in the laboratory. A recogniser trained on one person rarely transfers to the next, and useful performance usually demands a fresh round of labelled calibration from the end user. A montage-agnostic encoder is introduced that reads each electrode with shared weights and locates it by its physical coordinate rather than its index, so one architecture ingests any channel count without montage-specific parameters. Trained across users, it exceeds a per-user Hudgins and linear-discriminant classifier by 0.234 macro-F1 on DB1 for every held-out subject and by 0.108 on DB2, and falls below it on the ten-subject DB5. Each of the encoder's three key components individually accounts for more than half of its 3-shot macro F1 in an otherwise budget-matched ablation study. A controlled subject-count sweep shows the margin is close to flat from nine training subjects to thirty-nine, so the training pool binds only as a stability floor below which cross-user training fails to converge; what tracks the direction of the comparison across the three databases is instead the strength of the per-user baseline, which signal fidelity sets. Comparing against an LDA baseline depends on budget spent training models and on how good that baseline is, and self-supervised pretraining had no benefits once a supervised model was adequately trained.

## Metadata
- **Published**: 2026-07-30T01:18:03Z
- **Authors**: Jethro Odeyemi, W. J. Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27565v1)