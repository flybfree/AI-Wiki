---
title: SPRKD: Effective Knowledge Distillation for Deep Neural Networks via Saddle Region Approximation
published: 2026-07-25T19:53:58Z
authors: Aditya Dewan, Arjun Yogeswaran, Benjamin Fedoruk
url: http://arxiv.org/abs/2607.23346v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPRKD: Effective Knowledge Distillation for Deep Neural Networks via Saddle Region Approximation

## Abstract
Modern deep neural networks are potent catalysts for scientific and industrial impact, yet excessive parameter counts impede deployment in low-compute settings such as hospital equipment and energy infrastructure. Predominant knowledge distillation (KD) methods favor replication: smaller students mimic teacher output logits, yet empirically yield low task performance, hamper convergence, and act merely as regularization rather than substantive knowledge transfer. We propose Saddle Point Recruitment for Knowledge Distillation (SPRKD), reframing distillation from replication to employing teachers as optimization-curvature and domain proxies, characterizing saddle points as regions of strong further-descent potential via embedding and basin-fractal properties. Using Hessian eigenvalue spectral density (ESD), SPRKD identifies low-loss saddle regions for student re-exploration; weak-teacher ensembles are aggregated into an Approximated Saddle Region (ASR), re-parameterized into the student via Transfer Learning by Injection, and approached with exponentially decaying Euclidean transformations, Negative Hessian Eigensteps, and Gaussian perturbations. On malaria blood smear classification with a 6,430-parameter CNN distilled from a weak 25,546-parameter teacher, SPRKD reaches 94.8% validation accuracy, outperforming Response KD by 24.70 percentage points (McNemar p = 6.3e-87) and matching scratch-trained baselines of the same architecture to statistical equivalence (p = 1.0). Across MNIST, CIFAR-100, and TinyImageNet, SPRKD exceeds scratch-trained baselines by up to 8 percentage points on preliminary benchmarks. Hessian ESD and 2-D loss landscape analysis show convergence to wider minima with substantially smaller Hessian trace and spectral radius than Response KD and control students, indicating smoother descent and greater noise robustness.

## Metadata
- **Published**: 2026-07-25T19:53:58Z
- **Authors**: Aditya Dewan, Arjun Yogeswaran, Benjamin Fedoruk
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23346v1)