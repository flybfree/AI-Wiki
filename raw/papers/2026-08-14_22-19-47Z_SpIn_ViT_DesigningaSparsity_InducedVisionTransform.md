---
title: SpIn-ViT: Designing a Sparsity-Induced Vision Transformer That Is Mechanistically Interpretable
published: 2026-08-14T22:19:47Z
authors: Philip H. Lee, Parth Padalkar
url: http://arxiv.org/abs/2608.14922v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SpIn-ViT: Designing a Sparsity-Induced Vision Transformer That Is Mechanistically Interpretable

## Abstract
Mechanistic interpretability has recently expanded to Vision Transformers (ViTs), with Sparse Autoencoders (SAEs) increasingly used as post-hoc tools to decompose internal representations into sparse and more interpretable features. However, because post-hoc SAEs are trained on frozen representations after the ViT has already been optimized, their latent features are not directly aligned with the downstream classification objective. We introduce SpIn-ViT, a framework that jointly trains a pretrained ViT and a modified SAE end-to-end, directly aligning sparse patch-level representations with image classification. SpIn-ViT learns semantically coherent neuron activations that localize meaningful image regions while maintaining competitive predictive performance. We evaluate SpIn-ViT across nine image-classification benchmarks using classification accuracy, quantitative interpretability metrics, AI-based and Human evaluations. Compared with the previous state-of-the-art post-hoc SAE method, SpIn-ViT achieves 8.84% higher average classification accuracy, an AI-based interpretability score nearly four times as high, and a human-evaluation score more than twice as high. We further extract interpretable rule-sets using the SAE neurons to create neurosymbolic models which achieve 5.97% higher average classification accuracy while requiring a 58.8\% smaller rule-set than the neurosymbolic models created from the SOTA post-hoc SAE method.

## Metadata
- **Published**: 2026-08-14T22:19:47Z
- **Authors**: Philip H. Lee, Parth Padalkar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14922v1)