---
title: Addressable Recall Compaction for Long Context-Window Control in AI Agents
url: http://arxiv.org/abs/2607.25066v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-27_20-51-05Z_AddressableRecallCompactionforLongContext_WindowCo.md
generated_at: 2026-07-28 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ARC, an addressable recall compaction framework that separates archival storage from active context presentation to handle long‑horizon LLM agents within fixed window limits. Experiments on Qwen3 models show exact‑answer accuracy of 99.40% versus 88.12% for the best baseline and lower serving costs.

## Key Takeaways
- ARC stores tool observations in an append‑only, ID‑addressable log so that older entries can be replaced by compact citations without losing task‑critical details.
- The framework enables agents to retrieve stored content via identifiers instead of relying on similarity‑based retrieval or re‑executing tools.
- ARC improves exact‑answer accuracy and reduces estimated serving time and HBM traffic compared with context‑management baselines.

## Context
Long‑context window constraints are a bottleneck for multi‑step AI agents, forcing developers to prune or summarize memory. Traditional compaction often discards information, leading to loss of critical data and degraded performance.

## Implications
Explicit addressable recall can become a standard technique for efficient long‑term reasoning in large language models. Practitioners may adopt ARC to maintain high accuracy while minimizing hardware costs and latency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25066v1)
