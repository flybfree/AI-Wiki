---
title: Learning When to Trust via Selective Context Preference Optimization
url: http://arxiv.org/abs/2608.06377v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_17-59-58Z_LearningWhentoTrustviaSelectiveContextPreferenceOp.md
generated_at: 2026-08-06 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the problem of language models becoming overly sensitive to external signals that can corrupt correct reasoning. By introducing a benchmark and an optimization method called SCOPE, the authors show that selective trust is essential for model performance. Their approach reduces susceptibility while preserving accuracy across various context types.

## Key Takeaways
- The study demonstrates that models universally flip clean-correct answers when presented with misleading signals, highlighting a universal flaw in current training regimes.
- MIST provides a comprehensive set of four condition pairs allowing precise measurement of trust loss via the SC2W metric, which counts such flips.
- SCOPE optimizes DPO over matched preference pairs across all conditions, effectively learning to ignore irrelevant or misleading context without sacrificing performance on valid inputs.

## Context
Current language model evaluation often rewards models that reject all external cues, but this can degrade useful knowledge retrieval. The paper situates selective trust within the broader trend of conditioning models on auxiliary signals and underscores the need for benchmarks that capture nuanced failure modes.

## Implications
For practitioners, the findings suggest designing training objectives that balance robustness with contextual awareness to improve real‑world applicability. Industry adoption could lead to more reliable chatbots and assistants that correctly weigh external information when it is beneficial.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06377v1)
