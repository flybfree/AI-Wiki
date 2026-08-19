---
title: Which Source Wins? Task-Dependent Reliance in Vision-Language Models
url: http://arxiv.org/abs/2608.17205v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_23-38-14Z_WhichSourceWins_Task_DependentRelianceinVision_Lan.md
generated_at: 2026-08-18 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how vision-language models reallocate attention when images and text conflict, using controlled degradation of one modality while keeping the other intact. The study finds that most models shift away from degraded text more than from degraded image on arithmetic benchmarks, but this pattern reverses on a chart-report dataset where visual information dominates.

## Key Takeaways
- On GSM8K and SVAMP, five out of six open-weight VLMs prefer to rely less on the degraded textual source than on the degraded visual source.  
- The reversal observed on ChartQA‑Conflict holds even after accounting for unimodal accuracy loss and when charts are replaced by plain table images.  
- Frontier API models such as GPT‑5.6‑Luna and Gemini‑3.5‑Flash exhibit the same chart‑conflict pattern, suggesting a broader trend in multimodal reasoning.

## Context
Understanding modality reallocation is crucial because real‑world data often contain mismatched or noisy inputs, and current evaluation metrics may not capture how models prioritize information. This work highlights that task structure and evidence type can dictate which sensory channel dominates model decisions.

## Implications
For developers, the findings suggest that model behavior should be evaluated under varied conflict scenarios rather than assuming a fixed preference for image over text. Practitioners must consider these dynamics when designing multimodal applications to ensure robust performance across different data structures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17205v1)
