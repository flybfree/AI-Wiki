---
title: CurveShift: Is Agent Progress Scalar? Separating Level from Shape
url: http://arxiv.org/abs/2608.00355v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_23-58-25Z_CurveShift_IsAgentProgressScalar_SeparatingLevelfr.md
generated_at: 2026-08-03 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether the observed increase in performance on difficult tasks by large language models reflects a genuine change in model capability or merely a shift due to ceiling effects and benchmark artifacts. Using METR time-horizon data they fit a Rasch model showing rising ability explains most of the gain, suggesting progress is scalar rather than shape‑dependent. A residual hard‑task effect remains after accounting for overall ability.

## Key Takeaways
- The Rasch model with rising ability reproduces the observed difficulty response, indicating that gains are largely due to ceiling effects rather than a change in the underlying skill distribution.
- After controlling for this, models released after September 2024 still solve harder competitive‑programming problems by about 0.40 logits, raising the success rate from 18% to 25%, driven primarily by strong reasoning models on short‑reasoning tasks.
- The analysis is specific to LiveCodeBench because it isolates model performance without agentic scaffolding, allowing clear attribution of gains to the models themselves.

## Context
Large language models are often evaluated with single scalar metrics that ignore how progress varies across task difficulty. This can mislead researchers into attributing emergent abilities to the models when they may be artifacts of measurement choice or benchmark design. The paper highlights a need for more nuanced assessments that separate ability from shape in performance curves.

## Implications
For practitioners, separating true capability gains from statistical artifacts is crucial for reliable model evaluation and investment decisions. Industry should adopt benchmarks with controlled difficulty ordering to avoid misleading conclusions about emergent abilities. Researchers must consider both scalar progress and potential ceiling effects when interpreting benchmark results.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00355v1)
