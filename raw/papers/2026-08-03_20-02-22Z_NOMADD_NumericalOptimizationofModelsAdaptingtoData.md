---
title: NOMADD: Numerical Optimization of Models Adapting to Data Drift
published: 2026-08-03T20:02:22Z
authors: Swapn Shah, Keith Burghardt
url: http://arxiv.org/abs/2608.02845v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NOMADD: Numerical Optimization of Models Adapting to Data Drift

## Abstract
Tabular model performance degrades when feature distributions change over time or the relationship between features and outcome variables change over time, known as data drift and concept drift, respectively. These issues are challenging to mitigate in real time because labeled data may not be immediately available, or re-training a model could be impractical. While tools exist to reduce drift, they are typically bespoke to neural network architectures and adapt how models are trained. In this paper, we offer an alternative post-hoc method to reduce concept drift, which is applicable to a variety of models, from trees to neural networks to tabular foundation models. This new tool is especially useful when constraints, such as high model accuracy, bounded inference time, or model size requires users to choose between different models for their specific use-cases. Our algorithm fits the base model separately on each labeled training period, measures how its parameters evolve against a single anchor model pooled over all of those periods, compresses those changes with a low-rank factorization, and extrapolates each latent factor forward with a damped, regularized forecast. On the 18-dataset Drift-Resilient TabPFN benchmark, evaluated under that benchmark's own protocol and metric, the extrapolation improves every base family it is applied to, and achieves performance competitive with the state-of-the-art Drift-Resilient TabPFN with seconds of training. In contrast, Drift-Resilient TabPFN requires pre-training on millions of synthetic datasets over approximately 1,300 GPU-hours, and is orders of magnitude slower in inference (depending on the model). In the discussion, we explore the promise and challenges of extending this tool to other modalities.

## Metadata
- **Published**: 2026-08-03T20:02:22Z
- **Authors**: Swapn Shah, Keith Burghardt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02845v1)