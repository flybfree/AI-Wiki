---
title: PersonalBench: Measuring the Authorship Gap in LLM Personalization
url: http://arxiv.org/abs/2608.19746v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_07-48-20Z_PersonalBench_MeasuringtheAuthorshipGapinLLMPerson.md
generated_at: 2026-08-20 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PersonalBench, a benchmark that measures how well inference‑time personalization methods replicate an author’s writing style. Experiments across 50 authors and two model families show that the models can differentiate target authors on several evaluation lenses but never achieve human‑level similarity to any real author.

## Key Takeaways
- The authorship verification model LUAR distinguishes target authors within generated text with AUC = 0.918, indicating strong stylistic alignment.
- All personalization methods produce output that is more distant from any human author than random humans are from each other, suggesting the gap cannot be bridged by LLMs alone.
- The three evaluation lenses (LUAR, LLM‑as‑judge, automated stylometrics) are statistically indistinguishable on LUAR despite appearing different on the LLM judge, highlighting a circularity in trait and profile extraction.

## Context
Personalized text generation is a key goal for making large language models more useful to individual users. Existing benchmarks focus on task accuracy or preference alignment rather than genuine authorship replication, which limits understanding of how close an AI can come to human writing styles.

## Implications
For practitioners, PersonalBench provides a calibrated metric to assess whether personalization truly reflects an author’s voice without overstating capabilities. The findings caution against expecting LLMs to mimic human authorship and guide more realistic expectations in model deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19746v1)
