---
title: Understanding Context Sampling in TabPFN on Small Tabular Datasets
published: 2026-07-29T08:54:45Z
authors: Mohammed Abdullah
url: http://arxiv.org/abs/2607.26628v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding Context Sampling in TabPFN on Small Tabular Datasets

## Abstract
TabPFN performs classification through in-context learning: it conditions on a set of labeled training rows (the context, or prototypes) and predicts test labels without gradient updates. On small tabular datasets, practitioners must still choose the context size and which rows constitute the context. We study how these choices affect prediction stability, accuracy, and selection cost using repeated context sampling on 15 OpenML datasets. Specifically, we investigate (i) whether larger contexts reduce prediction variability across random draws, (ii) whether accuracy depends on preserving the training distribution or on feature-space coverage, and (iii) whether expensive selection methods such as K-Means and farthest-point sampling provide benefits over uniform random sampling.   We find that larger contexts are both more accurate and substantially more stable, with AUC coefficient of variation decreasing from roughly 6 to 18% at k=16 to 1 to 4% at larger context sizes on datasets with room for improvement. Although accuracy correlates with distribution representativeness in random contexts, controlled experiments show that matching feature means alone can reduce accuracy by up to 0.5 AUC because it reduces context diversity. Mixed-effects analysis identifies diversity and coverage, rather than feature-mean matching, as the stronger predictor of accuracy (diversity beta=+0.23, p=3x10^-12; feature-mean shift beta=-0.01, p=0.71). K-Means and farthest-point sampling achieve similar accuracy to random selection while requiring two to three orders of magnitude more selection cost. These results show that random sampling succeeds because it provides feature-space coverage in expectation, not because it reproduces the underlying data distribution.

## Metadata
- **Published**: 2026-07-29T08:54:45Z
- **Authors**: Mohammed Abdullah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26628v1)