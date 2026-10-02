---
title: Closing the Loop: Practical Training Recipes for Looped Language Models
url: http://arxiv.org/abs/2610.00673v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-09-30_20-09-58Z_ClosingtheLoop_PracticalTrainingRecipesforLoopedLa.md
generated_at: 2026-10-01 21:32
model: qwen3.6-35b-a3b
---

## Summary
This paper establishes practical training recipes for looped language models to make them more efficient and accessible, demonstrating that recurrence can be effectively leveraged without massive compute budgets or complex multi-stage schedules. The authors present a from-scratch pipeline that drastically reduces token requirements while maintaining strong reasoning performance, show that their 1.4B LoopLM outperforms parameter-matched dense models across multiple benchmarks, and introduce a minimal conversion method for existing pretrained checkpoints.

## Key Takeaways
- The authors develop a compute-efficient training pipeline that reduces the pretraining budget from 7.7 trillion tokens to just 310 billion tokens compared to previous methods like Ouro, achieving stable recurrent training through pretraining followed by high-quality mid-training, learning-rate warmup, and enhanced exit-gate regularization without needing prior multi-stage schedules.
- Under controlled comparisons, the proposed 1.4B LoopLM model surpasses a parameter-matched dense model trained on identical data and token budgets across all 12 evaluated benchmarks, showing significant gains such as +14 points on GSM8K and +22 on DROP, while approaching the performance of a 3.9B dense model at matched inference compute using only 36% of the parameters.
- A minimal recipe is introduced to convert pretrained dense models into looped architectures by adding a single learned input-mixing scalar and applying a smoothed exit loss, which requires no step-specific parameters; when applied to Qwen3-1.7B-Base, this approach yields statistically clear improvements on reasoning benchmarks like GSM8K, MATH, and MMLU-Pro across different data regimes compared to

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.00673v1)
