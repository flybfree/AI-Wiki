---
title: Some Emotions Run Deeper: Layer-wise Probing and Causal Intervention in Large Language Models
url: http://arxiv.org/abs/2609.01279v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_14-14-13Z_SomeEmotionsRunDeeper_Layer_wiseProbingandCausalIn.md
generated_at: 2026-09-01 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how emotion is encoded in large language models across diverse text sources and model families by combining layer‑wise probing with offline scaling, online interventions, transfer analyses, and early‑exit classifiers. The study shows that the optimal probing layer moves from near the input to deeper layers depending on the emotional expressiveness of the data, that targeted forward interventions degrade performance more than random bands, that selected affective bands are transferable across datasets, and that early‑exit representations outperform full‑depth ones by about six points.

## Key Takeaways
- The best probing layer shifts systematically from input‑adjacent layers to over half model depth across Twitter posts, Reddit comments, and autobiographical narratives, indicating that the accessibility of emotion depends on both text source and model architecture.  
- Forward‑pass interventions on probe‑selected bands reduce test accuracy by 5–6 points more than same‑width random bands (p < 0.01), demonstrating that targeted manipulation of affective representations is effective but sensitive to layer choice.  
- Selected emotion bands transfer across datasets and categories, suggesting a partially shared affective substrate rather than strictly per‑emotion specificities.

## Context
Understanding where and how emotions are represented in LLMs helps researchers design better prompt engineering and alignment strategies that respect the model’s internal knowledge structure. This work bridges probing methodology with causal intervention to reveal actionable insights beyond static accuracy metrics.

## Implications
For industry practitioners, these findings suggest that early‑exit representations can be leveraged for efficient emotion detection while minimizing performance loss. Practitioners should also consider dataset characteristics when selecting probing layers and interventions to maximize model utility in affective applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01279v1)
