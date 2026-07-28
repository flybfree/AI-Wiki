---
title: Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair
url: http://arxiv.org/abs/2607.24604v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_16-05-23Z_LoopingIsNotReliability_State_BoundEvidenceandType.md
generated_at: 2026-07-27 23:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why looping in agentic code repair can degrade reliability despite correctness, presenting evidence from a five-seed study on 30 HumanEval repairs. It shows that forced revision reduces overall correctness while ever-correct improves, and stale traces cause significant harm to correct starts. The authors propose a typed loop contract that binds verification evidence to exact states.

## Key Takeaways
- Forced revision drops correctness from 0.820 after one revision to 0.673 after two revisions, indicating loops amplify errors.
- Stale traces increase the proportion of correct starts harmed by 22.2 points (from 4/135 to 34/135) with high confidence.
- The proposed typed loop contract separates admission, preservation, certification, competence, and liveness into a mechanically enforceable specification.

## Context
Agentic code repair relies on loops that generate patches but does not guarantee reliability. Current systems treat correctness as a single metric, ignoring how repeated revisions interact with trace states to affect outcomes. This study bridges the gap between empirical observations and formal guarantees.

## Implications
For practitioners, the findings warn against assuming loop repetitions preserve quality and suggest adopting state-bound contracts for auditable repair processes. For industry, this could lead to more robust tooling that enforces evidence binding rather than relying on statistical correctness alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24604v1)
