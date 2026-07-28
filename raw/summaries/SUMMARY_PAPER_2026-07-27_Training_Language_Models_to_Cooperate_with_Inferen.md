---
title: Training Language Models to Cooperate with Inference-Time Controllers
url: http://arxiv.org/abs/2607.23771v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_17-44-33Z_TrainingLanguageModelstoCooperatewithInference_Tim.md
generated_at: 2026-07-27 23:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CALM, a post‑training framework that integrates inference‑time controllers directly into the training loop to address the mismatch between model optimization and real‑world workflows.

## Key Takeaways
- CALM treats controller insertion as part of the training objective, using multi‑task reinforcement learning where each local reasoning module is optimized for its role within a specific interaction protocol.
- The approach decomposes mixed‑controller scenarios into turn‑level gradient‑proportional‑reward (GRPO) updates, allowing systematic evaluation of how different controller compositions affect performance.
- Results show that models trained with CALM generalize better to unseen controllers than those fine‑tuned on a single fixed workflow.

## Context
Current LLM deployment often relies on ad‑hoc reasoning pipelines, yet most training data and optimization focus on one pipeline at a time, limiting adaptability. This creates a gap between what is learned offline and how models are used online.

## Implications
For practitioners, CALM suggests that future model releases should be accompanied by modular controller libraries to enable seamless integration with diverse workflows without retraining the base model.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23771v1)
