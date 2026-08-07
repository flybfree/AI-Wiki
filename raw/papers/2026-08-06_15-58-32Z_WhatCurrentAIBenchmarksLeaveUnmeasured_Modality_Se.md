---
title: What Current AI Benchmarks Leave Unmeasured: Modality, Search, Citations, and Implications (for Safety Evaluations)
published: 2026-08-06T15:58:32Z
authors: Ro Encarnación, Tina Behzad, Emma Lurie, Danaé Metaxa
url: http://arxiv.org/abs/2608.06202v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Current AI Benchmarks Leave Unmeasured: Modality, Search, Citations, and Implications (for Safety Evaluations)

## Abstract
Large language model (LLM) benchmark evaluations are routinely used to support claims about model safety, reliability, and deployment readiness. Yet most evaluations rely on a single access modality (model APIs), perform a single run per prompt, and report accuracy as the primary outcome metric, without accounting for conditions such as web search that may have effects on model behavior in deployment. We audit these assumptions for one of the most widely-used LLMs, comparing two modalities, ChatGPT's chat UI and OpenAI's API, with and without web search enabled. We use a stratified total sample of 401 prompts from two popular benchmarks, BBQ and SafetyBench, collecting 4,812 total responses across three repeated runs per prompt. Beyond standard performance measures, we evaluate model output dimensions including response consistency, response text similarity, citation grounding, and abstention behavior. For instance, chat UI responses were less accurate than API responses on both benchmarks with search disabled. Enabling web search reduced accuracy by up to 8 percentage points, and even reversed the direction of modality performance trends for one benchmark. Repeated runs of the same prompt produced inconsistent responses in up to 21\% of prompts. The two modalities also grounded answers in different citations, and abstention behavior was also inconsistent across both modalities. These results illustrate that, even within a model family, reporting only simple accuracy metrics can obscure important forms of model behavioral variation relevant to AI safety assessments. We argue that AI safety evaluations should systematically account for modality, multi-run consistency, search conditions, and response-level behaviors to better reflect how deployed AI systems behave in practice.

## Metadata
- **Published**: 2026-08-06T15:58:32Z
- **Authors**: Ro Encarnación, Tina Behzad, Emma Lurie, Danaé Metaxa
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06202v1)