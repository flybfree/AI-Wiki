---
title: SAT-Edge-Agent: Hardware-in-the-Loop Edge-Agent Orchestration for Onboard Satellite Intelligence
url: http://arxiv.org/abs/2608.03728v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_14-25-27Z_SAT_Edge_Agent_Hardware_in_the_LoopEdge_AgentOrche.md
generated_at: 2026-08-05 01:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents SAT-Edge-Agent, a hardware‑in‑the‑loop edge‑agent system that runs on an ARM‑based SoC to orchestrate satellite intelligence tasks under communication and power limits. It coordinates a browser workspace with a FastAPI language service and a YOLO‑style detector endpoint, delivering FAIR1M metadata in structured results. The study reports mean full‑agent latencies of 29.35 s and 60.94 s with P95 values of 31.17 s and 66.88 s.

## Key Takeaways
- Mean Full-Agent latency is under a minute, indicating that orchestration overhead dominates rather than detector computation.
- Detector execution contributes only about 2–3 % of the total mean time, showing it is not the bottleneck.
- CPU utilization stays below 21 %, while NPU load averages 100 %, but this reflects shared‑accelerator usage rather than detector‑only occupancy.

## Context
Satellite edge agents must balance low latency, limited bandwidth, and strict power budgets. This work demonstrates that orchestration frameworks can meet these constraints on commercial hardware without sacrificing performance. The results provide a benchmark for similar AI workloads in space applications where real‑time inference is critical.

## Implications
The findings validate the feasibility of deploying edge‑AI agents on existing satellite platforms, reducing reliance on ground‑based processing. Practitioners can use SAT-Edge-Agent as a reference architecture to design low‑overhead, high‑throughput systems that meet mission requirements.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03728v1)
