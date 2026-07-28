---
title: "Summary: Defeating Nondeterminism in LLM Inference"
date: 2025-09-10
type: source-note
tags: [thinking-machines, source-note, inference, reproducibility]
source_url: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
---

# Summary: Defeating Nondeterminism in LLM Inference

**Source**: [Thinking Machines Lab](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)

Saved: 2026-07-27 10:58

## Summary
Thinking Machines argues that LLM nondeterminism is a real systems problem, not just a sampling artifact. The post breaks the issue into concrete causes — floating-point ordering, concurrency, and kernel behavior — and then shows how to make the core inference path batch-invariant.

## Key Takeaways
- Temperature 0 still does not guarantee repeatable outputs in practice.
- The blog traces nondeterminism to specific kernel-level behaviors rather than hand-waving about "GPU weirdness." 
- The fix path focuses on batch-invariant RMSNorm, matrix multiplication, and attention.

## Context
Deterministic inference matters for debugging, evaluation, regression testing, and any workflow that expects the same prompt to produce the same output across runs.
Thinking Machines treats that as a tractable engineering problem instead of an unavoidable property of LLMs.

## Implications
If these techniques hold up broadly, they improve reproducibility for model serving and make inference systems easier to reason about.
That is especially relevant for evaluation pipelines, agent harnesses, and any product that needs stable behavior across repeated calls.

## Related Concepts

- [[concepts/ai-agents/agentic-workflows-hub.md|Agentic Workflows Hub]]
- [[concepts/software-development/software-development-hub.md|Software Development Hub]]
- [[concepts/llm-models/llm-models-hub.md|LLM Models Hub]]
- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation Benchmarks Hub]]
