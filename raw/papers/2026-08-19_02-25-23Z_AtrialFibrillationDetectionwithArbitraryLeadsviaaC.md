---
title: Atrial Fibrillation Detection with Arbitrary Leads via a Codebook-Based Reconstruction-Classification Framework
published: 2026-08-19T02:25:23Z
authors: Hongtao Li, Jia Wei, Guoyao Li, Yuchen Lei, Guangnian Ma, Jia Xiao, Yuanjun Lai, Shuzhen Lv, Xueqiang Ouyang
url: http://arxiv.org/abs/2608.18451v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Atrial Fibrillation Detection with Arbitrary Leads via a Codebook-Based Reconstruction-Classification Framework

## Abstract
\textbf{Background and Objective}: Reliable atrial fibrillation (AF) detection from electrocardiogram (ECG) signals remains challenging in real-world clinical settings due to variable lead configurations, cross-dataset domain shifts, and pervasive physiological and technical artifacts. So we develop a robust and generalizable deep learning model for accurate AF detection.\\ \textbf{Methods}: We propose the Dual-Codebook Graph Collaborative Network (DCGCNet), a novel end-to-end vector-quantized variational autoencoder that jointly performs AF classification and ECG reconstruction. DCGCNet introduces two key components: (1) a Local-Global Contrastive Module for learning noise-invariant representations, and (2) an Adaptive Codebook Vector Quantizer that dynamically refines codebook prototypes to better align with input data distributions, thereby preventing codebook collapse and enhancing generalization.\\ \textbf{Results}: DCGCNet achieves state-of-the-art performance in standard intra-dataset 12-lead evaluation and demonstrates exceptional cross-dataset generalization across seven diverse settings, consistently attaining AUC > 0.98 in all cases. Furthermore, it maintains high diagnostic accuracy under realistic noisy conditions, including baseline wander, powerline interference, and EMG artifacts.\\ \textbf{Conclusions}: DCGCNet establishes a new benchmark for robust, generalizable, and noise-resilient AF detection, showing strong potential for deployment in real-world clinical environments.

## Metadata
- **Published**: 2026-08-19T02:25:23Z
- **Authors**: Hongtao Li, Jia Wei, Guoyao Li, Yuchen Lei, Guangnian Ma, Jia Xiao, Yuanjun Lai, Shuzhen Lv, Xueqiang Ouyang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18451v1)