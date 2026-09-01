---
title: Training-Free Action Correction for VLA Model Failures via Language Feedback
url: http://arxiv.org/abs/2608.29967v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_18-54-03Z_Training_FreeActionCorrectionforVLAModelFailuresvi.md
generated_at: 2026-08-31 22:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CorrectVLA, a method that corrects Vision-Language-Action model failures by translating human task-level corrections into uniform additive adjustments to action magnitudes without retraining the policy. Experiments show the approach recovers execution misalignment errors in both simulated and real-world settings where the base model fails. The framework distinguishes between correctable execution misalignments and uncorrectable semantic comprehension breakdowns.

## Key Takeaways
- CorrectVLA applies a single task-level correction uniformly across all rollouts, modifying only action magnitude rather than policy weights.
- It successfully recovers tasks that suffer from execution misalignment failures on both in-distribution and out-of-distribution scenarios.
- The method is limited to failure modes where the policy reaches the correct target but miscalibrates magnitudes; it cannot fix semantic comprehension failures.

## Context
Vision-Language-Action models excel at understanding language instructions yet often fail during deployment due to execution errors. Traditional fixes require retraining, which is costly and impractical for real-time systems. This work offers an inference‑time correction that can be deployed alongside the model.

## Implications
Practitioners can now apply simple textual feedback to improve robot actions without disrupting training pipelines. The approach sets a clear operational boundary: it works when policies are strategically correct but fails where underlying understanding is broken, guiding where to invest in better comprehension models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29967v1)
