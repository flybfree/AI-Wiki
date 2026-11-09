---
title: A Proxy-Based Method for Measuring Racial Disparities in~Text-to-Image~Generators
url: http://arxiv.org/abs/2611.07132v1
type: paper-summary
date: 2026-11-08
source_paper: 2026-11-04_20-58-20Z_AProxy_BasedMethodforMeasuringRacialDisparitiesin_.md
generated_at: 2026-11-08 21:33
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces an automated auditing method for text-to-image generators that measures representational bias against ground-truth demographic benchmarks using racial proxy variables adapted from U.S. antidiscrimination law. The authors classify generated images by race, compare distributions to census data, and additionally measure skin tone variation via CIELAB color values and cosine similarity to detect quality disparities across racial groups. Testing three models (Imagen 4 Fast, Stable Diffusion 3.5 Large Turbo, and Flux Schnell) across geographic, occupational, and surname proxy categories, the study reveals significant and model-specific patterns of racial over- and under-representation.

## Key Takeaways
- The method adapts racial proxy variables from U.S. antidiscrimination law (geographic, occupational, and surname categories) to create a legally grounded, fine-grained auditing framework that avoids relying on implicit normative definitions of fairness, instead anchoring comparisons to publicly available demographic benchmark data such as census statistics.
- Imagen 4 Fast was found to overrepresent white-classified images more than the other tested models, producing images with lighter and more homogeneous skin tones, and exhibited the largest representational disparity for Black demographics specifically when prompted with surname and geographical proxy categories.
- Stable Diffusion 3.5 Large Turbo diverged most from census data overall in its racial distribution but paradoxically produced the most diverse range of skin tones, while the paper also introduces CIELAB-based skin tone measurement and cosine similarity analysis to capture biases invisible in simple demographic counts, such as differences in image quality across races and skin tones.

## Context
As text-to-image generators become widely deployed in creative, commercial, and public-facing applications, concerns about representational bias in generated imagery have grown substantially. Existing fairness auditing approaches often rely on subjective or normative definitions of what constitutes equitable representation, making them difficult to standardize or legally defensible. This paper addresses that gap by grounding its methodology in established legal frameworks for measuring racial discrimination, offering a reproducible and legally coherent alternative for evaluating generative AI systems.

## Implications
For AI practitioners and model developers, this work provides a concrete, generalizable auditing tool that can be integrated into model evaluation pipelines to surface detailed racial representation patterns before deployment, helping teams identify and mitigate biases in specific prompt categories rather than treating fairness as a monolithic concern. For industry stakeholders and regulators, the legally grounded proxy-based approach offers a pathway toward compliance-ready auditing of generative AI systems, potentially informing policy discussions about discriminatory outputs in AI-generated media and setting a precedent for how demographic fairness can be measured without subjective judgment calls.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.07132v1)
