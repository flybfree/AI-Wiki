---
title: Predictable Confabulations: Factual Recall by LLMs Scales with Model Size and Topic Frequency
url: http://arxiv.org/abs/2605.18732v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-18_17-53-44Z_PredictableConfabulations_FactualRecallbyLLMsScale.md
generated_at: 2026-06-11 10:42
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how factual recall by large language models scales with model size and training‑data composition, finding a sigmoid relationship between parameter count and topic frequency that explains most of the variance in performance across diverse models.

## Key Takeaways
- Recall quality follows a sigmoid in the log‑linear combination of model parameter count and topic representation in training data.  
- These two variables alone explain 60 % of the variance across 16 dense models from four families, rising to 74‑94 % within individual families.  
- The form matches a superposition‑inspired account where recall is gated by signal‑to‑noise ratio: signal strength scales with concept frequency and the noise floor with model capacity.

## Context
This work extends scaling law theory beyond pure parameter count to include data composition, revealing that factual knowledge depends on both model capacity and the representational richness of training corpora. It challenges assumptions that larger models automatically improve all tasks equally.

## Implications
For practitioners, it suggests optimizing training‑data diversity can boost factual recall without proportional size increase. Researchers should consider signal‑to‑noise dynamics when predicting model performance across domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.18732v1)
