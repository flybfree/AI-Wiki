---
title: Procedural Graphs: Self-Evolving Execution Structures for LLM Agents
url: http://arxiv.org/abs/2609.09153v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-08_17-59-41Z_ProceduralGraphs_Self_EvolvingExecutionStructuresf.md
generated_at: 2026-09-08 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Procedural Graphs, a self-evolving execution structure for LLM agents that organizes procedural knowledge into (procedure, relation, procedure) triplets to guide actions. It enables agents to generate tasks guided by subgraph context and improves over memory baselines.

## Key Takeaways
- The Procedural Graph encodes what-to-do tasks using (procedure, relation, procedure) triplets, allowing the agent’s decision at each step to be locally biased by surrounding graph structure.
- The framework self-evolves via an LLM refiner that edits graph topology and attributes based on trajectory success, preserving held-out validation performance while discouraging repetition of rejected nodes.
- Starting from a minimal skeleton, the loop constructs graphs that match or surpass hand‑designed ones and can repair flawed expert priors.

## Context
In AI research, long-horizon agent planning often leads to forgetting objectives and repeating actions, limiting performance over time. Memory‑based baselines are widely used but struggle with scalability and adaptability. Procedural Graphs address these issues by providing a structured procedural knowledge base that adapts automatically without manual engineering.

## Implications
This approach offers a scalable way to improve LLM agents across diverse tasks and models without requiring handcrafted protocols, reducing reliance on expert‑driven design. It enables continual improvement of execution structures, potentially leading to more reliable and efficient autonomous systems in industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09153v1)
