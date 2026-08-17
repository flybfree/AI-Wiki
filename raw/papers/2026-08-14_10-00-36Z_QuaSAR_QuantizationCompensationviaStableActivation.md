---
title: QuaSAR: Quantization Compensation via Stable Activation-Aware Rank Truncation
published: 2026-08-14T10:00:36Z
authors: Lin-Fa Lee, Yi-Yu Chang, Kuo-Hei Yeh
url: http://arxiv.org/abs/2608.14149v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# QuaSAR: Quantization Compensation via Stable Activation-Aware Rank Truncation

## Abstract
Recent training-free post-training quantization methods restore model accuracy through closed-form residual compensation. To constrain additional model storage overhead, several existing methods gate layer selection by goodness-of-fit, retaining only those layers whose compensation yields a positive residual fit score and discarding the rest. In this paper, we show that, under the low-bit W4A4 setting, this gating mechanism fails to distinguish poorly predictable quantization error from numerical solver failure. Rank-deficient input activations yield severely ill-conditioned or numerically singular Gram matrices, causing the closed-form solver to become unstable and produce spuriously negative fit scores. Consequently, existing goodness-of-fit gates misclassify affected layers as uncompensable and discard them. Many of these discarded layers can nevertheless provide substantial error recovery when their compensation is computed using a numerically stable solver. To address this problem, we propose a parameter-free truncated pseudoinverse solver which removes collapsed directions prior to inversion. On ViT-B with the W4A4 setting, our training-free method achieves 81.42\% top-1 accuracy, outperforming prior post-training methods and fine-tuning-based baselines. Combined with joint low-rank and quantization compression, the proposed method reaches a deployable operating point of 80.26\% accuracy at 54.7 MB, providing a well-balanced trade-off between model size and accuracy.

## Metadata
- **Published**: 2026-08-14T10:00:36Z
- **Authors**: Lin-Fa Lee, Yi-Yu Chang, Kuo-Hei Yeh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14149v1)