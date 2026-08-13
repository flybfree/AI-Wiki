---
title: Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents
url: http://arxiv.org/abs/2608.11888v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_10-15-19Z_AgentSkillsCanBeHarmful_AnEmpiricalStudyofSkill_In.md
generated_at: 2026-08-12 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how skills attached to large language model agents can cause failures or increase computational costs. By analyzing paired runs with and without skills on benchmark datasets, the authors identify 307 skill‑induced incidents, including functional breakdowns and efficiency regressions. They also introduce SkillTriage, a tool that attributes these issues to specific skills.

## Key Takeaways
- Skill induced functional failures are rarely caused by obviously irrelevant skills; instead, seemingly relevant skills often make the agent incorrectly implement or omit task‑required elements.
- Skill‑induced efficiency regressions are not explained solely by prompt length; they stem from excessive verification and heavy implementation pipelines that consume many tokens.
- The largest contributors to these problems within the Excessive Procedure category are excessive verification (67 cases) and heavy implementation pipelines (30 cases), showing that validation checklists and construction recipes can become mandatory work.

## Context
The study highlights a growing reliance on skill‑based prompting for LLM agents, which promises modularity but introduces hidden risks. As organizations adopt more complex agent workflows, understanding the impact of each skill is crucial for reliable deployment.

## Implications
Researchers should develop safer skill reuse frameworks that prevent unintended functional errors and cost spikes. Practitioners must evaluate skills not only by their intended purpose but also by their side effects on task execution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11888v1)
