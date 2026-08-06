---
title: AgentAntibody: An Adaptive Immune System for Defending LLM Agents against Prompt Injection
url: http://arxiv.org/abs/2608.04053v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_10-41-34Z_AgentAntibody_AnAdaptiveImmuneSystemforDefendingLL.md
generated_at: 2026-08-05 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces AgentAntibody, an adaptive immune system that equips LLM agents with a persistent library of antibodies representing their evolving security boundary against prompt injection attacks. Experiments across three benchmarks and four backbone LLMs demonstrate that the approach outperforms existing defenses by learning user boundaries through experience while still completing legitimate tasks.

## Key Takeaways
- The defense must learn from each encounter and apply its knowledge to subsequent requests, reflecting a dynamic adaptation of understanding.
- AgentAntibody maintains a persistent library of antibodies that evolve as the agent’s security boundary is refined over time.
- Empirical results show that the system prevents harmful actions without sacrificing legitimate task completion, even when both are compatible with the stated goal.

## Context
Prompt injection remains a critical threat to LLM agents because current defenses treat each task in isolation and cannot anticipate evolving user expectations. This work addresses the need for memory‑based learning that aligns security responses with concrete user cases across multiple interactions.

## Implications
The adaptive framework offers a scalable method for protecting deployed LLMs, encouraging integration of persistent knowledge into security pipelines. Practitioners can leverage this approach to build trustworthy agents that evolve their defenses without compromising functionality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04053v1)
