---
title: LeanMem: Simple and Efficient Long-Term Memory for LLM Agents
url: http://arxiv.org/abs/2608.03463v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_10-59-49Z_LeanMem_SimpleandEfficientLong_TermMemoryforLLMAge.md
generated_at: 2026-08-05 01:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
LeanMem proposes a lightweight long-term memory framework for LLM agents that distinguishes between low-value and high-value dialogue content. By filtering out unimportant information and storing only informative segments as compact profiles or event memories, the system reduces token consumption while preserving fidelity. Experiments on LoCoMo and LongMemEval-S with GPT-4.1-mini and Qwen3-8B show up to 15.1 accuracy improvement over baselines at minimal cost.

## Key Takeaways
- The framework filters low-value content, storing only informative segments as compact profile memory, event memory, or source-grounded record memory based on compressibility and fidelity needs.
- Only dynamically evolving event memories are updated during maintenance, avoiding redundant consolidation of stable profiles and immutable records.
- During inference, LeanMem selects appropriate memory types and allocates retrieval budgets per query, assembling evidence on demand.

## Context
Long-term memory remains a bottleneck for LLM agents because uniform summarization pipelines waste tokens or lose fine-grained details. Existing solutions either over-summarize or discard crucial context, limiting performance in multi-step interactions.

## Implications
This approach enables more efficient agent design with lower resource usage and higher accuracy, encouraging adoption of memory-aware systems without sacrificing performance. Practitioners can implement LeanMem to improve dialogue continuity while maintaining cost constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03463v1)
