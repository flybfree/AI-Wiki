---
title: Small Models Scout Bottleneck Order for Large-Model Data Control
url: http://arxiv.org/abs/2608.14936v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_23-24-34Z_SmallModelsScoutBottleneckOrderforLarge_ModelDataC.md
generated_at: 2026-08-17 21:41
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether small proxy models can reveal a transferable curriculum for resolving skill bottlenecks in large language model training, introducing LogFloor as a closed‑loop controller that directs each round toward current bottlenecks. The study demonstrates that this phase‑ordered resolution reduces token cost by 56.2% on average and enables successful three‑round replay across multiple large models.

## Key Takeaways
- LogFloor reduces token cost by 56.2% on average across five bAbI skill slices on Qwen2.5-1.5B.
- In 70M-to-12B transfer, a three‑round replay of a scout path reaches every floor in all eight target runs, saving 30.9% pair mean and 39.4% pooled training tokens.
- A frozen scout path succeeds across all eight 12B runs on MMLU-control.

## Context
This work extends curriculum learning to monitored skill acquisition, showing that small models can guide large model training efficiently by focusing on bottlenecks. The approach aligns with broader efforts to make training more efficient by leveraging lightweight models as proxies for large‑scale objectives and adding a sentence about the study's demonstration of order transfer.

## Implications
Practitioners can adopt phase‑ordered bottleneck resolution to cut training costs and improve performance without retraining from scratch. Industry can reduce compute budgets and accelerate deployment of specialized models, making advanced capabilities more accessible.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14936v1)
