---
title: Lost in the bf16 Cast: Exporting Ternary Language Models Can Revert Most Low-Learning-Rate Code Changes
url: http://arxiv.org/abs/2610.07853v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_06-58-35Z_Lostinthebf16Cast_ExportingTernaryLanguageModelsCa.md
generated_at: 2026-10-06 21:19
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper audits export pipelines for ternary language models such as BitNet b1.58, Falcon-E, and BitCPM, showing that casting latent weights to bf16 before ternary quantization can silently revert many low-learning-rate fine-tuning changes. It finds measurable disagreements between fp32 quantization of shipped latents and deployed ternary codes, especially when bf16 rounding places values exactly on quantization thresholds. The authors demonstrate severe accuracy drops in greedy GSM8K evaluation and propose compatibility remedies that preserve strict accuracy.

## Key Takeaways
- In released checkpoints, fp32 quantization of shipped latents disagrees with deployed codes on 0.83-1.77% of codes in Falcon-E and BitCPM and on 1.530% in BitNet 2B-4T, with most disagreements in Falcon-E and BitCPM arising from products that bf16 rounding lands exactly on the threshold and ties-to-even maps to zero.
- At fine-tuned endpoints selected to match a nominal learning-rate-to-bf16-ULP ratio, the documented export step can collapse strict accuracy, lowering greedy GSM8K strict accuracy from 58.79% to 0.78% for Falcon-E-1B-Base and from 36.13% to 0.39% for BitCPM-CANN-0.5B, while a bf16 save and reload lowers BitNet 2B-4T strict accuracy by 27.54 points even as last-number accuracy rises.
- Two remedies meet a 4-point strict-accuracy non-inferiority criterion against online evaluation across all three models: writing the training quantizer's codes directly, or adjusting bf16 inputs until unchanged export tools emit the desired codes; randomized interventions also support distance-dependent selection of codes changed by fine-tuning.

## Context
Ternary language models aim to reduce memory and compute costs by storing weights as ternary codes, but their practical deployment depends on export pipelines that convert higher-precision latent weights into deployed codes. This paper matters because it exposes a subtle numerical compatibility failure in widely used quantization workflows, where bf16 casting can erase small fine-tuning updates rather than faithfully preserving them.

## Implications
For practitioners, the findings warn that ternary model exports must be audited numerically, not assumed to preserve fine-tuned behavior, especially when learning rates are small relative to bf16 precision. For industry, the results suggest that model release pipelines, quantization tools, and evaluation protocols should include safeguards such as direct code export, threshold-aware rounding, or non-inferiority checks to avoid silent accuracy degradation in compressed language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07853v1)
