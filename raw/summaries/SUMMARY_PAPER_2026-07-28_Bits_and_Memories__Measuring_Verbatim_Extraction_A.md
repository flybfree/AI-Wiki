---
title: Bits and Memories: Measuring Verbatim Extraction Across LLM Quantization
url: http://arxiv.org/abs/2607.25451v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_08-41-31Z_BitsandMemories_MeasuringVerbatimExtractionAcrossL.md
generated_at: 2026-07-28 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how quantizing large language models affects verbatim extraction of memorized training sequences. It finds that quantization reduces verbatim memorization more than it degrades general capability and that the amount of retained memorized data grows with model size, challenging earlier privacy claims based on membership inference.

## Key Takeaways
- Quantization selectively forgets verbatim memorized sequences faster than it degrades general language ability across all precision levels and model sizes.
- The remaining fraction of memorized data increases as models become larger, indicating that compression does not reliably erase training data.
- This suggests that extraction-based privacy metrics are more informative than membership inference for assessing real‑world risk.

## Context
Current research often measures model privacy using membership inference attacks, which assess whether an attacker can infer if a specific instance was in the training set. However, these methods do not capture the practical concern of verbatim data leakage, which could be exploited by users seeking exact outputs from the model.

## Implications
For practitioners, focusing on extraction metrics will guide more accurate privacy risk assessments and help design quantization strategies that balance performance with data protection. Industry adoption should prioritize monitoring verbatim memorization rather than relying solely on inference‑based benchmarks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25451v1)
