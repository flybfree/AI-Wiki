---
title: The Limits of Simulated Societies: How Post-Training and Survey Fine-Tuning Erase Cross-Cultural Variance
published: 2026-09-22T06:55:46Z
authors: Rojin Ziaei
url: http://arxiv.org/abs/2609.25760v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Limits of Simulated Societies: How Post-Training and Survey Fine-Tuning Erase Cross-Cultural Variance

## Abstract
Using large language models (LLMs) to simulate diverse human populations has the potential to transform many aspects of computational social science, yet many evaluations score the average response rather than the spread of opinion within real groups. Here, we develop a diagnostic framework that measures point accuracy alongside dispersion retention, the ratio of predicted to human standard deviation ($\dr$), on 10{,}000 respondent--question pairs from the World Values Survey (WVS) spanning twelve countries and six continents. We evaluate eleven zero-shot language models and five variants fine-tuned on WVS data with SFT, DPO, and GRPO. We identify a failure mode we term \textit{consensus collapse}, where alignment training compresses outputs toward one stereotype per group. Along the post-training trajectory from the Llama~3.1 70B base to the Tulu~3 checkpoints, the first stage, supervised instruction tuning, removes half of the spread with minimal accuracy gain ($\dr$ 1.22 to 0.59; accuracy $+0.9$ points), the later stages do not restore it, and a gap opens between WEIRD and non-WEIRD countries that survey fine-tuning then deepens while pursuing higher point accuracy. The most accurate model (Tulu~3 70B-DPO fine-tuned on WVS, 57.9\%) keeps half the human spread overall ($\dr = 0.50$) and 11\% of it for Nigeria, against 0.70--0.87 for WEIRD countries. Raising the sampling temperature to 1.0 leaves the Wasserstein-1 distance ($\wone$) to human distributions unchanged for both fine-tuned DPO models, and GRPO on Qwen~3.5 9B does not restore the spread under either an accuracy reward or a distribution-shaped reward. Mixing the aligned model with an unaligned prior raises $\dr$ from 0.51 to 0.62 on a held-out split but leaves Nigeria at 0.36. Point accuracy alone therefore misjudges these simulators, and current post-training trades diversity for consensus.

## Metadata
- **Published**: 2026-09-22T06:55:46Z
- **Authors**: Rojin Ziaei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25760v1)