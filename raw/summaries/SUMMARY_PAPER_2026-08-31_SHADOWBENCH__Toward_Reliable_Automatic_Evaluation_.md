---
title: SHADOWBENCH: Toward Reliable Automatic Evaluation of Semantic Alignment in Autoformalization
url: http://arxiv.org/abs/2608.29270v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_13-49-20Z_SHADOWBENCH_TowardReliableAutomaticEvaluationofSem.md
generated_at: 2026-08-31 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SA-Pass and ShadowBench to evaluate semantic alignment in autoformalization, achieving high agreement with expert judgments. It shows that a generated statement receives full credit only when it compiles, implies each shadow, and is implied by their conjunction. Across multiple agent configurations, SA-Pass achieves 98.8% binary agreement with experts.

## Key Takeaways
- SA-Pass requires both compile-time success and implication checks via shadows to ensure semantic correctness beyond syntax.
- ShadowBench contains 178 problems across eight mathematical areas, providing a diverse evaluation set for autoformalization.
- Expert judgments align with SA-Pass at 98.8%, indicating strong reliability in the proposed metric.

## Context
Autoformalization aims to translate informal theorems into formal code for proof assistants like Lean, but current evaluation metrics are limited and often accept type-correct yet misaligned statements or reject correct ones due to different formulations. This work addresses the need for reliable semantic alignment in automated theorem generation.

## Implications
Reliable evaluation is crucial for trustworthy AI agents that produce correct proofs, as it ensures that generated code truly reflects intended mathematical content. The benchmark and SA-Pass provide a standard for evaluating autoformalization systems, guiding both research and industry adoption.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29270v1)
