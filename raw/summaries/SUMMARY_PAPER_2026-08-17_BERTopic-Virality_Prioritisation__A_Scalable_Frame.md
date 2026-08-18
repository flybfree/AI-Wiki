---
title: BERTopic-Virality Prioritisation: A Scalable Framework for Thematic and Comparative Analysis of COVID-19 and Monkeypox Misinformation on Twitter
url: http://arxiv.org/abs/2608.15691v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_11-42-37Z_BERTopic_ViralityPrioritisation_AScalableFramework.md
generated_at: 2026-08-17 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces BERTopic-VP, a framework that merges BERTopic’s embedding‑based clustering with a virality‑prioritisation layer to rank COVID‑19 and Monkeypox misinformation on Twitter. The system also integrates a two‑stage hybrid misinformation detector using supervised classification and public‑health knowledge signals, achieving high F1 scores (up to 0.95) and ROC‑AUC (up to 0.989). It can surface low‑volume but high‑risk narratives even when engagement data are absent.

## Key Takeaways
- The framework combines semantic clustering with a virality‑prioritisation score, allowing topics that are both coherent and rapidly spreading to be identified within the top 1%, 5% or 10% of VP rankings.  
- When native engagement metadata are unavailable, BERTopic-VP relies on a logistic propensity‑to‑spread model as an ordinal proxy for diffusion potential rather than direct engagement metrics.  
- The hybrid misinformation detection module fuses a supervised content classifier with external verification signals from public‑health knowledge bases to improve classification performance.

## Context
The rapid spread of health misinformation during pandemics poses challenges for AI systems that rely on traditional topic modelling, which often ignores diffusion dynamics. BERTopic-VP addresses this gap by embedding virality into the clustering process, offering a more nuanced view of emerging narratives in real‑time social media streams.

## Implications
For researchers and practitioners monitoring public health information, BERTopic-VP provides a scalable tool to prioritize high‑risk clusters for analyst review, enabling earlier intervention. The approach can be adapted across domains where semantic coherence and rapid spread are critical, enhancing the utility of AI in crisis communication.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15691v1)
