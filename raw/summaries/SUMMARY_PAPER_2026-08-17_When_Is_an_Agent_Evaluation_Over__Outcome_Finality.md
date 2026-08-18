---
title: When Is an Agent Evaluation Over? Outcome Finality and Cross-Unit Separation
url: http://arxiv.org/abs/2608.14940v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_23-39-47Z_WhenIsanAgentEvaluationOver_OutcomeFinalityandCros.md
generated_at: 2026-08-17 21:41
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper argues that current agent evaluation systems treat each stopped run as a single trial and score it based on the final state, but this interpretation rests on two conditions — outcome finality and cross‑unit separation — that are not guaranteed by the endpoint alone. The authors demonstrate through experiments that delayed outcomes can alter scores while runs share state, and that isolated runs prevent such carryover. They also propose an open‑effects record to capture operations that may persist after a run ends.

## Key Takeaways
- An agent evaluation is only final when there is no possibility for the outcome to change later; otherwise the label remains provisional.
- The endpoint of a stopped run does not automatically guarantee outcome finality because delayed writes can affect subsequent runs if service state persists.
- Cross‑unit separation is essential: runs must be isolated or reset so that the scored outcome cannot influence another trial.

## Context
In AI research, evaluating autonomous agents often relies on stopping a long-running simulation and measuring its result. However, many protocols assume that once a run ends, all relevant information is captured, which can lead to misleading conclusions when operations continue to have effects beyond the stop point.

## Implications
This work highlights a gap in current evaluation practices that could misrepresent agent performance if delayed outcomes are ignored. Practitioners should adopt open‑effects records and ensure outcome finality before treating scores as definitive, improving reliability across industry deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14940v1)
