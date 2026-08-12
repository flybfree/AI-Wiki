---
title: P3CA: Encoder-Agnostic Interpretation of Vision Foundation Model Embeddings via Spatial Probing
published: 2026-08-10T18:42:38Z
authors: Amoon Jamzad, Dilakshan Srikanthan, Faranak Akbarifar, Nooshin Maghsoodi, Parvin Mousavi
url: http://arxiv.org/abs/2608.10131v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# P3CA: Encoder-Agnostic Interpretation of Vision Foundation Model Embeddings via Spatial Probing

## Abstract
Vision foundation models are increasingly used as reusable encoders in medical image computing, yet their high-dimensional spatial embeddings are difficult to inspect beyond downstream task performance or global dimensionality reduction. We propose position-prompted PCA (P3CA), an encoder-agnostic method for local probing of channel-rich spatial tensors. Given a user-selected spatial prompt, P3CA estimates the feature normalization and dominant covariance directions within that region, then applies the resulting projection to the full tensor to visualize where locally informative directions are expressed. This produces a region-conditioned representation lens without modifying the encoder, retraining, or requiring task-specific labels. We implement P3CA in EmbedVision, an interactive 3D Slicer-based workflow, and evaluate it across natural images, colorectal pathology foundation-model embeddings, and spatial transcriptomic tensors. Across these settings, prompted projections reveal local structure suppressed by global PCA, improve prompt-matched pathology discrimination from frozen three-dimensional projections, and support comparison between learned and measured spatial representations.

## Metadata
- **Published**: 2026-08-10T18:42:38Z
- **Authors**: Amoon Jamzad, Dilakshan Srikanthan, Faranak Akbarifar, Nooshin Maghsoodi, Parvin Mousavi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10131v1)