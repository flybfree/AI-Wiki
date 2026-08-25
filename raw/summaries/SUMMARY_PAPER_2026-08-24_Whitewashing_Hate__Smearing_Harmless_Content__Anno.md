---
title: Whitewashing Hate, Smearing Harmless Content: Annotator-Style Rebuttal Attacks on LLM-Based Moderation
url: http://arxiv.org/abs/2608.22230v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_05-59-25Z_WhitewashingHate_SmearingHarmlessContent_Annotator.md
generated_at: 2026-08-24 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how annotator‑style rebuttals can manipulate large language model (LLM) hate speech moderation decisions, showing that such feedback can both whitewash harmful content and smear harmless material. Experiments on multiple LLMs and two datasets reveal that rejudge attacks degrade performance, especially in multi‑turn settings, while the impact of whitewashing versus smearing varies systematically across attack configurations.

## Key Takeaways
- Annotator‑style rebuttals cause a noticeable drop in moderation accuracy for both hateful and non‑hateful content, indicating that feedback can be weaponized to alter model judgments.  
- The degradation is more pronounced when the rejudge occurs after multiple rounds of human review, suggesting that cumulative manipulation amplifies errors.  
- Whitewashing (treating hate speech as normal) and smearing (labeling benign text as hateful) exhibit stable but opposite asymmetries in model vulnerability, revealing direction‑specific weaknesses.

## Context
The growing reliance on LLMs for content moderation creates a feedback loop where human reviewers can influence AI decisions. Understanding how such interventions affect model robustness is essential to building trustworthy automated systems that operate alongside human oversight.

## Implications
For practitioners, the findings call for direction‑aware safeguards and dedicated evaluation of feedback robustness in human‑AI workflows. Ignoring these vulnerabilities could lead to biased moderation outcomes and erode user confidence in AI‑driven content filtering.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22230v1)
