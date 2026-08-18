---
title: Domain-Specific Text Embedding Models for Entity Resolution
published: 2026-08-17T06:26:05Z
authors: Khajesh Sapram, Srivardhani Raju, Kishore Konda
url: http://arxiv.org/abs/2608.16161v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Domain-Specific Text Embedding Models for Entity Resolution

## Abstract
General-purpose text embedding models are designed to capture semantic similarity but are not optimised for distinguishing entity records that represent the same real-world business or person. This limitation affects applications such as entity resolution and duplicate record retrieval, where small textual differences may either preserve or change identity. This paper investigates whether domain-specific triplet fine-tuning can adapt pretrained embedding models for identity-sensitive retrieval. A synthetic dataset of business and person records was created with identity-preserving variations and challenging non-matching examples. Two widely used embedding models were evaluated before and after fine-tuning using a margin-based similarity evaluation. The results show substantial improvements in separating true matches from highly similar non-matches, demonstrating that domain-specific triplet training can effectively reshape general-purpose embedding spaces for entity retrieval. These findings suggest that targeted fine-tuning provides a practical approach for improving embedding models in data quality management and information retrieval applications.

## Metadata
- **Published**: 2026-08-17T06:26:05Z
- **Authors**: Khajesh Sapram, Srivardhani Raju, Kishore Konda
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16161v1)