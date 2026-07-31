---
title: Back to All-Entity Ranking: Sampler-Dependent Evaluation in Continuous-Time Dynamic Graphs
url: http://arxiv.org/abs/2607.27861v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_08-37-43Z_BacktoAll_EntityRanking_Sampler_DependentEvaluatio.md
generated_at: 2026-07-30 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how the choice of negative destinations and candidate sets in next‑destination prediction on continuous‑time dynamic graphs influences model rankings. Experiments across multiple models show that a non‑uniform negative distribution or even a uniformly drawn finite set can alter Bayes‑optimal ranking, destabilize module effects, and change relative order between benchmark metrics. The authors conclude that all‑entity ranking, which evaluates every destination in a fixed catalog, provides more reliable evidence for architecture comparisons.

## Key Takeaways
- A non‑uniform negative distribution changes the Bayes‑optimal ranking because the evaluation score becomes dependent on the chosen negative set rather than the true data distribution.  
- Even a uniformly drawn finite candidate set can destabilize model rankings and measured module effects, indicating that sampling variation directly impacts scores.  
- All‑entity ranking eliminates negative‑selection freedom and sampling variation while preserving the original CTDG scorer, making it a more stable benchmark for architecture evaluation.

## Context
In dynamic graph settings such as music recommendation or MOOC navigation, models rank observed interactions against sampled negatives to estimate relevance. Traditional benchmarks rely on these random samples, which introduce variability that can obscure true model performance differences. This paper highlights the need for methods that are less sensitive to sampling artifacts when comparing architectures.

## Implications
Practitioners should adopt all‑entity ranking as a primary metric for CTDG benchmarking because it provides consistent, non‑biased scores independent of candidate set size or training objectives. Using this approach will lead to more trustworthy conclusions about model superiority and guide better architectural design decisions in real‑world recommendation systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27861v1)
