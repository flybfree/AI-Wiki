---
title: Continue or Replan? Bernoulli-Continuation Policy Learning for Adaptive Horizon Execution
url: http://arxiv.org/abs/2608.03483v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_11-21-08Z_ContinueorReplan_Bernoulli_ContinuationPolicyLearn.md
generated_at: 2026-08-05 01:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Bernoulli‑Continuation Policy (BCP), a lightweight reinforcement‑learning framework that lets VLA models decide whether to continue an action chunk or replan based on task progress. By training a continuation head with a Replanning‑Efficiency Reward, BCP adapts the execution horizon without freezing the base policy. The method lifts success rates by 11.08% on low‑success tasks and improves overall performance from 74% to 92% on real robots.

## Key Takeaways
- BCP adds a continue‑or‑replan decision head that imposes an ordinal, prefix‑sharing inductive bias over candidate horizons rather than treating them as independent classes.  
- The head is trained with reinforcement learning using a Replanning‑Efficiency Reward that jointly rewards task success and efficient VLA usage, preventing the policy from collapsing to unnecessarily short horizons.  
- BCP generalizes to the Randomized setting and transfers well to other base policies such as π0.5, achieving +6.8% on LIBERO‑PRO.

## Context
Fixed‑horizon chunk execution in vision‑language‑action systems often forces replanning at arbitrary times, which can miss critical manipulation stages. This paper’s approach makes horizon selection adaptive through reinforcement learning, aligning policy decisions with task progress without requiring major architectural changes to existing VLA models.

## Implications
BCP provides a plug‑and‑play solution that can be integrated into current VLA pipelines, reducing overhead while boosting success rates across diverse tasks. It highlights the value of context‑aware, dynamic planning in robotic AI and encourages developers to prioritize adaptive horizon management over static schedules.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03483v1)
