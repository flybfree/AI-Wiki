---
title: Scale-to-Dialogue: Low-Burden Elicitation of Daily Premenstrual Symptom Ratings with Small Language Models
url: http://arxiv.org/abs/2608.08746v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_14-50-28Z_Scale_to_Dialogue_Low_BurdenElicitationofDailyPrem.md
generated_at: 2026-08-10 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a conversational system that reduces the burden of daily premenstrual symptom tracking by using small language models to elicit ordinal severity ratings through natural dialogue. It evaluates fixed six-item questions versus three joint cluster questions and finds the latter improves agreement while halving the number of queries. The study uses mcPHASES data with 3,320 participant-days.

## Key Takeaways
- The system achieves a quadratic weighted kappa of 0.976 with six separate items but reduces to 0.913 using three joint cluster questions while halving the question count.
- Moderate-or-higher symptom recall is 80.94% under the three-cluster approach, offering better detection efficiency.
- Adaptive open-first policies require more questions and produce lower agreement than fixed strategies.

## Context
Daily symptom tracking remains a manual burden despite its clinical value, prompting interest in AI‑driven interfaces that can streamline data collection without sacrificing accuracy. This work demonstrates how lightweight language models can map conversational cues to structured health metrics, aligning with broader trends toward low‑effort health monitoring.

## Implications
Clinicians and researchers can adopt this approach to integrate symptom logging into routine patient conversations, reducing administrative load and increasing adherence. The method also provides a reusable framework for other ordinal health assessments that rely on natural language input.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08746v1)
