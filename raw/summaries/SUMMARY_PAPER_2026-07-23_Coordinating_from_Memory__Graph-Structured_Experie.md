---
title: Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing
url: http://arxiv.org/abs/2607.19985v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_10-17-53Z_CoordinatingfromMemory_Graph_StructuredExperienceR.md
generated_at: 2026-07-23 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Graph-Structured Experiential Memory (GSEM), a framework that reuses past coordination episodes encoded as heterogeneous relational graphs to improve multi‑agent adaptation in dynamic manufacturing settings. By leveraging graph neural network retrieval, GSEM enables experience‑guided policy updates instead of starting from scratch each time a disturbance occurs. Experiments demonstrate measurable gains in makespan and adaptation speed compared with the strongest memory‑augmented baseline.

## Key Takeaways
- GSEM encodes historical coordination episodes as heterogeneous relational graphs that capture task dependencies, machine states, and inter‑agent collaboration patterns.
- A graph neural network retrieval mechanism identifies structurally similar past episodes when a new disturbance occurs, allowing experience‑guided policy adaptation rather than learning from scratch.
- The framework reduces makespan by 4.1%–10.0% and adaptation time by 33%–38%, with the advantage increasing under higher disturbance frequency.

## Context
This research tackles the memory limitation of reinforcement learning in dynamic environments, where forgetting past experience slows adaptation. By representing coordination history as graph structures, GSEM provides a principled method to preserve relevant episodes across diverse disturbances, offering a more efficient alternative to traditional replay or static memory banks.

## Implications
Practitioners can integrate GSEM into manufacturing control systems to create resilient multi‑agent workflows that recover quickly from disruptions. The framework’s cross‑disturbance transferability suggests it could be adapted to other complex coordination domains beyond job‑shop scheduling, enhancing overall system robustness and efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19985v1)
