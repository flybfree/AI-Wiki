---
title: MetaSkill: Reusable Problem-Solving Methods for Adaptive Skill Orchestration in LLM Agents
url: http://arxiv.org/abs/2611.29274v1
type: paper-summary
date: 2026-11-24
source_paper: 2026-11-22_06-42-45Z_MetaSkill_ReusableProblem_SolvingMethodsforAdaptiv.md
generated_at: 2026-11-24 22:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
MetaSkill introduces a two-layer framework that enables LLM agents to reuse curated problem-solving methods across diverse tasks and domains by separating method selection from execution orchestration. The framework combines a method layer that selects from 26 curated methods and binds abstract roles to task objects with an execution layer that identifies intermediate objectives, coordinates native skills, and guides repair or method reselection. Evaluations on 89 SkillsBench tasks and 995 ToolHop examples demonstrate consistent accuracy gains of 3.51–13.48% over the strongest baseline across all six tested configurations.

## Key Takeaways
- MetaSkill's two-layer architecture explicitly decouples method selection from execution orchestration, allowing agents to choose from 26 curated problem-solving methods and bind abstract method roles to concrete task objects, rather than relying on ad-hoc reasoning or direct method injection alone.
- The execution layer goes beyond simple method application by identifying intermediate objectives, coordinating native agent skills, and incorporating a repair or method reselection mechanism, which ablation studies confirm contributes additional performance gains beyond the initial method-guided orchestration.
- The framework was validated across two distinct benchmarks—SkillsBench (89 tasks) and ToolHop (995 examples)—and outperformed all evaluated baselines in every configuration tested, with accuracy improvements ranging from 3.51% to 13.48%, demonstrating robustness across task types and tool-use scenarios.

## Context
This work addresses a persistent challenge in LLM agent design: while reusable skills and tool-use capabilities have advanced significantly, agents still struggle to determine how to organize, sequence, and adapt those skills for novel tasks. MetaSkill contributes to the growing body of research on structured agent orchestration by formalizing problem-solving methods as first-class, transferable components rather than leaving method selection to implicit chain-of-thought reasoning. It sits at the intersection of skill-based agent architectures, tool-use planning, and adaptive reasoning frameworks that have gained traction since 2024.

## Implications
For practitioners building agentic systems, MetaSkill offers a principled blueprint for moving beyond prompt-engineered workflows toward structured, auditable method orchestration that can be maintained, extended, and evaluated independently of the underlying LLM. The demonstrated gains from explicit method reselection suggest that production agent pipelines should incorporate feedback loops for method adaptation rather than committing to a single strategy per task. For the broader field, the separation of a curated method library from task-specific execution opens a path toward standardized, composable agent capabilities that could accelerate benchmarking, safety auditing, and cross-domain transfer of agent competence.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.29274v1)
