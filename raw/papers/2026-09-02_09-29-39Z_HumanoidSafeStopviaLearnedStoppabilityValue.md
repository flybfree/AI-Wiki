---
title: Humanoid Safe Stop via Learned Stoppability Value
published: 2026-09-02T09:29:39Z
authors: Junfeng Long, Pieter Abbeel, Koushil Sreenath, Roberto Horowitz, Guanya Shi, C. Karen Liu
url: http://arxiv.org/abs/2609.02358v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Humanoid Safe Stop via Learned Stoppability Value

## Abstract
Humanoid robots responding to emergency stop commands typically execute a fixed maneuver, without reasoning about whether a safe stop is actually feasible from the current state. We cast emergency stopping as a reach-avoid problem and propose Safe-Stop, a task-agnostic framework that pairs a learned stop policy with learned stoppability estimators. The estimators are complementary: a stop-probability estimator supervised by the actual outcomes of the fixed stop policy, and a reach-avoidance estimator supervised by a Hamilton-Jacobi backup over physical state. The first captures emergent stopping behavior of the learned controller; the second provides a complementary recoverability signal. Because the stop policy and estimators do not depend on the behavior policy that preceded the stop command, they transfer across diverse upstream tasks without retraining. At deployment, the two estimates are combined: Safe-Stop commits to the stop only when both estimators indicate that stopping remains feasible, otherwise it hands off to a fall policy, instantiated as a damping fallback. This agreement check yields decisions that are robust without sacrificing reactivity.

## Metadata
- **Published**: 2026-09-02T09:29:39Z
- **Authors**: Junfeng Long, Pieter Abbeel, Koushil Sreenath, Roberto Horowitz, Guanya Shi, C. Karen Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02358v1)