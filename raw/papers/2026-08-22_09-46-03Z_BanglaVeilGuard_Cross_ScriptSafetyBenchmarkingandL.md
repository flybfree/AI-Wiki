---
title: BanglaVeilGuard: Cross-Script Safety Benchmarking and Lightweight Guardrails for Bangla Large Language Models
published: 2026-08-22T09:46:03Z
authors: Md. Rakibul Hassan, Muhammad Iqbal Hossain
url: http://arxiv.org/abs/2608.21880v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BanglaVeilGuard: Cross-Script Safety Benchmarking and Lightweight Guardrails for Bangla Large Language Models

## Abstract
Bangla large language model (LLM) safety is difficult to evaluate with English-centric or standard-script benchmarks because Bangla users routinely write across scripts, spellings, code-mixed forms, and regional registers. This paper presents BanglaVeilGuard, a compact Bangla-first safety benchmark and lightweight prompt guard for six language forms: standard Bangla, Romanized Bangla, Banglish, code-mixed Bangla--English, noisy Bangla, and dialectal Bangla. The benchmark contains 2,366 quality-filtered prompts and a held-out 354-prompt evaluation split spanning unsafe, safe, and safe-sensitive requests. BanglaVeilGuard uses non-destructive multi-view normalization with a prompt-risk classifier and thresholded pre-generation gate, allowing it to screen prompts for heterogeneous target models without changing their weights. Across target-model families, guarded runs reduce attack success under deterministic response scoring from 93.8--100.0\% to 6.3\% for Claude Opus 4.8, BanglaLLama, and TituLLM; TigerLLM-1B with BanglaVeilGuard achieves 78.2\% accuracy with 8.8\% ASR. The prompt guard also attains 88.5\% unsafe recall, substantially above the evaluated prompt-only guard baselines. The main remaining cost is over-refusal on dialectal and noisy benign prompts, revealing a concrete safety-helpfulness frontier for Bangla LLM deployment.

## Metadata
- **Published**: 2026-08-22T09:46:03Z
- **Authors**: Md. Rakibul Hassan, Muhammad Iqbal Hossain
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21880v1)