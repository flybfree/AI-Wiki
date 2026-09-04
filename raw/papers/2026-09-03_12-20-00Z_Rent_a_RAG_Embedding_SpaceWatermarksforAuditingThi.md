---
title: Rent-a-RAG: Embedding-Space Watermarks for Auditing Third-Party RAG
published: 2026-09-03T12:20:00Z
authors: Alexandr Goultiaev Tolstokorov, Kyriakos Mouratidis, Javad Dogani, Nikolaos Laoutaris
url: http://arxiv.org/abs/2609.03749v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rent-a-RAG: Embedding-Space Watermarks for Auditing Third-Party RAG

## Abstract
Third-party retrieval-augmented generation (RAG) marketplaces create a new auditing problem: data providers may license corpora to a RAG operator, yet later have no visibility into whether their documents are being reused without compensation. Auditing this misuse is difficult because the operator is non-cooperative, answers are paraphrased by the generator, and one response may combine evidence from many providers. We propose DirBucket, a provider-side semantic watermarking and black-box auditing framework for document-level reuse in multi-provider RAG. DirBucket watermarks documents by meaning-preserving paraphrases whose embeddings are biased toward provider-bucket secret directions, enabling detection from black-box answers while preserving retrieval utility. On a challenging benchmark that reflects mixed-provider reuse under black-box access, DirBucket is the only method that consistently achieves strong target detection with no non-target activation, detecting non-compliance in every audit within 23 audited answers on our primary benchmark. The watermark survives adversarial post-answer laundering, and none of the evaluated evasion strategies simultaneously defeats detection while preserving user-perceived answer quality. Detection transfers unchanged to a second benchmark built from real clinical, cyber-threat-intelligence, and legal provider corpora. These results suggest that embedding-space watermarking can make document reuse in third-party RAG statistically auditable.

## Metadata
- **Published**: 2026-09-03T12:20:00Z
- **Authors**: Alexandr Goultiaev Tolstokorov, Kyriakos Mouratidis, Javad Dogani, Nikolaos Laoutaris
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03749v1)