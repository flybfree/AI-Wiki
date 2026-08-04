---
title: Before Reasoning Fails: Pre-Evidence Procedural Failures in Agentic RAG
url: http://arxiv.org/abs/2608.02011v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_10-09-19Z_BeforeReasoningFails_Pre_EvidenceProceduralFailure.md
generated_at: 2026-08-03 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates procedural failures in agentic RAG where agents retrieve candidate snippets but finalize answers without inspecting them. It decomposes these failures into pre‑evidence discipline failures and post‑gold‑read failures using saved tool‑call traces across 12,000 trajectories on HotpotQA, 2WikiMultiHopQA, and MuSiQue. The study shows that forcing agents to read after search improves performance by up to 19.9 points.

## Key Takeaways
- The two failure types are largely non‑redundant: the both‑trigger rate is in [11.2%, 13.1%] across regex and spaCy entity extractors.
- Forced reading improves LLM‑Acc by 14.9‑19.9 points on trajectories that would otherwise skip reading and by 3.2‑9.4 points on full minimal‑reasoning cells.
- Larger hidden thinking budgets do not necessarily increase evidence inspection.

## Context
Retrieval‑augmented generation is a core technique in modern AI systems, yet its reliability hinges on whether agents follow proper procedural steps. This research highlights that even with sufficient reasoning capacity, skipping the reading step can lead to systematic errors, underscoring the need for process‑level safeguards beyond answer quality.

## Implications
For practitioners, this work suggests designing RAG pipelines that enforce a read gate as a trajectory‑level control rather than relying solely on downstream accuracy metrics. Integrating such procedural checks into training and evaluation can yield more robust and trustworthy systems in both research and industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02011v1)
