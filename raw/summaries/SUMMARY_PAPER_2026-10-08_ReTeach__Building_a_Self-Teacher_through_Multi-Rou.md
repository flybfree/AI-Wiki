---
title: ReTeach: Building a Self-Teacher through Multi-Round Reflection and Retry
url: http://arxiv.org/abs/2610.11529v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_08-58-01Z_ReTeach_BuildingaSelf_TeacherthroughMulti_RoundRef.md
generated_at: 2026-10-08 21:04
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ReTeach introduces a reflective self-distillation framework that builds a self-teacher through multi-round reflection and retry, using only self-generated attempts and outcome-level verification without requiring reference answers, external feedback, or cross-example memory. The framework demonstrates that iterative self-correction can meaningfully improve reasoning performance, achieving a 1.39 percentage point average accuracy improvement over GRPO across six benchmarks spanning mathematical reasoning, science question answering, and tool use.

## Key Takeaways
- ReTeach constructs its self-teacher by starting from an unsuccessful student rollout and alternating explicit reflection with renewed attempts until success or the retry budget is exhausted. This process relies solely on self-generated attempts and outcome-level verification, eliminating the need for reference answers, external diagnostic feedback, or persistent cross-example memory that prior reflection-based methods typically depend on.
- The framework employs an outcome-aware selection and weighting strategy that categorizes examples into initially correct, reflection-corrected, and unresolved groups, assigning separate weights to their category-normalized distillation losses. This ensures that the distillation signal is calibrated according to the actual utility of the teacher context rather than treating all examples uniformly.
- Through on-policy distillation, the student matches the teacher's context-conditioned token-level predictive distributions at prefixes of its own rollouts, effectively transferring the benefits of iterative multi-round correction while retaining single-pass inference at deployment time, making the approach practical for real-world inference without additional computational overhead.

## Context
Self-distillation and self-improvement methods represent a growing frontier in AI research, aiming to enhance model reasoning without the cost and complexity of training a separate, more capable teacher model. Prior approaches in this space have typically relied on reference solutions, rich task feedback, or persistent memory to give the self-teacher a meaningful advantage over the student. ReTeach addresses a practical gap by demonstrating that reflection and retry mechanisms alone, grounded only in outcome-level verification, can produce sufficient teacher-student advantage to drive meaningful performance gains, making self-improvement more accessible in settings where ground-truth references are unavailable or expensive to obtain.

## Implications
For practitioners deploying reasoning models in domains where reference answers are scarce or costly to produce, ReTeach offers a pathway to improve model performance through self-generated iterative correction without requiring curated datasets or external feedback loops. The finding that a 1.39 percentage point improvement over GRPO is achievable across diverse task types suggests that multi-round reflection can be a broadly applicable augmentation strategy for reinforcement learning-based training pipelines. For the broader field, this work signals that self-improvement mechanisms need not depend on privileged information, potentially expanding the applicability of self-distillation to open-ended and real-world reasoning tasks where verification signals are limited to binary success or failure.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11529v1)
