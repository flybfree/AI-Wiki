---
title: Retrieved But Not Reliable: A Survey on Attacks, and Defenses in Retrieval-Augmented Generation
url: http://arxiv.org/abs/2608.24977v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-25_16-18-04Z_RetrievedButNotReliable_ASurveyonAttacks_andDefens.md
generated_at: 2026-08-26 20:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper surveys attacks and defenses in Retrieval-Augmented Generation, formalizing threat models over the corpus, retriever, and generator, and organizing attacks into accuracy, privacy, and fairness objectives. It reviews pipeline‑aware defenses across retrieval, rerank, generation, and traceback stages and summarizes robustness benchmarks.

## Key Takeaways
- The survey introduces a unified threat model covering three components of the RAG pipeline.  
- Attacks are categorized by objective: accuracy degradation, privacy leakage, and fairness violations.  
- Defenses are organized per pipeline stage including retrieval, reranking, generation, and traceback.

## Context
Retrieval-Augmented Generation combines large language models with external knowledge sources to improve factuality but introduces new security vulnerabilities that were not addressed in earlier LLM literature. This work fills a gap by providing a comprehensive view of robustness across the entire RAG pipeline.

## Implications
Practitioners must consider threat modeling and stage‑specific defenses when deploying RAG systems to avoid harmful outputs or privacy breaches. The framework can guide research on robust retrieval mechanisms, fair knowledge grounding, and explainable traceability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24977v1)
