---
title: DiSCo: A Distribution-First Steering and Cultural Prior Evaluation Framework for Measuring Cultural Preference Bias in LLMs
url: http://arxiv.org/abs/2609.10253v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-09_14-40-08Z_DiSCo_ADistribution_FirstSteeringandCulturalPriorE.md
generated_at: 2026-09-09 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DiSCo, a distribution-first forced-choice framework that measures cultural preference bias in large language models by isolating default cultural priors and testing steerability across four context gradients. Using DiSCo-Bench with 304 items from BLEnD across twelve cultures, the authors find that UK and US dominate selections despite being only two out of twelve cultures. Prompt‑based steering widens gaps between high‑ and low‑resource cultures.

## Key Takeaways
- The default cultural priors are heavily concentrated, with UK and US absorbing about 35% of all model selections despite representing only two out of twelve cultures.
- Prompt‑based steering consistently widens the selection gap between high‑ and low‑resource cultures, indicating that personalisation alone cannot mitigate bias.
- Injecting explicit cultural facts produces negligible distributional disruption, showing that cultural preference bias is not resolved by prompt‑based personalisation.

## Context
Large language models are widely used in global assistants, but their outputs often reflect dominant cultural norms, limiting equitable localisation. Existing benchmarks treat cultural correctness as a single answer, obscuring how preferences emerge and persist across diverse contexts.

## Implications
Practitioners must move beyond prompt engineering to redesign evaluation methods that capture distribution‑level bias. This research highlights the need for frameworks that can reveal hidden cultural dominance and guide more inclusive model development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.10253v1)
