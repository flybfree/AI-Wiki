---
title: Selective Forgetting: A Graph-Based Memory Framework for Long-Term LLM Agents
url: http://arxiv.org/abs/2608.28978v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_01-11-10Z_SelectiveForgetting_AGraph_BasedMemoryFrameworkfor.md
generated_at: 2026-08-31 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a graph‑based memory framework called Selective Forgetting that encodes conversational turns as typed nodes and edges, answers questions via two‑hop subgraph queries, and periodically prunes low‑scoring nodes using recency, access frequency, degree centrality, and age. On LongMemEval the graph underperforms flat retrieval at five roots with token F1 0.417 versus 0.468, while a forgetting module reduces node count by 9.8% without harming recall.

## Key Takeaways
- The assumption that decomposing turns into entities improves recall is false; token F1 drops and correctness falls sharply on questions needing the prior turn’s surface form.
- Periodic pruning removes many nodes with minimal impact on token F1 but noticeably reduces judged correctness by 1.6 points, indicating forgetting hurts performance.
- The extraction pipeline’s gains are limited to this specific benchmark; broader graph memory may behave differently.

## Context
Graph‑based memory aims to replace flat retrieval in long‑term LLM agents by preserving structured knowledge. This study shows that naive graph encoding can degrade performance when surface‑level cues are lost, highlighting the need for careful design beyond simple node extraction.

## Implications
For practitioners, it suggests that structured memory must balance complexity and fidelity, and that forgetting mechanisms should be carefully tuned; otherwise they may introduce errors rather than improve recall.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28978v1)
