---
title: Auto-Fill: Learning to Predict Missing Values Accurately with Specialist Language Models
url: http://arxiv.org/abs/2607.19847v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_07-32-09Z_Auto_Fill_LearningtoPredictMissingValuesAccurately.md
generated_at: 2026-07-23 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Auto-Fill, a method that learns to predict missing values in tabular data by combining world knowledge, text-based reasoning, and code-based reasoning through three specialist small language models. It achieves higher accuracy than large frontier models while using less than 1% of their computational cost.

## Key Takeaways
- Achieving high precision requires integrating world knowledge, text-based reasoning, and code-based reasoning as separate capabilities.
- The Auto-Fill ensemble dynamically selects the most confident specialist or abstains to avoid hallucinations.
- Experiments on 11 benchmarks with real tables show superior accuracy over o3-pro, Gemini 3 Pro, DeepSeek R1 at a fraction of their cost.

## Context
Tabular data cleaning remains challenging because missing values often depend on complex interdependencies across rows and columns. Traditional reasoning models attempt holistic analysis but are computationally expensive and prone to errors. This work demonstrates that specialized components can outperform monolithic large models in precision.

## Implications
For industry practitioners, Auto-Fill offers a cost-effective alternative for automated data cleaning pipelines. Practitioners can deploy lightweight models that prioritize accuracy without the overhead of massive language models, enabling scalable real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19847v1)
