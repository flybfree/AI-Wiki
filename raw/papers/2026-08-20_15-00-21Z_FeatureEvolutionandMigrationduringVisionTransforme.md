---
title: Feature Evolution and Migration during Vision Transformer Training
published: 2026-08-20T15:00:21Z
authors: Joonas Järve, Halil Ibrahim Aysel, Tarun Khajuria, Meelis Kull
url: http://arxiv.org/abs/2608.20134v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Feature Evolution and Migration during Vision Transformer Training

## Abstract
We present a novel view on feature evolution in Vision Transformers (ViTs) by visualizing the training process over two dimensions -- network depth (layer) and training time (epochs). We employ Sparse Autoencoders (SAEs) to extract candidate sparse features from CLS-token representations and compare their activation profiles across epoch--layer pairs. This allows us to study feature-level dynamics that are not directly visible from representation-level similarity measures. Furthermore, we demonstrate how this framework of feature evolution allows us to describe feature migration, the change in the layer where a feature is most detectable during training. Our experiments show that migration is concentrated early in training, occurs more often toward earlier layers than toward deeper layers, and declines as feature organization stabilizes. We further find that deeper layers stabilize earlier and more strongly than shallow layers. The results show that our approach can be employed as a tool for understanding how ViTs learn and evolve.

## Metadata
- **Published**: 2026-08-20T15:00:21Z
- **Authors**: Joonas Järve, Halil Ibrahim Aysel, Tarun Khajuria, Meelis Kull
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20134v1)