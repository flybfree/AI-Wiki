---
title: Scaling Laws for Looped Mixture of Experts
url: http://arxiv.org/abs/2609.40316v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-09-30_17-53-47Z_ScalingLawsforLoopedMixtureofExperts.md
generated_at: 2026-10-01 10:57
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces Loop Scaling Laws, the first framework to jointly model recurrence and sparsity alongside model size and data, addressing how looped transformers and Mixture-of-Experts complement each other for efficient scaling. The authors develop a bounded, sparsity-conditional recurrence mapping that predicts held-out loss more accurately than prior methods while recovering standard dense and MoE laws as special cases. Downstream evaluations demonstrate significant efficiency gains, showing that joint scaling of loops and experts yields superior performance on reasoning benchmarks compared to non-looped or sparse-only models.

## Key Takeaways
- The core contribution is a bounded, sparsity-conditional recurrence mapping that quantifies the effective-parameter gain from looping and demonstrates how increased sparsity amplifies this gain, allowing for precise modeling of the interaction between recurrent depth and expert sparsity.
- Empirical results reveal complementary benefits across scaling axes: sparsity provides approximately 3x active-parameter efficiency, while recurrence delivers roughly 2x total-parameter efficiency on reasoning tasks, with joint scaling further pushing the performance frontier beyond what either technique achieves alone.
- At trillion-token training scales, looped MoE models designed using these laws match the performance of non-looped MoEs with twice the parameter count under matched compute constraints, while uniquely enabling test-time scaling capabilities through recurrence without increasing active parameters during inference.

## Context
As large language models approach physical and economic limits of scaling, researchers are exploring architectural innovations like recurrence and sparsity to extend model capabilities without proportional increases in compute costs. Existing scaling laws have largely treated these mechanisms in isolation,

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.40316v1)
