---
title: PAIChecker: Uncovering and Checking PR-Issue Misalignment in SWE-Bench-Like Benchmarks
url: http://arxiv.org/abs/2607.28587v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_17-42-44Z_PAIChecker_UncoveringandCheckingPR_IssueMisalignme.md
generated_at: 2026-07-30 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates misalignment between pull requests and linked issues in SWE-bench Verified instances, finding that 13.6% of cases exhibit mismatches across five patterns in eleven fine‑grained scenarios. To address this problem, the authors propose PAIChecker, a multi‑agent system designed to detect such misalignments reliably. The study reveals that misalignment not only reduces benchmark utility but also complicates downstream analysis.

## Key Takeaways  
- 13.6% of SWE-bench Verified instances exhibit PR‑Issue misalignment across five patterns in eleven fine‑grained scenarios.  
- PAIChecker uses a three‑phase design: pattern identification, cross‑agent label synthesis, and code‑level validation for accurate detection.  
- Experiments on SWE‑Gym and SWE‑bench Multilingual achieve up to 92.12% binary accuracy with LLM backbones.

## Context  
The paper addresses a critical issue in evaluating large language model reasoning benchmarks where PR‑Issue pairings are often incorrect, undermining benchmark reliability; this misalignment can lead to inflated performance metrics and hinder trustworthy AI research. This problem is especially relevant as benchmarks proliferate, each relying on PR‑Issue pairs without validation.

## Implications  
For practitioners building SWE-bench‑like datasets, PAIChecker offers a scalable framework to verify data integrity, reducing false positives in model evaluation; industry adoption could improve reproducibility and confidence in LLM reasoning claims. Future work may integrate PAIChecker into CI pipelines to automate dataset quality checks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28587v1)
