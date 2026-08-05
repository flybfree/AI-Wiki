---
title: SAGE: Semantic Explainability of Attention-Based Survival Models in Computational Pathology
url: http://arxiv.org/abs/2608.02803v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_18-58-39Z_SAGE_SemanticExplainabilityofAttention_BasedSurviv.md
generated_at: 2026-08-05 01:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SAGE, a post‑hoc framework that turns the local attention maps of frozen attention‑based multiple instance learning models into global, language‑grounded explanations for survival prediction in computational pathology. Applied to seven TCGA cancer cohorts and three foundation models, SAGE recovered known prognostic features such as necrosis risk while uncovering disease‑specific biology like an angiogenic signature in renal cell carcinoma.

## Key Takeaways
- SAGE extracts a dictionary of 25 histological concepts, scores image patches against them, and aggregates these scores according to the model’s learned attention to produce cohort‑level explanations.  
- Ablation studies show that the identified associations depend on the model’s attention rather than concept prevalence alone, indicating that attention drives the predictive signal.  
- The concept dictionary captures much of the prognostic information encoded by foundation model features, demonstrating a strong link between visual attention and semantic concepts.

## Context
Attention‑based multiple instance learning dominates slide‑level prediction in pathology, yet its explanations are limited to local regions without semantic insight. This work bridges that gap by providing interpretable, scalable, and model‑agnostic global explanations that can be used for cohort analysis and biomarker discovery.

## Implications
Pathologists will gain a clearer understanding of what ABMIL survival models learn beyond pixel intensities, enabling more informed clinical decision making. The framework also offers a pathway to identify novel biomarkers by linking attention patterns with biological concepts across diverse patient groups.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02803v1)
