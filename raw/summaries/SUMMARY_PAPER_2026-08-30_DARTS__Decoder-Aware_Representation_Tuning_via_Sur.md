---
title: DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging
url: http://arxiv.org/abs/2608.28547v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_17-22-47Z_DARTS_Decoder_AwareRepresentationTuningviaSurgeryf.md
generated_at: 2026-08-30 23:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
Model merging combines multiple task‑specific fine‑tuned LLMs into a single multi‑task model without retraining, but the merged hidden states often diverge from those of the source models—a problem called representation bias. The paper introduces DARTS, which corrects this bias with an entropy‑weighted L1 loss and per‑position additive bias, achieving strong gains on code generation, math reasoning, and instruction following while adding only 0.1 % extra parameters.

## Key Takeaways
- the causal attention mask in decoder models causes representation bias to accumulate across token positions, demanding position‑dependent correction.
- high‑entropy (decision‑critical) token positions are far more sensitive to errors than low‑entropy ones, so they must be prioritized for tuning.
- DARTS applies an entropy‑weighted L1 loss that upweights corrections at high‑entropy positions and adds a lightweight per‑position additive bias without overparameterizing the model.

## Context
Multi‑task models are increasingly used to reduce compute costs in large language systems, yet aligning representations across tasks is essential for consistent performance. Prior research has focused on encoder‑based models, leaving decoder architectures—critical for generation—understudied and uncorrected.

## Implications
For practitioners merging LLMs, DARTS offers a low‑overhead way to improve cross‑task consistency without retraining large parameter budgets. This can lead to higher quality outputs in production systems where efficiency and performance both matter.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28547v1)
