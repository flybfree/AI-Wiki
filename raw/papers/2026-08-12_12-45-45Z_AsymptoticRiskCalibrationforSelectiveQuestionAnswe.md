---
title: Asymptotic Risk Calibration for Selective Question Answering
published: 2026-08-12T12:45:45Z
authors: Shufan Lin, Sijin Dong
url: http://arxiv.org/abs/2608.12008v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Asymptotic Risk Calibration for Selective Question Answering

## Abstract
Large language models (LLMs) may generate fluent but incorrect answers, making uncertainty quantification important for reliable question answering. However, heuristic uncertainty scores cannot perfectly distinguish correct predictions from incorrect ones, and directly applying a fixed uncertainty threshold provides no statistical control over the error rate among accepted answers. To address this limitation, we propose A-CRC-QA, a post-hoc calibration framework for uncertainty-aware selective question answering. The proposed method reformulates selection-conditioned error control as a linear expectation constraint and applies a monotonized empirical-risk calibration procedure inspired by conformal risk control. Since the resulting instance-wise loss is generally non-monotone with respect to the acceptance threshold, our framework targets asymptotic rather than finite-sample risk control. A-CRC-QA is model-agnostic, requires no additional training, and can be combined with different uncertainty estimators. Experiments on CoQA and MedMCQA demonstrate its applicability to both open-ended and closed-ended question answering, achieving a favorable trade-off between accepted-answer reliability and answer retention compared with uncalibrated and confidence-bound-based baselines.

## Metadata
- **Published**: 2026-08-12T12:45:45Z
- **Authors**: Shufan Lin, Sijin Dong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12008v1)