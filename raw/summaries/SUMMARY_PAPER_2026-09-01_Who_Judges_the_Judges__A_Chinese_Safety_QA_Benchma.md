---
title: Who Judges the Judges? A Chinese Safety QA Benchmark for Evaluating LLM Responses and Safety Judges
url: http://arxiv.org/abs/2609.01210v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_13-15-01Z_WhoJudgestheJudges_AChineseSafetyQABenchmarkforEva.md
generated_at: 2026-09-01 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces C‑SafeQA, a benchmark that evaluates the safety of Chinese language model responses by distinguishing between policy violations and factual answers. The dataset contains 538 base queries and 8,877 adversarial queries answered by seven LLM deployments, producing 37,660 labeled records with expert adjudication. Unsafe‑response rates are low on base queries but high on adversarial ones, highlighting the difficulty of detecting hidden intent.

## Key Takeaways
- The benchmark demonstrates that adversarial transformations can inflate unsafe‑response rates up to 30%, while base queries remain under 4%  
- Evaluators trade off recall and false‑positive rates, with no single judge achieving optimal performance across all metrics  
- Acrostic attacks consistently lower unsafe recall for all judges, exposing specific weaknesses in their evaluation mechanisms  

## Context
Chinese harmful‑content detection faces challenges from linguistic variation and adversarial rewrites that obscure malicious intent. Existing safety benchmarks often lack policy‑grounded response labeling, making it hard to assess whether a model’s answer is truly unsafe or merely controversial. C‑SafeQA addresses this gap by providing a comprehensive, policy‑aligned dataset for both target models and automated judges.

## Implications
The results suggest that current automated safety judges are not universally reliable, especially under adversarial conditions, which could lead to over‑blocking or missed detections in production systems. Practitioners must consider human‑in‑the‑loop audits and model‑specific weaknesses when deploying Chinese LLM services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01210v1)
