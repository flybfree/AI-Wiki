---
title: Personalized Privacy Control in LLMs via Attention Head Intervention
url: http://arxiv.org/abs/2608.21209v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_15-22-20Z_PersonalizedPrivacyControlinLLMsviaAttentionHeadIn.md
generated_at: 2026-08-23 21:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the challenge of personalizing privacy control in large language models by introducing a framework that combines user-specific disclosure preferences with contextual norms. The authors demonstrate that prompt‑based policies often ignore personalized settings, leading to high policy ignorance rates in models such as Qwen2.5-7B and Gemma3-4B. They propose Repair, an inference‑time attention head intervention that steers model output toward compliance with individual privacy rules.

## Key Takeaways
- The study reveals that prompt‑based policies fail to reliably enforce personalized privacy settings, resulting in average policy ignorance ratios of 51.25% for Qwen2.5-7B and 74.28% for Gemma3-4B.  
- Personalized privacy incorporates user‑specific disclosure preferences into the existing contextual framework, moving beyond generic rules to individual tolerance levels.  
- Repair adjusts attention head behavior during inference to reduce violations of personalized privacy policies, improving adherence significantly.

## Context
The rapid expansion of agentic AI and LLMs creates new avenues for data exposure, prompting a need for fine‑grained privacy mechanisms that respect diverse user expectations. This work contributes to the broader discourse on contextual privacy by extending it with personalization, offering a more adaptable approach than static policies.

## Implications
For practitioners, this research suggests that privacy enforcement must be dynamic and user‑centric rather than one‑size‑fits‑all. It also highlights the importance of model‑level interventions like attention head manipulation to achieve reliable compliance, guiding future development toward truly personalized AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21209v1)
