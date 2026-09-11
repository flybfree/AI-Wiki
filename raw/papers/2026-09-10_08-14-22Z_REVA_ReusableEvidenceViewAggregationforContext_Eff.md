---
title: REVA: Reusable Evidence View Aggregation for Context-Efficient RAG Serving
published: 2026-09-10T08:14:22Z
authors: Tuan Nguyen, Qiran Hu, Banruo Liu, Khoa D. Doan, Kok-Seng Wong, Fan Lai
url: http://arxiv.org/abs/2609.11209v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# REVA: Reusable Evidence View Aggregation for Context-Efficient RAG Serving

## Abstract
Retrieval-augmented generation (RAG) improves knowledge-intensive large language model (LLM) applications by conditioning generation on retrieved documents, but longer contexts increase latency, key-value (KV) cache memory, and token cost. Post-retrieval compression can reduce this cost, yet existing compressors often operate independently for each query, rely on auxiliary models or rewriting, and introduce online overhead that can offset the benefit of shorter prompts. We revisit RAG compression from a data-mining perspective by aggregating historical query--document--model interactions into reusable evidence views. We first show that modern compressors have unstable gains over simple truncation and can add substantial inference-time latency. We then propose Reusable Evidence View Aggregation (REVA), a framework that mines the target generator's historical attention traces into a document-keyed, budget-agnostic score store. REVA maps token-level attention to readable word units, aggregates importance across repeated document accesses, and renders budget-specific plain-text views that preserve document order and the standard RAG interface. Across four representative benchmarks and modern LLMs, REVA improves generation quality by 1.0--5.8 points over existing advances, while reducing compression overhead by a factor of 5.3 to 15.6, adding less than 40 ms of latency.

## Metadata
- **Published**: 2026-09-10T08:14:22Z
- **Authors**: Tuan Nguyen, Qiran Hu, Banruo Liu, Khoa D. Doan, Kok-Seng Wong, Fan Lai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.11209v1)