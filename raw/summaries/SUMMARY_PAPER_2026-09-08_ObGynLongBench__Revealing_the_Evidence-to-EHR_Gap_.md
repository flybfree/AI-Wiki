---
title: ObGynLongBench: Revealing the Evidence-to-EHR Gap in Longitudinal EHR Decision-Making
url: http://arxiv.org/abs/2609.07601v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_15-12-36Z_ObGynLongBench_RevealingtheEvidence_to_EHRGapinLon.md
generated_at: 2026-09-08 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ObGynLongBench, a rule‑grounded long‑context EHR benchmark for obstetric and gynecologic decision‑making that contains 1,500 clinical cases with traceable rules. Evaluating 17 large language models shows an evidence‑to‑EHR gap: performance is high when evidence is supplied directly but drops sharply when the model must extract information from same‑day records or full pre‑decision histories.

## Key Takeaways
- Models perform well only when evidence is directly provided; accuracy declines when extracting evidence from same‑day EHRs.  
- Performance decreases with longer EHR contexts and more complex evidence requirements, and earlier failures often predict later failures within the same patient history.  
- Active‑search agents outperform other strategies, indicating that patient‑specific evidence utilization is a central bottleneck.

## Context
This work moves beyond static question‑answering benchmarks to examine how LLMs handle longitudinal, unstructured EHR data in real clinical settings. It contributes to understanding the challenges of extracting and utilizing medical evidence over time within complex patient histories.

## Implications
The findings highlight that reliable personalized medical assistants must overcome evidence retrieval obstacles and adapt to individual patient records. These insights are crucial for developing robust AI tools for obstetric‑gynecologic care and for broader clinical decision‑support systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.07601v1)
