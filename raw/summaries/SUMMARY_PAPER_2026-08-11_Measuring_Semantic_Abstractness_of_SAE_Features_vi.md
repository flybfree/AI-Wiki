---
title: Measuring Semantic Abstractness of SAE Features via Nonlocality
url: http://arxiv.org/abs/2608.10537v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_06-19-48Z_MeasuringSemanticAbstractnessofSAEFeaturesviaNonlo.md
generated_at: 2026-08-11 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Feature Nonlocality (FNL), a metric that measures the entropy of normalized per-position influence on an SAE feature’s activation, and demonstrates its correlation with semantic abstractness across LLM tasks. FNL successfully distinguishes contextual reasoning features from token‑driven ones, assigning higher values to the former in most random pairs.

## Key Takeaways
- FNL is defined as the entropy of normalized per‑position influence on an SAE feature’s activation.  
- FNL correlates with existing LLM proxy metrics of semantic abstractness and correctly assigns higher values to contextual features in most randomly drawn pairs.  
- High‑FNL features boost MATH‑500 accuracy by 4.6 points when steered, while low‑FNL features do not.

## Context
Sparse autoencoders are widely used to extract task‑relevant representations in large language models, but evaluating whether these representations capture genuine high‑level concepts remains challenging. This work offers a label‑free, model‑independent measure that can be applied across different architectures and tasks.

## Implications
FNL provides practitioners with an objective tool to assess abstraction levels without relying on human annotations or task‑specific proxies. It can guide feature selection for interventions such as jailbreak mitigation and improve model performance when steering high‑level features, offering a practical bridge between mechanistic analysis and real‑world deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10537v1)
