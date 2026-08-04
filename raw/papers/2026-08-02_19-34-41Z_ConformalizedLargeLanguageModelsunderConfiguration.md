---
title: Conformalized Large Language Models under Configuration Shift
published: 2026-08-02T19:34:41Z
authors: Yuqicheng Zhu, Jialin Yu, Lin Li, Gengyuan Zhang, Zhen Yang, Steffen Staab, Puneet Dokania, Philip Torr, Jie Tang, Evgeny Kharlamov
url: http://arxiv.org/abs/2608.01460v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conformalized Large Language Models under Configuration Shift

## Abstract
Conformal prediction (CP) is a distribution-free framework for uncertainty quantification that has recently been adapted to large language models (LLMs), providing prediction sets with finite-sample coverage guarantees under exchangeability. Yet for LLMs, nonconformity scores are often induced by an inference pipeline, not just a fixed model, making them depend not only on the data distribution but also on configurable factors such as the prompt template, decoding parameters, and deployment setting. Since such configurations are routinely modified in practice but rarely treated as a source of shift, their impact on CP validity remains poorly understood. We call this \emph{configuration shift} and study it systematically along three axes: prompt template, decoding temperature, and weight quantization. In a broad empirical study spanning $9$ LLMs, $4$ datasets, and $4$ nonconformity scores, we find that configuration shift consistently erodes CP validity, often driving empirical coverage below the target. By contrast, efficiency is largely preserved: valid prediction sets remain close in size to the i.i.d. baseline. We derive coverage lower bounds that attribute this loss to a discrepancy between calibration and test score distributions, and use their finite-sample plug-in versions as empirical diagnostics of shift severity. We further show that these findings lead to practical mitigations: bound-inspired recalibration is effective with limited test examples, while fragility-aware calibration ensembling recovers much of the lost coverage without test data.

## Metadata
- **Published**: 2026-08-02T19:34:41Z
- **Authors**: Yuqicheng Zhu, Jialin Yu, Lin Li, Gengyuan Zhang, Zhen Yang, Steffen Staab, Puneet Dokania, Philip Torr, Jie Tang, Evgeny Kharlamov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01460v1)