---
title: Self-Supervised Representations for Binary Program Clustering: From Empirical Study to Retrieval-Augmented Learning
published: 2026-08-03T15:01:00Z
authors: Martin Mocko, Daniela Chudá
url: http://arxiv.org/abs/2608.02348v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Supervised Representations for Binary Program Clustering: From Empirical Study to Retrieval-Augmented Learning

## Abstract
Malware clustering is a critical task in cybersecurity that helps discover threats and analyze evolving malware families. While self-supervised learning (SSL) and tabular representation learning (TRL) have achieved breakthroughs in other domains, their application to binary program clustering (the task of clustering all incoming samples regardless of label) remains largely unexplored. This study presents the first systematic investigation of SSL and TRL methods for binary program clustering, conducted in two phases on the public Ember and Bodmas datasets. In Phase 1, we establish a performance ceiling by adapting prominent vision-based SSL models (BYOL, SimSiam, Barlow Twins, VICReg) for tabular data with supervised pair generation, finding that BYOL and SimSiam achieve performance comparable to fully supervised models, while Barlow Twins and VICReg significantly underperform. In Phase 2, we evaluate purely unsupervised TRL methods against strong baselines (PCA, Autoencoder, UMAP), demonstrating that VIME establishes a new state of the art for binary program clustering. Informed by these findings, we propose VIME-R, a retrieval-augmented extension of VIME that replaces random marginal-distribution corruption with retrieval-based augmentation to generate more informative training pairs. VIME-R further improves upon VIME, achieving 2.7\%-5.8\% higher Homogeneity on both datasets. Our results highlight retrieval-augmented tabular representation learning as a promising direction for enhancing automated malware analysis. Code will be made available.

## Metadata
- **Published**: 2026-08-03T15:01:00Z
- **Authors**: Martin Mocko, Daniela Chudá
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02348v1)