---
title: Improving Test-Time Scaling with Adaptive Looped Transformers
url: http://arxiv.org/abs/2609.35748v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_17-56-55Z_ImprovingTest_TimeScalingwithAdaptiveLoopedTransfo.md
generated_at: 2026-09-29 02:06
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates how layer-reuse strategies impact test-time scaling as language model outputs grow longer. The authors propose TaH2, an adaptive looping framework that dynamically allocates additional decoding iterations only to tokens that genuinely benefit from further refinement, rather than applying fixed-depth looping uniformly. Experimental results demonstrate substantial improvements in both the efficiency and peak accuracy of test-time computation compared to non-looped baselines and conventional looped architectures.

## Key Takeaways
- Existing looped transformers frequently achieve steeper accuracy-compute slopes than non-looped models but underperform at matched compute budgets because fixed-depth looping wastes iterations on tokens that do not require further refinement.
- TaH2 introduces an adaptive iteration decider trained jointly with the backbone using lookahead depth supervision, which leverages online labels to predict whether additional decoding steps will improve token predictions before committing extra FLOPs.
- On challenging AIME benchmarks, TaH2 increases the accuracy-compute slope by 53% over a non-looped baseline and continues to scale positively up to an iteration depth of 8, whereas conventional looped models quickly plateau in performance gains.

## Context
As large language models increasingly rely on test-time compute to solve complex reasoning tasks, understanding how architectural choices like layer reuse impact scaling behavior becomes critical for both efficiency and capability development. While parameter-efficient techniques such as looped transformers have gained attention for reducing training costs, their actual utility during extended decoding phases remains poorly understood. This work bridges that gap by systematically evaluating and optimizing how looping strategies interact with test-time computational budgets.

## Implications
The proposed adaptive approach offers a practical pathway to enhance reasoning capabilities without proportionally increasing inference costs, making it highly relevant for resource-constrained deployment scenarios and real-world applications. Practitioners can leverage dynamic iteration allocation to maximize model performance on complex benchmarks while maintaining strict compute limits. Furthermore, the lookahead supervision framework could inspire new training paradigms that prioritize computational efficiency across various sequence modeling architectures beyond standard transformer designs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35748v1)
