---
title: Auditing Agent Actions through Query-Conditioned Attribution
url: http://arxiv.org/abs/2609.33676v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_15-37-05Z_AuditingAgentActionsthroughQuery_ConditionedAttrib.md
generated_at: 2026-09-28 21:39
model: qwen3.6-35b-a3b
---

## Summary
This paper formulates query-conditioned agent action attribution to automate the recovery of source data and ordered intermediate evidence for LLM agent actions based on natural-language auditing queries. The authors present $A^3Bench$, a benchmark with 1,396 queries covering policy basis, parameter provenance, failure propagation, and unsafe-behavior tracing, alongside an attribution proposer using small open-weight models that combines gradient saliency with semantic relevance to rank history units efficiently.

## Key Takeaways
- The authors introduce query-conditioned agent action attribution as a novel task that ingests natural-language auditing queries to recover specific sources and ordered evidence for targeted aspects of an agent's action, addressing the limitation of existing methods that lack question-specific traces and struggle in API-only deployments where full model access is unavailable.
- The proposed attribution proposer leverages small open-weight models to combine query-conditioned gradient saliency with query-semantic relevance, achieving significant performance gains over bas

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33676v1)
