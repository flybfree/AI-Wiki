---
title: MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows
url: http://arxiv.org/abs/2608.10509v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_05-31-18Z_MAP_Graph_Provenance_AwareSharedMemoryforMulti_Age.md
generated_at: 2026-08-11 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MAP-Graph, a provenance-aware memory layer that integrates agents, sources, memories, claims and actions into a typed execution graph. It demonstrates high task success rates on synthetic benchmarks by combining permission filtering, trust-based ranking, and risk-sensitive gating while preserving lineage for audit.

## Key Takeaways
- The system excludes records that lack proper permissions, preventing unauthorized reads or unsafe actions.
- Eligible memories are ranked using both semantic similarity and multiplicative path trust to prioritize relevant evidence.
- A risk-sensitive gate evaluates action risk before execution, allowing only safe interventions while logging affected lineage for later audit.

## Context
In multi-agent AI workflows, shared memory is essential but often lacks fine-grained access control. Current solutions either provide coarse-grained permissions or rely on post‑hoc auditing, leaving gaps in real‑time safety and trust enforcement.

## Implications
This work shows provenance can serve as an operational signal rather than merely audit data, enabling safer collaborative AI systems. Practitioners can adopt similar graph‑based memory layers to improve both correctness and accountability in complex workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10509v1)
