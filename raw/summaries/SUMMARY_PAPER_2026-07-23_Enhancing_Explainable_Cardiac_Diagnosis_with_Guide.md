---
title: Enhancing Explainable Cardiac Diagnosis with Guide-Grounded Multimodal LLMs
url: http://arxiv.org/abs/2607.20814v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_01-00-10Z_EnhancingExplainableCardiacDiagnosiswithGuide_Grou.md
generated_at: 2026-07-23 22:36
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a guide‑grounded multimodal framework that improves the interpretability and reliability of deep learning models for ECG analysis. By integrating Grad‑CAM heatmaps, CNN class probabilities, and an offline‑distilled clinical interpretation guide into a multimodal LLM prompt, the system generates diagnostic reports that align closely with established guidelines. Experiments on PTB‑XL show a significant boost in BERTScore from 0.818 to 0.953 compared to a baseline CNN+Grad‑CAM+MLLM model.

## Key Takeaways
- The framework uses an offline distillation of ECG textbooks into a structured guide that is injected as a fixed knowledge block for every sample, ensuring reports are grounded in clinical criteria.
- Adding this guide raises the average BERTScore from 0.818 to 0.953, indicating closer alignment with reference reports and reduced hallucinations.
- The method maintains competitive classification performance while delivering more consistent and trustworthy diagnostic language.

## Context
Current deep learning systems for ECG interpretation often produce explanations that are not anchored in medical guidelines, leading to potential misinterpretation or loss of clinical credibility. This work addresses the need for explainable AI by embedding authoritative knowledge directly into the generation pipeline, a step toward practical deployment in healthcare settings.

## Implications
Clinicians and developers can rely on more trustworthy LLM‑generated ECG reports that follow standard diagnostic language, potentially increasing adoption of AI tools in cardiology. The approach also serves as a template for grounding other multimodal models with domain‑specific knowledge to mitigate hallucinations and improve explainability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20814v1)
