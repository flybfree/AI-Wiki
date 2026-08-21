---
title: One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows
url: http://arxiv.org/abs/2608.19741v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_07-37-57Z_OneSuccessIsn_tReliability_Thinkingbox_aSandboxand.md
generated_at: 2026-08-20 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Thinkingbox, a sandbox environment that enables evaluation of agents in complex stateful business workflows beyond simple tool calls. The benchmark, Thinkingbox‑Bench, contains 507 policy‑conditioned tasks across domains such as retail and insurance, measuring end‑to‑end task completion rather than just response plausibility.

## Key Takeaways
- Agents can produce valid tool calls yet fail to complete the overall workflow because they miss intermediate state updates or violate domain policies.  
- The strongest models achieve a pass@1 rate of 65.36% but only 25.25% succeed on the full task, highlighting a large gap between isolated successes and reliable execution.  
- Many failed trials terminate cleanly with correct actions, indicating that terminal success does not guarantee end‑to‑end correctness.

## Context
The rapid rise of agentic AI systems has shifted evaluation toward executable sandboxed environments where tools mimic real APIs. However, most benchmarks still focus on single‑turn responses or isolated tool usage, overlooking the cumulative nature of stateful business processes.

## Implications
For practitioners, Thinkingbox shows that reliable agents require robust coordination across multiple turns and strict adherence to domain policies. The gap identified pushes research toward metrics that capture full workflow completion and for industry to design benchmarks reflecting real‑world operational constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19741v1)
