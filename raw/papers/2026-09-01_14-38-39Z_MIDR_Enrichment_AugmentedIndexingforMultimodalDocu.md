---
title: MIDR: Enrichment-Augmented Indexing for Multimodal Document Retrieval
published: 2026-09-01T14:38:39Z
authors: Debanjan Mahata, Atharva Tendle, Daniel Preotiuc-Pietro, Yong Zhuang, Ozan Irsoy
url: http://arxiv.org/abs/2609.01316v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MIDR: Enrichment-Augmented Indexing for Multimodal Document Retrieval

## Abstract
Retrieval over visually rich documents has a representation problem: important content often lives in tables, charts, figures, and layout relations that plain OCR linearizes, corrupts, or omits. ColPali-family visual retrievers address this with patch-level multi-vector indexes and late-interaction scoring, keeping image-derived retrieval on the query-time serving path. We introduce MIDR (Multimodal Indexing for Document Retrieval), a training-free framework for enrichment-augmented indexing that shifts multimodal reasoning to index time. During ingestion, a multimodal LLM converts rendered pages into verified textual fields that are indexed with BM25F and optionally fused with dense retrieval, enabling text-centric serving over multimodally grounded evidence. On ViDoRe V3, MIDR Hybrid achieves 0.6219 average nDCG across five English domains, a 23.0% relative gain over BM25, remaining competitive with ColQwen2.5. On two French-document domains, enrichment bridges English queries and French page text, lifting BM25 from 0.1532 to 0.5448 nDCG and outperforming ColQwen2.5. Across all seven domains, MIDR leads ColQwen2.5 on four while using approximately 9x smaller index memory and approximately 2x lower query latency. These results establish index-time multimodal reasoning as a compelling accuracy-deployment alternative to serving-time visual late interaction.

## Metadata
- **Published**: 2026-09-01T14:38:39Z
- **Authors**: Debanjan Mahata, Atharva Tendle, Daniel Preotiuc-Pietro, Yong Zhuang, Ozan Irsoy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01316v1)