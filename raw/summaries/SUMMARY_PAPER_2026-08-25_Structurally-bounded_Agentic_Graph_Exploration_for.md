---
title: Structurally-bounded Agentic Graph Exploration for Evidence-Grounded Scholarly DeepSearch
url: http://arxiv.org/abs/2608.24809v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_16-51-26Z_Structurally_boundedAgenticGraphExplorationforEvid.md
generated_at: 2026-08-25 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Crase, a bounded alternative to deep research agents that performs scholarly search by querying once for seed papers, expanding within a 1.5-hop citation neighborhood, pruning edges lacking entailment support, and ranking results via recency-aware random walk. On LitSearch and an arXiv benchmark of 500K papers, Crase achieves up to three times the recall@50 compared with proprietary deep research agents while using roughly a third of their cost.

## Key Takeaways
- Crase limits its search to a fixed citation neighborhood and stops after one query, unlike open-ended loops.  
- It prunes citations that do not provide entailment support, ensuring only evidence‑grounded papers are considered.  
- The ranking uses recency‑aware random walk, making the stopping condition explicit and predictable.

## Context
Scholarly search agents often suffer from unbounded exploration leading to high computational cost and diminishing returns. This work demonstrates that a bounded, inspectable approach can match or exceed performance of large proprietary models with lower resource usage. The method aligns with trends toward explainable AI and efficient knowledge retrieval in academic settings.

## Implications
For researchers seeking reliable citations, Crase offers a transparent pipeline that reduces hallucinations and over‑exploration. Practitioners can integrate it into automated literature review pipelines without sacrificing recall, supporting scalable scholarly research at reduced cost.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24809v1)
