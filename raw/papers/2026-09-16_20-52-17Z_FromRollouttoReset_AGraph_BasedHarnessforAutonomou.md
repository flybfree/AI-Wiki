---
title: From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation
published: 2026-09-16T20:52:17Z
authors: Jing Jiang, Yue Yang, Xinkai Jiang, Gedas Bertasius, Daniel J. Szafir, Rudolf Lioutikov
url: http://arxiv.org/abs/2609.19413v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation

## Abstract
Robot manipulation policies are improving quickly, and real-robot evaluation remains the standard evidence for that progress. It still relies on a human to reset the scene between rollouts, which consumes operator time and leaves the initial state distribution unspecified, so results reproduce poorly. A recent system, AutoEval, automates both reset and scoring, but only for single-step tasks, because a long-horizon rollout can terminate in combinatorially many configurations that no single learned reset policy covers. We present HALTER, a Harness for Autonomous Long-horizon Task Evaluation and Reset, which restores the scene by planning over a library of learned atomic reset skills, so demonstration cost scales with the size of that library rather than with the number of terminal states. HALTER builds a spatial scene graph online from point clouds and vision foundation models, and an LLM reasons over this graph to score the rollout, plan the reset, and verify that the reset succeeded, without collecting labeled success images for any task. On four long-horizon tasks on a Franka arm, HALTER restores the scene in 76% of episodes, against 52% for AutoEval and 65% for a motion-planning reset, and it estimates the completed-skill fraction correctly in 90% of episodes, against 76%. Its reset-verification verdict is correct in 91% of episodes, compared with 78% for AutoEval. It also cuts the operator time of an evaluation campaign by 72% relative to manual reset. We further measure compositional generalization on three held-out tasks, where HALTER resets 74.7% of episodes against 1.3% for a per-task reset policy, and we ablate the scene representation and the graph update rate.

## Metadata
- **Published**: 2026-09-16T20:52:17Z
- **Authors**: Jing Jiang, Yue Yang, Xinkai Jiang, Gedas Bertasius, Daniel J. Szafir, Rudolf Lioutikov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19413v1)