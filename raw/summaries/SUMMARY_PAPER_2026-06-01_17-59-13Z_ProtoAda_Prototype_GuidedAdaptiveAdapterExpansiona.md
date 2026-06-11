---
title: ProtoAda: Prototype-Guided Adaptive Adapter Expansion and Geometric Consolidation for Multimodal Continual Instruction Tuning
url: http://arxiv.org/abs/2606.02576v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-01_17-59-13Z_ProtoAda_Prototype_GuidedAdaptiveAdapterExpansiona.md
generated_at: 2026-06-11 10:51
model: nvidia/nemotron-3-nano-4b
---

## Summary
ProtoAda introduces a prototype‑guided adaptive framework for multimodal continual instruction tuning that aligns task assignment with both semantic meaning and output structure, while consolidating format‑compatible updates in a geometry‑aware manner. The method reduces inter‑task interference by preventing similar visual‑linguistic semantics from sharing parameters across tasks with different response formats, thereby improving performance especially on tasks whose answer structures are easily corrupted by sequential tuning.

## Key Takeaways
- ProtoAda uses format‑aware task prototypes to route tasks based on both semantic similarity and expected output structure, avoiding the pitfalls of image‑text similarity alone.  
- It consolidates updates for compatible formats in a geometry‑aware way, reusing existing parameters and progressively refining them.  
- Experiments show superior results on benchmarks where sequential tuning would otherwise degrade answer structures.

## Context
Multimodal continual instruction tuning is crucial as large language models must keep learning new vision‑language capabilities without degrading prior knowledge. Existing approaches often rely on sparse routing that ignores response format, leading to harmful parameter sharing and gradient interference.

## Implications
ProtoAda offers a practical solution for deploying MLLMs in real‑world settings where tasks evolve over time, ensuring stable performance across diverse answer formats. Practitioners can adopt this framework to maintain high accuracy while minimizing the need for extensive retraining.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.02576v1)
