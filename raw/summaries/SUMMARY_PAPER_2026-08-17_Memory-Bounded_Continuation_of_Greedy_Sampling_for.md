---
title: Memory-Bounded Continuation of Greedy Sampling for Continual Anomaly Detection
url: http://arxiv.org/abs/2608.15277v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_15-19-12Z_Memory_BoundedContinuationofGreedySamplingforConti.md
generated_at: 2026-08-17 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ContCore, a memory‑bound continuation of greedy sampling for continual anomaly detection that maintains a fixed coreset size across sequential tasks. By iteratively applying greedy selection to new data while discarding older points, the method preserves representativeness and achieves a bounded gap between its constructed coreset and the optimal oracle coreset. Empirical results show state‑of‑the‑art performance on multiple task schedules.

## Key Takeaways
- Continual greedy sampling can be made memory‑bound by iteratively applying greedy selection over previously sampled points, which gracefully degrades coreset quality without catastrophic loss.  
- The resulting greedy‑continued coreset approximates the oracle coreset within a theoretical bounded gap, guaranteeing reliable anomaly detection under fixed memory constraints.  
- ContCore constructs new task features via greedy expansion followed by greedy consolidation to enforce the memory budget, unlike neural methods that suffer from forgetting or require unbounded memory.

## Context
Continual learning faces challenges of maintaining performance as new tasks arrive while limiting computational resources. Coreset techniques aim to compress data for efficient downstream modeling, yet most approaches either accumulate indefinitely or lose representativeness over time. This work bridges that gap by providing a principled, bounded‑memory greedy continuation method.

## Implications
Practitioners can deploy anomaly detection pipelines with predictable memory usage and stable performance across tasks. The theoretical guarantees reduce reliance on empirical tuning, making the approach scalable for real‑time systems where resource constraints are critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15277v1)
