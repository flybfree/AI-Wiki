---
title: When Absence Is Evidence: Evaluating Completeness-Sensitive Negative Reasoning in Large Language Models
url: http://arxiv.org/abs/2608.04591v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_08-53-16Z_WhenAbsenceIsEvidence_EvaluatingCompleteness_Sensi.md
generated_at: 2026-08-05 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates completeness-sensitive negative reasoning in large language models, where a model should answer “no” only when the evidence fully covers the query. The authors introduce CROWN-QA to test this concept across three LLM families and find that models frequently make unstable closure judgments, often over‑closing or under‑closing based on how they interpret evidence coverage.

## Key Takeaways
- Models exhibit asymmetric failures: they recognize implicitly complete evidence but treat partially covered evidence as fully covering the query.  
- Prompting merely shifts errors between over‑ and under‑closure rather than producing consistent correct answers.  
- CROWN-Real confirms that partial‑coverage asymmetry persists on real documents, though its strength varies with model, prompt, and source.

## Context
The issue of negative reasoning in LLMs is critical because many applications rely on precise absence judgments to avoid hallucinated information. Current models’ inability to respect evidence scope can lead to unsafe or misleading outputs, undermining trust in automated systems that depend on factual correctness.

## Implications
For developers, this research highlights the need for structured certificate generation and careful prompt design to align model behavior with completeness criteria. Practitioners should treat negative answers as high‑risk decisions and implement verification layers to mitigate over‑closure errors.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04591v1)
