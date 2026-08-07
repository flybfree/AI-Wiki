---
title: When Privileged Guidance Misaligns: State-Matched Routing and Contextualized Self-Distillation for Multi-Turn Agents
url: http://arxiv.org/abs/2608.05219v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_10-50-46Z_WhenPrivilegedGuidanceMisaligns_State_MatchedRouti.md
generated_at: 2026-08-06 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces State-Matched Routing and Contextualized Self-Distillation (SMRC-SD) to align privileged guidance with the student agent's current execution state, improving multi-turn agent performance. On ALFWorld and WebShop it raises task success from 0.746 to 0.865 on ALFWorld and from 0.574 to 0.693 on WebShop using Qwen3-1.7B.

## Key Takeaways
- SMRC-SD only applies privileged distillation when the student's execution state matches a supported state along the reference trajectory, preventing state-reference mismatch.
- The method constructs state-conditioned teacher context from successful trajectories, ensuring supervision is grounded in the actual reached state.
- Ablations show that both locally supported turn selection and state-compatible teacher context are key contributors to performance gains.

## Context
This work addresses a fundamental challenge in multi-turn agent training where privileged data becomes stale due to dynamic execution paths, highlighting the need for context-aware guidance mechanisms. It contributes to more robust self-distillation strategies beyond simple full-path matching.

## Implications
Practitioners can adopt SMRC-SD to improve agent reliability in interactive settings without sacrificing supervision efficiency, leading to higher task success rates and better deployment outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05219v1)
