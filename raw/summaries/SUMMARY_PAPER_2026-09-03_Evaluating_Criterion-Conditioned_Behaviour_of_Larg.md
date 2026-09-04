---
title: Evaluating Criterion-Conditioned Behaviour of Large Language Models in Content Moderation
url: http://arxiv.org/abs/2609.03814v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_13-17-38Z_EvaluatingCriterion_ConditionedBehaviourofLargeLan.md
generated_at: 2026-09-03 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Diagnostic Evaluation of COntent (DECO), a criterion‑independent factorisation that allows researchers to evaluate large language models on individual moderation criteria rather than aggregated labels. Experiments across four datasets and four LLMs reveal that strong benchmark scores can mask failures when specific aspects of content must be judged, showing that models often cannot reliably apply each criterion in isolation.

## Key Takeaways
- Strong aggregate performance does not guarantee that a model can correctly identify harmfulness based on the particular moderation aspect required by a given criterion.  
- The DECO framework separates content into independent factors, enabling controlled evaluation of each criterion without confounding them with others.  
- Pairwise comparisons between criteria expose systematic weaknesses where models prioritize overall harm over precise, criterion‑specific judgments.

## Context
In AI safety research, the ability to moderate content accurately is essential for responsible deployment. Current benchmarks that combine multiple criteria risk obscuring nuanced failures, which could lead to unsafe or biased outputs in real‑world systems.

## Implications
For industry practitioners, this means that relying solely on high aggregate scores may result in models that miss important safety constraints. Future evaluation tools must explicitly test criterion‑conditioned behaviour to ensure compliance with diverse policy requirements.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03814v1)
