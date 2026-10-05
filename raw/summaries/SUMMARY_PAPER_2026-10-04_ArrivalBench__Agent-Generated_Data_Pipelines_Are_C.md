---
title: ArrivalBench: Agent-Generated Data Pipelines Are Correct Once and Wrong Under Time
url: http://arxiv.org/abs/2610.02363v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-01_18-39-06Z_ArrivalBench_Agent_GeneratedDataPipelinesAreCorrec.md
generated_at: 2026-10-04 22:06
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ArrivalBench introduces a benchmark that evaluates agent-generated data pipelines not by a single execution against a fixed snapshot, but by re-executing them under adversarial yet replayable delivery schedules—including late, duplicated, out-of-order, and retried records—and requiring the final state to match a batch recomputation of the complete log. The central finding is that single-execution grading certifies 86–100% of pipelines produced by eleven models, yet re-executing those same artifacts reveals 7.0–79.2% of the certified pipelines are silently wrong, exposing a fundamental blind spot in current agent evaluation methodology.

## Key Takeaways
- Single-execution grading is dangerously insufficient: across 40 tasks and eleven models, the authors' reimplementation of standard grading certifies 86–100% of agent-produced pipelines, but adversarial replay uncovers silent errors in 7.0–79.2% of those "certified" pipelines. This means the majority of pipelines that pass conventional benchmarks would produce incorrect tables in production under realistic delivery conditions.
- The repair loop does not close the gap. Within the same model and task, pipelines that were repaired against a snapshot test fail replay about as often as pipelines that passed the snapshot test on the first attempt. This indicates that snapshot-based repair does not teach agents the structural invariants needed for robustness under adversarial delivery.
- Idempotency hazards (duplicate and retried records) cause failures more frequently than ordering hazards (out-of-order and late records) across every model tested. Furthermore, distinguishing a wrong table from a crash changes how interventions appear effective: a hazard warning reduced one model's silent failure rate from 48.2% to 10.5% but simultaneously raised its crash rate from 9.0% to 37.0%, so the all-in failure rate moved only from 51.0% to 44.0%. All eleven experimental arms were independently re-run, with rates shifting by at most 5.9 points, confirming statistical stability.

## Context
This paper sits at the intersection of LLM agent evaluation, data engineering, and software reliability testing. Most current agent benchmarks grade a single output against a static ground truth, treating agent-generated code or pipelines as if they execute in a deterministic, single-shot environment. ArrivalBench reframes the problem as a streaming-systems correctness question, borrowing concepts from distributed computing such as idempotency, out-of-order delivery, and crash semantics. By using a recomputation oracle rather than a classification oracle, the benchmark separates two failure modes—silent data corruption versus visible crashes—that existing monitoring infrastructure can already detect, making the evaluation directly actionable for teams deploying agent-generated pipelines in production.

## Implications
For practitioners building agentic data pipelines, this work demonstrates that passing a single-execution benchmark is not evidence of production readiness; teams must test against adversarial delivery schedules before trusting agent-generated code. For the benchmarking and evaluation community, it argues that agent evaluation must incorporate replayable, adversarial execution environments and must distinguish silent correctness failures from crash failures, since interventions that reduce one failure mode may simply shift failures into the other. For industry, the finding that idempotency hazards dominate ordering hazards suggests that agent training and prompting should prioritize deduplication and retry-safety reasoning as a first-class concern rather than an afterthought.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02363v1)
