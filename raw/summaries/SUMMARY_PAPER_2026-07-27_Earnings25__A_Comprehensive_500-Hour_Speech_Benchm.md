---
title: Earnings25: A Comprehensive 500-Hour Speech Benchmark for Finance
url: http://arxiv.org/abs/2607.23813v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_19-24-00Z_Earnings25_AComprehensive500_HourSpeechBenchmarkfo.md
generated_at: 2026-07-27 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
Earnings25 is a new benchmark that evaluates automatic speech recognition on English‑language earnings calls within the finance domain. The paper presents two test sets—the full 498‑hour S&P 500 set from Q4 2025 and a 46‑hour industry‑balanced subset—and reports reproducible baselines for Whisper and Parakeet‑TDT using standardized scoring.

## Key Takeaways
- The testset‑full contains 498 hours of complete S&P 500 earnings calls recorded in Q4 2025.  
- The testset‑segmented is a 46‑hour set composed of 290 industry‑balanced segments drawn from English‑language U.S. earnings calls in 2025.  
- The benchmark supplies aligned transcripts and structured metadata such as speaker roles, industry labels, and call structure to enable speaker‑ and industry‑aware evaluation beyond aggregate word error rate.

## Context
Automatic speech recognition for financial statements is critical because earnings calls contain high‑value information that investors rely on for decision‑making. This paper contributes a domain‑specific benchmark that addresses the lack of standardized, realistic test data in ASR research.

## Implications
The Earnings25 benchmark will guide researchers and practitioners to develop models that understand speaker and industry nuances, improving accuracy where it matters most. It also sets a precedent for creating sector‑focused evaluation suites, encouraging more robust AI solutions for finance communication.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23813v1)
