---
title: A Repeated-Measurement Study for Cultural Analytics of English Song Lyrics Using Five Large Language Models
url: http://arxiv.org/abs/2609.04428v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-03_19-49-10Z_ARepeated_MeasurementStudyforCulturalAnalyticsofEn.md
generated_at: 2026-09-06 21:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates five large language models as zero‑shot annotators for four social constructs expressed in English song lyrics, measuring self‑esteem, self‑control, seeking belonging, and seeking recognition. Repeated annotations reveal that self‑esteem shows the strongest reliability across runs and models, while seeking recognition is the least stable; self‑control and seeking belonging fall between these extremes, with model‑dependent performance.

## Key Takeaways
- Self‑esteem exhibits the highest repeated‑measurement consistency among all constructs, indicating that LLM outputs for this concept are more stable over time.  
- Seeking recognition demonstrates the greatest variability across models and runs, suggesting that its measurement is fragile and not suitable for reliable cultural analytics.  
- The consensus labels from multiple LLMs contain useful signal for downstream supervised classification, yet their convergence does not automatically validate the underlying constructs.

## Context
The study addresses a growing reliance on AI to scale human‑coded cultural analysis, where reliability of model outputs must be demonstrated before they can replace manual annotation. By focusing on repeated‑measurement stability and cross‑model convergence, it highlights gaps in current LLM performance for social‑construct labeling tasks.

## Implications
For researchers, the findings call for systematic reporting of measurement consistency when using LLMs as cultural analytics tools. Practitioners should treat self‑esteem annotations as more trustworthy than those for seeking recognition, and consider model‑specific approaches for intermediate constructs to avoid misinterpretation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04428v1)
