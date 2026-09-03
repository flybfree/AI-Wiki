---
title: Humanoid Safe Stop via Learned Stoppability Value
url: http://arxiv.org/abs/2609.02358v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_09-29-39Z_HumanoidSafeStopviaLearnedStoppabilityValue.md
generated_at: 2026-09-02 20:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Safe-Stop, a task‑agnostic framework that enables humanoid robots to decide whether an emergency stop is feasible by combining two learned estimators. The first estimator predicts the likelihood of stopping based on actual outcomes, while the second uses a Hamilton‑Jacobi backup to gauge reachability. When both indicators agree, the robot performs a safe stop; otherwise it deploys a damping fallback.

## Key Takeaways
- A stop‑probability estimator is trained on real stop results, capturing emergent stopping behavior of the learned controller.
- A reach‑avoidance estimator is derived from a Hamilton‑Jacobi backup over physical state, providing a recoverability signal independent of prior policies.
- The two estimators are combined at deployment to commit to a stop only when both indicate feasibility, otherwise a fallback damping policy is used.

## Context
The work addresses the challenge of safe robot control where fixed stop maneuvers ignore current system dynamics. By learning complementary signals that transfer across diverse upstream tasks, Safe-Stop offers a flexible solution without retraining for each new behavior policy.

## Implications
For industry and practitioners, this approach improves safety by making emergency stops context‑aware while preserving rapid response. It reduces the risk of unsafe halts or unnecessary interventions, supporting broader adoption of autonomous humanoid robots in real‑world environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02358v1)
