---
title: LiteRAG: Cost-Efficient Graph-Based Retrieval-Augmented Generation
url: http://arxiv.org/abs/2609.10239v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-09_14-32-07Z_LiteRAG_Cost_EfficientGraph_BasedRetrieval_Augment.md
generated_at: 2026-09-09 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
LiteRAG introduces a graph‑based retrieval method that replaces costly LLM control with query‑conditioned algorithmic exploration, achieving state‑of‑the‑art performance on multi‑hop question answering benchmarks while dramatically cutting latency and cost. The approach yields the highest overall quality (0.798) among evaluated methods and reduces per‑query latency by over 100× and cost by over 99% compared with GraphRAG Global and DRIFT.

## Key Takeaways
- LiteRAG’s query‑adaptive thresholding dynamically limits token usage, enabling generation with about 14× fewer tokens than LinearRAG.  
- Community‑aware hub penalization suppresses low‑impact nodes in the graph, further improving token efficiency and relevance.  
- The method replaces expensive retrieval‑time LLM control with algorithmic reasoning chains, resulting in a >100× latency reduction and >99% cost saving.

## Context
Graph‑based retrieval has become a cornerstone for multi‑hop question answering, yet most systems rely on large context windows that strain generation models. LiteRAG’s focus on token efficiency addresses this bottleneck, aligning retrieval with the limited context capacity of modern LLMs.

## Implications
For industry practitioners, LiteRAG offers a scalable solution to reduce inference costs and latency in real‑time applications, encouraging adoption of algorithmic over LLM‑driven retrieval pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.10239v1)
