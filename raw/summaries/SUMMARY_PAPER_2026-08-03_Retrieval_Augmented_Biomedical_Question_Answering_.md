---
title: Retrieval Augmented Biomedical Question Answering with Weak Question Recovery and Neural Reranking for BioASQ Task 14b
url: http://arxiv.org/abs/2608.01468v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_20-02-44Z_RetrievalAugmentedBiomedicalQuestionAnsweringwithW.md
generated_at: 2026-08-03 23:16
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper describes the DS@GT ARC BioASQ team's pipeline for biomedical question answering, which integrates query expansion, neural reranking, and retrieval refinement. The system leverages PubMed data, a MiniLM‑based semantic reranker, Reciprocal Rank Fusion, and OpenBioLLM to generate answers while handling queries with weak retrieval through conditional recovery strategies.

## Key Takeaways  
- The proposed conditional weak‑question recovery expands queries semantically, augments them with relationship‑aware terms, and merges results selectively to boost relevance for difficult questions.  
- A post‑retrieval pruning stage eliminates redundant or low‑relevance snippets while maintaining evidence coverage for downstream answer generation.  
- These recovery and cleanup steps lead to substantial improvements in retrieval robustness and MAP@10 performance on BioASQ evaluation batches.

## Context  
Current biomedical QA systems often struggle with queries that do not retrieve relevant documents, limiting answer quality. Retrieval‑augmented pipelines that combine semantic expansion, neural reranking, and post‑processing are emerging as a promising approach to address this challenge in large‑scale knowledge extraction tasks.

## Implications  
For researchers, the work demonstrates how lightweight retrieval recovery can be integrated into existing QA frameworks without heavy computational overhead. Practitioners may adopt these strategies to enhance system reliability on real‑world biomedical datasets and improve user trust in automated answer generation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01468v1)
