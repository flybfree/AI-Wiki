---
title: When Does Deep Representation Learning Help Single-Cell Clustering? A Sensitivity-Aware Diagnostic Benchmark for Biomedical AI Pipelines
published: 2026-07-28T04:48:47Z
authors: Nguyen Thanh Phong, Truong Viet Vu, Nguyen Ha Thu, Tran An Ky, Tran Hoang Thong, Le Pham Thuy Hien, Nguyen Thai Anh
url: http://arxiv.org/abs/2607.25288v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Does Deep Representation Learning Help Single-Cell Clustering? A Sensitivity-Aware Diagnostic Benchmark for Biomedical AI Pipelines

## Abstract
Single-cell ribonucleic acid sequencing (scRNA-seq) is a foundational technology for precision-medicine workflows that contribute to United Nations Sustainable Development Goal 3 on Good Health and Well-being, and unsupervised clustering is the analytical step that turns raw expression matrices into interpretable cell populations. Practitioners therefore face a recurring engineering decision: is an additional deep representation stage worth its compute and tuning cost, or do classical principal component analysis (PCA) pipelines already suffice? We address this question with a diagnostic benchmark of nine clustering pipelines on ten real datasets (90-5,685 cells, 19,046-41,480 genes, 4-11 cell types), augmented by a partial scVI V2 specialized comparison on seven datasets. The protocol integrates Optuna hyperparameter search, repeated-run robustness, Friedman/Wilcoxon-Holm/TOST testing, and Sobol total-order sensitivity analysis. The contrastive autoencoder achieved the highest mean Adjusted Rand Index (0.7872), but Holm-corrected tests did not establish dominance over the strongest baselines. Per-dataset analysis reveals three reproducible regimes: probabilistic variational autoencoder (VAE) variants help on the smallest datasets, deep autoencoders win on mid-scale data with multi-batch or many-type structure, and classical PCA pipelines remain competitive when linear projection already captures the dominant variation. Sobol indices identify learning rate ($S_T=0.70$) and latent dimensionality ($S_T=0.56$) as the dominant variance contributors, indicating where limited tuning budgets should be allocated. The contribution is therefore a dataset-aware and compute-conscious decision framework for biomedical AI pipelines supporting sustainable healthcare analytics, rather than a universal superiority claim.

## Metadata
- **Published**: 2026-07-28T04:48:47Z
- **Authors**: Nguyen Thanh Phong, Truong Viet Vu, Nguyen Ha Thu, Tran An Ky, Tran Hoang Thong, Le Pham Thuy Hien, Nguyen Thai Anh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25288v1)