---
title: CLOSER-Bench: Evaluating Budgeted Cross-Stage Design Closure for Hardware Agents
url: http://arxiv.org/abs/2607.16632v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-18_04-28-47Z_CLOSER_Bench_EvaluatingBudgetedCross_StageDesignCl.md
generated_at: 2026-07-23 23:17
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper introduces CLOSER‑Bench, a benchmark that evaluates hardware design closure across multiple synthesis and implementation stages under a budget constraint. The study shows that agents can solve localized RTL repair tasks but often fail to achieve full closure, highlighting the difficulty of coordinating long‑horizon tool calls.

## Key Takeaways  
- Agents exhibit sharp completion–closure gaps: three agents fix an AXI register issue while the verification‑to‑GDS task separates a top agent from two successful baselines.  
- The benchmark records every simulator, synthesis, STA, and place‑and‑route invocation, measuring final quality, anytime progress, tool cost, and cross‑stage recovery to quantify budgeted sequential decisions.  
- A full RTL‑to‑GDS flow is validated using a macro‑based AXI/DMA streaming accelerator, demonstrating that closure requires coordinated multi‑tool orchestration rather than isolated code generation.

## Context  
Hardware AI agents must navigate long‑horizon workflows where tool feedback is delayed and heterogeneous, making it hard for existing pass‑at‑k benchmarks to capture true progress. This work addresses the need for a unified evaluation that respects budget limits and cross‑stage dependencies in hardware design.

## Implications  
Treating hardware closure as a budgeted sequential decision problem influences AI research by guiding model architectures toward multi‑step planning. Practitioners can leverage CLOSER‑Bench to benchmark agents, prioritize tool integration, and allocate computational budgets more effectively in real hardware projects.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.16632v1)
