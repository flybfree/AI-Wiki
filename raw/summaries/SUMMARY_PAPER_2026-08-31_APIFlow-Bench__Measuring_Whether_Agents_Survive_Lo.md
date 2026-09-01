---
title: APIFlow-Bench: Measuring Whether Agents Survive Long, Dependent API Workflows
url: http://arxiv.org/abs/2608.29128v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_08-12-11Z_APIFlow_Bench_MeasuringWhetherAgentsSurviveLong_De.md
generated_at: 2026-08-31 20:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
Tool-using agents are evaluated by whether an end-to-end workflow succeeds, but this binary metric overlooks production-relevant failures. APIFlow-Bench introduces a benchmark that measures seven engineering capabilities and tracks the actual call path of REST-API workflows. Across 19 models we find success drops from 93% on single subtasks to 74% on long chains and 61% when including flagged trials.

## Key Takeaways
- Longer dependency chains reduce overall success rates, dropping from 93% on individual subtasks to 74% on a clean 20-subtask chain and further to 61% when including the 8% of trials that no model can pass. - Reliability varies widely across models: best-of-five spans seven points, while all‑five reliability spans 44 points, showing that consistency is far more important than peak performance. - The observed pass rates exceed what would be expected from independent error accumulation; on the clean slice 77% of failing runs reach the correct final state but fail only at delivery.

## Context
The paper addresses a gap in evaluating AI agents beyond simple success/failure metrics, highlighting that long‑horizon workflows involve subtle failures such as expired credentials or malformed payloads. By providing auditable, provenance‑sensitive benchmarks, it supports more reliable model comparison and system design.

## Implications
For practitioners, APIFlow-Bench offers a concrete way to quantify agent reliability in production‑like environments, guiding improvements in state management and error handling. For the field, it pushes research toward holistic performance metrics rather than single‑point success rates.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29128v1)
