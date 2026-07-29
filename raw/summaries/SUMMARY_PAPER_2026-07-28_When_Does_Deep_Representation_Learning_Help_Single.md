---
title: When Does Deep Representation Learning Help Single-Cell Clustering? A Sensitivity-Aware Diagnostic Benchmark for Biomedical AI Pipelines
url: http://arxiv.org/abs/2607.25288v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_04-48-47Z_WhenDoesDeepRepresentationLearningHelpSingle_CellC.md
generated_at: 2026-07-28 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a benchmark that evaluates whether adding deep representation learning improves single-cell clustering beyond classical PCA, using nine pipelines on ten real datasets and partial scVI V2 comparisons. It finds the contrastive autoencoder highest in mean Adjusted Rand Index but statistical tests do not confirm superiority across all regimes.

## Key Takeaways
- The contrastive autoencoder achieved a mean Adjusted Rand Index of 0.7872, yet Holm-corrected tests did not establish dominance over the strongest baselines.
- Per-dataset analysis shows probabilistic VAEs help on small datasets, deep autoencoders win on mid-scale data with multi-batch or many-type structure, and classical PCA remains competitive when linear projection captures dominant variation.
- Sobol indices identify learning rate (S_T=0.70) and latent dimensionality (S_T=0.56) as the main variance contributors, guiding where limited tuning budgets should be allocated.

## Context
Single-cell RNA sequencing generates massive expression matrices that require unsupervised clustering to reveal cell populations. Deciding whether to add deep learning layers adds computational cost without guaranteed benefit, a challenge for sustainable biomedical AI pipelines.

## Implications
This framework offers a dataset-aware decision rule that prioritizes tuning effort where it matters most, supporting efficient and environmentally responsible AI in precision medicine research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25288v1)
