---
title: Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification
url: http://arxiv.org/abs/2607.25904v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_16-01-38Z_InteractiveRewardAgent_GUITaskEvaluationviaEnviron.md
generated_at: 2026-07-28 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces an interactive reward agent (IRA) that evaluates GUI task completion by combining visible screenshots with post‑execution environment verification. It proposes a propose‑then‑verify framework and demonstrates high accuracy on a benchmark of 321 tasks across ten Ubuntu desktop categories, achieving 86.9% performance.

## Key Takeaways
- IRA uses both screen evidence and system tools to verify task conditions, moving beyond static screenshot analysis.
- The proposed framework yields an 86.9% accuracy rate on GUI‑RewardBench, surpassing existing evaluators.
- When applied in reinforcement learning, IRA improves OSWorld success rates to 34.0%, showing its utility as a reward signal.

## Context
Automated evaluation of graphical user interface agents is essential for scaling and improving their behavior, yet current methods often rely solely on visual snapshots which can be misleading. This work addresses the gap by integrating environmental state verification into the evaluation loop.

## Implications
The interactive approach can be adopted by developers to create more reliable reward mechanisms for GUI agents, enabling better training outcomes. It also provides a benchmark that encourages community research in automated UI task completion assessment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25904v1)
