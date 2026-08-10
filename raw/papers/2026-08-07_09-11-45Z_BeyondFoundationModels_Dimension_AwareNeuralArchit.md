---
title: Beyond Foundation Models: Dimension-Aware Neural Architecture Search with Small-Data Representation Models for Cryocooler Lifetime Prediction
published: 2026-08-07T09:11:45Z
authors: Gregor Molan, Grafika Jati, Francesco Barchi, Andrea Acquaviva, Aljaž Osterman, Martin Molan
url: http://arxiv.org/abs/2608.06993v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Foundation Models: Dimension-Aware Neural Architecture Search with Small-Data Representation Models for Cryocooler Lifetime Prediction

## Abstract
Large-scale pretrained time-series models achieve strong results through large-scale pretraining and task-agnostic representation learning, but they rely on abundant, diverse data that industrial and scientific domains often lack. We therefore propose the FSD-RM (Family of Small-Data Representation Models) paradigm as a practical alternative for limited, domain-specific telemetry. Rather than relying on large-scale pretraining, we focus on capacity-controlled representation learning using established encoder architectures (CNN1D, LSTM, GRU, Transformer), selected for their suitability in small-data settings and interpretability.   These encoders are trained unsupervised on multivariate telemetry data and integrated into a two-stage pipeline for downstream lifetime prediction. To systematically examine architectural trade-offs under data constraints, we employ \textbf{dimension-aware neural architecture search (NAS)} to jointly optimize model capacity and input dimensionality.   Experiments on cryocooler telemetry show that the proposed approach achieves competitive predictive performance while reducing training cost and model complexity. The contribution lies in combining established representation learning techniques within a coherent, NAS-driven framework tailored to small-data regimes, with explicitly defined parameter settings and design choices. The results indicate that effective representation learning can be achieved without large-scale pretraining when appropriate inductive bias and capacity control are applied.

## Metadata
- **Published**: 2026-08-07T09:11:45Z
- **Authors**: Gregor Molan, Grafika Jati, Francesco Barchi, Andrea Acquaviva, Aljaž Osterman, Martin Molan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06993v1)