---
title: Sampling Luck Masquerades as Allocation Gain: Auditing Test-Time Budget Allocation for Neural Combinatorial Optimization
url: http://arxiv.org/abs/2608.13087v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_10-53-48Z_SamplingLuckMasqueradesasAllocationGain_AuditingTe.md
generated_at: 2026-08-13 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether non‑uniform allocation of a fixed budget to neural combinatorial optimization solvers yields measurable gains beyond the standard equal sampling approach. It finds that apparent in‑sample gains are artifacts, while real benefits appear only under distribution shift and can be captured with a corrected allocation strategy.

## Key Takeaways
- On uniform TSP‑100 tasks the reported 2‑6 % gain disappears when evaluated out of sample or calibrated against zero‑gain instances.  
- Allocation guided by held‑out sample statistics improves best‑of‑k performance by about 11–12 % on distribution‑shift workloads, exceeding a frozen baseline.  
- A small probe experiment shows that the allocation effect can be partially recovered even when only 20 samples are used against the same budget.

## Context
Neural combinatorial optimization solvers often assume uniform sampling to simplify reporting, but this may mask genuine improvements from smarter budget use. The study highlights a gap between observed and true performance gains in AI benchmarking practices.

## Implications
For practitioners, the findings suggest that equal‑budget allocation is not always optimal and that auditing sample statistics can reveal hidden inefficiencies. Researchers should adopt correction procedures to avoid overstating results and ensure fair comparison across solvers.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13087v1)
