---
title: Calibrating Criterion Revision in LLM Agents: Failure Modes and a Trace-Anchored Protocol
url: http://arxiv.org/abs/2608.20729v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_04-21-28Z_CalibratingCriterionRevisioninLLMAgents_FailureMod.md
generated_at: 2026-08-23 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how language‑model agents revise their success criteria when a narrow criterion K0 is violated while a broader commitment B remains intact. The authors find that no model trial satisfies all five required conditions, revealing that CMB‑0.1 measures instrument calibration rather than genuine capability.

## Key Takeaways
- The five non‑compensatory conditions—criterion‑failure detection, a model‑emitted proposal, new‑episode transfer, intervention sensitivity on the claimed carrier, and preservation—are not met in any trial, indicating that CMB‑0.1 does not confirm criterion revision.  
- Eleven calls remain invalid after one retry, showing persistent failures that expose zero‑state reconstruction when Qwen2.5‑7B answers transfers without revising its state.  
- The harness performs commitments and deletion reuses a stateless call, while conflict changes multiple factors, demonstrating that the observed behavior is driven by external mechanisms rather than internal learning.

## Context
The study addresses a subtle failure mode in large language model agents where they may continue to use an outdated criterion despite broader goals being violated. This phenomenon challenges existing benchmarks that assume consistent performance across episodes and highlights the need for rigorous diagnostic tools beyond simple scoring metrics.

## Implications
For practitioners, this work warns against treating low scores as evidence of capability loss without probing underlying mechanisms. It calls for protocol‑level designs that isolate transfer, commits, and interventions to obtain trustworthy evaluations of criterion revision in future AI research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20729v1)
