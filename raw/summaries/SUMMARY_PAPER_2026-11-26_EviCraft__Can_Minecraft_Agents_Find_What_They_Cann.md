---
title: EviCraft: Can Minecraft Agents Find What They Cannot See?
url: http://arxiv.org/abs/2611.32765v1
type: paper-summary
date: 2026-11-26
source_paper: 2026-11-24_15-03-47Z_EviCraft_CanMinecraftAgentsFindWhatTheyCannotSee.md
generated_at: 2026-11-26 21:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
EviCraft formalizes "evidence closure" for embodied agents in Minecraft: every decision of an agent system, including those inside its tools, may depend on the world only through facts for which the agent holds evidence. It introduces a runtime and benchmark that enforces this closure below the agent and treats the admission rule as an experimental variable, comparing a perception-grounded regime (G), which admits only line-of-sight or self-action-returned facts, against a loaded-state regime (L), which reproduces standard tool stacks, with agents, tools, and worlds held fixed. The central finding is that the regime effect is larger than the strongest agent's lead, so reported scores can overstate genuine search ability.

## Key Takeaways
- Standard semantic tools such as mineBlock select targets from the simulator's loaded world state without a visibility test, meaning a buried ore the agent has never seen is one call away; as a result, scores cannot show whether the agent actually searched.
- On Survival, under G three mid-sized agents reach the diamond in 32%-40% of runs, versus 76%-94% under L, and the strongest agent under G scores below each of those mid-sized agents under L, showing that the admission rule matters more than agent choice.
- In two models, removing only the line-of-sight test closes 93%-96% of the score gap, and loading state only inside tools recovers 70%-98%, so safeguards on observations and queries leave most of the leak open; in open-ended acquisition, the gain from L concentrates in items that depend on buried resources or mobs.

## Context
Minecraft is a common testbed for embodied agents, but many tool stacks quietly bypass perception by reading the simulator's loaded world state rather than what the agent can observe. This creates a gap between reported benchmark performance and the ability to find things the agent cannot see, which matters for evaluating whether agents reason from evidence or merely exploit privileged simulator information. EviCraft addresses this by making the admission rule an explicit experimental variable while holding agents, tools, and worlds fixed.

## Implications
For researchers, the results imply that Minecraft scores should be reported alongside the admission regime, since gains from stronger agents can be smaller than gains from changing what tools are allowed to see. For practitioners building embodied agents, the work suggests that observation and query safeguards are insufficient and that closure must be enforced below the agent, inside tools, to avoid leakage from loaded world state. The open-source runtime and benchmark provide a reusable way to test whether agents genuinely search for buried resources and mobs rather than exploiting simulator-side state.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.32765v1)
