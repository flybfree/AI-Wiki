---
title: Beyond Objective Expressivity: Geometry Preservation in Multimodal Contrastive Learning
published: 2026-07-20T08:25:45Z
authors: Tillmann Rheude, Roland Eils, Benjamin Wild
url: http://arxiv.org/abs/2607.17673v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Objective Expressivity: Geometry Preservation in Multimodal Contrastive Learning

## Abstract
Contrastive learning is increasingly moving toward settings with three or more modalities instead of image-text pairs. Yet, extending models from pairwise to higher-order multimodal alignment can introduce optimization and representation challenges. We identify encoder Jacobian conditioning as a key factor in trimodal contrastive learning: poorly conditioned encoders exhibit collapsing or amplified singular-value spectra, leading to exploding Jacobian condition numbers and degraded multimodal alignment. We introduce geometry-preserving encoders (GPEs) by directly conditioning the Jacobian through regularization and demonstrating that simple modifications like LeakyReLU activations and residual paths recover these geometric benefits. Across a synthetic benchmark and four real-world datasets including missing modalities, improving Jacobian conditioning boosts retrieval and linear probe performance across multiple contrastive objectives, whereas expressive objectives yield little benefit in linear probes. More broadly, our results show that multimodal contrastive learning depends not only on objective expressivity, but also on the geometric and optimization properties of the underlying encoders.

## Metadata
- **Published**: 2026-07-20T08:25:45Z
- **Authors**: Tillmann Rheude, Roland Eils, Benjamin Wild
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17673v1)