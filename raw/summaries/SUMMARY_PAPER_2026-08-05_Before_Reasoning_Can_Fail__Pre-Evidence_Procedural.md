---
title: Before Reasoning Can Fail: Pre-Evidence Procedural Failures in Agentic RAG
url: http://arxiv.org/abs/2608.02011v2
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_10-09-19Z_BeforeReasoningCanFail_Pre_EvidenceProceduralFailu.md
generated_at: 2026-08-05 01:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates procedural failures in agentic retrieval‑augmented generation (RAG) that occur before evidence is actually read. By analyzing 12,000 paired trajectories across multiple QA datasets, the authors identify two distinct failure modes: pre‑evidence discipline failures where agents retrieve snippets but skip inspection, and post‑gold‑read failures where they read but still produce wrong answers. Forced reading improves performance by roughly 15 points on these trajectories.

## Key Takeaways
- The both‑trigger rate of pre‑evidence and post‑gold‑read failures is between 11.2% and 13.1% across regex and spaCy extractors, indicating they are largely non‑redundant.  
- Implementing a minimal runtime invariant called Read‑Gate forces agents to read after search and before finalization, raising LLM‑Acc by 14.9–19.9 points on trajectories that would otherwise skip reading.  
- Larger hidden thinking budgets do not automatically increase evidence inspection, showing that procedural discipline is separate from computational resources.

## Context
Agentic RAG systems aim to combine large language model reasoning with external knowledge bases, yet current approaches treat evidence handling as a side effect rather than a controlled step. Understanding where failures arise in the trajectory can lead to more robust and interpretable models.

## Implications
For practitioners, treating evidence inspection as a trajectory‑level control problem could prevent systematic errors without sacrificing compute efficiency. This insight may guide system design, prompting developers to embed read gates and monitor procedural compliance across diverse retrieval pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02011v2)
