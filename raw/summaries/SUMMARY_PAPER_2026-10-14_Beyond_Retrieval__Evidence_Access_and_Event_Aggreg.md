---
title: Beyond Retrieval: Evidence Access and Event Aggregation in Agent Memory
url: http://arxiv.org/abs/2610.19474v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_02-53-17Z_BeyondRetrieval_EvidenceAccessandEventAggregationi.md
generated_at: 2026-10-14 21:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper addresses a critical gap in agent memory systems: answering questions about an agent's history often requires aggregating events across multiple interactions, a task that standard retrieval-based memory cannot adequately handle. The authors propose two complementary architectures—Trajectory Memory (TM), which preserves original trajectories and constructs source-addressable reading views, and TallyMem, which augments this with a reusable event ledger, model-generated event specifications, and deterministic execution. Experiments on MINTEval and AMA-Bench benchmarks demonstrate that executable aggregation yields substantial gains (up to 13.8 points) on event-combination tasks, though benefits are highly dependent on task structure and the quality of event specifications.

## Key Takeaways
- TallyMem raises Qwen3-32B exact match from 35.2% to 49.0% on 776 questions from 99 held-out MINTEval repositories, representing a 13.8-point improvement over Trajectory Memory alone, with consistent gains of 12.8–13.9 points across three different reader models, demonstrating that the benefit is not model-specific but architectural.
- A controlled probe using event sets parsed independently from raw logs shows an 11.0-point gain (82.8% to 93.8%) without any routing mechanism, isolating the contribution of structured event aggregation from retrieval routing, while on the full AMA-Bench the routed system yields only a 1.3-point gain (69.8% to 71.1%), revealing that routing overhead can dilute aggregation benefits on broader tasks.
- Event specification quality is identified as the largest residual system-error category in the authors' diagnostic analysis, meaning that the model-generated event specifications feeding the deterministic execution engine represent the primary bottleneck, and gains are contingent on how well events are extracted and structured from raw agent trajectories.

## Context
Agent memory systems have increasingly relied on retrieval-augmented approaches, where past interactions are stored and fetched via embedding similarity or keyword search. This paper challenges the sufficiency of retrieval by demonstrating that many realistic agent queries—such as counting occurrences, tracking state changes, or combining information across sessions—require computational aggregation rather than mere document retrieval. This work sits at the intersection of agent architectures, memory design, and program synthesis, pushing the field toward hybrid systems that combine neural retrieval with deterministic symbolic execution.

## Implications
For practitioners building long-running autonomous agents, this research signals that retrieval-only memory architectures will systematically fail on aggregation-heavy queries, and that incorporating structured event ledgers with deterministic execution engines can close a meaningful accuracy gap. The task-dependence of gains and the identification of event specification as the dominant error source suggest that future work should prioritize robust event extraction pipelines and task-aware routing rather than uniform aggregation across all query types, guiding both academic research and production agent system design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19474v1)
