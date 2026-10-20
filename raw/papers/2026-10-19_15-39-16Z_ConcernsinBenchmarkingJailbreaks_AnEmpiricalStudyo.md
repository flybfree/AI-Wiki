---
title: Concerns in Benchmarking Jailbreaks: An Empirical Study of Attack Success Rates
published: 2026-10-19T15:39:16Z
authors: Leon Tu Nguyen, Rohan Menon, Rafael Tappe Maestro, Eric Aubinais, Chih-Hong Cheng
url: http://arxiv.org/abs/2610.26595v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Concerns in Benchmarking Jailbreaks: An Empirical Study of Attack Success Rates

## Abstract
Jailbreak methods are commonly compared using Attack Success Rate (ASR), but these comparisons depend on how responses are generated and judged. In this paper, we examine eight attacks against three open-weight language models using three evaluation procedures. Low-resource language attacks achieve a mean ASR of 96.0% under keyword matching but 2.7% under a Qwen3 evaluator following StrongREJECT scoring instructions. Changing the number and arrangement of attempts reverses the ranking of DeepInception and rewriting. In a separate experiment, sampling 100 responses for each unchanged request at Ollama's default temperature of 0.8 yields 100% ASR under keyword matching but 50% under the Qwen3 evaluator. Beyond evaluator sensitivity, these findings raise a safety concern: repeated sampling can expose residual unsafe behavior despite an initial refusal, suggesting probabilistic suppression rather than robust exclusion. We recommend explicit success definitions, matched response budgets, validated evaluators, and reporting cumulative failure under repeated interaction rather than relying on single-generation tests.

## Metadata
- **Published**: 2026-10-19T15:39:16Z
- **Authors**: Leon Tu Nguyen, Rohan Menon, Rafael Tappe Maestro, Eric Aubinais, Chih-Hong Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.26595v1)