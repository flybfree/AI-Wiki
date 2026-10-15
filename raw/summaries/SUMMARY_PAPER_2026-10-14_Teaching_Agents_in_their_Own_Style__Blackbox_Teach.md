---
title: Teaching Agents in their Own Style: Blackbox Teacher Distillation for Web Agents
url: http://arxiv.org/abs/2610.19834v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_09-06-49Z_TeachingAgentsintheirOwnStyle_BlackboxTeacherDisti.md
generated_at: 2026-10-14 21:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces WebKD, a novel distillation framework for training open-weight web agents using closed frontier models as black-box teachers. Rather than imitating teacher demonstrations or requiring access to teacher logits, WebKD treats the teacher as an editor of the student's failed episodes, rewriting reasoning traces, harness states, and actions from the first point of mistake onward. The method achieves 5.5–10.7 percentage point improvements over behavior cloning, outcome-reward RL, and teacher editing baselines on the TimeWarp benchmark, with performance transferring to unseen task variants and the live web via OnlineMind2Web.

## Key Takeaways
- WebKD solves the fundamental constraint that token-level teacher distillation is impossible for closed models because they do not expose logits. Instead of requiring full teacher trajectories, the teacher only edits the student's own failed episodes starting from the first mistake, making the approach compatible with black-box API access to frontier models.
- The method introduces a "minimal editing" principle in both data space and objective space. In data space, the teacher rewrites corrections in the student's own writing style to avoid distribution shift. In objective space, reasoning tokens are weighted by their contribution to the final action, and a role-asymmetric KL anchor keeps reasoning anchored to the student's prior while allowing the corrected action to move freely. This prevents the student from being overwhelmed by a teacher's foreign reasoning style.
- Performance gains of 5.5–10.7 percentage points over multiple baselines demonstrate that editing-based distillation outperforms imitation-based approaches. Crucially, the improvements generalize to unseen task versions and to the live web environment, indicating the learned corrections capture transferable web navigation strategies rather than memorized episode-specific patterns.

## Context
This work sits at the intersection of model distillation, web agent training, and the growing practical need to deploy capable agents without paying frontier-model inference costs. As closed models dominate the frontier while open-weight models remain the only viable option for on-premise or cost-sensitive deployments, the community has lacked a principled way to transfer capabilities from closed teachers to open students. Prior approaches either required logit access (impossible for closed models) or relied on offline imitation that trains students on state distributions they never encounter during their own rollouts, creating a train-test mismatch. WebKD reframes distillation as targeted correction editing, aligning with broader trends in reinforcement learning from human feedback and self-improvement loops where a model learns from its own failures rather than from external demonstrations.

## Implications
For practitioners building web agents in production, WebKD offers a practical recipe: deploy a small open model, run it on real tasks, and use a closed frontier model as a post-hoc editor of failures to generate training data that stays in-distribution for the student. This reduces the need for expensive human annotation or full teacher rollouts while still leveraging frontier capabilities. For the broader research community, the paper validates that distillation need not require white-box access to teacher internals, opening a pathway for iterative self-improvement pipelines where open models progressively close the gap with closed ones through structured editing rather than wholesale imitation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19834v1)
