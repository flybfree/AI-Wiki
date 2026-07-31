---
title: Simplifying Neural Networks During Training
published: 2026-07-30T08:32:40Z
authors: Lorenzo Sciandra, Samuele Fonio, Roberto Esposito
url: http://arxiv.org/abs/2607.27854v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Simplifying Neural Networks During Training

## Abstract
Understanding and exploiting the training dynamics of overparameterized deep neural networks remains a central challenge in modern machine learning. Recent evidence on Neural Collapse (NC) shows that class representations and classifiers exhibit highly structured geometry, while the Tunnel Effect suggests that only a subset of layers is essential for feature extraction. We combine these two perspectives and propose an NC-inspired training framework for simplifying deep networks during training. Our method monitors representation dynamics through the Inverse Fisher Criterion, a stable and efficient proxy for the variability collapse behavior, to identify both the split point between feature extraction and classification and the training stage at which simplification becomes viable. We then replace the trailing layers with a lightweight classification head and continue training the reduced model. Experiments on image-classification benchmarks across MLP, VGG, and ResNet architectures show that the proposed method achieves substantial parameter reductions while maintaining accuracy comparable to that of the full model. Code to reproduce the experiments can be found at: https://github.com/LorenzoSciandra/NNS.

## Metadata
- **Published**: 2026-07-30T08:32:40Z
- **Authors**: Lorenzo Sciandra, Samuele Fonio, Roberto Esposito
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27854v1)