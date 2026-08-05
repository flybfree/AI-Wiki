---
title: TraceCAD: Trace-Guided Repair for Agentic CAD Generation
url: http://arxiv.org/abs/2608.03062v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_03-23-11Z_TraceCAD_Trace_GuidedRepairforAgenticCADGeneration.md
generated_at: 2026-08-05 01:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
TraceCAD introduces a persistent state layer for LLM‑based CAD agents that links requirements, modeling steps, failure evidence, and repair candidates. The system diagnoses faulty operations, performs bounded edits in their dependency regions, validates outcomes via execution checks, and stores both successful and failed repairs as reusable skills. On DeepCAD benchmarks it improves geometric quality metrics such as IoU, Chamfer distance, and Hausdorff distance.

## Key Takeaways
- Persistent state linking requirements to modeling steps and repair candidates enables systematic diagnosis of faulty operations.
- Bounded edits within dependency regions reduce token cost and latency while preserving geometric fidelity.
- Reusable skill memory stores both successful and failed repairs, improving recovery reliability across model variations.

## Context
LLM‑driven CAD generation aims to produce executable parametric programs with high accuracy. Current repair mechanisms often discard evidence of earlier steps, leading to degraded results. TraceCAD addresses this by maintaining a traceable history that guides localized corrections.

## Implications
The approach lowers the number of code‑agent invocations and token consumption, making large‑scale CAD tasks more efficient. Practitioners can adopt persistent state layers to enhance reliability without sacrificing speed or quality in automated design workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03062v1)
