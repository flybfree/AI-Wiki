---
title: Unstable Features, Reproducible Subspaces: Understanding Seed Dependence in Sparse Autoencoders
published: 2026-06-10T14:32:57Z
authors: Gleb Gerasimov, Timofei Rusalev, Nikita Balagansky, Daniil Laptev, Vadim Kurochkin, Daniil Gavrilov
url: http://arxiv.org/abs/2606.12138v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unstable Features, Reproducible Subspaces: Understanding Seed Dependence in Sparse Autoencoders

## Abstract
Sparse autoencoders (SAEs) are widely used to interpret neural network representations, but their utility depends on whether the learned features are reproducible across training runs. We study this question through \emph{feature stability}: for each SAE feature, we estimate the probability that a similar feature reappears in an independently trained SAE. This yields a scalable per-feature signal that separates stable from unstable features. In a large-scale study across seeds, models, layers, dictionary sizes, and SAE variants, we find a pronounced functional asymmetry: stable features carry most of the reconstruction- and prediction-relevant signal, while unstable features have weak marginal impact and are dominated by low-frequency surface-form triggers in both activation statistics and automatic explanations. Geometrically, unstable features are individually non-reproducible but concentrate in reproducible lower-rank subspaces, suggesting that seed dependence often reflects basis ambiguity within a shared region of activation space rather than pure noise. A controlled synthetic model makes this mechanism explicit, showing that low-rank ground-truth features can be recovered at the subspace level while remaining non-identifiable as individual SAE latents across seeds. Finally, by pooling unique cross-seed features, we construct more stable SAEs while preserving explained variance in this setting. Together, these results show that unstable features are not merely failed or noisy latents: they have weak individual functional impact, but reflect reproducible low-dimensional structure that standard SAEs resolve differently across seeds.

## Metadata
- **Published**: 2026-06-10T14:32:57Z
- **Authors**: Gleb Gerasimov, Timofei Rusalev, Nikita Balagansky, Daniil Laptev, Vadim Kurochkin, Daniil Gavrilov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.12138v1)