---
title: "AI Benchmarks"
date: 2026-06-10
type: concept
tags: [ai-benchmarks, evaluation]
---

## Summary

Placeholder summary — please add a concise summary.


**Source**: [Original Article](https://github.com/flybfree/AI-Wiki/wiki)

## Semantic links
- [[concepts/self-improving-ai-loops/2026-06-10_Lesson6_Evaluation.md|Lesson 6 — Evaluation & Verification: The Judge Node]] — shared tags: evaluation, 5 topic terms overlap, same area: home
- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation and Benchmarks Hub]] — 1 title term overlap, shared tags: evaluation, 1 topic term overlap
- [[concepts/ai-foundations/ai-ml-foundations-lesson-15-evaluation-overfitting-and-limits.md|AI/ML Foundations Lesson 15 - Evaluation, Overfitting, and Limits]] — shared tags: evaluation, 5 topic terms overlap, same area: home

## AI Benchmarks

**Last Updated**: 2026-06-10

**Description**: Tracking AI model benchmarks, evaluation methodologies, and performance trends.

---

## Key Benchmarks

### MMLU (Massive Multitask Language Understanding)
- **Purpose**: Measure broad knowledge across 57 subjects
- **Variants**: MMLU-Pro (harder, more rigorous)
- **Current SOTA**: Llama 4 Scout (82.6%)

### HumanEval
- **Purpose**: Measure code generation capabilities
- **Metric**: Pass@1 on Python coding problems
- **Current SOTA**: Llama 4 Scout (95%)

### GPQA (Graduate-Level Google-Proof Q&A)
- **Purpose**: Measure expert-level reasoning
- **Variants**: GPQA-Diamond (hardest subset)
- **Current SOTA**: Varies by model

### AGIEval
- **Purpose**: Measure performance on academic benchmarks
- **Subjects**: Law, math, physics, etc.

### HellaSwag
- **Purpose**: Measure commonsense reasoning
- **Task**: Complete sentences with plausible endings

### ARC (AI2 Reasoning Challenge)
- **Purpose**: Measure grade-school science reasoning
- **Variants**: ARC-Challenge, ARC-Easy

### IFEval (Instruction Following Evaluation)
- **Purpose**: Measure ability to follow instructions
- **Task**: Follow specific formatting/content constraints

### LiveBench
- **Purpose**: Measure performance on recent, challenging tasks
- **Focus**: Avoids data contamination

---

## Benchmark Trends

- **MMLU-Pro** is becoming the standard for knowledge evaluation
- **HumanEval** is the standard for code generation
- **GPQA-Diamond** is the hardest reasoning benchmark
- **Data contamination** is a growing concern for older benchmarks

---

## Source Articles

- [[2026-04-24_LLMLeaderboard_Comparisonofover100AImodelsfromOpen_article.md]]
- [[2026-04-27_LLMLeaderboard2026_Compare220AIModelsAcross178_article.md]]