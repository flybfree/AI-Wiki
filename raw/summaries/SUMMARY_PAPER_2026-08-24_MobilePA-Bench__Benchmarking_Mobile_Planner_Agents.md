---
title: MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks
url: http://arxiv.org/abs/2608.23035v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_09-38-24Z_MobilePA_Bench_BenchmarkingMobilePlannerAgentsonCo.md
generated_at: 2026-08-24 21:07
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces MobilePA‑Bench, a benchmark that tests mobile planning agents on complex real‑world tasks by evaluating tool‑calling and long‑horizon planning. Experiments reveal that current frontier LLMs struggle with strict ordering, permission limits, and runtime errors. The benchmark spans 13 domains and 212 tools.

## Key Takeaways  
- MobilePA‑Bench emphasizes stateful interaction and structured feedback, unlike static function‑calling benchmarks.  
- It assesses sub‑agent collaboration, memory usage, and skill reuse as core capabilities.  
- Frontier LLMs show sharp performance drops under runtime constraints such as tool ordering and permission limits.

## Context  
Mobile planning agents are moving from research prototypes to on‑device assistants that must interact with live applications. Existing benchmarks either focus only on UI manipulation or rely on offline API matching, creating gaps in realistic evaluation.

## Implications  
For developers, MobilePA‑Bench provides a diagnostic framework to identify failure modes early. For researchers, it offers an interactive foundation for reinforcement learning that can accelerate reliable mobile agent deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23035v1)
