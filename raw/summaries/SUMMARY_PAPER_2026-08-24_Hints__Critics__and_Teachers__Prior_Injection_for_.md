---
title: Hints, Critics, and Teachers: Prior Injection for Sparse-Reward RL in Vision-Language Math Reasoning
url: http://arxiv.org/abs/2608.21811v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_07-17-14Z_Hints_Critics_andTeachers_PriorInjectionforSparse_.md
generated_at: 2026-08-24 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how prior knowledge can alleviate the sparse‑reward problem in vision‑language math reasoning, training eleven reinforcement‑learning methods that inject either textual hints, on‑policy distributions, or value‑based priors. It finds that only six of the arms benefit from a well‑aligned prior while five remain ineffective, and it uncovers an unexpected anti‑correlation between in‑domain performance and cross‑domain transfer.

## Key Takeaways
- A prior improves learning exactly when it reaches the policy; otherwise the no‑prior baseline and teacher‑capped or misparameterized arms perform similarly.  
- Evaluation of a long‑used general‑distribution slice shows a Spearman rank correlation of –0.74 with genuine cross‑domain transfer, while the hardest in‑domain slice correlates positively at 0.89, indicating that some methods are evaluated on near‑chance multiple‑choice subsets.  
- Hint‑guided exploration yields gains, and swapping the critic’s MSE loss for HL‑Gauss categorical cross‑entropy boosts accuracy by about 14.4 points.

## Context
Vision‑language models must solve math problems from images, but rewards are extremely rare, making gradient updates scarce. Prior injection is a known technique to guide learning when data is sparse, yet its impact on evaluation remains unclear. This work adds empirical evidence that prior design can both help and mislead performance metrics.

## Implications
For practitioners, the paper warns against trusting in‑domain scores that do not align with cross‑domain behavior, especially when priors are poorly integrated. It also suggests using hint‑based exploration and categorical loss functions to improve real‑world reasoning accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21811v1)
