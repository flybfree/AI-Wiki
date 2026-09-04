---
title: STAIR (STructure Aware Information Retriever): A novel dataset and LLM based retriever for document structure augmentation
url: http://arxiv.org/abs/2609.03874v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_14-02-53Z_STAIR_STructureAwareInformationRetriever__Anovelda.md
generated_at: 2026-09-03 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces STAIR, a retrieval system that uses document structure like Table of Contents to improve Retrieval Augmented Generation and reduce hallucinations below 0.05%. On the SearchTome benchmark it achieves Recall@1 82.6% versus DSI's 76.9%, significantly outperforming BM25 (59.5%), DPR (68.7%) and out‑of‑the‑box Mistral (13.8%). The ablation studies confirm that ToC-based retrieval builds a low hallucination generative IR system.

## Key Takeaways
- STAIR leverages global document structure such as Table of Contents to store information in the LLM's parameters, enabling precise and accurate retrieval.
- Ablation experiments show that using ToC reduces hallucinations to less than 0.05% and improves recall by about 6 percentage points over DSI.
- The system generalizes well even with very few training samples, achieving high Recall@1 scores across diverse domains.

## Context
Current RAG systems rely on chunking long texts into length‑based pieces which discard semantic global structure, leading to loss of context and higher hallucination rates. This paper addresses that limitation by showing how structured metadata can be exploited for retrieval without explicit chunking.

## Implications
For practitioners developing AI assistants, STAIR offers a practical way to maintain factual accuracy with minimal data. The approach could be integrated into document processing pipelines across industries where precise information retrieval is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03874v1)
