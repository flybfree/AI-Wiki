---
title: Asymmetric Capacity Allocation in Self-Refinement Pipelines
url: http://arxiv.org/abs/2608.21345v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_17-52-17Z_AsymmetricCapacityAllocationinSelf_RefinementPipel.md
generated_at: 2026-08-23 21:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how model size influences three stages of self-refinement pipelines across five benchmarks using Qwen3 and Gemma3 models. It finds that larger generators and refiners boost performance while an undersized revison model can degrade results, whereas the critic's size has little effect as long as critique is present.

## Key Takeaways
- Larger generator and revision models improve pipeline output, but a too-small revison model harms performance.
- The critic stage benefits from any non‑zero capacity; even minimal critics outperform no critique at all.
- Model capacities should be allocated asymmetrically rather than uniformly across the three stages.

## Context
Self‑refinement is a key technique for advancing large language models, yet most research treats model size as an implementation detail. This study breaks that assumption by systematically varying sizes and observing stage‑specific effects.

## Implications
Designing pipelines with mismatched capacities can reduce compute costs without sacrificing quality. Practitioners should prioritize larger generators and refiners while keeping a modest critic active to maintain benefits of critique.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21345v1)
