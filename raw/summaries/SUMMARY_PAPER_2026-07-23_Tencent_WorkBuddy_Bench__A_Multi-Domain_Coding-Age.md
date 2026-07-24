---
title: Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant Task Construction
url: http://arxiv.org/abs/2607.20911v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_04-34-06Z_TencentWorkBuddyBench_AMulti_DomainCoding_AgentBen.md
generated_at: 2026-07-23 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The Tencent WorkBuddy Bench is a multi‑domain coding‑agent evaluation suite that creates tasks by reverse‑engineering real commits, pull requests, and business scenarios into short role‑played prompts, ensuring the dataset cannot be discovered via web search. The benchmark runs these tasks on two agent harnesses, uses distinct scoring instruments per domain, and publishes all components openly for reproducible auditing.

## Key Takeaways
- Each task is reverse‑engineered from a real commit or business scenario and rewritten as an unrecoverable colloquial prompt, providing contamination resistance through construction rather than secrecy.  
- The suite comprises four work domains—Code, Web, Office, Security—each with its own verification style and scoring instrument, preventing cross‑subset score comparison.  
- Full reproducibility is achieved because task directories, environment images, evaluation harnesses, tests, and reference solutions are released openly.

## Context
This paper addresses a longstanding challenge in AI research: evaluating coding agents on tasks that reflect real work without allowing external leakage of the underlying data. By publishing an open, reproducible benchmark, it contributes to fair model comparison across diverse domains.

## Implications
For practitioners, WorkBuddy Bench offers a transparent framework to assess agent performance on realistic tasks, encouraging more rigorous and trustworthy AI development. For the industry, it sets a standard for contamination‑resistant evaluation that can be adopted in production pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20911v1)
