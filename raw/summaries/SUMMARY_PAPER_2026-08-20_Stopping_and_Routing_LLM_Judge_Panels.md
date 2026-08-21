---
title: Stopping and Routing LLM Judge Panels
url: http://arxiv.org/abs/2608.19802v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_08-58-00Z_StoppingandRoutingLLMJudgePanels.md
generated_at: 2026-08-20 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a framework for designing judge panels in LLM evaluation by treating the allocation of judges as a role-conditioned problem. It learns which judges to call, on which examples, and when to stop based on validation gains, using a small audit set. The method outperforms many existing strategies across reasoning, code, safety, etc.

## Key Takeaways
- The framework identifies that copies add no conditional information and should be dropped while complements improve the global panel.
- Specialists are routed conditionally only to specific slices where they provide value.
- Evaluation stops when validation gain falls below a predefined threshold.

## Context
LLM evaluation relies on assembling diverse judges, but current approaches lack systematic guidance for when to include which judge or stop early. This paper addresses that gap by formalizing the allocation problem and providing an empirical regime map.

## Implications
Practitioners can now generate auditable call plans that balance quality and cost, reducing unnecessary compute while preserving performance. The method supports scalable deployment across multiple evaluation tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19802v1)
