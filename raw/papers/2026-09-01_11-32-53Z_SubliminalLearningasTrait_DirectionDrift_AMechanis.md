---
title: Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation
published: 2026-09-01T11:32:53Z
authors: Zhixuan Liu, Zhichen Dong, Yuyu Fan, Xiangtian Li, Chao Yang
url: http://arxiv.org/abs/2609.01091v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation

## Abstract
Beyond intended capabilities, model distillation can transfer hidden traits from a teacher. A teacher biased by a system prompt can generate semantically clean training data, such as numeric sequences, that still causes a downstream student to inherit the hidden preference, a phenomenon known as subliminal learning. Prior work has identified several parts of this process. How the signal builds up during training and produces behavioral transfer remains unclear, making targeted mitigation difficult. We propose and validate trait-direction drift as a mechanism for subliminal learning: biased generation creates measurable preference gaps in teacher data, and student-recognizable gaps induce trait-aligned updates during supervised fine-tuning that accumulate into behavioral transfer. Guided by this mechanism, we propose probe-space corridor regularization, a targeted defense that constrains drift along a calibrated trait direction during distillation. The method substantially reduces hidden-trait transfer, preserving task performance: for example, it lowers malicious-response transfer from 29.55% to 6.45% with low main-task accuracy cost, and consistently suppresses animal-preference transfer across the main Qwen setting. The preference-gap, training-trajectory, and intervention evidence links subliminal learning to trait-direction drift and motivates corridor regularization as a targeted control during distillation.

## Metadata
- **Published**: 2026-09-01T11:32:53Z
- **Authors**: Zhixuan Liu, Zhichen Dong, Yuyu Fan, Xiangtian Li, Chao Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01091v1)