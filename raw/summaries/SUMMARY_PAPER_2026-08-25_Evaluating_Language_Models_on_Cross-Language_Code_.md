---
title: Evaluating Language Models on Cross-Language Code Functional Equivalence
url: http://arxiv.org/abs/2608.23961v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_01-41-00Z_EvaluatingLanguageModelsonCross_LanguageCodeFuncti.md
generated_at: 2026-08-25 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper evaluates whether large language models can correctly determine if programs written in different languages produce the same functional output. Using a dataset of human‑written code across C++, Java, and Python, it finds that current LLMs often misclassify non‑equivalent code as equivalent, especially on harder problems.

## Key Takeaways
- The difficulty-dependent breakdown shows that models become more prone to false positives when the equivalence problem is complex.
- GPT-o4-mini exhibits model‑specific sensitivity, being overly conservative with Python and less so with other languages.
- Run‑to‑run instability indicates inconsistent reasoning rather than a permanent lack of capability.

## Context
Assessments of code understanding have traditionally relied on single‑language benchmarks or synthetic examples, limiting insight into true cross‑lingual reasoning. This study highlights the gap between reported performance and real‑world functional equivalence across languages.

## Implications
For developers relying on LLMs for translation or migration tasks, the findings warn against trusting automated equivalence checks without human verification. The instability also suggests a need for more robust evaluation protocols that account for model variability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23961v1)
