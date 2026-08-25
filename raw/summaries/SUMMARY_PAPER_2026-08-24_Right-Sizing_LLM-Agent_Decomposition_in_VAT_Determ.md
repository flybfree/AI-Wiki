---
title: Right-Sizing LLM-Agent Decomposition in VAT Determination: A Pilot Controlled Sweep
url: http://arxiv.org/abs/2608.23395v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_15-40-15Z_Right_SizingLLM_AgentDecompositioninVATDeterminati.md
generated_at: 2026-08-24 21:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a pilot study comparing different ways to decompose left‑right VAT determination tasks among LLM agents. It varies the number of workers from one strong agent to five narrow ones while keeping all other components fixed, and finds that accuracy improves up to four workers but does not reach the best possible score.

## Key Takeaways
- The matched‑token criterion suggests that prompt budget constraints may explain why a single agent scores lower than orchestrated setups when token limits are aligned. - Accuracy peaks at four narrow agents (0.830) against endpoints of 0.720 and 0.770 but fails to meet the fine endpoint, leaving the intermediate‑optimum hypothesis unsupported at pilot scale. - Failure injection shows that schema‑conforming hallucinations degrade all configurations, especially fragmented ones, indicating robustness issues in narrow decompositions.

## Context
This work addresses a tension in large language model agent design: whether to consolidate capabilities into one powerful tool or split them across many specialized agents. The study’s controlled sweep provides empirical evidence on how decomposition granularity affects performance under realistic cross‑border VAT calculations with reverse charge.

## Implications
For practitioners, the findings suggest that right‑sizing agent partitions may require careful placement at dependency layers and awareness of prompt budgets. The released pipeline offers a reproducible benchmark for evaluating such trade‑offs in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23395v1)
