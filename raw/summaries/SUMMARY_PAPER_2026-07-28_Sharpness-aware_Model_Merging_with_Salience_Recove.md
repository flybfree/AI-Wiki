---
title: Sharpness-aware Model Merging with Salience Recovery for LLM-based Cross-Domain Sequential Recommendation
url: http://arxiv.org/abs/2607.25366v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_07-17-44Z_Sharpness_awareModelMergingwithSalienceRecoveryfor.md
generated_at: 2026-07-28 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SharpRec, a framework for merging large language models to improve cross‑domain sequential recommendation by addressing conflict and saturation. Experiments show it lifts performance beyond prior baselines in both dual‑ and multi‑domain settings.

## Key Takeaways
- Cross‑domain knowledge conflict arises from parameter misalignment during model merging.
- Performance saturation occurs due to statistical homogenization that erodes domain distinctiveness.
- SharpRec’s two modules—Sharpness‑aware Geometric Alignment and Preference Salience Activation—restore interference‑free fusion and recover distinctive features.

## Context
LLM‑based recommendation systems aim to generalize across domains without relying on shared user data. Model merging offers a scalable way to fuse heterogeneous knowledge, yet current methods often degrade performance due to these issues. This work contributes a principled approach that preserves domain specificity while improving overall utility.

## Implications
For practitioners, SharpRec provides a practical recipe for integrating diverse LLM knowledge streams in recommendation pipelines. The method can be adopted by companies seeking higher conversion rates and reduced data dependency across unrelated domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25366v1)
