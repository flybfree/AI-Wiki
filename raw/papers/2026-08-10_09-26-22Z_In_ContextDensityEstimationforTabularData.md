---
title: In-Context Density Estimation for Tabular Data
published: 2026-08-10T09:26:22Z
authors: Patryk Marszałek, Jacek Tabor, Marek Śmieja
url: http://arxiv.org/abs/2608.09348v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# In-Context Density Estimation for Tabular Data

## Abstract
Density estimation underlies many unsupervised tasks on tabular data such as anomaly detection, out-of-distribution detection, and data augmentation. Although all these problems reduce to questions about where probability mass lies, they are typically solved individually by fitting a separate model to each dataset, with its own hyperparameters and tuning budget. We introduce ICED, an in-context, energy-based density estimator that removes this per-dataset cost. ICED is a transformer-based model pretrained once on a synthetic prior built specifically for density estimation under an objective that fits log-density where it is informative and preserves its ordering elsewhere. In the inference, it reads a dataset as context and returns an unnormalized log-density for any query point in a single forward pass, with no fitting, sampling, or hyperparameter selection. A single frozen ICED model then drives four tasks usually handled by four specialized pipelines: density estimation, out-of-distribution detection, unsupervised anomaly detection, and generative augmentation. Across all four, it is competitive with the strongest task-specific method, while being the only approach that needs no retraining, no tuning, and no labels to move between them. The code is available at https://github.com/gmum/iced.

## Metadata
- **Published**: 2026-08-10T09:26:22Z
- **Authors**: Patryk Marszałek, Jacek Tabor, Marek Śmieja
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09348v1)