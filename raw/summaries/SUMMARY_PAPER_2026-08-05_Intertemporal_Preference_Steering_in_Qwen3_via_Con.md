---
title: Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition
url: http://arxiv.org/abs/2608.03892v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_16-25-38Z_IntertemporalPreferenceSteeringinQwen3viaContrasti.md
generated_at: 2026-08-05 01:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how to measure and steer the temporal preferences of Qwen3-32B by using contrastive linear probes on teacher‑forced answers. It demonstrates that these probes can identify a short‑term versus long‑term direction in the model’s residual stream, allowing large bidirectional changes in preference. Experiments show steering shifts the model’s indifference threshold between immediate small rewards and delayed larger ones.

## Key Takeaways
- The contrastive linear probes on teacher‑forced temporal‑choice answers reveal a clear short‑term vs long‑term direction within Qwen3's residual activation stream.
- Adding these identified directions via activation addition can steer the model to strongly prefer either smaller‑sooner or larger‑later monetary rewards, moving its indifference threshold in both directions.
- The same steering improves performance on a TravelPlanner capability benchmark when moderate temporal cues are applied.

## Context
Large language models often encode implicit biases toward immediate outcomes, which can affect advice and planning. Measuring these biases is crucial for aligning AI behavior with human values that consider delayed consequences.

## Implications
This work shows intertemporal preferences are not fixed but can be tuned, offering a method to adjust model recommendations for delayed benefits or costs. Practitioners can use such steering to improve safety in long‑horizon planning and more reliable decision‑making under uncertainty.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03892v1)
