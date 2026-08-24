---
title: Enhancing LLMs in Predictive Political QA with Semi-Structured Data
url: http://arxiv.org/abs/2608.21218v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_15-27-28Z_EnhancingLLMsinPredictivePoliticalQAwithSemi_Struc.md
generated_at: 2026-08-23 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PSL, a dual‑view framework for predictive political question answering that leverages semi‑structured political records to improve LLM performance. By extracting stance signals and high‑order structure signals from actor profiles and interaction graphs, PSL consistently outperforms baselines across three datasets and multiple LLMs.

## Key Takeaways
- Stance signals capture issue‑specific preferences of actors, providing direct evidence for prediction tasks.
- Structure‑aware actor representations model indirect dependencies among political actors through an interaction graph.
- The complementary gains from stance and structure signals are confirmed by ablations on diverse real‑world datasets.

## Context
Predictive political QA is a challenging task that requires models to infer future behavior from rich, non‑structured historical data. Current LLM augmentation methods often treat external resources as static knowledge, neglecting dynamic relational cues that influence predictions.

## Implications
For AI researchers, PSL offers a practical pathway to integrate multi‑modal signals into political QA systems without overhauling existing architectures. Practitioners can apply the stance and structure extraction techniques to enhance model accuracy in real‑time applications such as policy forecasting and campaign analysis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21218v1)
