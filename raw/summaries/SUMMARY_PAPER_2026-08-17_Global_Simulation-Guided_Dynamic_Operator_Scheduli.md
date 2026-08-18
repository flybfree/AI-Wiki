---
title: Global Simulation-Guided Dynamic Operator Scheduling for Efficient Multi-Tenant Model Serving
url: http://arxiv.org/abs/2608.15762v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_14-31-56Z_GlobalSimulation_GuidedDynamicOperatorSchedulingfo.md
generated_at: 2026-08-17 21:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SliceScheduler, a dynamic operator‑level scheduling system designed to improve GPU utilization in multi‑tenant model serving. By exposing cluster‑wide execution state through the Global Mapping Graph (GMG) and using simulation‑based reasoning, SliceScheduler reallocates short‑lived idle slices within containers without violating SLAs. The approach achieves token throughput gains of 1.10–2.29× while keeping SLA violations under 9%.

## Key Takeaways
- SliceScheduler builds a Global Mapping Graph that unifies operator dependencies, tensor shapes, resource mappings and execution states to provide real‑time cluster awareness.
- A global simulator predicts how candidate placements affect memory usage and execution timing, enabling what‑if reasoning before committing resources.
- The incremental scheduling module selects placements that exploit fragmented idle slices while preventing memory violations and respecting SLA constraints.

## Context
AI model serving faces a bottleneck where containers often leave short‑lived GPU slices unused because of the heavy cost of moving entire containers. Traditional operator‑level schedulers struggle to balance dependencies, safety and real‑time performance under strict SLAs, limiting overall GPU efficiency in multi‑tenant environments.

## Implications
This work demonstrates that operator‑level scheduling can be both practical and effective for large language model serving, offering a scalable way to squeeze out additional throughput. Practitioners can adopt SliceScheduler’s simulation‑driven framework to reduce idle GPU time and improve cost efficiency without sacrificing service quality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15762v1)
