---
title: AUSO: Action-Level Unified Skill Optimization from Internalization to Utilization
url: http://arxiv.org/abs/2608.21292v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_16-53-27Z_AUSO_Action_LevelUnifiedSkillOptimizationfromInter.md
generated_at: 2026-08-23 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes AUSO, an action-level unified skill optimization framework that integrates skill learning and utilization within a single reinforcement‑learning process. It replaces fragmented approaches by progressively internalizing skills while preserving task feedback, leading to better performance on benchmark tasks. The framework demonstrates consistent gains across diverse domains, highlighting its robustness.

## Key Takeaways
- Early training jointly uses teacher guidance and environment rewards to let the policy acquire foundational skills without discarding task‑oriented signals.
- Later stages emphasize outcome‑based optimization, consolidating autonomous problem solving while still allowing skill‑conditioned actions to be evaluated.
- Each action is compared in both skill‑present and skill‑absent contexts, creating an action‑level signal that updates only when the skill improves decision quality.

## Context
This work addresses a longstanding gap in reinforcement learning where skills are treated as static external modules rather than integrated components of policy evolution. By unifying internalization and utilization, AUSO aligns with modern efforts to make agents more adaptable and less brittle. Such integration reduces the risk of skill misalignment that can degrade performance on unseen tasks.

## Implications
For practitioners, AUSO offers a practical method to embed skill‑specific knowledge directly into learned policies, reducing the need for separate supervision systems. It also suggests that future RL frameworks should treat skills as dynamic resources rather than static assets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21292v1)
