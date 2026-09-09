---
title: MARBO: Relational Belief Grounding for LLM Agents in Social Deduction Games
url: http://arxiv.org/abs/2609.06563v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-06_12-18-39Z_MARBO_RelationalBeliefGroundingforLLMAgentsinSocia.md
generated_at: 2026-09-08 23:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MARBO, a belief-grounded preference optimization framework for LLM agents playing social deduction games. It shows that grounding actions and speech in relational beliefs improves consistency and performance, especially for compact agents.

## Key Takeaways
- MARBO only provides preference feedback when behaviors are supported by reliable relational beliefs and lead to strategically favorable outcomes.
- The framework encourages consistent learning under uncertainty by linking belief reliability to reward signals.
- Experiments demonstrate that compact LLM agents using MARBO consistently outperform existing baselines on representative SDGs.

## Context
Social deduction games demand agents to infer hidden roles while observing limited information, a challenge for AI systems lacking explicit belief tracking. Recent work focuses on prompting and preference optimization but often neglects the underlying belief mechanisms that drive strategic consistency.

## Implications
MARBO offers a principled approach to aligning LLM behavior with real-time relational knowledge, which could improve reliability in multi-agent collaborative tasks. Practitioners may adopt this grounding technique to reduce strategically inconsistent outputs in complex social simulations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.06563v1)
