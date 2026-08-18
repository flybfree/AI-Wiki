---
title: RETRACE: Resilience-Guided Trait-Conditioned Craving Estimation from Wearable Physiology in Opioid Use Disorder
url: http://arxiv.org/abs/2608.14947v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_00-05-16Z_RETRACE_Resilience_GuidedTrait_ConditionedCravingE.md
generated_at: 2026-08-17 21:41
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents RETRACE a resilience‑guided trait‑conditioned framework for estimating opioid craving from wearable physiological signals in subjects with opioid use disorder. It demonstrates that craving is not directly detectable on short‑term wearables because its signals are weak and overlap with stress physiology, but that resilience can be inferred through post‑stress heart‑rate recovery and autobiographical memory recall. RETRACE achieves up to 7% absolute improvement over the best baseline in a subject‑independent evaluation.

## Key Takeaways
- Stress elicits strong autonomic responses while craving signals are weaker and often hidden within stress physiology, making direct detection difficult.
- Resilience is not observable from short wearable windows but can be captured using post‑stress heart‑rate recovery and autobiographical memory recall as subject‑level proxies.
- RETRACE’s dual‑encoder architecture uses a frozen stress encoder and a resilience‑conditioned craving encoder with feature‑level gating to enable lightweight personalization without per‑user retraining.

## Context
This work advances the field of affective computing by integrating psychological traits into physiological signal interpretation, moving beyond simple pattern matching toward personalized inference. It highlights how subject‑specific factors such as resilience can be leveraged to improve model robustness in a setting where labels are unavailable.

## Implications
For clinicians and AI developers, RETRACE offers a practical tool for early craving detection that respects privacy by avoiding explicit user data labeling. The approach could inform wearable health products that provide timely interventions while maintaining subject independence.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14947v1)
