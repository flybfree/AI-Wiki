---
title: What Transfers Under Source Shift? Definitions, Examples, and Fine-Tuning for Climate Disclosure Classification
url: http://arxiv.org/abs/2607.17952v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_13-54-40Z_WhatTransfersUnderSourceShift_Definitions_Examples.md
generated_at: 2026-07-23 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how climate disclosure classification adapts when moving from one source to another, such as annual reports to press releases or earnings calls. The authors evaluate three adaptation strategies — definitions, examples, and fine‑tuning — across eleven large language models using two corpora with identical labels but different sources, finding that simple approaches often outperform complex ones under source shift.

## Key Takeaways
- Retrieval‑based similarity and LoRA fine‑tuning give the largest in‑source gains but lose most of their advantage when the source changes.  
- Randomly selected few‑shot examples, a weaker baseline, retain their cross‑source performance more consistently across models.  
- Definitions transfer best only when their granularity matches that of the target text, suggesting precise label mapping is crucial.

## Context
The study addresses a growing need for robust AI systems to handle data from heterogeneous sources without retraining or extensive adaptation. As climate disclosure becomes central to ESG reporting, evaluating cross‑source performance helps ensure models remain reliable in real‑world applications where documents vary widely.

## Implications
For practitioners, the findings suggest that lightweight strategies like few‑shot examples are safer for deploying classification pipelines across disparate source types. Researchers should prioritize granularity alignment and avoid over‑relying on similarity or fine‑tuning when adapting to new sources.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.17952v1)
