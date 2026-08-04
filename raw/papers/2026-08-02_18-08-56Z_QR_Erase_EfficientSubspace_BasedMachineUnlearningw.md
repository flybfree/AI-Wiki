---
title: QR-Erase: Efficient Subspace-Based Machine Unlearning with Layer Localization
published: 2026-08-02T18:08:56Z
authors: Tyler Lizzo, Larry Heck
url: http://arxiv.org/abs/2608.01422v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# QR-Erase: Efficient Subspace-Based Machine Unlearning with Layer Localization

## Abstract
Machine unlearning seeks to remove targeted information from trained models without requiring costly retraining. Existing optimization-based methods often degrade unrelated capabilities, while subspace-based approaches rely on computationally expensive singular value decompositions (SVD). We introduce QR-Erase, a subspace-based framework that uses Pivoted QR decomposition to identify and remove task-specific representations directly from model parameters. We further propose Layer-Localized QR-Erase, which restricts updates to layers containing the highest concentration of task-specific information. We show that Pivoted QR provides accurate subspace recovery with bounded error, and that under a mild spectral gap condition, the recovered subspace approaches the optimal SVD solution. Across task-level, cross-lingual, and speech unlearning, QR-Erase achieves a stronger forgetting-retention tradeoff than optimization-based methods while remaining within 5% of SVD across all metrics. Exploiting low-rank and layer-localized structure further improves forgetting (for example, reducing speech forget-set accuracy from 53.1% to 15.7%). These results demonstrate that accurate subspace recovery, rather than optimal reconstruction, is sufficient for effective unlearning and provides an efficient and general alternative to SVD-based methods for modern foundation models.

## Metadata
- **Published**: 2026-08-02T18:08:56Z
- **Authors**: Tyler Lizzo, Larry Heck
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01422v1)