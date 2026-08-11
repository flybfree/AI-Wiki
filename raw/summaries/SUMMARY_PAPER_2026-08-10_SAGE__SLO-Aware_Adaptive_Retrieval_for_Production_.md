---
title: SAGE: SLO-Aware Adaptive Retrieval for Production RAG Systems
url: http://arxiv.org/abs/2608.08237v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_17-05-36Z_SAGE_SLO_AwareAdaptiveRetrievalforProductionRAGSys.md
generated_at: 2026-08-10 22:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SAGE, a learned adaptive retrieval policy that tailors the number of passages retrieved per query to meet strict service level objectives while preserving answer quality. On Natural Questions with a 5‑second P95 latency target, SAGE meets 95 % SLO compliance compared to only 30 % for static baselines, cuts latency by 36 %, and reduces retrieval cost by 51 % with minimal impact on exact match scores.

## Key Takeaways
- SAGE dynamically adjusts the retrieval budget k per query using lightweight features such as score distributions and rank gaps, avoiding fixed‑k overhead.  
- The policy is trained offline via imitation learning from an oracle that balances latency and quality, enabling zero‑LLM inference at deployment.  
- A single model trained on Natural Questions generalizes across HotpotQA, UnSeenTimeQA, and four LLM families, delivering +45‑52 point SLO improvements without sacrificing answer quality.

## Context
Retrieval‑augmented generation systems must reconcile high accuracy with operational constraints like latency budgets and cost. Traditional fixed‑k retrieval often fails to meet these service level objectives, leading to either poor answers or non‑compliant performance. This work addresses the need for a scalable, policy‑driven approach that adapts to query difficulty without compromising real‑time efficiency.

## Implications
For practitioners deploying RAG in production, SAGE offers a practical framework to align retrieval with service level agreements while minimizing resource usage. The ability of one model to generalize across diverse datasets and models suggests broader applicability, encouraging industry adoption of adaptive retrieval strategies that balance quality and cost.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08237v1)
