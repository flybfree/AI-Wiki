---
title: "Summary: ECHO: Prune to act, trace to learn with selective turn memory in agentic RL"
url: http://arxiv.org/abs/2606.31650v1
type: paper-summary
date: 2026-06-30
source_paper: 2026-06-30_13-29-58Z_ECHO_Prunetoact_tracetolearnwithselectiveturnmemor.md
generated_at: 2026-06-30 21:00
model: nvidia/nemotron-3-nano-4b
---
# Summary: 2026-06-30 Echo  Prune To Act  Trace To Learn With Selective 

## Summary
The paper introduces ECHO, a selective turn-memory framework for long‑horizon language agents that compresses environment turns into compact records while preserving source indices. It enables policy rollouts within bounded windows and aligns outcome credit with the evidence used to generate successful answers. On BrowseComp‑Plus, ECHO achieves 43.4% accuracy, beating GRPO (28.9%) and SUPO (36.1%), using fewer turns.

## Key Takeaways
- ECHO compresses each completed environment turn into a compact memory record that retains source indices for traceable learning.
- The framework reconstructs bounded policy contexts by selecting from these records, allowing fine‑grained evidence reuse without loss of context.
- Positive outcome credit is routed to the selected source indices and selection actions, providing explicit alignment between rollout and successful answers.

## Context
Long‑horizon language agents face challenges in managing extensive interaction histories within limited context windows. Traditional methods truncate or summarize distant turns, sacrificing fine‑grained evidence reuse and traceability. ECHO addresses these issues by maintaining source‑indexed records that support both compression and accountability.

## Implications
For practitioners developing agentic systems, ECHO offers a practical way to balance memory efficiency with explainable learning. The approach can be applied across diverse tasks such as multi‑objective QA, code generation, and deep information seeking, enhancing generalization and performance without sacrificing interpretability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.31650v1)
