---
title: Foundation Models Meet Agriculture: Challenges Beyond Pretraining
published: 2026-08-31T07:47:57Z
authors: Vishal Nedungadi, Xingguo Xiong, Marc Rußwurm, Ioannis N. Athanasiadis
url: http://arxiv.org/abs/2608.30392v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Foundation Models Meet Agriculture: Challenges Beyond Pretraining

## Abstract
Global food security and sustainable climate action increasingly rely on robust, scalable agricultural monitoring. Earth observation foundation models have emerged as powerful, label-efficient tools across general remote sensing domains, yet early attempts to deploy them for agricultural applications have yielded surprisingly poor results. We hypothesize that this performance gap stems from the extreme heterogeneity of agricultural landscapes and the inherent inability of current earth observation foundation models to adapt to task-specific nuances. In this work, we systematically evaluate two critical bottlenecks hindering the deployment of foundation models in agricultural tasks, benchmarking two earth observation foundation models, a foundation model designed for tabular data, and conventional supervised baselines across seven real-world agricultural datasets spanning yield prediction, phenology estimation, and crop classification. First, we identify a pretraining-deployment modality gap: agricultural downstream tasks frequently require diverse, non-imagery data modalities that earth observation foundation models are architecturally unequipped to ingest, while a foundation model built for tabular data handles this heterogeneity more naturally. Second, we formalize the agricultural task space across five structural axes to demonstrate why current models fail to generalize reliably, resulting in highly unstable model rankings across evaluation settings. By characterizing these structural and modal gaps, our insights highlight the friction between general-purpose architectures and specialized agricultural downstream data, providing a strategic roadmap for developing the next generation of domain-aware foundation models.

## Metadata
- **Published**: 2026-08-31T07:47:57Z
- **Authors**: Vishal Nedungadi, Xingguo Xiong, Marc Rußwurm, Ioannis N. Athanasiadis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30392v1)