---
title: What Current AI Benchmarks Leave Unmeasured: Modality, Search, Citations, and Implications (for Safety Evaluations)
url: http://arxiv.org/abs/2608.06202v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_15-58-32Z_WhatCurrentAIBenchmarksLeaveUnmeasured_Modality_Se.md
generated_at: 2026-08-06 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper critiques common LLM benchmark practices that focus on a single access modality and a single run per prompt. By comparing ChatGPT’s chat UI with OpenAI’s API under and without web search, the authors show that accuracy can drop sharply when search is enabled and responses vary across runs. The study highlights response consistency, citation grounding, abstention behavior, and text similarity as dimensions often ignored in safety evaluations.

## Key Takeaways
- Chat UI responses were less accurate than API responses on both BBQ and SafetyBench with search disabled, indicating modality‑dependent performance.
- Enabling web search reduced accuracy by up to eight percentage points and even reversed the modality trend for one benchmark, showing that external data can degrade model reliability.
- Repeated runs produced inconsistent responses in up to twenty‑one percent of prompts, underscoring the need to measure multi‑run consistency.

## Context
Current AI safety assessments often rely on narrow metrics like single‑run accuracy measured via API calls. This approach overlooks real‑world deployment factors such as user interfaces, web search integration, and stochastic output variability. The paper situates these gaps within ongoing debates about model reliability and responsible AI development.

## Implications
For practitioners, the findings suggest that safety reports must capture modality effects, run consistency, and response behaviors to avoid misleading conclusions. Industry standards should incorporate multi‑modal evaluations and repeated testing to better reflect how deployed systems behave in practice.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06202v1)
