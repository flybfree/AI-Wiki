---
title: DistilVDR: A Compact End-to-End Visual Document Retriever via Dual-Student Distillation
url: http://arxiv.org/abs/2608.10636v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_08-23-39Z_DistilVDR_ACompactEnd_to_EndVisualDocumentRetrieve.md
generated_at: 2026-08-11 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DistilVDR, a compact end‑to‑end visual document retriever that compresses an 8 billion‑parameter vision‑language teacher into two student models totaling 524 M parameters. By using bilateral distillation with pointwise cosine alignment and asymmetric encoders, the system achieves strong retrieval performance while drastically reducing index size and latency.

## Key Takeaways
- The student encoder is trained solely on the frozen teacher’s embedding space, eliminating the need for relevance labels or negative sampling.
- One variant stores one million documents in a 15.6‑times smaller index than sub‑1 B multi‑vector baselines and indexes the corpus an order of magnitude faster.
- DistilVDR-HiRes reaches 61.74 average NDCG@5 on ViDoRe, matching 86.9 % of the teacher’s performance.

## Context
Current visual document retrieval systems rely on massive multi‑billion‑parameter models that are impractical for large corpora due to high indexing cost and latency. This work demonstrates that end‑to‑end compression can preserve strong retrieval quality without sacrificing the need for relevance supervision, offering a path toward scalable and efficient VDR.

## Implications
For industry practitioners, DistilVDR provides a ready‑to‑deploy model that balances performance with resource constraints, enabling real‑time search at scale. Researchers gain insight into how bilateral distillation can reduce parameter count while maintaining alignment between text and image embeddings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10636v1)
