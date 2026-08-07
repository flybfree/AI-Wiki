---
title: Search2Skill: Skill Distillation Beyond Knowledge Boundaries Via Rubric-Based Reinforcement Learning
url: http://arxiv.org/abs/2608.05245v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_15-09-07Z_Search2Skill_SkillDistillationBeyondKnowledgeBound.md
generated_at: 2026-08-06 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
Search2Skill introduces a framework that automatically discovers and fills skill gaps in LLM agents by searching external resources and distilling them into reusable skills using rubric‑based reinforcement learning. Experiments on eight expert domains show the method outperforms both search‑augmented and trajectory‑based baselines, indicating effective skill abstraction and cross‑scale transfer.

## Key Takeaways
- The framework identifies capability gaps between the model’s internal knowledge and required professional procedures, then searches external sources to fill those gaps.  
- A rubric‑driven reinforcement learning scheme jointly optimizes search timing, query formulation, and skill generation, leading to structured reusable skills rather than raw evidence.  
- Skill abstraction is the source of gains, enabling transfer across model scales and demonstrating consistent improvement in streaming and held‑out evaluations.

## Context
LLM agents can evolve expertise by acquiring procedural knowledge, but existing methods are limited by the model’s existing parameters or trajectories. Search2Skill addresses this limitation by leveraging external information to create skills that go beyond what the model initially knows, aligning with broader goals of self‑improving AI systems.

## Implications
This approach could enable industry‑specific agents to continuously upgrade their capabilities without manual skill engineering, reducing reliance on static training data and fostering scalable, adaptable expertise across domains. Practitioners may integrate Search2Skill into pipelines for rapid deployment of domain‑expert LLM assistants.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05245v1)
