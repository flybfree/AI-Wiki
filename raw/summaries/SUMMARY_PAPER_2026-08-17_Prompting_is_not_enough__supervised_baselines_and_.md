---
title: Prompting is not enough: supervised baselines and leakage control for measuring shared decision-making with LLMs in pediatric encounters
url: http://arxiv.org/abs/2608.14792v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_18-02-08Z_Promptingisnotenough_supervisedbaselinesandleakage.md
generated_at: 2026-08-17 21:43
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether zero‑shot prompting of a large language model can reliably detect shared decision‑making behaviors in pediatric surgical encounters and whether adding supervised learning improves performance under patient‑grouped evaluation. It finds that a supervised classifier yields higher kappa than zero‑shot, while a combined approach is best, but leakage from patient‑level grouping undermines results.

## Key Takeaways
- Zero‑shot prompting alone achieves low macro Cohen's kappa (0.139) compared to human coders.
- Supervised learning over frozen sentence embeddings improves kappa to 0.227, showing modest gains.
- Leakage occurs when patient‑grouped splits allow labels from held‑out patients to influence few‑shot exemplars.

## Context
This study addresses a gap in evaluating LLM performance on nuanced human interactions where shared decision‑making is critical. By exposing leakage in patient‑grouped splits and the impact of precomputed exemplars, it highlights methodological pitfalls in AI clinical assessment.

## Implications
Clinicians and developers must be cautious about data splitting that could bias model evaluation. The findings suggest that external validation is essential before deploying LLMs for decision support in pediatric care.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14792v1)
