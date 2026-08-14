---
title: Diagnosing JEPA World Models with Action-Conditioned Predictive Consistency
url: http://arxiv.org/abs/2608.12939v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_08-18-41Z_DiagnosingJEPAWorldModelswithAction_ConditionedPre.md
generated_at: 2026-08-13 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Action-Conditioned Predictive Consistency (ACPC) as a diagnostic for Joint-embedding predictive architectures to assess how visual perturbations affect world model predictions and planner costs. It defines invariance radius and separation rate measures that quantify rollout divergence between clean and perturbed histories under identical actions, proving they bound error and cost changes. Experiments on four tasks show ACPC reliably predicts perturbation impacts across diverse models.

## Key Takeaways
- ACPC captures the requirement of bisimulation by measuring how clean and visually perturbed observations diverge after a common action sequence.
- The invariance radius quantifies the spread of rollout outcomes, bounding multi-step prediction error induced by visual noise.
- The separation rate evaluates whether distinct states remain distinguishable post‑rollout, indicating robustness to perturbations.

## Context
Joint‑embedding models aim to compress world representations while maintaining predictive power, yet they often ignore how appearance changes propagate through action pipelines. ACPC provides a principled way to evaluate this hidden dependency, aligning with the field’s push for transparent and robust control systems.

## Implications
For practitioners developing visual AI agents, ACPC offers an automated diagnostic that can guide model design before deployment. By quantifying perturbation sensitivity, it enables safer integration of perception into planning pipelines across industries such as robotics and autonomous navigation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12939v1)
