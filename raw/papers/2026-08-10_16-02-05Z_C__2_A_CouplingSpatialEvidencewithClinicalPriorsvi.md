---
title: C$^2$A: Coupling Spatial Evidence with Clinical Priors via Co-occurrence Aware Class Attention for Multi-Label Chest X-Ray Classification
published: 2026-08-10T16:02:05Z
authors: Akash Gogineni, Nagur Shareef Shaik, Aasrith Mandava, Adnan Masood, Dong Hye Ye
url: http://arxiv.org/abs/2608.09774v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# C$^2$A: Coupling Spatial Evidence with Clinical Priors via Co-occurrence Aware Class Attention for Multi-Label Chest X-Ray Classification

## Abstract
Thoracic pathologies rarely occur in isolation, yet standard multi-label classifiers rely on shared global descriptors, discarding \emph{where} findings lie and \emph{how} they co-occur. We propose \textbf{C$\mathbf{^2}$A} (Co-occurrence Aware Class Attention), a classification head that explicitly couples spatial evidence with clinical priors. First, C$^2$A casts pooling as an expectation over learned per-class spatial attention maps, yielding localized descriptors for each disease. Second, it couples these descriptors via a learnable graph warm-started from empirical label co-occurrence. A single residual message-passing step shares evidence among related findings, proving to be a bounded perturbation of the identity where co-occurrence enters each logit through an explicit bilinear interaction. On CheXpert, C$^2$A achieves a superior $0.895$ macro-mean AUROC, outperforming advanced context-gating baselines. Crucially, gains concentrate on highly co-occurrent classes with ambiguous spatial evidence (rescuing Atelectasis by $+1.5$ over GCG), demonstrating the prior's regularizing effect with a negligible overhead of one linear projection and a $C\!\times\!C$ edge matrix.

## Metadata
- **Published**: 2026-08-10T16:02:05Z
- **Authors**: Akash Gogineni, Nagur Shareef Shaik, Aasrith Mandava, Adnan Masood, Dong Hye Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09774v1)