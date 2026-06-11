---
title: Language Models Compare Quantities Using Number-specific and Unit-specific Heuristics
url: http://arxiv.org/abs/2606.03982v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-02_17-58-02Z_LanguageModelsCompareQuantitiesUsingNumber_specifi.md
generated_at: 2026-06-11 10:52
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how language models compare quantities that include measurement units such as 110 cm and 1.2 m across different unit systems. The study reveals that model performance drops near the comparison boundary where small numerical differences dictate the correct answer, indicating reliance on heuristic shortcuts rather than precise conversion.

## Key Takeaways
- Accuracy declines when the numeric values are close to each other because the model must decide which is larger without exact conversion.
- Systematic errors align with linear surrogate models that use cues derived from both the numerical difference and the unit‑scale difference.
- Causal interventions targeting subspaces linked to these cue dimensions shift the model’s output, suggesting a heuristic bag rather than a unified representation.

## Context
Understanding how language models handle unit‑laden comparisons is crucial for applications like measurement data interpretation and scientific reasoning. This work contributes to the broader effort of diagnosing model biases in quantitative reasoning tasks.

## Implications
For developers, recognizing that LMs rely on heuristics can guide design strategies such as providing explicit conversion cues or training with boundary examples. Practitioners may need to adjust evaluation metrics to reflect these systematic errors rather than assuming perfect unit handling.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.03982v1)
