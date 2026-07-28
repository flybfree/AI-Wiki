---
title: Accuracy Hides How Language Models Fail: Measuring Failure States Under Matched Output Budgets
url: http://arxiv.org/abs/2607.24268v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_11-04-17Z_AccuracyHidesHowLanguageModelsFail_MeasuringFailur.md
generated_at: 2026-07-27 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper argues that standard accuracy scores hide how language models fail by conflating whether a response reaches an evaluable state with its correctness. It introduces a two‑layer framework that separates execution evidence from verification results and shows this separation matters across model outputs. On MATH and ARC‑Challenge, matched token limits produce different mixes of termination, answer exposure, parseability, and length, leading to sharply varying accuracy despite similar scores.

## Key Takeaways
- 49 of 450 Qwen MATH outputs terminate without a final answer while only 5 of 300 DeepSeek MATH outputs do so, indicating execution failures are not uniformly captured by accuracy.
- At 8,192 tokens the same DeepSeek MATH pairs never show missing‑final length termination, showing that longer contexts can mitigate certain failure modes.
- Candidate‑selection and aggregation policies can substantially alter comparative accuracy estimates, meaning reported scores depend on evaluation policy as well as execution.

## Context
Current AI research often reports a single numeric accuracy metric that masks the underlying reasons for model failures. This conflation makes it hard to compare models or diagnose weaknesses in test‑time pipelines. The paper highlights that performance depends not only on model capability but also on how outputs are handled during evaluation.

## Implications
Researchers and practitioners should report pre‑intervention execution states, verification coverage, and scorer provenance alongside accuracy scores. This transparency will enable more reliable comparisons and guide improvements in both model design and test‑time processing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24268v1)
