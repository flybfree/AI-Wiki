---
title: Post-Training Science for Supervised Fine-Tuning
url: http://arxiv.org/abs/2609.01244v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_13-44-21Z_Post_TrainingScienceforSupervisedFine_Tuning.md
generated_at: 2026-09-01 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how various hyperparameters for supervised fine-tuning vary with model scale, architecture family, and dataset characteristics, aiming to discover transferable selection rules that reduce repeated experimentation. It conducts systematic sweeps across LoRA and full fine‑tuning on four customer‑generated SFT datasets, measuring learning rates, batch sizes, optimizer choices, and training epochs up to 235B parameters.

## Key Takeaways
- The optimal learning rate decreases roughly linearly with model parameter count and improves when using geometry‑aware optimizers compared to AdamW. - Full fine‑tuning requires larger batches than LoRA for models above 100B, while LoRA’s rank and α jointly determine the capacity of the adapter to capture task‑specific knowledge. - Validation loss correlates strongly with downstream performance across all model families, suggesting it can serve as a reliable ranking metric.

## Context
This work addresses a longstanding challenge in LLM fine‑tuning: the need for hyperparameter tuning that scales with model size and dataset complexity. By establishing systematic relationships between training settings and performance, the study reduces reliance on trial‑and‑error methods, supporting more reproducible and efficient deployment pipelines.

## Implications
For practitioners, these findings provide clear guidelines that can be applied across different model families without extensive re‑tuning effort. Industry adoption of such selection rules could accelerate product iteration cycles, lower compute costs, and improve the consistency between training objectives and customer‑defined evaluation criteria.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01244v1)
