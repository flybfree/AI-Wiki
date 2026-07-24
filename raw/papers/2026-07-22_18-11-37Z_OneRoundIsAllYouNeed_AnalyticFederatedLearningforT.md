---
title: One Round Is All You Need: Analytic Federated Learning for Task-Heterogeneous Multi-Label Medical Image Classification
published: 2026-07-22T18:11:37Z
authors: Afsaneh Mahanipour, Hana Khamfroush
url: http://arxiv.org/abs/2607.20641v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One Round Is All You Need: Analytic Federated Learning for Task-Heterogeneous Multi-Label Medical Image Classification

## Abstract
Federated learning (FL) enables multiple clinical institutions to collaboratively train a shared disease classifier without centralizing patient data. In practice, however, each institution annotates only the pathologies within its area of expertise, so the federation operates under task heterogeneity: each client holds labels for a strict subset of the target disease categories while the remaining classes are entirely unobserved at that site. Existing gradient-based FL methods fail under this setting because they require hundreds of communication rounds to converge and because missing class labels introduce systematic false-negative bias that the model cannot correct without a principled mechanism. We propose an analytic federated learning framework for multi-label medical image classification under task heterogeneity. The proposed method replaces iterative gradient optimization with three closed-form operations: a balanced label projection that neutralizes class-imbalance bias by normalizing positive and negative contributions to equal total mass; a per-class absolute aggregation law that independently assembles the optimal ridge-regression classifier for each disease category from the sufficient statistics uploaded by its annotating clients; and an optional analytic pseudo-label refinement round that propagates missing-class knowledge from a confidence-filtered teacher classifier to non-annotating clients. The entire procedure requires at most two communication rounds, irrespective of the degree of task heterogeneity or the number of participating clients. Experiments on ChestXray14 under four progressively severe missing-class configurations demonstrate that the proposed method consistently outperforms the state-of-the-art federated multi-label method FedMLP by up to 18.44 BACC points and 13.24 AUC points, while reducing the communication.

## Metadata
- **Published**: 2026-07-22T18:11:37Z
- **Authors**: Afsaneh Mahanipour, Hana Khamfroush
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20641v1)