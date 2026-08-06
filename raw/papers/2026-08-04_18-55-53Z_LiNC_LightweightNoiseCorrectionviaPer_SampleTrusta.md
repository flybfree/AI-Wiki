---
title: LiNC: Lightweight Noise Correction via Per-Sample Trust and Gaussian Mixture Modeling
published: 2026-08-04T18:55:53Z
authors: Abhishek Moturu, Babak Taati, Anna Goldenberg
url: http://arxiv.org/abs/2608.04147v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LiNC: Lightweight Noise Correction via Per-Sample Trust and Gaussian Mixture Modeling

## Abstract
Label noise is common in medical imaging datasets due to factors such as inter-rater variability, annotation errors, and ambiguous cases. This can severely undermine the reliability and clinical effectiveness of machine learning models trained using those datasets. To address this challenge, we introduce Lightweight Noise Correction (LiNC), which adds a single trainable trust parameter per training sample and learns when to use the observed label and when to defer to the model during a standard training loop. The key idea is to train using a convex combination of the observed label and the model's own predictive distribution, controlled by a per-sample trust parameter. We show that the gradient of this objective drives trust values in opposite directions for clean versus noisy samples in the early training phase, yielding separable trust distributions. We use a 3-component Gaussian Mixture Model over the trust values to separate them into clean, ambiguous, and noisy cases and then execute a short soft-correction phase on the noisy cases and a final hard correction phase. Experiments on ten 2D datasets from MedMNISTv2 under label noise of up to 50% show consistent gains in accuracy and strong mislabel detection. LiNC adds negligible asymptotic overhead: the training-time complexity remains dominated by the base network, with additional memory growing linearly with the size of the training set.

## Metadata
- **Published**: 2026-08-04T18:55:53Z
- **Authors**: Abhishek Moturu, Babak Taati, Anna Goldenberg
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04147v1)