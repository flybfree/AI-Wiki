---
title: TailSFT: Filtered Fine-Tuning Improves Post-Training Performance
url: http://arxiv.org/abs/2608.25756v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_13-04-08Z_TailSFT_FilteredFine_TuningImprovesPost_TrainingPe.md
generated_at: 2026-08-26 20:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TailSFT, a modification of supervised fine‑tuning that removes already well‑covered data points so the model learns from the tail distribution. On OLMo‑3 7B it raises pass@16 on math and coding by up to 17 percentage points with little extra compute. The improved checkpoints then boost GRPO pass@1 by about 4 points, showing TailSFT yields better RL starting points.

## Key Takeaways
- TailSFT filters out already fit sequences during supervised fine‑tuning, focusing learning on under‑modeled regions of the data distribution.
- On OLMo‑3 7B the method improves pass@16 performance by up to 17 percentage points while keeping computational overhead minimal.
- The higher coverage checkpoints derived from TailSFT translate into about 4 percentage point gains in subsequent reinforcement learning evaluations.

## Context
Modern AI systems rely on post‑training reinforcement learning to unlock reasoning abilities, but the quality of the fine‑tuned checkpoint often limits RL success. This work shows that a simple data‑filtering step can produce checkpoints with higher coverage, which are more effective as starting points for RL training.

## Implications
Researchers and practitioners should consider stage‑aware model development, evaluating intermediate checkpoints by their suitability for downstream tasks like reinforcement learning. TailSFT offers a practical way to improve both supervised and RL performance without costly re‑training.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25756v1)
