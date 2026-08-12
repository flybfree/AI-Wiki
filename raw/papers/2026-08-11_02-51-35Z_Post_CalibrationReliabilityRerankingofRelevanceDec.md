---
title: Post-Calibration Reliability Reranking of Relevance Decisions via Label-wise Monotone Projection
published: 2026-08-11T02:51:35Z
authors: Inwoo Tae, Yongjae Lee
url: http://arxiv.org/abs/2608.10406v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Post-Calibration Reliability Reranking of Relevance Decisions via Label-wise Monotone Projection

## Abstract
Web search, product search, and question-answering retrieval systems often assign a relevance label and confidence score to each query-candidate pair. The relevance label describes how well a page, product, or passage matches the query, while the confidence often guides downstream use or fallback decisions. Post-hoc calibration is therefore needed because misaligned confidence can make systems over-trust wrong predictions or unnecessarily defer correct ones. However, calibration mainly aligns confidence with average correctness, and does not remove predicted-label-dependent reliability differences that remain within the same calibrated confidence level. We address this gap with Label-wise Monotone Reliability Projection (MRP), which learns label-wise monotone functions that map calibrated confidence to correctness reliability while preserving the original predicted labels and class probabilities. The resulting reliability score reranks fixed predictions according to residual risk. Across six information access relevance datasets and multiple post-hoc calibrators, MRP improves reliability reranking and average fallback utility while preserving full-coverage accuracy and ECE. Structural ablations show that the main gains come from label-wise residual reliability rather than from global confidence remapping. We further analyze when MRP reliability scores can be embedded back into top-label probability geometry, showing that this projection is useful as a compatibility analysis but is distinct from the main reliability-reranking objective. The implementation will be made publicly available.

## Metadata
- **Published**: 2026-08-11T02:51:35Z
- **Authors**: Inwoo Tae, Yongjae Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10406v1)