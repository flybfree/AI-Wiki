---
title: EnSI-RAG: Entity-Structure-Indexed Retrieval-Augmented Generation for Long-Document Question Answering
url: http://arxiv.org/abs/2608.21252v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_16-05-00Z_EnSI_RAG_Entity_Structure_IndexedRetrieval_Augment.md
generated_at: 2026-08-23 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces EnSI‑RAG, a retrieval‑augmented generation system that indexes long documents by entities rather than raw text chunks. By creating an entity‑structure index (e, t, k, v) the model can retrieve relevant passages even when they are split across multiple entities or require multi‑hop reasoning. The authors report an average accuracy of 78.24 on Loong and Oolong, outperforming baseline scores by six points.

## Key Takeaways
- EnSI‑RAG builds a query‑independent index where each record stores an entity, its type (property, relation, aspect), a semantic category, and the original passage link, enabling precise evidence retrieval.  
- The framework separates evidence localization from answer synthesis, allowing the LLM to synthesize retrieved passages into final answers while preserving traceable sources.  
- On Loong and Oolong benchmarks EnSI‑RAG achieves 78.24 accuracy, which is six points higher than published baseline scores.

## Context
Long‑document question answering suffers from chunking that breaks entity continuity, limiting retrieval relevance. Traditional RAG methods treat documents as independent text blocks, often missing cross‑entity evidence. This work addresses the limitation by centering indexing on entities and their relationships, a shift toward more structured knowledge representation in AI systems.

## Implications
For practitioners, EnSI‑RAG demonstrates that entity‑centric indexing can boost QA performance across diverse corpora without sacrificing traceability. The approach may inspire future systems to integrate structured knowledge graphs with generative models for better factual grounding and explainable outputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21252v1)
