---
title: Noise-Aware Shrinkage for Differentially Private Zeroth-Order Fine-Tuning of Large Language Models
url: http://arxiv.org/abs/2608.03277v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_07-52-23Z_Noise_AwareShrinkageforDifferentiallyPrivateZeroth.md
generated_at: 2026-08-05 01:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SAGE, a noise‑aware shrinkage method for differentially private zeroth‑order fine‑tuning of large language models. By estimating the signal energy from observed second moments and tracking it over time, SAGE adaptively reduces the impact of noisy updates while preserving useful descent, outperforming existing DP‑ZO baselines on several benchmarks.

## Key Takeaways
- The method subtracts the known Gaussian noise variance from the observed second moment to estimate underlying signal energy.  
- It stabilizes this estimate through temporal tracking and compares it with a warm‑up reference to compute a bounded shrinkage factor.  
- SAGE requires only constant additional state, adds no extra privacy budget or model queries, and is applied purely as post‑processing.

## Context
Differentially private zeroth‑order optimization allows fine‑tuning large language models using only forward passes, which is crucial for memory efficiency in low‑resource settings. Existing aggregation‑based approaches treat all updates uniformly, leading to suboptimal performance when noise dominates certain gradients. This work addresses that limitation by tailoring shrinkage to the quality of each update.

## Implications
SAGE demonstrates that adaptive post‑processing can improve model utility without sacrificing privacy or query efficiency. Practitioners can adopt SAGE to fine‑tune large models on limited compute and memory, achieving higher accuracy under the same differential privacy constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03277v1)
