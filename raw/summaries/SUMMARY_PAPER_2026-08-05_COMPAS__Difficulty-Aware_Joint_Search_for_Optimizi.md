---
title: COMPAS: Difficulty-Aware Joint Search for Optimizing Code Generation
url: http://arxiv.org/abs/2608.04336v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_01-28-43Z_COMPAS_Difficulty_AwareJointSearchforOptimizingCod.md
generated_at: 2026-08-05 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces COMPAS, a difficulty‑aware optimization framework for code generation that jointly tunes model selection, prompts, and decoding settings. By learning group‑specific quality‑cost fronts through low‑cost model selection and combined prompt‑decoding search, COMPAS routes each task to its optimal configuration online. On LiveCodeBench it raises pass@1 from 45.9 % to 52.8 % while cutting cost from $36.57 to $4.92, and on SWE‑bench it lifts success rate to 76.0 % versus 70.0 %.

## Key Takeaways
- Prompts and decoding settings interact in non‑trivial ways; the effect of tuning one parameter depends heavily on the model used.  
- The optimal configuration is not uniform across tasks; it shifts with task difficulty, indicating a need for per‑task adaptation.  
- COMPAS learns distinct quality‑cost fronts for each group of tasks via low‑cost model selection and joint prompt‑decoding search, enabling online routing without further search.

## Context
Optimizing LLM calls in code generation has traditionally focused on single levers such as global models or fixed decoding settings, overlooking how multiple choices interact. This paper addresses that gap by demonstrating that the interaction between prompts and decoding is crucial for performance gains.

## Implications
For practitioners, COMPAS offers a practical path to higher pass@1 rates with dramatically lower operational cost, making large‑scale code generation more scalable and affordable. The approach highlights the importance of task‑aware optimization in deploying LLM systems efficiently.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04336v1)
