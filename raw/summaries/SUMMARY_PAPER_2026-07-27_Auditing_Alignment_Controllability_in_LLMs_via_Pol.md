---
title: Auditing Alignment Controllability in LLMs via Political Axes
url: http://arxiv.org/abs/2607.23519v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_07-38-11Z_AuditingAlignmentControllabilityinLLMsviaPolitical.md
generated_at: 2026-07-27 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates how large language models respond to political framing by testing them across a range of ideological personas and measuring the resulting shifts on economic and societal dimensions. It finds that prompt‑based controllability explains most variance, while model identity contributes only a small fraction, indicating that responses are highly adjustable rather than fixed.

## Key Takeaways
- Prompt steering dominates influence over LLM outputs, accounting for roughly 88%–93% of the variation on both axes.  
- Model differences are minor; most models produce similar displacements under identical prompts.  
- The geometric nature of dispersion, symmetry and saturation reveals that prior audits misinterpreted non‑centered baselines as differential compliance.

## Context
Understanding controllability is essential for safe deployment, as it determines how far a model can be nudged toward harmful or biased content without breaking. This work provides empirical evidence that political alignment can be manipulated through prompts rather than inherent model bias.

## Implications
Practitioners must audit not only where models land but also the spread and limits of their steering capabilities to prevent unintended ideological drift in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23519v1)
