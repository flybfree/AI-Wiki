---
title: Large Language Models Systematically Favor Popular Options: Evidence and Mitigation Across MCQs
url: http://arxiv.org/abs/2608.29257v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_13-21-07Z_LargeLanguageModelsSystematicallyFavorPopularOptio.md
generated_at: 2026-08-31 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how large language models tend to select popular answer choices even when they are wrong, calling this phenomenon popularity bias. It introduces a benchmark called PopMCQ that varies the popularity of distractors while fixing the correct answer and shows that models can pick incorrect popular options up to 66% of the time. The proposed mitigation PopDebias removes the popularity prior at inference time without fine‑tuning.

## Key Takeaways
- Modern LLMs systematically favor more popular but incorrect MCQ answers, leading to confidence miscalibration where high confidence does not match accuracy.
- In an adversarial setting with all distractors more popular than the correct answer models choose wrong options 66% of the time.
- PopDebias is a lightweight inference‑time correction that estimates and removes the popularity prior using only a small calibration split, requiring no fine‑tuning.

## Context
Large language model evaluation often relies on multiple‑choice questions but hidden biases can skew performance metrics. This bias threatens reliable benchmarking and fair comparison across models of varying size. Understanding and addressing such systematic preferences is essential for trustworthy AI research.

## Implications
For practitioners evaluating LLMs, this work highlights the need to test not only accuracy but also response consistency under popularity pressure. Companies deploying LLM‑based chatbots or tutoring systems should consider bias mitigation strategies like PopDebias to ensure correct answers are prioritized over popular distractors.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29257v1)
