---
title: Orientation, not magnitude: the causal structure of task-vector interference in merged language models
url: http://arxiv.org/abs/2608.11797v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_08-40-24Z_Orientation_notmagnitude_thecausalstructureoftask_.md
generated_at: 2026-08-12 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why merging language models by task arithmetic fails, showing that the interference between tasks is not explained by magnitude alone but by a specific causal direction in the merged model’s forward pass. It finds that layerwise cross‑term amplification dominates the effect and can be reversed only when applied near the output, revealing that erasing this flux removes interference dose‑dependently.

## Key Takeaways
- The dominant source of interference is an amplifying transport of existing cross‑terms (~65‑70% in both families) that increases >1 per late block, and its removal leaves 99% of the original norm at cosine 0.99 unless applied near the output.
- Erasing this causal direction removes interference dose‑dependently and saturates at exact erasure, whereas wrong‑direction controls fail or backfire, indicating a load‑bearing axis rather than a magnitude issue.
- Instruction wrappers mitigate the effect by amplifying the cross‑term internally, so the same erasure yields 13× less relative interference to remove because the wrapper drowns the interaction in a template‑pinned main effect.

## Context
Task‑based model merging is a key technique for fine‑tuning large language models without full retraining, yet empirical work often attributes failures to differences in magnitude or parameter overlap. This study challenges that view by isolating a specific causal pathway that persists across model families and instruction templates.

## Implications
Understanding the causal direction of interference can guide more robust merging strategies, helping engineers avoid hidden biases that degrade performance. Practitioners should focus on preserving this axis rather than merely adjusting magnitudes to achieve consistent outputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11797v1)
