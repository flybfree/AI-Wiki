---
title: Scaling an Autoregressive Transformer for Single-Cell Generation
published: 2026-08-03T23:54:30Z
authors: Aleksandr Sharipov, Yusif Mukhtarov, Igor Molybog
url: http://arxiv.org/abs/2608.02961v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scaling an Autoregressive Transformer for Single-Cell Generation

## Abstract
We study a self-supervised generation task for single-cell gene expression vectors: given a set of vectors from a cell type, we aim to generate additional gene expression vectors of that cell type. For this task we characterize both the biological fidelity of the generated gene expression vectors and the scaling behavior of the pretraining loss. The model is a causal transformer paired with a learned quantized VAE tokenizer, trained with a cross-entropy loss. To evaluate the model, we condition it on held-out gene expression vectors of a cell type and generate vectors of gene expression, comparing the resulting distribution over gene expression vectors to the ground truth distribution of that cell type. We study the scaling properties of the proposed architecture by varying the number of trained parameters and the amount of training data. To our knowledge, we find the first jointly-fit two-exponent scaling law and compute-optimal frontier for a single-cell foundation model. Finally, we discuss how this pretrained model could be finetuned for perturbation response prediction.

## Metadata
- **Published**: 2026-08-03T23:54:30Z
- **Authors**: Aleksandr Sharipov, Yusif Mukhtarov, Igor Molybog
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02961v1)