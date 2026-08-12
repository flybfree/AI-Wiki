---
title: How Robust Are LLMs to Vietnamese Dialects?
published: 2026-08-11T03:02:57Z
authors: Minh Tran, Trinh Chau, Thanh-Nhan Le, Nam Tran, Luan Thanh Nguyen, Cuong Dang, Duc Hoang
url: http://arxiv.org/abs/2608.10414v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Robust Are LLMs to Vietnamese Dialects?

## Abstract
Large Language Models (LLMs) are typically evaluated on standard written Vietnamese, yet everyday communication frequently involves regional dialects that preserve meaning but differ in surface form. Existing Vietnamese dialect work largely addresses this issue through dialect-to-standard normalization instead of measuring how the model fails under Vietnamese dialectal inputs. To address this gap, we present the first systematic evaluation of LLM robustness to Vietnamese dialect variation across multiple tasks, quantifying performance degradation and failure patterns. We introduce VialectBench (Vietnamese Dialects Benchmarking), a controlled benchmark for testing whether model decisions remain stable across six Vietnamese dialect groups. VialectBench contains 400 Standard Vietnamese source instances and 2,400 human-written dialectal rewrites spanning emotion recognition (ER), natural language inference (NLI), question answering (QA), and multiple-choice question answering (MCQA). Dataset evaluation with a fixed reference language model shows that the dialectal rewrites induce a measurable model-relative likelihood shift while remaining nearly equal in length to their Standard counterparts. Across ten instruction-tuned models, dialectal inputs reduce average performance by 2.82%, and no evaluated model is fully dialect-invariant. All four tasks are affected, with QA showing the largest average degradation. Robustness also varies substantially across dialect groups: PNT3 and PNT2 cause the largest average performance drops, at 6.17% and 4.73%, respectively, whereas PNB slightly improves average performance by 0.42%. The Central dialect group (PNT1-PNT4) also yields the highest average harmful-flip rate across all models, at 6.54%. These findings show that strong performance on Standard Vietnamese does not guarantee reliable behavior under meaning-preserving regional variation.

## Metadata
- **Published**: 2026-08-11T03:02:57Z
- **Authors**: Minh Tran, Trinh Chau, Thanh-Nhan Le, Nam Tran, Luan Thanh Nguyen, Cuong Dang, Duc Hoang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10414v1)