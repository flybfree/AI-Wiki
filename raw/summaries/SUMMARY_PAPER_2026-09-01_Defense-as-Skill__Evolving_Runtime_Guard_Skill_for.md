---
title: Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents
url: http://arxiv.org/abs/2609.01487v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_16-19-31Z_Defense_as_Skill_EvolvingRuntimeGuardSkillforSkill.md
generated_at: 2026-09-01 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Defense-as-Skill, a framework that treats runtime guards as installable skills to protect skill‑augmented agents from malicious behavior. The authors evaluate the evolving guard SkillSonar on the SCOPE-R dataset and show it reduces attack success rates dramatically while preserving safety‑utility balance.

## Key Takeaways
- SkillSonar runs alongside untrusted tasks, inspecting actions against task boundaries without altering the agent runtime.
- Runtime guard evolution via Monte‑Carlo Tree Search improves detection of malicious skill usage across 21 sub‑categories.
- The evolved guard cuts ID ASR from 0.482 to 0.104 and OOD ASR from 0.606 to 0.115, demonstrating strong transfer across models.

## Context
Skill‑augmented agents are increasingly common in AI systems where developers can load reusable functions at runtime, but this flexibility creates a persistent attack surface that traditional pre‑install vetting cannot fully mitigate. This work addresses the gap between static security checks and dynamic, task‑aware defenses.

## Implications
For practitioners deploying skill‑based assistants, integrating Defense-as-Skill offers a practical way to enforce safety without rewriting core code. The approach could become standard in AI platforms that rely on modular runtime skills, raising the overall security posture of such systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01487v1)
