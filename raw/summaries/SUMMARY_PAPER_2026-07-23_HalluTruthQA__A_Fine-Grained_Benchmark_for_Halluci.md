---
title: HalluTruthQA: A Fine-Grained Benchmark for Hallucination Detection, Localization, and Explanation in Arabic Question Answering
url: http://arxiv.org/abs/2607.20219v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_14-37-25Z_HalluTruthQA_AFine_GrainedBenchmarkforHallucinatio.md
generated_at: 2026-07-23 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HalluTruthQA, a fine‑grained benchmark for detecting, localizing, verifying, and explaining factual errors in Arabic question answering. It contains 2400 expert‑curated examples across Islamic knowledge, history, science, and geography, each with model answers, reference answers, binary labels, candidate facts, erroneous spans, explanations, and macro/micro hallucination types. Evaluation shows top scores of 0.880 Macro‑F1 for detection, 0.516 F1‑Sp localization, 0.852 LO‑Score verification, and 0.644 explanation score.

## Key Takeaways
- The benchmark distinguishes between detection, localization, verification, and explanation of hallucinations, moving beyond binary labels to granular analysis.
- Each task captures distinct model abilities, with no single model dominating all metrics across the four domains.
- Expert‑curated candidate answers and character‑level erroneous spans enable precise evaluation of factual errors in Arabic QA.

## Context
Hallucination detection remains a critical challenge for Arabic LLMs due to limited resources and domain‑specific knowledge gaps. This work addresses that gap by providing a comprehensive, multi‑task dataset that supports both research and industry applications.

## Implications
For practitioners, HalluTruthQA offers tools to improve model reliability in Arabic QA systems. For the field, it sets a new standard for fine‑grained hallucination evaluation, encouraging future models to focus on accurate localization and explanation rather than just detection.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20219v1)
