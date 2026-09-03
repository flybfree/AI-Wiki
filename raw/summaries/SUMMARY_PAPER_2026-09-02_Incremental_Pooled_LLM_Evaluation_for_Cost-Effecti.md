---
title: Incremental Pooled LLM Evaluation for Cost-Effective Retrieval Model Selection
url: http://arxiv.org/abs/2609.02745v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_15-47-49Z_IncrementalPooledLLMEvaluationforCost_EffectiveRet.md
generated_at: 2026-09-02 23:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces pooled LLM evaluation for incremental retrieval model selection in RAG systems. It shows that by having an LLM judge the union of documents from multiple candidate models and reusing those judgments as new candidates are added, teams can evaluate many configurations efficiently. The approach yields rankings that match gold standards and reduces evaluation cost dramatically.

## Key Takeaways
- Pooled LLM judgments reuse 65‑80% of previous document evaluations when new systems contribute only their own documents.
- This reuse cuts overall evaluation cost up to 4.9 times compared with re‑judging all documents each time.
- The method preserves pairwise system orderings for 97% of cases even after accounting for bootstrap uncertainty in ground truth.

## Context
Current RAG pipelines rely on frequent LLM‑based relevance judgments to compare retrieval candidates, which is both costly and time‑consuming. As more models are deployed, the need for scalable, repeatable evaluation becomes a bottleneck. This work addresses that bottleneck with a pooled strategy that leverages the same model outputs across evaluations.

## Implications
For practitioners deploying RAG systems, this approach enables rapid benchmarking of new retrieval configurations without sacrificing accuracy. It also reduces operational expense in large‑scale AI deployments where frequent re‑evaluation is impractical. The methodology sets a practical standard for cost‑effective model selection in production AI services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02745v1)
