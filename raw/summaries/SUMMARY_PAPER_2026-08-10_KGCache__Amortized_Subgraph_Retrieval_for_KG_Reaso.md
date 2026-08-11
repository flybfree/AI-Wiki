---
title: KGCache: Amortized Subgraph Retrieval for KG Reasoning with LLMs
url: http://arxiv.org/abs/2608.07954v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_06-36-24Z_KGCache_AmortizedSubgraphRetrievalforKGReasoningwi.md
generated_at: 2026-08-10 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces KGCache, an in‑memory cache for one‑hop knowledge graph neighborhoods that reduces repeated queries in Knowledge Graph Question Answering workloads. It is positioned between the KGQA engine and the backend serving the KG and supports both iterative traversal (ToG) and one‑shot planning (RoG) paradigms. Evaluation on WebQSP and CWQ demonstrates substantial speedups when entity caching is used.

## Key Takeaways
- Entity caching reduces retrieval time by up to 1.91 times, as many queries reuse the same graph neighborhoods.
- Semantic‑context caching provides an additional 6% overall speedup, with each hit being about 3.73 times faster than a fresh query.
- The cache improves both datasets but semantic caching requires further accuracy testing on CWQ.

## Context
Knowledge graphs are increasingly used to ground large language models in factual information, yet current systems repeatedly query the same graph structures for different questions, causing latency. Caching these neighborhoods can alleviate this bottleneck and make KG reasoning more scalable.

## Implications
For industry practitioners, KGCache offers a practical way to accelerate real‑time KGQA applications without sacrificing accuracy. Researchers can explore similar caching strategies for other graph‑based reasoning tasks to improve system responsiveness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07954v1)
