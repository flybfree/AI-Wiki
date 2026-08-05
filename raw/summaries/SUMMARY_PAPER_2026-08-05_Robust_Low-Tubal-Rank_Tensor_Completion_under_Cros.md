---
title: Robust Low-Tubal-Rank Tensor Completion under Cross-Concentrated Sampling
url: http://arxiv.org/abs/2608.03928v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_16-59-58Z_RobustLow_Tubal_RankTensorCompletionunderCross_Con.md
generated_at: 2026-08-05 01:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Robust Iterative t-CUR (R‑ItCUR), a method for recovering third‑order low‑tubal‑rank tensors from partially observed cross‑concentrated samples that contain arbitrarily large outliers. The algorithm works directly on the sampled tensor cross, avoiding full reconstruction and thus saving memory and computation. Experiments show accurate recovery and strong robustness to sparse gross corruptions.

## Key Takeaways
- R‑ItCUR partitions the t‑CCS sample into two exterior blocks and an intersection block to enable adaptive Welsch correction for outlier suppression.
- The method updates the low‑rank component via projected blockwise gradient descent, operating entirely on the sampled cross without reconstructing the full tensor.
- Robustness is demonstrated across synthetic tensors, cardiac MRI data, and three‑dimensional seismic data, showing accurate recovery despite large sparse outliers.

## Context
Tensor completion remains a challenging problem in AI where missing data often includes corrupted entries. Existing t‑CCS methods assume clean observations, limiting their applicability to real‑world noisy datasets. This work addresses that gap by integrating robust outlier handling directly into the completion pipeline.

## Implications
The approach enables practical tensor completion for medical imaging and geoscience applications where data integrity is critical. By preserving memory efficiency and computational cost while maintaining robustness, R‑ItCUR can be deployed in large‑scale systems without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03928v1)
