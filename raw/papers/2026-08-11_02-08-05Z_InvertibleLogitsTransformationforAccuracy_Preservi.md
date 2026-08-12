---
title: Invertible Logits Transformation for Accuracy-Preserving Post-Hoc Uncertainty Calibration
published: 2026-08-11T02:08:05Z
authors: Lening Zhao, Qipeng Zhan, Li Shen
url: http://arxiv.org/abs/2608.10372v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Invertible Logits Transformation for Accuracy-Preserving Post-Hoc Uncertainty Calibration

## Abstract
Post-hoc calibration aligns a classifier's predicted confidences with its empirical accuracy without retraining. An ideal calibrator should correct nonlinear miscalibration, scale gracefully to large label spaces, and preserve the original predictions; existing methods typically violate at least one of these properties---temperature scaling lacks expressivity, more flexible parametric alternatives introduce parameters that grow with the number of classes $C$, and other expressive methods do not preserve the rank ordering of class scores and may alter the predicted class. We propose \textbf{Invertible Logits Transformation (InvLT)}, which applies a learned scalar MLP $f:\mathbb{R}\to\mathbb{R}$ element-wise to the pre-softmax logits. Sharing $f$ across all logit dimensions makes the parameter count independent of $C$. Monotonicity of $f$---and hence preservation of the argmax prediction---is softly encouraged via a paired inverse network rather than enforced through the numerical integration required by prior monotone calibrators; this avoids their computational overhead while empirically preserving the original classification accuracy in every setting we evaluate. Across standard image classification benchmarks and a range of architectures, InvLT consistently outperforms a broad set of post-hoc baselines on standard calibration metrics.

## Metadata
- **Published**: 2026-08-11T02:08:05Z
- **Authors**: Lening Zhao, Qipeng Zhan, Li Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10372v1)