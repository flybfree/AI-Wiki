---
title: Specification Portability Across LLM Development Agents: Cross-Agent Compatibility in Specification-Driven Software Migration
url: http://arxiv.org/abs/2608.21208v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_15-21-40Z_SpecificationPortabilityAcrossLLMDevelopmentAgents.md
generated_at: 2026-08-23 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper evaluates how specifications for software migration can be transferred between different large language model agents, using Oracle‑to‑PostgreSQL scripts as a test case. It finds that moving specifications from one agent to another often degrades implementation quality and that the performance depends heavily on which specific models are involved.

## Key Takeaways
- Specification size alone does not predict how well an agent can implement it; a large spec may still be poorly handled by some agents.  
- Cross‑agent transfer can cause substantial degradation, as seen when Gemini consumed a Kiro‑origin specification with very low Token F1 (0.035), SQL syntax validity (2.33 %), and AST mean similarity (0.015).  
- Retrieval‑augmented ingestion is the only strategy that consistently appears on both agents’ Pareto frontiers, indicating its importance for reliable cross‑agent specification handling.

## Context
This work addresses a growing need in AI‑driven software engineering where multiple models collaborate on complex tasks. Understanding how specifications behave across models helps prevent costly errors and resource waste, especially when integrating heterogeneous tools into SDD pipelines.

## Implications
For practitioners, the findings stress that specifications should not be assumed to be universally portable; they must be evaluated with respect to each agent’s capabilities. This encourages developers to design retrieval‑based access mechanisms and to explicitly consider agent‑specific interpretation when building multi‑agent workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21208v1)
