---
title: Item-Mean Surrogates: Why Richer Persona Data Fail to Improve LLMs as Human Surrogates
url: http://arxiv.org/abs/2608.29455v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_22-17-23Z_Item_MeanSurrogates_WhyRicherPersonaDataFailtoImpr.md
generated_at: 2026-08-31 20:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether richer persona data can improve LLM performance as human surrogates across large survey datasets. It finds that LLMs match average responses well but fail to capture individual deviations, showing only 3% of variance beyond item means versus 54% in humans.

## Key Takeaways
- LLM predictions align with aggregate human means but explain little of the remaining respondent-specific variation after removing item means.
- The reliable signal is person-by-item deviation, which is eight times larger than stable person effects and not encoded by richer personas.
- Persona data compress distributions, using fewer categories and distorted shapes, limiting LLM surrogacy.

## Context
Current research explores AI as personal assistants, assuming that extensive persona information can replace human respondents. This study challenges that assumption by demonstrating the limits of LLM surrogates in capturing fine-grained individual responses across diverse surveys.

## Implications
For developers, reliance on LLMs for personalized data collection may yield misleading results and reduce trust in automated tools. Practitioners should focus on preserving human variability rather than chasing richer persona inputs to improve model performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29455v1)
