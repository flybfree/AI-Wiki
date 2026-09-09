---
title: Experience Funnel: A State-Policy Alternating Loop for Self-Evolving Agents
url: http://arxiv.org/abs/2609.08919v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-08_15-48-11Z_ExperienceFunnel_AState_PolicyAlternatingLoopforSe.md
generated_at: 2026-09-08 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Experience Funnel, an alternating loop that combines rapid textual state updates with slow policy consolidation for self‑evolving agents. It shows the method outperforms both pure state evolution and internalized policies across benchmarks. The framework continuously converts interactive experience into autonomous competence. The method demonstrates that rapid state updates do not hinder policy generalization, unlike earlier approaches where fast adaptation caused instability.

## Key Takeaways
- Interaction trajectories are distilled into an explicit textual state that can be quickly added and checked for usefulness, allowing rapid adaptation to new tasks.
- Useful behaviors identified in the state are then transferred to the policy via transition‑aware distillation, creating compact parameter updates.
- The loop repeatedly generates fresh rollouts, so each cycle refines both the state representation and the underlying policy. This explicit textual state is generated from each interaction and can be edited by human operators or automated scripts, providing a clear audit trail of what the agent has learned.

## Context
Self‑evolving agents rely on two complementary mechanisms: explicit textual states for fast learning and parametric policies for stable competence. Prior work treats these as separate pipelines that cannot be combined efficiently. This paper bridges that gap by embedding them in a single alternating loop, addressing the tradeoff between speed of adaptation and robustness of policy.

## Implications
Practitioners can adopt Experience Funnel to build agents that learn quickly from new interactions while maintaining long‑term stability, reducing reliance on external context. The approach may lower training costs in large language model deployments where continual improvement is essential.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.08919v1)
