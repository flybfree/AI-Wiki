---
title: QUORUM: QUality-Optimized Routing Using Multiple annotators
url: http://arxiv.org/abs/2608.27974v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_06-39-36Z_QUORUM_QUality_OptimizedRoutingUsingMultipleannota.md
generated_at: 2026-08-30 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces QUORUM, a budget‑aware routing framework that decides whether to use human or LLM annotators for each instance based on feature‑based difficulty signals. It combines multiple annotations per task through agreement‑based rewards and improves quality by up to 34.4% while cutting costs by 8.8%. The approach outperforms prior methods that rely solely on model confidence.

## Key Takeaways
- QUORUM uses a fixed annotation budget and dynamically routes instances to human or LLM annotators according to estimated difficulty derived from features rather than confidence scores.
- It allows multiple annotations per instance, merging them via agreement‑based rewards which boosts reliability compared with single‑annotation methods.
- The framework achieves up to 34.4% higher annotation quality while reducing total cost by 8.8%, demonstrating a clear trade‑off between accuracy and expense.

## Context
Annotation remains a bottleneck in NLP pipelines, especially as LLM outputs become cheaper but less reliable for complex tasks. Prior work often treats each instance independently with confidence thresholds, ignoring the budget constraint that limits human labor. QUORUM addresses both reliability and cost simultaneously within a shared budget.

## Implications
For practitioners, QUORUM offers a practical way to balance quality and expense in annotation workflows without redesigning entire pipelines. In industry settings where budgets are tight, the method can be integrated into existing systems to improve model training data quality while staying within financial limits.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27974v1)
