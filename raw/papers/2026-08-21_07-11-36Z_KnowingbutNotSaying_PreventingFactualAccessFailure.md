---
title: Knowing but Not Saying: Preventing Factual Access Failures in LLM SFT via Recall-Anchored Distillation
published: 2026-08-21T07:11:36Z
authors: Haodong Chen, Yadong Wang, Shengtao Wen, Dong Liang, Xiang Chen
url: http://arxiv.org/abs/2608.20794v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Knowing but Not Saying: Preventing Factual Access Failures in LLM SFT via Recall-Anchored Distillation

## Abstract
Supervised fine-tuning (SFT) can degrade factual behavior outside the target domain. This degradation is often described as catastrophic forgetting, yet open-ended factual failures do not necessarily imply that the underlying facts have been erased. In this work, we identify a more specific phenomenon, factual access failure: after domain SFT, models can still recognize or rank the correct answer under constrained evaluation, while failing to produce it in closed-book generation. Through benchmark-level comparisons, same-fact multiple-choice and generation probes, and failure-mode analysis, we show that SFT-induced factual degradation reflects both genuine wrong-answer generations and expression-level failures such as verbosity, formatting mismatch, and exact-match artifacts. To address this problem, we introduce Recall-Anchored Distillation (RAD), a base-anchored self-distillation objective that preserves out-of-distribution generation behavior by aligning the adapted model with the original base model's soft continuation distribution on unlabeled OOD text. RAD requires no gold OOD answers, external judges, or labeled factual data. Across three backbones fine-tuned on MedMCQA, RAD recovers a consistent portion of the lost OOD recall while preserving target-domain adaptation. Compared with replay on the same OOD text, RAD shows that the key preservation signal is the base model's soft distribution rather than additional text exposure alone.

## Metadata
- **Published**: 2026-08-21T07:11:36Z
- **Authors**: Haodong Chen, Yadong Wang, Shengtao Wen, Dong Liang, Xiang Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20794v1)