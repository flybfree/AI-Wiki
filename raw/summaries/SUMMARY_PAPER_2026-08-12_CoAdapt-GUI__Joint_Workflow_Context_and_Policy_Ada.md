---
title: CoAdapt-GUI: Joint Workflow Context and Policy Adaptation for Unseen GUI Applications
url: http://arxiv.org/abs/2608.11588v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_02-55-50Z_CoAdapt_GUI_JointWorkflowContextandPolicyAdaptatio.md
generated_at: 2026-08-12 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CoAdapt-GUI, a test‑time adaptation framework that jointly adapts the workflow context and policy for unseen GUI applications using only the agent’s own rollouts and rewards. The approach separates transferable procedures from app‑specific details, enabling reusable knowledge to guide adaptation without transferring source‑interface state. On two unseen‑app benchmarks, CoAdapt-GUI improves performance by 7.5 percentage points over a policy‑only baseline.

## Key Takeaways
- The workflow context is constructed to retain transferable procedures and verification rules while discarding app‑bound source information, allowing the adaptation process to focus on reusable knowledge rather than fragile UI specifics.
- Policy adaptation uses task‑context matched group‑relative optimization to update a low‑rank adapter on a frozen vision‑language model, enabling efficient fine‑tuning without full retraining of the model.
- Joint workflow and policy adaptation yields a 7.5% absolute gain in AndroidWorld‑Generalization (45.0% vs 37.5%) and a substantial boost from 38.6% to 52.9% on AndroidWorld Plus.

## Context
The work addresses the brittleness of mobile GUI agents when transferred to applications not seen during training, a common challenge in real‑world deployment where interaction budgets are limited. By leveraging only self‑generated rollouts and rewards, CoAdapt-GUI aligns with broader trends toward efficient test‑time adaptation that minimizes data collection and computational cost.

## Implications
For practitioners developing mobile assistants, this framework offers a practical way to extend agent capabilities across diverse apps without extensive retraining or source access. The industry can adopt the separation of workflow context from policy updates to create more robust, reusable AI agents for heterogeneous user interfaces.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11588v1)
