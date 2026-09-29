---
title: FlowState: Execution State as Memory for Long-Horizon LLM Agents
url: http://arxiv.org/abs/2609.34565v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_08-18-03Z_FlowState_ExecutionStateasMemoryforLong_HorizonLLM.md
generated_at: 2026-09-28 22:50
model: qwen3.6-35b-a3b
---

## Summary
FlowState introduces a novel memory mechanism for long-horizon LLM agents that treats execution state as persistent, revisitable memory rather than relying on full context history or lossy compression. By maintaining semantically typed state nodes linked to raw tool observations and employing Incremental State Update (ISU) alongside Progressive State Access (PSA), the framework allows agents to dynamically update their internal state while selectively retrieving relevant historical evidence during reasoning. Experimental results demonstrate that FlowState significantly outperforms full-context baselines, achieving higher success rates on MemoryArena and τ³-Bench benchmarks while reducing token consumption by over 40%.

## Key Takeaways
- FlowState utilizes Incremental State Update (

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34565v1)
