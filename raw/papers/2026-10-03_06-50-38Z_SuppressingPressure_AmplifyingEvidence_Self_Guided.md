---
title: Suppressing Pressure, Amplifying Evidence: Self-Guided Attention Steering to Mitigate Sycophancy and Stubbornness
published: 2026-10-03T06:50:38Z
authors: Yinghao He, Mengyu Xu, Haixiang Sun, Donghan Li, Yibo Wang, Lixu Wang, Kezhen Chen, Chi Li, Chunwei Liu, Bharat Bhargava, Chongyang Gao
url: http://arxiv.org/abs/2610.04329v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Suppressing Pressure, Amplifying Evidence: Self-Guided Attention Steering to Mitigate Sycophancy and Stubbornness

## Abstract
Reliable language models should resist unsupported user pressure while effectively using objective contextual information. However, models may exhibit sycophancy by yielding to unsupported user pressure or contextual stubbornness by failing to update their answers when relevant contextual information warrants revision. Evaluating interventions for these failures separately can obscure whether mitigating one failure exacerbates the other. To assess this trade-off, we introduce CoPE-Bench with six conditions per question: a neutral baseline, correct or incorrect user pressure, contextual information consistent with or conflicting with the neutral answer, and a joint condition combining incorrect claims with conflicting contextual information. To regulate the influence of user pressure and contextual information, we propose SPAE (Suppressing Pressure, Amplifying Evidence), a training-free framework that uses the model's own judgments to identify relevant tokens, suppressing user pressure and amplifying contextual information through token-level attention steering. On average across five backbones, SPAE reduces pressure following by 18.8 percentage points and increases joint-condition updating by 5.5 percentage points relative to the strongest baseline in the main comparison. In two-turn dialogue, it improves joint-condition updating by an average of 13.2 percentage points over the strongest prompting baseline. The source data and codes can be found at https://github.com/03Grant/sycophancy-and-stubbornness.

## Metadata
- **Published**: 2026-10-03T06:50:38Z
- **Authors**: Yinghao He, Mengyu Xu, Haixiang Sun, Donghan Li, Yibo Wang, Lixu Wang, Kezhen Chen, Chi Li, Chunwei Liu, Bharat Bhargava, Chongyang Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04329v1)