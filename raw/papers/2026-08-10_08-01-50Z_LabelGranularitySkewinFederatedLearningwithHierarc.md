---
title: Label Granularity Skew in Federated Learning with Hierarchical Image Classification
published: 2026-08-10T08:01:50Z
authors: Jaeheon Kim, Hokeun Kim, Bong Jun Choi
url: http://arxiv.org/abs/2608.09236v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Label Granularity Skew in Federated Learning with Hierarchical Image Classification

## Abstract
Federated learning enables privacy-preserving collaboration across distributed devices without centralizing local data. However, clients may differ not only in data distributions but also in domain knowledge and annotation capabilities. In this paper, we introduce label granularity skew, a new form of statistical heterogeneity in federated hierarchical classification, in which clients provide taxonomy-consistent labels at different levels of detail within a shared class hierarchy. To model this heterogeneity, we generate client-specific local label hierarchies using a probabilistic relational neighbor classifier and construct a WordNet-guided hierarchy via silhouette score-based coarsening. Our analysis shows that strongly coupled hierarchical models are sensitive to incomplete supervision, while the conditional softmax classifier is more robust. Based on this insight, we propose Branch-wise Decoupled Fine-Tuning (BDFT) and its federated version, FedBDFT, which fine-tune branch-wise classifiers and aggregate them through federated optimization. Experiments on CIFAR-100, TinyImageNet, and ImageNet show that FedBDFT substantially improves robustness under severe label granularity skew, with average gains of 27.9% and 56.4% at skewness levels of 0.6 and 0.9, respectively. Zero-shot results further indicate that FedBDFT better preserves hierarchical representations for unseen fine-grained classes. These findings demonstrate its effectiveness for federated hierarchical classification with heterogeneous label granularities.

## Metadata
- **Published**: 2026-08-10T08:01:50Z
- **Authors**: Jaeheon Kim, Hokeun Kim, Bong Jun Choi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09236v1)