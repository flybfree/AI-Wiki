---
title: TurboVec: A Case Study in Cost-Efficient Private Retrieval for Enterprise RAG via Codebook-Oblivious Quantization
url: http://arxiv.org/abs/2607.16973v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-18_21-43-40Z_TurboVec_ACaseStudyinCost_EfficientPrivateRetrieva.md
generated_at: 2026-07-23 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TurboVec, an open‑source vector index that leverages codebook‑oblivious quantization via TurboQuant to address privacy and performance gaps in enterprise RAG systems. On the DBpedia OpenAI benchmark, TurboQuant 4‑bit achieves higher Recall@5 than trained FAISS Product Quantization while using far less memory, and kernel‑level filtering maintains strong recall across multiple tenant workloads.

## Key Takeaways
- TurboQuant’s codebook‑oblivious design eliminates corpus‑dependent training, preventing leakage in multi‑tenant environments.  
- The index delivers Recall@5 improvements of 8.5–8.9 percentage points compared with trained PQ methods at the same memory budget.  
- Kernel allowlist filtering sustains Recall@10 between 0.86 and 0.93, far surpassing post‑filter baselines that drop to 0.09–0.19.

## Context
Enterprise RAG systems rely on vector indexes that must balance recall, latency, and privacy. Traditional quantization techniques often require training on the data, creating exploitable information leakage. This work demonstrates a practical alternative that preserves performance without exposing corpus statistics.

## Implications
The findings suggest that codebook‑oblivious quantization can be adopted in production RAG pipelines to meet strict tenant isolation requirements. Practitioners can reduce infrastructure costs and improve privacy guarantees while maintaining high retrieval quality, making large language model applications more scalable and compliant.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.16973v1)
