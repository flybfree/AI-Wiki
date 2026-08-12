---
title: Scheduling Mixed RL Rollouts Beyond Prefix Locality
url: http://arxiv.org/abs/2608.11152v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_17-10-50Z_SchedulingMixedRLRolloutsBeyondPrefixLocality.md
generated_at: 2026-08-11 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MISA‑T, a routing‑layer admission policy designed to schedule heterogeneous reinforcement learning rollouts that share an asynchronous inference service. Experiments on Step3.7 and Qwen3.6-35B-A3B show that MISA‑T boosts rollout throughput by 53.3% and 43.6% respectively, while keeping prefix‑cache hit rates high and preserving the workload mixture set by the trainer.

## Key Takeaways
- Adaptive session admission dynamically decides which rollouts to accept based on current demand, preventing overload of KV‑cache resources.
- Workload‑aware KV‑capacity allocation assigns more cache slots to sessions with longer residency times or higher priority, balancing fairness and efficiency.
- Residency‑time‑aware KV accounting tracks how long each sequence occupies the cache, enabling precise budgeting that reduces mean iteration time by 22.8% in matched experiments.

## Context
Large language model inference increasingly serves mixed reinforcement learning tasks such as RLVR, RLHF, and agentic rollouts simultaneously. As these sessions have varying interaction patterns and KV‑residency durations, naïve scheduling cannot efficiently share the limited cache, leading to bottlenecks that limit overall throughput and degrade user experience.

## Implications
For practitioners deploying large‑scale LLM services, MISA‑T offers a practical way to maximize resource utilization without sacrificing task quality. The approach can be integrated into existing routing layers, delivering measurable gains in speed and cost efficiency for both research prototypes and production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11152v1)
