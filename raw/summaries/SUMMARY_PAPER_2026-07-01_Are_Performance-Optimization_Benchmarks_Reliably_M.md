---
title: "Summary: Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?"
url: http://arxiv.org/abs/2607.01211v1
type: paper-summary
date: 2026-07-01
source_paper: 2026-07-01_17-50-48Z_ArePerformance_OptimizationBenchmarksReliablyMeasu.md
generated_at: 2026-07-01 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper audits three repository‑level performance‑optimization benchmarks — GSO, SWE‑Perf, and SWE‑efficiency — to reveal that their leaderboard scores often reflect technical flaws rather than genuine coding‑agent progress. The authors demonstrate that only a minority of benchmark tasks can be replayed with valid reference patches across different machines, that public submissions are frequently ranked inconsistently due to scoring rule biases, and that many submissions already match or exceed the reference performance on most tasks.

## Key Takeaways
- Only 39 % of GSO tasks, 11 % of SWE‑Perf tasks, and 411 % of SWE‑efficiency tasks can be replayed with valid reference patches across four machine types.  
- Public submission rankings disagree on 9 out of 28 pairwise comparisons between GSO and SWE‑efficiency submissions, while SWE‑efficiency’s scoring gives the worst ten tasks unusually high weight scores (58.5 %–82.8 %).  
- Across 10 public submissions per task, at least one submission matches or beats the reference patch on 85.3 % of replay‑valid GSO and SWE‑efficiency tasks and improves over unoptimized base code on 99.8 %.

## Context
Benchmark leaderboards are widely used to gauge advances in AI coding agents, yet they often conflate runtime instability with actual optimization quality. This study highlights how benchmark design choices can obscure genuine progress and mislead comparisons across diverse hardware.

## Implications
For researchers and industry practitioners, the findings suggest that relying solely on aggregate leaderboard scores may produce misleading conclusions about agent capabilities. More transparent, reproducible evaluation methods are needed to ensure fair assessment of coding‑agent performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.01211v1)
