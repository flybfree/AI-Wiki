---
title: Do Current Retrievers Cover All the Evidence? A Controlled Study of Conjunctive Cross-Page Retrieval
url: http://arxiv.org/abs/2607.24165v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_08-46-27Z_DoCurrentRetrieversCoverAlltheEvidence_AControlled.md
generated_at: 2026-07-27 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether current document retrievers fully cover all evidence when answering conjunctive multi-part requests that span multiple pages. It uses the n-Clue benchmark to compare retrieval performance across different models and configurations, finding that while some systems locate gold documents, they often fail to satisfy every condition simultaneously.

## Key Takeaways
- The study shows that condition coverage is a major bottleneck: even when a dense model finds a top‑10 gold for 81.1 % of queries, it succeeds in satisfying all conditions only on 35.8 %.  
- Lexical‑visual fusion improves dense backbones by 6.8–7.3 points but generic rerankers reduce Gold‑NDCG, indicating that hybrid approaches still leave gaps.  
- Scaling a dense model from 0.6B to 8B does not change complete‑first success, highlighting that size alone is insufficient.

## Context
Retrieval systems must handle complex queries where evidence appears on different pages of the same document, a challenge central to long‑document understanding and answer generation. This work contributes to the growing effort to evaluate retrieval beyond simple gold discovery toward full condition satisfaction.

## Implications
For industry practitioners, the findings suggest that improving condition coverage is more critical than merely increasing model size or using richer fusion strategies. Researchers should focus on mechanisms that ensure each explicit condition is met across pages rather than relying solely on dense passage retrieval.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24165v1)
