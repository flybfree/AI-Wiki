---
title: Fusion Training for Mathematical Generalization in Large Language Models
url: http://arxiv.org/abs/2608.09893v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_17-41-19Z_FusionTrainingforMathematicalGeneralizationinLarge.md
generated_at: 2026-08-10 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates the training dynamics of Thinking Mode Fusion (TMF) in large language models, focusing on how the ratio of non‑thinking to thinking supervision and the order of training affect performance on mathematical problem solving. It finds that increasing non‑thinking data reduces thinking accuracy and that optimal schedules depend on this ratio.

## Key Takeaways
- Increasing the proportion of non‑thinking supervision lowers the accuracy of the thinking mode, indicating a negative feedback between modes.
- The effect is not constant; different training schedules can mitigate or amplify this trade‑off depending on the data ratio.
- An inherent tension exists between the two modes, and the best schedule must balance both types of supervision.

## Context
Large language models often need to switch between concise answers and deep reasoning, yet current designs treat these as separate components. TMF seeks to merge them into a single model, but empirical guidance on training remains scarce.

## Implications
Designers can use this study to choose schedules that preserve reasoning quality while maintaining efficiency. The insights may improve real‑world applications where both speed and depth are required, reducing the need for costly dual‑model setups.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09893v1)
