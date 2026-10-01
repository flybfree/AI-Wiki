---
title: Scaling Laws for Looped Mixture of Experts
url: http://arxiv.org/abs/2609.40316v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_17-53-47Z_ScalingLawsforLoopedMixtureofExperts.md
generated_at: 2026-09-30 22:04
model: qwen3.6-35b-a3b
---

## Summary
This work introduces Loop Scaling Laws, the first scaling framework to jointly model recurrence and sparsity alongside model size and data for Looped Mixture-of-Experts architectures. The authors demonstrate that these laws accurately predict held-out loss, recover standard dense and MoE scaling laws as special cases, and reveal complementary efficiency gains where sparsity provides ~3x active-parameter efficiency and recurrence yields ~2x total-parameter efficiency on reasoning tasks.

## Key Takeaways
- Loop Scaling Laws utilize a bounded, sparsity-conditional recurrence mapping to characterize effective-parameter gain, showing how sparsity amplifies the benefits of looping while jointly modeling recurrence, sparsity, size, and data.
- Empirical evaluations confirm that sparsity delivers approximately 3x active-parameter efficiency and recurrence provides roughly 2x total-parameter efficiency on reasoning benchmarks, with joint scaling further pushing performance frontiers beyond individual axes.
- At trillion-token scale, law-derived looped MoE models match the performance of non-looped MoEs with twice the parameters under matched training compute, while uniquely enabling test-time scaling through recurrence mechanisms.

## Context
Existing research has largely treated recurrence and sparsity as independent scaling factors, failing to capture their synergistic effects in modern efficient transformer variants. This paper addresses that limitation by establishing a unified mathematical foundation for Looped MoEs, which are increasingly relevant as the field seeks to maximize performance within fixed compute budgets through architectural innovations like recurrent processing and expert routing.

## Implications
These scaling laws provide practitioners with a rigorous toolset for optimizing model design under compute and memory constraints, allowing for data-driven decisions on balancing recurrence depth and sparsity levels. The findings suggest that integrating looped architectures with MoE strategies can significantly reduce training costs while maintaining or improving reasoning capabilities, and they open new avenues for test-time scaling approaches that leverage recurrence to enhance inference efficiency

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.40316v1)
