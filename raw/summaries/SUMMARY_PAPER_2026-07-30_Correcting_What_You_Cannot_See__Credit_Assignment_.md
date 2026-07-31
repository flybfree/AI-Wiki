---
title: Correcting What You Cannot See: Credit Assignment for Perception Distillation in Multimodal Reasoners
url: http://arxiv.org/abs/2607.28336v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_15-03-55Z_CorrectingWhatYouCannotSee_CreditAssignmentforPerc.md
generated_at: 2026-07-30 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Perception-Correction Distillation, a label-free method that distinguishes perception errors from reasoning failures in multimodal reasoners. By using downstream failure signals and teacher-student disagreement as witnesses, it improves performance on large models across benchmarks. The approach demonstrates that correcting perception can outperform focusing solely on reasoning distillation.

## Key Takeaways
- Perception Success Rate ambiguity is resolved by treating the product of two witness signals as a soft AND gate.
- The method relies on separated perception-reasoning rollouts with mean-preserving weights to keep the reasoning objective unchanged.
- Experiments show gains from 44.50 to 61.22 macro average across eight benchmarks.

## Context
Multimodal AI systems often conflate perceptual shortcomings with logical errors, limiting the utility of distillation techniques that rely on teacher predictions alone. This work addresses a key limitation by providing an objective measure for when perception correction is needed.

## Implications
Practitioners can apply Perception-Correction Distillation to refine large language models without additional supervision, enhancing robustness in real-world applications where perception errors are common. The approach offers a scalable way to improve model reliability across diverse tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28336v1)
