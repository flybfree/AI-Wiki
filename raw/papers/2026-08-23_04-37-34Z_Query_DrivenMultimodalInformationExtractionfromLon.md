---
title: Query-Driven Multimodal Information Extraction from Long Documents
published: 2026-08-23T04:37:34Z
authors: Yikai Gao, Ding Xia, Xi Yang
url: http://arxiv.org/abs/2608.22214v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Query-Driven Multimodal Information Extraction from Long Documents

## Abstract
In domain-specific multimodal long documents, images and text jointly convey complex knowledge that cannot be fully captured by plain text alone. However, existing paradigms like DocVQA primarily focus on generating textual answers or localizing evidence regions, rather than outputting query-specific textual attribute values and corresponding images. To address this gap, we propose query-driven image-text joint extraction from long documents, requiring models to output query-requested textual attribute values and corresponding image bounding boxes. Based on challenges related to both user intent and document content, we designed a two-level taxonomy that operates at the query and instance levels. Further, we construct ITJoint, the first high-quality, manually annotated benchmark for this new task, comprising 2,455 pages of domain-specific documents with numerous non-decorative images, 316 queries, and 910 answer instances. Finally, we evaluate representative standalone Vision-Language Models from different providers and further design Q2IT, a multi-agent collaborative framework consisting of three progressively collaborating agents for evidence collection, page selection, and target-image localization. Using a joint evaluation approach that assesses both text extraction and image localization, our experiments show that standalone VLMs struggle with this task, while Q2IT significantly improves performance on ITJoint, although a substantial gap remains toward perfect results.

## Metadata
- **Published**: 2026-08-23T04:37:34Z
- **Authors**: Yikai Gao, Ding Xia, Xi Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22214v1)