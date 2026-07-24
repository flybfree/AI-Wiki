---
title: SLAPBench: Benchmarking Multimodal Large Language Models for Four-Finger SLAP Fingerprint Verification
url: http://arxiv.org/abs/2607.15517v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-17_00-04-53Z_SLAPBench_BenchmarkingMultimodalLargeLanguageModel.md
generated_at: 2026-07-23 23:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
SLAPBench introduces a benchmark for evaluating multimodal large language models on four‑finger SLAP fingerprint verification using NIST SD302b data. The study shows that prompting can collapse open‑source models to high false acceptance rates while Claude Opus performs better, and model capability varies widely as measured by AUC scores.

## Key Takeaways
- Prompting governs collapse: task‑description prompts cause near‑100% FAR across four open‑source MLLMs.  
- Gemma‑3‑12B collapses under zero‑shot prompting, while Claude Opus 4.8 resists both binary and task‑description prompts, achieving the lowest FAR of 20.2%.  
- Model capability gaps are evident: Qwen3‑VL‑8B attains perfect AUC=1.0 on SD302b but this may be due to resolution duplication rather than true discrimination.

## Context
SLAP verification is critical for border control and law enforcement, yet existing benchmarks ignore multimodal AI performance. This work highlights the need for evaluation frameworks that capture both technical accuracy and fairness in real‑world security applications.

## Implications
This research warns that model capability alone cannot guarantee reliable or equitable results when demographic disparities increase as discrimination weakens. Practitioners must consider prompt design alongside model architecture to ensure robust, fair fingerprint verification systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.15517v1)
