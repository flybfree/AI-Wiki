---
title: Measure, Don't Optimize: Forecasting Recovery in LLM Unlearning
published: 2026-08-11T20:16:20Z
authors: Zirui Song, Huaxing Liu, Xiang Wang, Shuai Li, Xinye Li, Lang Gao, Jinghui Zhang, Zheng Lu, Fengxian Ji, Xiaojun Chang, Xiuying Chen
url: http://arxiv.org/abs/2608.11408v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Measure, Don't Optimize: Forecasting Recovery in LLM Unlearning

## Abstract
Prior white-box studies show that large language models can retain latent traces of target knowledge after unlearning, even when the knowledge is no longer expressed in their outputs. However, existing audits remain limited to one-off diagnostics: it is unclear whether these residual signals can predict future recovery under continued training or serve as reliable optimization targets. Resolving this gap is essential to determine whether internal auditing can move beyond post-hoc evaluation toward proactive risk monitoring and safer unlearning. We propose J-Access, an inference-time audit that uses the Jacobian lens to map intermediate representations into vocabulary space and measures how often target concepts remain accessible along the model's output pathway. We hypothesize that residual accessibility reflects recovery susceptibility: knowledge that remains closer to the output pathway requires less fine-tuning to restore, leading to faster recovery. We audit 398 public unlearned models spanning eight unlearning methods. We find that: (1) most unlearned models retain access above the retain-only gold level; (2) pre-attack accessibility predicts recovery speed and extent at the model level, but cannot identify which specific facts will be recovered; and (3) directly minimizing J-Access does not promote genuine deletion. Instead, the model learns to hide knowledge from the audit, producing lower audit scores but greater post-attack recovery. These findings position J-Access as a model-level diagnostic for assessing residual susceptibility in unlearned models. We argue internal audits should serve as an independent diagnostic dimension in unlearning evaluation, and should not be converted into optimization targets without validation.

## Metadata
- **Published**: 2026-08-11T20:16:20Z
- **Authors**: Zirui Song, Huaxing Liu, Xiang Wang, Shuai Li, Xinye Li, Lang Gao, Jinghui Zhang, Zheng Lu, Fengxian Ji, Xiaojun Chang, Xiuying Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11408v1)