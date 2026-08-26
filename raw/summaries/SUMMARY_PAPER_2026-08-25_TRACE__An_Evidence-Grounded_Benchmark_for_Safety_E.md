---
title: TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models
url: http://arxiv.org/abs/2608.24232v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_08-35-47Z_TRACE_AnEvidence_GroundedBenchmarkforSafetyEvaluat.md
generated_at: 2026-08-25 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TRACE, an evidence‑grounded benchmark for evaluating safety in large reasoning models. It shows that safety judgments of reasoning traces are harder than those of prompts or final responses and that current guardrail models often fail to locate unsafe content with supporting evidence.

## Key Takeaways
- The benchmark covers the full inference pipeline—prompts, reasoning traces, and final responses—spanning nine risk categories and ten attack strategies.  
- Safety judgments for reasoning traces are substantially more challenging than for prompts or final responses because traces contain hidden unsafe elements.  
- Current guardrail models struggle to extract supporting evidence from the trace text, leading to inaccurate safety labels.

## Context
Large reasoning models generate intermediate traces that can embed harmful content even when outputs appear benign. Existing safety benchmarks focus on binary labels without evidence, limiting model improvement. This work addresses a gap by providing detailed annotations and highlighting the difficulty of trace‑level detection.

## Implications
Guardrail systems must be trained to understand both prompts and internal reasoning steps to prevent downstream harm. Practitioners should prioritize models that can locate and justify unsafe traces, ensuring safer deployment in high‑risk applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24232v1)
