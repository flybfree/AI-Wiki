---
title: Lost in the bf16 Cast: Exporting Ternary Language Models Can Revert Most Low-Learning-Rate Code Changes
published: 2026-10-06T06:58:35Z
authors: Avichal Sahai, Nishant Raj, Animesh Srivastava
url: http://arxiv.org/abs/2610.07853v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lost in the bf16 Cast: Exporting Ternary Language Models Can Revert Most Low-Learning-Rate Code Changes

## Abstract
Ternary language models such as BitNet b1.58, Falcon-E and BitCPM are fine-tuned with higher-precision latent weights and deployed as ternary codes produced by an export step that, in the labs' documented pipelines, first casts the latents to bf16. We audit those pipelines across three labs. In released checkpoints, fp32 quantization of the shipped latents disagrees with the deployed codes on 0.83-1.77% of codes in Falcon-E and BitCPM and on 1.530% in BitNet 2B-4T; for Falcon-E and BitCPM most disagreements are products that bf16 rounding lands exactly on the threshold, which ties-to-even maps to zero, and the unmodified onebitllms exporter reproduces all four Falcon-E releases byte for byte. At fine-tuned endpoints, with learning rates selected to match a nominal learning-rate-to-bf16-ULP ratio, the documented export lowers greedy GSM8K strict accuracy from 58.79% to 0.78% for Falcon-E-1B-Base and from 36.13% to 0.39% for BitCPM-CANN-0.5B, and a bf16 save and reload lowers BitNet 2B-4T's strict accuracy by 27.54 points while its last-number accuracy rises. Two compatibility remedies, writing the training quantizer's codes directly or adjusting the bf16 inputs until the unchanged tools emit them, each met a 4-point strict-accuracy non-inferiority criterion against online evaluation in all three models. In two model families, randomized interventions on the initial distance from the threshold support distance-dependent selection of the codes that fine-tuning changes.

## Metadata
- **Published**: 2026-10-06T06:58:35Z
- **Authors**: Avichal Sahai, Nishant Raj, Animesh Srivastava
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07853v1)