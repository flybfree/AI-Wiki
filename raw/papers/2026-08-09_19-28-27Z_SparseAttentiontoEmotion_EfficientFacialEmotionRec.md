---
title: Sparse Attention to Emotion: Efficient Facial Emotion Recognition via Token Reduction
published: 2026-08-09T19:28:27Z
authors: Aya Manel Zitouni, Aicha Zenakhri, Karim Haroun, Larbi Boubchir
url: http://arxiv.org/abs/2608.08873v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sparse Attention to Emotion: Efficient Facial Emotion Recognition via Token Reduction

## Abstract
Facial Emotion Recognition (FER) is an important task that has significant implications across various fields such as biometrics, health, and human-computer interaction. Current Vision Transformer-based approaches display quadratic complexity $\mathcal{O}(N^2)$, with N being the input sequence length, making them cumbersome to deploy at the edge. In this paper, we hypothesize that the FER task does not necessarily require all facial information to correctly interpret emotional states, as specific regions such as the eyes, the mouth, and parts of the cheeks carry discriminative information that can be sufficient to recognize emotions. Based on this, we propose Sparse Attention to Emotion (SAE), a model that discards image tokens that have no added value to the emotional context, while preserving good accuracy and achieving a significant gain in computational cost. Surprisingly, even after suppressing 90\% of the image tokens, our model achieves competitive accuracy to state of the art methods at much lower cost, providing a lightweight Facial Emotion Recognition approach. Experimental results demonstrate that SAE achieves new state of the art results on the RAF-DB dataset while reducing the computational complexity by up to 90\%.

## Metadata
- **Published**: 2026-08-09T19:28:27Z
- **Authors**: Aya Manel Zitouni, Aicha Zenakhri, Karim Haroun, Larbi Boubchir
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08873v1)