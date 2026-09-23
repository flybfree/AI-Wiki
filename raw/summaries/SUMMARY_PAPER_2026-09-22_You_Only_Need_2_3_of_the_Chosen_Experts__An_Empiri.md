---
title: You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs
url: http://arxiv.org/abs/2609.25809v1
type: paper-summary
date: 2026-09-22
source_paper: 2026-09-22_07-39-35Z_YouOnlyNeed2_3oftheChosenExperts_AnEmpiricalStudyo.md
generated_at: 2026-09-22 20:10
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This paper provides a systematic empirical evaluation of dynamic expert pruning in fine-grained Mixture-of-Experts (MoE) Large Language Models (LLMs). The researchers demonstrate that expert selection is significantly more redundant than previously assumed, showing that retaining approximately two-thirds of the selected experts preserves 98.8% of performance across various benchmarks including mathematics and code generation.

## Key Takeaways
- High Redundancy in Fine-Grained MoEs: The study reveals that fine-grained MoE architectures contain substantial redundancy; specifically, a simple uniform truncation strategy—retaining about two-thirds of the selected experts—preserves nearly all performance across diverse tasks like knowledge QA and general reasoning.
- Comparison with Existing Pruning Rules: At conservative budgets, the best currently published pruning rules differ from simple uniform truncation by less than 1%, suggesting that complex dynamic allocation methods may not be necessary for standard efficiency gains.
- Performance under Aggressive Pruning: The value of sophisticated dynamic allocation only becomes significant during aggressive pruning, where it can recover up to 3% more performance than uniform truncation, particularly in generative tasks that suffer from sharp degradation.
- Model-Specific Sensitivity: The research identifies that model architecture significantly impacts pruning resilience; larger "thinking" models are notably more robust to expert reduction, whereas multimodal models are much more vulnerable to aggressive pruning.

## Context
As MoE architectures have become the standard for training large-scale open-weight LLMs due to their parameter efficiency, optimizing inference costs has become a primary goal for researchers and practitioners. This paper addresses a critical gap in understanding how much computation can be safely discarded in fine-grained regimes compared to the coarser architectures previously studied.

## Implications
These findings suggest that developers can achieve significant speedups (1.2x–1.7x) using simple, one-integer change pruning methods without sacrificing model accuracy at moderate budgets. For the industry, this clarifies the trade-offs between inference efficiency and model types, highlighting that while many models are highly resilient to pruning, multimodal systems require much more careful management during optimization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.25809v1)
