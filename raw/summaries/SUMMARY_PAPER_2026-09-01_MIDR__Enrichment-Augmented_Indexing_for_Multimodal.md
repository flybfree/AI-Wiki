---
title: MIDR: Enrichment-Augmented Indexing for Multimodal Document Retrieval
url: http://arxiv.org/abs/2609.01316v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_14-38-39Z_MIDR_Enrichment_AugmentedIndexingforMultimodalDocu.md
generated_at: 2026-09-01 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MIDR, a training‑free framework that enriches document indexing by converting rendered visual content into verified textual fields during ingestion. On the ViDoRe V3 benchmark, MIDR Hybrid reaches an average nDCG of 0.6219 across five English domains, outperforming BM25 and ColQwen2.5 while using far less index memory and lower query latency.

## Key Takeaways
- MIDR shifts multimodal reasoning from serving time to index time, creating a hybrid index that fuses BM25F with dense retrieval for text‑centric serving over multimodally grounded evidence.  
- The framework achieves a 23 % relative gain in nDCG compared with plain BM25 on English domains and bridges language gaps between English queries and French page text, lifting nDCG from 0.1532 to 0.5448.  
- MIDR Hybrid outperforms ColQwen2.5 on four of seven evaluation domains while consuming roughly nine times less index memory and delivering about two times lower query latency.

## Context
The rise of multimodal document retrieval highlights the need for efficient, accurate indexing that can capture visual information without costly late‑interaction processing at query time. This work contributes to AI research by demonstrating that index‑time reasoning can match or exceed serving‑time approaches in performance metrics.

## Implications
For practitioners, MIDR offers a practical way to improve document search quality with minimal infrastructure changes and reduced latency, making it suitable for large‑scale deployment across multiple languages and domains. The findings suggest that embedding multimodal knowledge into the index itself is a viable alternative to computationally heavy serving‑time visual processing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01316v1)
