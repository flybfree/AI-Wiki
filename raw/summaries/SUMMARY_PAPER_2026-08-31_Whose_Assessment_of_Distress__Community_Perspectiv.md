---
title: Whose Assessment of Distress? Community Perspectives and LLM Alignment on Well-Being Posts
url: http://arxiv.org/abs/2608.29446v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_21-23-57Z_WhoseAssessmentofDistress_CommunityPerspectivesand.md
generated_at: 2026-08-31 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how large language models assess psychological distress and whether their judgments reflect the community norms that define what is concerning. It finds that open‑weight LLMs systematically overestimate mild cases, producing many false positives, while frontier models like GPT‑5 and Gemini 2.5 Pro exhibit similar inflation despite mixed overall performance.

## Key Takeaways
- Raters in a contextualized in‑group condition agree more with their community than uncontextualized out‑group raters (OR = 1.18), showing a modest but significant bias toward in‑group perspectives across six identity‑based communities.
- Open‑weight LLMs achieve only 31–44% accuracy on none‑to‑mild distress labels, overwhelmingly generating false positives because their underlying distress prior exceeds both human in‑group and out‑group judgments.
- GPT‑5 and Gemini 2.5 Pro inflate none‑to‑mild cases even when their full‑sample over/under rates are balanced, indicating a consistent overestimation rather than random noise.

## Context
This study highlights a gap between AI models trained on generic data and the culturally specific ways communities label emotional distress, a concern that has been noted in prior work on bias in mental health detection. The findings extend these concerns by quantifying how model priors diverge from both human in‑group and out‑group norms.

## Implications
For practitioners deploying AI in mental‑health support, miscalibrated distress detection can lead to inappropriate interventions that disproportionately affect the very communities the models are meant to serve. Aligning models with community‑specific norms is essential for equitable and effective deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29446v1)
