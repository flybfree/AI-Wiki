---
title: Global Optimization and Inference-Time Region Grafting for Agentic Workflows
url: http://arxiv.org/abs/2608.02353v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_15-04-26Z_GlobalOptimizationandInference_TimeRegionGraftingf.md
generated_at: 2026-08-03 23:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GRAFT, a method that keeps a globally optimized workflow intact while locally swapping regions based on execution-time quality feedback. It replaces only selected parts of the workflow without re‑optimizing the whole system, enabling instance‑wise adaptation across tasks such as math reasoning and code generation.

## Key Takeaways
- GRAFT evaluates region alternatives using label‑free execution‑quality signals and accepts replacements that improve local quality while preserving overall consistency. - It avoids costly whole‑workflow re‑optimization by only changing the executor when needed. - The approach yields a 3.85‑point improvement over MaAS on average, showing that incremental adaptation can match or exceed static optimization.

## Context
Current agentic workflow systems are designed to be fixed before execution, limiting their ability to adapt to real‑time performance signals. This limitation hampers deployment in dynamic environments where task difficulty varies and hardware resources differ across instances.

## Implications
For practitioners, GRAFT offers a practical path toward flexible, self‑improving agentic pipelines without extensive retraining or re‑search. It encourages designing workflows as adaptable policies that can evolve with stronger executors and real‑time feedback loops.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02353v1)
