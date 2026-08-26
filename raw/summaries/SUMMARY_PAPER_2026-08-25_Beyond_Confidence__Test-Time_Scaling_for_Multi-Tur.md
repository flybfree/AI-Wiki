---
title: Beyond Confidence: Test-Time Scaling for Multi-Turn Search Agents via Retrieval Grounding
url: http://arxiv.org/abs/2608.24024v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_03-28-17Z_BeyondConfidence_Test_TimeScalingforMulti_TurnSear.md
generated_at: 2026-08-25 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the limitation of confidence-based voting when used in multi‑turn search agents that retrieve external documents. It shows that confidence scores become flat due to copy inflation and weighted votes degrade. The authors propose Retrieval‑Grounded Voting (RGV) which uses lexical overlap with retrieved docs as a score, avoiding contaminated log probabilities.

## Key Takeaways
- Confidence‑based voting transfers poorly to multi‑turn search agents because appended document tokens cause inflated token log probabilities leading to copy inflation.
- This flattening reduces confidence scores within each question and weakens the final weighted vote resulting in lower accuracy.
- Retrieval‑Grounded Voting (RGV) mitigates this by scoring rollouts based on lexical overlap with retrieved documents, computing signal outside contaminated context without extra LLM calls.

## Context
Modern large language models are increasingly deployed as multi‑turn search agents that retrieve and condition on external documents. Traditional confidence‑based voting methods, designed for single‑turn reasoning, do not scale well due to contamination from retrieved content. This gap highlights a need for evaluation strategies that remain robust when external knowledge is integrated.

## Implications
For practitioners developing search agents, adopting RGV can improve accuracy especially on minority‑correct questions where correct answers appear in few rollouts. The approach reduces reliance on noisy confidence signals and enables more reliable multi‑turn reasoning across diverse LLMs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24024v1)
