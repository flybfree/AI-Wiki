---
title: Every Wrong Answer Counts: Option-Level Psychometrics for LLM Multiple-Choice Benchmarks
url: http://arxiv.org/abs/2608.02966v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_23-59-39Z_EveryWrongAnswerCounts_Option_LevelPsychometricsfo.md
generated_at: 2026-08-05 01:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes the LLM Nominal Response Model (LLM-NRM), an option‑aware psychometric framework that treats multiple‑choice answers as a full distribution rather than binary correct/incorrect labels. Experiments on 189 LLMs and 31,554 items show that LLM‑NRM yields more accurate predictions and stronger correlations with human preference rankings than conventional binary scoring methods.

## Key Takeaways
- Distractor identity adds roughly a 101 % boost to Fisher information per item beyond simple correctness.  
- Incorrect responses alone recover full‑information ability estimates, achieving a Spearman correlation of 0.943.  
- The learned item parameters allow efficient benchmarking with only 41 items preserving the full‑bank ranking (Kendall = 0.85), reducing data needs by 770×.

## Context
Current LLM evaluation relies on binary correctness, ignoring how models rank wrong answers and discarding valuable psychometric signals about item difficulty or distractor quality. This work bridges that gap by modeling the complete response distribution across options.

## Implications
For researchers, the method offers a richer diagnostic of model behavior, enabling finer‑grained analysis of error patterns. Practitioners can use these insights to design more informative benchmarks and calibrate models for higher predictive fidelity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02966v1)
