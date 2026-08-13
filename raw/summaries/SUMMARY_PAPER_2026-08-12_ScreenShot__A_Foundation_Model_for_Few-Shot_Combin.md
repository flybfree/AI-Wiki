---
title: ScreenShot: A Foundation Model for Few-Shot Combination Drug Screening
url: http://arxiv.org/abs/2608.12219v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_16-13-50Z_ScreenShot_AFoundationModelforFew_ShotCombinationD.md
generated_at: 2026-08-12 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
ScreenShot is a hierarchical transformer model that predicts how new patients will respond to combination therapies using only a few observations from functional measurements. The model leverages in‑context learning without fine‑tuning or molecular profiling and outperforms all baselines on four held‑out datasets. Its internal representations also enable an active experimental design strategy that reduces the required screening budget by one third while maintaining hit detection.

## Key Takeaways
- ScreenShot uses a hierarchical transformer pretrained on 40 drug screening datasets covering 3,700 drugs and 6,000 biological samples, mirroring the nested structure of screening data.  
- It performs in‑context learning directly on functional measurements without any fine‑tuning or molecular profiling.  
- The model’s internal representations drive a weighted k‑means++ active learning strategy that selects experiments to achieve the same hit detection as uniform screening with only one third of the budget.

## Context
This work showcases how large language models can be adapted for few‑shot, multimodal tasks in drug discovery, demonstrating that transformers can generalize across diverse biological datasets. It highlights a shift toward AI systems that operate directly on raw functional measurements rather than requiring extensive pre‑processing or fine‑tuning pipelines.

## Implications
For the field of personalized medicine, ScreenShot offers a rapid way to identify effective drug combinations without costly experimental screening. In industry, it reduces development timelines and resource expenditure, enabling faster translation of AI insights into clinical practice. Practitioners can now leverage these models as decision support tools for experimental planning and patient‑specific therapy design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12219v1)
