---
title: FedDOSE: Federated Learning Framework Decomposing Site Effects for Modeling Brain Dynamic Functional Connectivity
published: 2026-08-07T16:37:30Z
authors: Deepank Girish, Yi Hao Chan, Yubin Zheng, Sukrit Gupta, Jagath C. Rajapakse
url: http://arxiv.org/abs/2608.07393v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FedDOSE: Federated Learning Framework Decomposing Site Effects for Modeling Brain Dynamic Functional Connectivity

## Abstract
Functional Magnetic Resonance Imaging ( fMRI ) data are often pooled into collaborative multi-site consortia, as deep learning models for analyses require large datasets to generalize well. While Federated Learning (FL) offers a privacy-preserving paradigm for collaborative training, standard approaches continue to struggle with statistical heterogeneity. In particular, site differences pose a key challenge in multi-site data settings. Additionally, existing FL approaches for fMRI rely on static Functional Connectivity ( FC), omitting dynamic information in brain networks. To address this, we propose FedDOSE, a novel framework that explicitly decomposes site differences for analysis of dynamic FC (dFC). FedDOSE introduces a Modularity-Guided Tucker Decomposition block to encode high-dimensional dFC tensors and capture modular-level spatio-temporal patterns efficiently. Class-specific prototypes are generated across all sites and subsequently aligned at the global level by using a combination of Optimal Transport (OT) barycenter formulation and Procrustes analysis. Extensive experiments for diagnosing Autism Spectrum Disorder (ASD) and Attention-Deficit Hyperactivity Disorder (ADHD) on three multi-site resting-state fMRI datasets: ABIDE-I, ABIDE-II, and ADHD-200, demonstrate that FedDOSE outperforms state-of-the-art methods in ASD and ADHD detection. Our results highlight its effectiveness in learning robust representations from multi-site datasets for reliable analysis.

## Metadata
- **Published**: 2026-08-07T16:37:30Z
- **Authors**: Deepank Girish, Yi Hao Chan, Yubin Zheng, Sukrit Gupta, Jagath C. Rajapakse
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07393v1)