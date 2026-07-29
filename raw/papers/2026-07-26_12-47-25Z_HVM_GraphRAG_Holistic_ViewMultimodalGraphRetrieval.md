---
title: HVM-GraphRAG: Holistic-View Multimodal Graph Retrieval-Augmented Generation on Complex Document
published: 2026-07-26T12:47:25Z
authors: Xin He, Yili Wang, Wenqi Fan, Qing Li, Qinggang Zhang, Yi Chang, Xin Wang
url: http://arxiv.org/abs/2607.24861v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HVM-GraphRAG: Holistic-View Multimodal Graph Retrieval-Augmented Generation on Complex Document

## Abstract
Question answering (QA) over complex documents requires models to retrieve and integrate evidence distributed across distant document regions and modalities. Multimodal GraphRAG provides a promising direction by organizing document evidence with graph structures. However, existing methods often suffer from unreliable cross-modal evidence indexing and expensive graph traversal. To address these issues, we propose HVM-GraphRAG, a holistic-view multimodal GraphRAG framework on complex document. HVM-GraphRAG uses a holistic view to guide graph construction, thereby reducing noisy and conflicting graph updates and building reliable indices between concept-level graph nodes and supporting multimodal chunks. During retrieval, HVM-GraphRAG searches over a compact concept-level graph and directly accesses supporting evidence through the constructed index, avoiding costly traversal over dense entity-level graphs. After obtaining the retrieved evidence, HVM-GraphRAG further reorganizes chunks into modality-specific groups, enabling the answering model to better integrate heterogeneous evidence. Experiments on three datasets show that HVM-GraphRAG achieves the best answer performance in most evaluated settings while substantially improving online retrieval efficiency over representative graph-based baselines.

## Metadata
- **Published**: 2026-07-26T12:47:25Z
- **Authors**: Xin He, Yili Wang, Wenqi Fan, Qing Li, Qinggang Zhang, Yi Chang, Xin Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24861v1)