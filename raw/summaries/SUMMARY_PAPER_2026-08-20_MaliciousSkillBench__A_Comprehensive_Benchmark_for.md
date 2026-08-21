---
title: MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection
url: http://arxiv.org/abs/2608.19901v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_11-13-00Z_MaliciousSkillBench_AComprehensiveBenchmarkforMali.md
generated_at: 2026-08-20 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MaliciousSkillBench, a unified benchmark that consolidates malicious agent skills from 13 public sources into a single dataset of 9,740 normalized artifacts. Learned text detectors achieve high macro‑F1 scores but their performance drops significantly under source‑disjoint evaluation, while the strongest TF‑IDF SVM model balances recall and false positives across all regimes.

## Key Takeaways
- The benchmark reduces fragmentation by normalizing 8,414 raw records into 7,539 unique identities across 4,588 structural families.  
- Learned detectors obtain 0.882‑0.932 Random Macro‑F1 but only 0.653‑0.665 under Source‑Disjoint evaluation, indicating reliance on overlapping source data.  
- Off‑the‑shelf scanners lower false positives at the expense of markedly reduced malicious recall.

## Context
Malicious agent skills provide a direct channel for harmful behavior in LLM systems, yet existing datasets are disjoint and lack standardized evaluation. This work fills that gap by providing a comprehensive, cross‑source benchmark and comparing detection methods across different operational regimes.

## Implications
Practitioners must adopt broader cross‑source benchmarks to avoid overfitting to specific sources, and they should evaluate detectors jointly on both malicious detection and benign over‑flagging. The findings highlight the need for balanced metrics that reflect real‑world deployment conditions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19901v1)
