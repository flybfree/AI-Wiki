---
title: One Skill Too Many: How Co-Installed Skills Conflict in Coding Agents
url: http://arxiv.org/abs/2610.11647v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_10-20-47Z_OneSkillTooMany_HowCo_InstalledSkillsConflictinCod.md
generated_at: 2026-10-08 21:07
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents the first empirical study of conflicts that arise when coding agents have multiple similar agent skills co-installed, where the model must choose between them based only on name and description. Through analysis of 20,947 repositories yielding 822,109 candidate similar-skill pairs and 6,368 experimental runs across three models, the authors demonstrate that nearly one in four installed skills conflicts with a similar skill, causing the installed skill to lose exclusive core functions in one out of five runs without any drop in task completion that benchmarks would detect.

## Key Takeaways
- Conflict-prone skills are widespread and structurally embedded: approximately 25% of installed skills are co-installed with a functionally similar skill, and 37% of judged skills reside inside copied collections, indicating that skill duplication is a systemic artifact of how teams, developers, and plugin ecosystems distribute agent capabilities rather than an isolated misconfiguration.
- Substitution silently degrades fidelity: a similar skill takes over one in five runs from the installed skill, and when the similar skill is opened first, the agent loses over a third of the exclusive core functions (such as a ban on touching git) that only the installed skill enforces, yet the task still passes because benchmarks measure only task completion rather than adherence to specific normative constraints.
- The conflict is decided at the very first skill read, almost always before any file is modified, and install location—not listing order—determines which skill the model selects; a pre-tool hook inserted at that first read can restore fidelity to the level seen when the installed skill is opened first, offering a practical mitigation strategy.

## Context
Coding agents increasingly rely on modular skill directories (SKILL.md files) to extend their capabilities, drawing from heterogeneous sources including team repositories, individual developers, plugin marketplaces, and copied collections. This paper addresses a gap in the AI agent evaluation landscape: existing benchmarks such as SWE-bench and similar task-completion suites cannot detect when an agent silently substitutes a conflicting skill and violates a specific normative constraint, meaning the field has been blind to a class of correctness failures that do not manifest as outright task failure.

## Implications
For practitioners deploying coding agents in production, this work argues that benchmarks must score exclusive core functions—specific prohibitions and constraints encoded in individual skills—rather than relying solely on task completion, and that agent platforms should guard the first skill read with pre-tool hooks and surface which skill was actually invoked in the final reply. For the broader AI safety and reliability community, the findings highlight that composability of agent capabilities introduces subtle correctness risks that standard evaluation pipelines miss, calling for new evaluation methodologies and platform-level safeguards as agent ecosystems continue to grow in complexity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11647v1)
