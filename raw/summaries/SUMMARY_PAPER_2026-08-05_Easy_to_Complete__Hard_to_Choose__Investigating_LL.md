---
title: Easy to Complete, Hard to Choose: Investigating LLM Performance on the ProverbIT Benchmark
url: http://arxiv.org/abs/2608.04670v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_10-28-51Z_EasytoComplete_HardtoChoose_InvestigatingLLMPerfor.md
generated_at: 2026-08-05 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ProverbIT, an Italian benchmark of 100 multiple-choice questions testing LLM performance on proverb completion and selection tasks. It evaluates 13 frontier models across three tasks and finds that while most models succeed at completing proverbs, their ability to select correct answers drops sharply when the correct answer is not provided.

## Key Takeaways
- Models consistently complete proverbs but fail in multiple‑choice without correct answers, indicating a gap between generation and selection. - The Chain‑of‑Thought analysis shows models favor literal synonyms and mention correct endings even though those options are absent. - Even state‑of‑the‑art reasoning models experience large performance degradation, suggesting reliance on memorized patterns rather than semantic understanding.

## Context
Understanding how LLMs handle culturally embedded expressions is crucial for evaluating their real‑world applicability in Italian language tasks. This study contributes to the broader discourse on figurative language comprehension and challenges assumptions about model robustness across task formats.

## Implications
For developers, the findings warn that deploying models for multiple‑choice quizzes may lead to unexpected failures when correct options are hidden. Practitioners should consider alternative evaluation methods or incorporate explicit reasoning steps to mitigate reliance on memorized patterns.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04670v1)
