---
title: Are Single-Token Sparse Autoencoder Features Causally Necessary? Layer-Depth and SAE-Family Effects
published: 2026-07-22T17:33:16Z
authors: Seonglae Cho, Zekun Wu, Kleyton Da Costa, Rishi Kalra, Ilham Wicaksono, Adriano Koshiyama
url: http://arxiv.org/abs/2607.20596v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Are Single-Token Sparse Autoencoder Features Causally Necessary? Layer-Depth and SAE-Family Effects

## Abstract
Sparse autoencoder (SAE) features are used to interpret and steer large language models, yet whether a feature's causal role is stable across SAE families remains untested. Single-token features that activate on one vocabulary item provide the diagnostic case where ground truth permits direct comparison. We analyze 3.9M features across six models and three SAE families using zero-ablation at full layer depth. Single-token features cluster 4.7x tighter in decoder space and concentrate in early layers (Layer 0 in GPT2-Small; L0-L4 in Gemma). Ablating them yields Benjamini-Hochberg-significant logit reductions in 178 of 208 full-layer conditions, with depth controlling whether damage cascades downstream or shapes the output directly. Cross-family causal differences exceed within-family scale effects: on the same base model, GemmaScope and BatchTopK features remain causally anchored, while LlamaScope features are locally redundant. The target token's rank recovers to within 2x baseline 96-98% of the time after the same ablation, and a controlled activation-function comparison reverses sign within the same model, leaving training recipe as the residual candidate. Cross-family interpretability claims are therefore sensitive to training methodology, not just activation function or scale.

## Metadata
- **Published**: 2026-07-22T17:33:16Z
- **Authors**: Seonglae Cho, Zekun Wu, Kleyton Da Costa, Rishi Kalra, Ilham Wicaksono, Adriano Koshiyama
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20596v1)