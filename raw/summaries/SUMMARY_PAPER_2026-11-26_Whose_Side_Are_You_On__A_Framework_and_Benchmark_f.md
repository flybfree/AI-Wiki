---
title: Whose Side Are You On? A Framework and Benchmark for Assessing LLM Political Stances through Politicians Social Media Posts
url: http://arxiv.org/abs/2611.34098v1
type: paper-summary
date: 2026-11-26
source_paper: 2026-11-25_10-05-40Z_WhoseSideAreYouOn_AFrameworkandBenchmarkforAssessi.md
generated_at: 2026-11-26 21:45
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces a framework for measuring how large language models (LLMs) align with or oppose political positions by simulating social media interactions around politicians' posts. It uses politicians' X/Twitter posts and multiple prompting methods to identify stances that are consistently expressed across prompts. Applying the framework, the authors construct WorldPOLL, a benchmark of 4,600 political posts from roughly 200 politicians spanning ruling and opposition blocs across 23 countries, and use it to analyze how support and opposition vary by model, country, and political direction.

## Key Takeaways
- The benchmark is built from real-world political communication: 4,600 X/Twitter posts from approximately 200 politicians, covering both ruling and opposition blocs across 23 countries, rather than from synthetic or single-country prompts.
- Quantitative analysis shows that LLM support and opposition differ across models, countries, and political directions, while qualitative analysis identifies the specific political views and policies that models tend to support or oppose.
- The authors examine whether models express consistent stances across prompting methods, investigate reasons for disagreement, and assess how model size and instruction tuning affect stance inconsistency, revealing both shared positions across models and differences across national contexts.

## Context
As LLMs increasingly participate in political discussions, understanding which positions they endorse or reject becomes important for evaluating their behavior in high-stakes domains. Existing evaluations often rely on narrow or controlled settings, whereas this work grounds stance assessment in authentic politician posts and multiple prompting methods. By spanning 23 countries and both ruling and opposition blocs, the study moves the question of LLM political alignment beyond a single ideology or national context.

## Implications
WorldPOLL provides a practical way for researchers and practitioners to measure LLM political tendencies, surface the views behind those tendencies, and assess consistency in real-world political discussions. The findings suggest that stance is not a fixed property of a model but varies with prompting method, national context, and model characteristics such as size and instruction tuning. This has implications for deployment, evaluation, and governance of LLMs in civic, media, and policy-adjacent settings where political framing can shape outputs and user trust.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.34098v1)
