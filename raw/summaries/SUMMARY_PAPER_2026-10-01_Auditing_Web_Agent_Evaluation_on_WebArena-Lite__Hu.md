---
title: Auditing Web Agent Evaluation on WebArena-Lite: Human Review of Outcomes and Trajectories
url: http://arxiv.org/abs/2610.01491v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-10-01_11-31-37Z_AuditingWebAgentEvaluationonWebArena_Lite_HumanRev.md
generated_at: 2026-10-01 22:00
model: qwen3.6-35b-a3b
---

## Summary
This paper audits the evaluation of web agents on WebArena-Lite by conducting human reviews of both final outcomes and detailed interaction trajectories. The researchers demonstrate that automated evaluators frequently misclassify task success, missing between 5.45 to 8.49 percentage points of actual completions. By analyzing step-level progress and testing memory-augmented mechanisms alongside procedural guidance, the study reveals that endpoint scoring alone provides a fundamentally incomplete picture of agent performance.

## Key Takeaways
- Human trajectory analysis recovers substantial success rates missed by automated evaluators while exposing recurring failure patterns such as infinite scrolling loops, premature answers, invalid actions, and incomplete form submissions across 102 failed GPT-5.5 runs.
- Integrating the Memory and Analysis Support Mechanism with task-specific Guide Text significantly improves corrected success rates, boosting performance from 34.55% to 38.18% for advanced models and from 13.90% to 18.80% for untrained architectures under a strict step budget.
- Step-level evidence consistently shows that agents can achieve substantial early progress yet still fail at the final stage, proving that binary outcome metrics obscure critical behavioral nuances and decision-making breakdowns during complex web navigation.

## Context
As large language models increasingly power autonomous web automation, benchmarking frameworks have struggled to capture the full complexity of multi-step digital interactions. Most current evaluation protocols rely on rigid rule-based checks or black-box LLM scorers that only inspect final states, ignoring the procedural logic required for reliable task execution. This research directly addresses a critical

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.01491v1)
