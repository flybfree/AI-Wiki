---
title: Partial Routing: Trace-Tuned Delegation for Resource-Efficient Agentic Workflows
url: http://arxiv.org/abs/2611.33402v1
type: paper-summary
date: 2026-11-26
source_paper: 2026-11-24_20-23-53Z_PartialRouting_Trace_TunedDelegationforResource_Ef.md
generated_at: 2026-11-26 21:58
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces partial routing, a method for resource-efficient agentic workflows in which a frontier "lead" model is guided to delegate suitable subtasks to a cheaper "worker" model rather than committing the whole task to one model. By mining recurring subtasks from both models' past runs and measuring each model's quality and cost on those subtasks, the method produces delegation guidance controlled by a parameter δ. On held-out ViBench and Terminal-Bench 4.0 tasks, partial routing improves mean task performance over the lead alone and over task-level routing, without training either model.

## Key Takeaways
- A single agentic task usually mixes easy and difficult subtasks, so choosing one model for the entire task is inefficient; partial routing instead lets the lead decide when and what to delegate during execution.
- The guidance is derived from past runs: recurring subtasks are identified, and each model's quality and cost on those subtasks are measured, yielding a tunable delegation policy via δ.
- With δ = 0.75, the lead's ViBench score rises from 70.2 to 78.5 at 19% lower cost, and its Terminal-Bench pass rate rises from 54% to 61% at similar cost; even giving the lead only the subtask breakdown, without a worker, reduces cost on both benchmarks and raises the Terminal-Bench pass rate.

## Context
AI models differ widely in capability and price, and existing model routing exploits this by sending easier tasks to cheaper models. Agentic workloads complicate that picture because one task can contain a heterogeneous mix of subtasks, so a coarse task-level choice wastes either capability or budget. This paper addresses that gap by treating delegation as a subtask-level decision informed by trace-like evidence from prior runs.

## Implications
The results suggest that analysis of past runs can support more efficient planning and more effective delegation with little cost and implementation overhead, making partial routing a practical option for deploying frontier models in agentic pipelines. For practitioners, it offers a way to raise benchmark performance while lowering or holding cost, and even the breakdown-only variant shows that subtask awareness alone can improve efficiency. This points toward trace-informed routing as a lightweight complement to, rather than a replacement for, model training or task-level routing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.33402v1)
