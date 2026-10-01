---
title: Rep2Skill: Representation-Guided Skill Self-Evolution for LLM Agents
url: http://arxiv.org/abs/2609.39149v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_07-15-10Z_Rep2Skill_Representation_GuidedSkillSelf_Evolution.md
generated_at: 2026-09-30 20:41
model: qwen3.6-35b-a3b
---

## Summary
Rep2Skill presents a representation-guided framework that allows LLM-based agents to evolve their textual skills by integrating internal model representations into the optimization process, moving beyond traditional text-only paradigms. By modeling internal state trajectories during agent rollouts, the method identifies execution deviations and converts these signals into actionable feedback for targeted skill revision. Experimental results demonstrate that Rep2Skill consistently outperforms text-only approaches in self-evolution settings, achieving superior performance without requiring a stronger external model to guide the optimization.

## Key Takeaways
- Existing skill evolution methods are limited to the text space, relying solely on execution trajectories and sparse task outcomes to diagnose failures; Rep2Skill addresses this by incorporating rich internal representations into the skill optimization loop, enabling the agent to reflect on its own evolving execution state rather than just surface-level results.
- The framework operates by analyzing collected agent rollouts to model representation trajectories, localizing specific turns where the agent's internal dynamics deviate from successful patterns; these deviations are interpreted alongside execution contexts to generate precise textual feedback that drives targeted revisions of the procedural skills.
- Rep2Skill demonstrates consistent performance gains over text-only baselines in a rigorous self-evolution setting where the same LLM serves as both the executor and optimizer, proving that representation-guided reflection is effective for self-improvement even when no external stronger model is available to assist in diagnosis or revision.

## Context
The development of autonomous LLM agents requires efficient mechanisms for accumulating reusable knowledge without frequent parameter updates, yet current skill acquisition methods often ignore the diagnostic potential hidden within a model's internal activations during execution. By leveraging these representations,

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39149v1)
