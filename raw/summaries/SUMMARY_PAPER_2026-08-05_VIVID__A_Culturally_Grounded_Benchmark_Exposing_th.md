---
title: VIVID: A Culturally Grounded Benchmark Exposing the Figurative Language Gap in Vietnamese NLP
url: http://arxiv.org/abs/2608.03095v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_04-13-26Z_VIVID_ACulturallyGroundedBenchmarkExposingtheFigur.md
generated_at: 2026-08-05 01:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces VIVID, a benchmark of 1,636 Vietnamese idioms and proverbs annotated with complexity traits and semantic themes. The study evaluates eight state‑of‑the‑art models using both generative and discriminative tasks, revealing that even top systems score below half the maximum possible performance.

## Key Takeaways
- Vietnamese‑specialized models underperform multilingual ones, achieving 0.13 versus GPT‑4o’s 2.46 on a key task.  
- Few‑shot prompting can degrade results, as seen in GPT‑4o’s stylistic overfitting.  
- Models frequently exhibit literal interpretation, lexical gaps, and pragmatic flattening.

## Context
Understanding figurative language remains a challenge for AI systems trained primarily on English data. Vietnamese is linguistically distinct with rich idiomatic expressions that lack direct equivalents elsewhere. This work addresses the gap by creating a culturally grounded evaluation set.

## Implications
Developers must prioritize cultural adaptation in model training to avoid misinterpretation of idioms. The benchmark provides a standard for measuring and improving figurative language comprehension, guiding both research and industry practice.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03095v1)
