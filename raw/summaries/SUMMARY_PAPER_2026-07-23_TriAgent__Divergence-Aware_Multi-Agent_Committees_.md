---
title: TriAgent: Divergence-Aware Multi-Agent Committees for Cost-Efficient Financial Sentiment Analysis
url: http://arxiv.org/abs/2607.19794v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_06-20-32Z_TriAgent_Divergence_AwareMulti_AgentCommitteesforC.md
generated_at: 2026-07-23 23:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
TriAgent introduces a multi‑agent committee architecture for financial sentiment analysis that separates lexical, sentence‑level, and cross‑sentence processing to avoid linear cost scaling. The core insight is the critic plateau: using an LLM as a critic yields stable F1 around 0.87 while a simple vote drops to 0.66 due to granularity‑driven disagreement.

## Key Takeaways
- The Semantic Divergence Index (SDI) routes queries through three agents, preventing unnecessary large‑model calls and achieving cost savings of $9.3M per year at 10 million users.
- A shared consensus dictionary enables near‑perfect cross‑language performance on Chinese queries with F1=0.99, demonstrating zero marginal cost for multilingual canonicalization.
- The SDI also functions as a hallucination detector with AUC=0.90 and delivers the highest risk‑adjusted Sharpe ratio (3.50) among all tested strategies.

## Context
Financial sentiment analysis relies heavily on costly large language models that process every query, leading to exponential bill growth as user volume rises. This paper addresses the structural cost trap by decomposing reasoning into lightweight agents and a meta‑critic, offering a scalable alternative that aligns with real‑world deployment constraints.

## Implications
For practitioners, TriAgent provides a framework to balance accuracy and expense in high‑throughput sentiment tasks, especially when multilingual support is required. The approach could be adopted by financial platforms seeking to reduce cloud spend while maintaining strong performance across diverse markets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19794v1)
