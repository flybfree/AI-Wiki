---
title: Dementia Etiology Diagnosis via Collaborative Meta Knowledge Enhancement
published: 2026-07-24T04:26:47Z
authors: Siyuan Du, Mengxi Chen, Xinyang Jiang, Zilong Wang, Jiangchao Yao, Dongsheng Li, Ya Zhang, Lili Qiu, Yanfeng Wang
url: http://arxiv.org/abs/2607.22770v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dementia Etiology Diagnosis via Collaborative Meta Knowledge Enhancement

## Abstract
Although artificial intelligence (AI) has shown promising performance in several medical tasks, accurate dementia etiology diagnosis with AI remains challenging due to complex overlapping symptoms among diseases. Scaling up the dataset size by combining the cross-center samples may bring a gain in the pursuit of performance, while the inherent data heterogeneity across centers or populations induces the conflict. Conventional multi-task learning paradigms offer a promising framework; however, they fail to consider critical meta information (e.g., site-specific acquisition and modality availability) to combat the heterogeneity. To address this challenge, we propose a Collaborative Meta Knowledge Enhancement (COME) framework for dementia etiology diagnosis, which injects multi-center acquisition semantics, source identifiers, and modality indicators as heterogeneity-aware embeddings into a unified Transformer architecture for scale-up training, enabling explicit modeling of heterogeneity. Besides, a trust-region constrained optimization scheme is designed to regularize the model from spurious correlations during training through a reference model. Across seven independent cohorts, our method achieves state-of-the-art in-domain performance with a mean macro-averaged AUC of 85.62% and a 4.29-point gain over the strongest baseline, while maintaining superior out-of-domain generalization under both cross-center and cross-sequence evaluations. Extensive validation also confirms the alignment between model predictions and established biomarkers (amyloid, tau) and clinical severity, highlighting the potential of COME to enable robust and interpretable dementia diagnostics in real-world settings.

## Metadata
- **Published**: 2026-07-24T04:26:47Z
- **Authors**: Siyuan Du, Mengxi Chen, Xinyang Jiang, Zilong Wang, Jiangchao Yao, Dongsheng Li, Ya Zhang, Lili Qiu, Yanfeng Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22770v1)