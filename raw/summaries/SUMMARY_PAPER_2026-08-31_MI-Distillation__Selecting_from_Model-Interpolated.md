---
title: MI-Distillation: Selecting from Model-Interpolated Instruct-Reasoning Data Spectrum for Chain-of-Thought Distillation
url: http://arxiv.org/abs/2608.29623v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_07-32-22Z_MI_Distillation_SelectingfromModel_InterpolatedIns.md
generated_at: 2026-08-31 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a new distillation method called MI-Distillation that selects from model-interpolated instruction-reasoning data to improve chain-of-thought student models. It shows that long chain-of-thought trajectories produce larger gradients and more concentrated updates than short ones, especially for larger students. The framework balances reasoning density with distributional alignment.

## Key Takeaways
- Long CoT induces larger gradient magnitudes and more concentrated update directions compared to Short CoT, a trend that intensifies as student capacity grows.
- Effective distillation must balance the density of reasoning information in trajectories with their alignment to the student model’s distribution.
- The proposed MI-Distillation framework constructs a continuous spectrum via model interpolation and uses SeqLSS to select informative yet learnable paths.

## Context
Large reasoning models are increasingly used for complex tasks, but compressing them into smaller students remains difficult. Traditional distillation often relies on either long or short chain-of-thought examples, each with limitations in gradient signal strength and learning efficiency. This work addresses the gap by introducing a principled selection mechanism that leverages model interpolation.

## Implications
For practitioners, MI-Distillation offers a scalable approach to training efficient reasoning students without sacrificing performance. In industry, it could reduce compute costs while maintaining high-quality outputs from large models. The method highlights the importance of gradient dynamics in knowledge transfer, guiding future research on distillation strategies for complex AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29623v1)
