---
title: Resample the Answer: Where to Spend Test-Time Compute in Recursive Reasoning
url: http://arxiv.org/abs/2610.16427v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_08-55-25Z_ResampletheAnswer_WheretoSpendTest_TimeComputeinRe.md
generated_at: 2026-10-14 00:49
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates where to allocate test-time compute in recursive reasoning models like the Tiny Recursive Model (TRM), which iteratively refine an answer state and a reasoning state. Through controlled experiments, the author demonstrates that failures in these models are encoded in the answer state rather than the reasoning state, and that resampling the answer state recovers significantly more failures than perturbing the reasoning state at equivalent compute budgets. The proposed method, Gated Answer Resampling (GAR), leverages the model's own halting head to selectively restart only rejected puzzles, dramatically improving accuracy without any additional training or hyperparameter tuning.

## Key Takeaways
- A failed trajectory in a recursive reasoning model carries its failure in the answer state (y), not the reasoning state (z). This means that perturbing or resampling the reasoning state is largely ineffective at recovering from bad basins, while resampling the answer state directly addresses the root cause of the failure. This finding challenges the prevailing assumption that reasoning-state perturbations are the primary lever for test-time recovery.
- At equal compute budgets in both depth and width, resampling the answer state recovers more failures than any tested perturbation of the reasoning state, and the performance gap widens as the test-time compute budget grows. This scaling property suggests that answer-state resampling is not merely a marginal improvement but a fundamentally more efficient use of test-time compute that compounds with additional budget.
- GAR achieves 99.4% on Sudoku-Extreme (up from 85.9%) and 85.6% on Pencil Puzzle Bench validation (up from 68.8%) using at most 64 restarts per puzzle, with no training or hyperparameter search. It outperforms Probabilistic TRM (PTRM), which perturbs z at every step, even when PTRM consumes 42 to 197 times more compute, demonstrating that targeted answer-state resampling is vastly more compute-efficient than indiscriminate reasoning-state perturbation.

## Context
Recursive reasoning models represent a growing class of architectures that iteratively refine internal latent states to solve complex puzzles and reasoning tasks, distinct from the chain-of-thought approaches used in large language models. The question of how to best allocate test-time compute—whether to deepen the recursion, widen the search, or perturb specific latent states—has become a central concern as these models are deployed on increasingly difficult benchmarks. This paper directly addresses a gap in the literature by providing controlled, apples-to-apples comparisons of different test-time intervention strategies, establishing a clear hierarchy of which latent state to target for maximum recovery per unit of compute.

## Implications
For practitioners deploying recursive reasoning models in puzzle-solving, planning, or structured reasoning tasks, this work provides a concrete, training-free recipe for boosting accuracy by selectively restarting only the model's own rejected outputs, dramatically reducing the compute overhead compared to blanket perturbation strategies. For the broader field, the finding that failures are encoded in the answer state rather than the reasoning state reshapes how researchers should design test-time scaling strategies for any model with a similar dual-state architecture, potentially redirecting effort away from reasoning-state perturbation methods and toward answer-state correction mechanisms. The compute-efficiency advantage over PTRM by a factor of 42 to 197 also has practical implications for inference cost and latency in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16427v1)
