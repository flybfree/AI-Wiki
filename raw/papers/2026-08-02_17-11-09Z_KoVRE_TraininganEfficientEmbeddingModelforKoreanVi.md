---
title: KoVRE: Training an Efficient Embedding Model for Korean Visual Document Retrieval
published: 2026-08-02T17:11:09Z
authors: Yongbin Choi, Gyuho Shim, Youngjoon Jang
url: http://arxiv.org/abs/2608.01389v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KoVRE: Training an Efficient Embedding Model for Korean Visual Document Retrieval

## Abstract
Visual Document Retrieval (VDR) directly matches text queries against document images, preserving visual and structural information that may be lost during text extraction. However, existing VDR models and training resources remain predominantly English-centric, while many high-performing systems rely on massive backbones or storage-intensive multi-vector representations. To address these limitations, we introduce KoVRE: Korean Visual Document Retrieval Embedding, a single-vector retriever for Korean visual documents, alongside a comprehensive training recipe. We train the model on 708,729 Korean and English query-page pairs using positive-aware hard-negative mining and conduct controlled analyses of training-data composition, hard-negative treatment, and reranker-based knowledge distillation. Across Korean visual document retrieval benchmarks, our 2B model substantially improves over the base backbone model, outperforming both its 8B single-vector counterpart and a strong multi-vector baseline. These results demonstrate that targeted bilingual supervision and our carefully designed training strategies can produce a highly effective Korean VDR model across diverse document domains, without requiring a scaled-up backbone or multi-vector representations.

## Metadata
- **Published**: 2026-08-02T17:11:09Z
- **Authors**: Yongbin Choi, Gyuho Shim, Youngjoon Jang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01389v1)