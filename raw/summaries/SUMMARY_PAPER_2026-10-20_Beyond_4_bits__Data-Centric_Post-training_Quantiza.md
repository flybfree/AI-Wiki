---
title: Beyond 4 bits: Data-Centric Post-training Quantization and Recovery
url: http://arxiv.org/abs/2610.28537v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_17-10-04Z_Beyond4bits_Data_CentricPost_trainingQuantizationa.md
generated_at: 2026-10-20 22:17
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates why post-training quantization (PTQ) collapses to chance-level accuracy at 2 bits and identifies three critical design choices—quantization representation, calibration data, and recovery fine-tuning data—that determine model quality at sub-4-bit precision. Across six dense and mixture-of-experts models ranging from 3.8B to 32B parameters, the authors demonstrate that vector codebook representations are the dominant factor in restoring usable models, and that calibration and recovery data must be chosen jointly rather than independently. The resulting recipe achieves 89–97% of full-precision QA accuracy at roughly 2.3 effective bits per weight while using 1.4 to 30 times less compute than quantization-aware-training baselines.

## Key Takeaways
- Quantization representation is the single largest factor in 2-bit model quality. Scalar PTQ pipelines collapse to chance-level accuracy, but vector codebooks restore usable models, making the choice of representation far more consequential than it is at 4 bits where these differences are negligible.
- The majority of remaining accuracy loss at 2 bits occurs specifically on generative tasks, and the magnitude of performance degradation is model-dependent, meaning that a one-size-fits-all quantization recipe cannot be applied uniformly across architectures.
- Calibration data and recovery fine-tuning data are coupled under short recovery budgets: the optimal recovery data depends on which calibration data was used, so the two must be selected jointly. The authors propose a recipe combining a vector codebook representation, a small task-aligned calibration mixture, and an inexpensive codebook-only recovery stage, achieving 89–97% full-precision QA accuracy at 2.3 effective bits per weight and 1.4–30× less compute than the strongest QAT baseline.

## Context
Post-training quantization has become a standard technique for deploying large language models on resource-constrained hardware, with 4-bit quantization widely regarded as near-lossless. However, the push toward 2-bit and sub-2-bit compression—driven by the need to serve models on edge devices, mobile phones, and low-power inference hardware—has revealed that scalar quantization methods fail catastrophically at these lower bit-widths. This paper addresses a gap in the literature by treating representation, calibration, and recovery not as minor implementation details but as first-class design decisions that determine whether a 2-bit model is usable or effectively random.

## Implications
For practitioners deploying large models on constrained hardware, this work provides a concrete, compute-efficient recipe that outperforms quantization-aware training by up to 30× in compute cost while retaining high QA accuracy, making sub-4-bit deployment practical without expensive retraining. For the broader field, the finding that calibration and recovery data are coupled challenges the common practice of selecting them independently and suggests that future PTQ tooling should treat data selection as a joint optimization problem. The model-dependent nature of generative-task degradation also signals that quantization recipes must be tailored per architecture rather than applied as universal defaults.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28537v1)
