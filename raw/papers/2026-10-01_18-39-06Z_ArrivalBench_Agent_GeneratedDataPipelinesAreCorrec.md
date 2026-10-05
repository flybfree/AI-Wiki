---
title: ArrivalBench: Agent-Generated Data Pipelines Are Correct Once and Wrong Under Time
published: 2026-10-01T18:39:06Z
authors: Pranay Kothari
url: http://arxiv.org/abs/2610.02363v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ArrivalBench: Agent-Generated Data Pipelines Are Correct Once and Wrong Under Time

## Abstract
Benchmarks for agent-generated data work grade a pipeline by running it once against a fixed snapshot. ArrivalBench instead re-executes the pipeline an agent leaves behind under adversarial but replayable delivery schedules (late, duplicated, out-of-order and retried records) and requires its final state to equal a batch recomputation of the complete log. Because the oracle recomputes rather than classifies, a wrong table and a crash are distinct verdicts: a crash is visible to monitoring a team already runs, and a wrong table is not. On 40 tasks we built, our reimplementation of single-execution grading certifies 86-100% of the pipelines eleven models produce; re-executing the same artifacts finds 7.0-79.2% of the certified ones silently wrong. The gap is not produced by the repair loop: within the same model and task, pipelines repaired against the snapshot test fail replay about as often as those that passed it first time. In every model, idempotency hazards fail more often than ordering hazards. Separating a wrong answer from a crash also changes how interventions read: a hazard warning cuts one model's silent failure from 48.2% to 10.5% while raising its crash rate from 9.0% to 37.0%, so all-in failure moves only from 51.0% to 44.0%. All eleven arms were independently re-run, and rates moved by at most 5.9 points.

## Metadata
- **Published**: 2026-10-01T18:39:06Z
- **Authors**: Pranay Kothari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02363v1)