---
title: Large Language Model Few-Shot Prompting with Dilemma Training Outperforms Human Surrogates in Predicting Patient Preferences
url: http://arxiv.org/abs/2608.25771v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_13-14-30Z_LargeLanguageModelFew_ShotPromptingwithDilemmaTrai.md
generated_at: 2026-08-26 20:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces P4-DT (Dilemma Training), a personalized patient preference predictor that learns decision policies through exposure to varied medical dilemmas rather than treating preferences as static ratings. In a study with 12 patient‑surrogate dyads, P4-DT achieved 81.7 % accuracy in predicting treatment choices, far above chance and human surrogates (68 %). The model also outperformed both unassisted (55 %) and P4‑assisted (62 %) surrogate systems.

## Key Takeaways
- P4-DT constructs a patient decision policy by engaging users with varied medical dilemmas, achieving 81.7 % accuracy—an odds ratio of 5.61 versus chance—significantly exceeding the 68 % human baseline.  
- The model surpasses both unassisted surrogates (55 %) and P4‑assisted surrogates (62 %), demonstrating a clear advantage over existing approaches.  
- Incorporating contextual scenario decisions and open‑ended text boosted accuracy by 15 percentage points compared with using only static value ratings.

## Context
The work advances the field of AI‑driven medical decision support by modeling patient preferences as dynamic, context‑dependent judgments rather than fixed scores. This shift reflects a broader trend toward agents that can simulate nuanced human reasoning and adapt to situational complexity, moving beyond simple rating systems toward richer, interactive models.

## Implications
For clinicians and AI developers, P4-DT offers a more reliable tool for anticipating patient choices, potentially reducing decision conflict and improving care coordination. The findings suggest that context‑aware AI agents can become valuable partners in complex medical decisions, enhancing both accuracy and empathy in patient‑centered interactions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25771v1)
