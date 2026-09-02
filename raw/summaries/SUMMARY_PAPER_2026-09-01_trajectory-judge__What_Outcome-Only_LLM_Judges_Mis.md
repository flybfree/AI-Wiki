---
title: trajectory-judge: What Outcome-Only LLM Judges Miss on Agent Trajectories
url: http://arxiv.org/abs/2609.00038v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-29_10-14-05Z_trajectory_judge_WhatOutcome_OnlyLLMJudgesMissonAg.md
generated_at: 2026-09-01 22:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper examines the limitations of outcome‑only LLM judges when assessing agent trajectories by constructing a deterministic support‑desk environment with a scripted oracle and a fault injector. It evaluates five different judging methods over four hundred trajectories and shows that while loud faults are caught at high rates, silent ones are missed and correct trajectories are flagged unnecessarily.

## Key Takeaways
- Outcome‑only judges detect 84% of loud faults but only 45% of silent faults, revealing a blind spot to non‑visible errors.  
- The step‑rubric judge achieves 77% recall for silent faults with zero false alarms despite three times the cost.  
- Invented promises appended to perfect trajectories evade both rule‑based and self‑consistency judges, showing that final output can be used as a cheat code.

## Context
This work highlights a persistent gap in LLM evaluation where agents are judged solely on end results rather than process quality, undermining trust in automated decision‑making systems. The findings underscore the need for richer metrics that consider intermediate steps and error visibility.

## Implications
Practitioners must move beyond outcome‑only scoring to incorporate step‑level analysis to ensure reliability and cost efficiency. Offline reconstruction of all verdicts will enable systematic auditing and improve agent design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00038v1)
