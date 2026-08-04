---
title: UniHEAR: Unified Heterogeneous-Source Attentive Retrieval for Knowledge-Based Visual Question Answering
url: http://arxiv.org/abs/2608.01147v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_10-57-53Z_UniHEAR_UnifiedHeterogeneous_SourceAttentiveRetrie.md
generated_at: 2026-08-03 23:39
model: nvidia/nemotron-3-nano-4b
---

## Summary  
UniHEAR is a unified lightweight framework for heterogeneous‑source entity retrieval and reranking in knowledge‑based visual question answering, achieving state‑of‑the‑art performance on benchmark datasets. The model integrates multiple external sources to answer visually grounded questions while keeping the reranking architecture compact.

## Key Takeaways  
- The paper identifies the Single‑Source Retrieval Bottleneck where only one modality can retrieve entities, missing ground‑truth information present elsewhere.  
- Dual‑tower pointwise rerankers suffer from Retrieval‑Source‑Blind Reranking by ignoring retrieval origins and candidate priors, causing redundant modality reliance.  
- UniHEAR introduces a hybrid training strategy that merges contrastive learning with an auxiliary modality‑preserving loss to jointly optimize entity‑level and section‑level retrieval.

## Context  
Knowledge‑based visual question answering (KB‑VQA) requires linking visual scenes to external knowledge bases, a task that is hindered by limited source integration. Existing approaches often treat modalities in isolation or ignore their provenance, leading to suboptimal recall and redundancy.

## Implications  
By integrating heterogeneous sources and conditioning attention on retrieval descriptors, UniHEAR offers a scalable solution for deploying accurate VQA systems in real‑world applications such as smart assistants and content recommendation, where knowledge diversity is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01147v1)
