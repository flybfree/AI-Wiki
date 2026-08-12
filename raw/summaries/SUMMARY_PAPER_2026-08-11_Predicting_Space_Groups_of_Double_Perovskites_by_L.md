---
title: Predicting Space Groups of Double Perovskites by LLM with Dynamic Few-Shot Learning
url: http://arxiv.org/abs/2608.10483v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_04-53-56Z_PredictingSpaceGroupsofDoublePerovskitesbyLLMwithD.md
generated_at: 2026-08-11 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DyRIS, an LLM‑based framework that predicts space groups of double perovskites by combining dynamic few‑shot retrieval with rule‑guided inference. The method outperforms composition‑based and descriptor‑based baselines, especially for underrepresented (minor) space group classes, achieving the highest overall Top‑1 macro‑F1 score.

## Key Takeaways
- Diversity‑enhanced dynamic few‑shot prompting retrieves relevant in‑context examples while limiting the dominance of frequently represented major SGs.  
- Rule‑guided inference uses B/B′ cation ordering and quantitative indicators to refine and rank the final Top‑3 SG candidates, improving prediction accuracy beyond conventional classifiers or rankers.  
- Ablation studies confirm that each component—diversity retrieval, quantitative indicators, major‑SG bias control, and B/B′ ordering—contributes meaningfully to performance.

## Context
The paper addresses a longstanding challenge in materials science: the imbalance of space group data where dominant classes dominate datasets, leaving minority classes under‑represented. By integrating large language model reasoning with crystallographic rules, DyRIS demonstrates how retrieval‑augmented prompting can capture domain knowledge and improve minority class recognition.

## Implications
Accurate space‑group prediction is crucial for guiding experimental synthesis and accelerating material discovery. The success of DyRIS suggests that LLM agents enhanced with rule‑based constraints can deliver reliable predictions even when training data are skewed, offering a scalable tool for the field.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10483v1)
