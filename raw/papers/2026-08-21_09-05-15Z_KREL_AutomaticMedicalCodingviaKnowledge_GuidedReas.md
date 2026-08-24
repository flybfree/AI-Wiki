---
title: KREL: Automatic Medical Coding via Knowledge-Guided Reasoning over Clinical Evidence with LLMs
published: 2026-08-21T09:05:15Z
authors: Xubin Chen, Yipeng Zhou, Wen Sun, Chengkai Huang, Xiaoming Fu, Quan Z. Sheng
url: http://arxiv.org/abs/2608.20887v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KREL: Automatic Medical Coding via Knowledge-Guided Reasoning over Clinical Evidence with LLMs

## Abstract
Automatic Medical Coding (AMC), which assigns standardized International Classification of Diseases (ICD) codes to clinical notes, is essential for medical reimbursement, quality reporting, and clinical research. Existing pre-trained language model (PLM)-based methods typically formulate AMC as an extreme multi-label classification problem over a predefined code set, while recent large language model (LLM)-based approaches instead frame it as generation or multi-step reasoning. However, key challenges remain, including the extreme length of clinical notes that hinders effective interpretation, the vast ICD label space, and complex coding rules that are not explicitly captured by LLMs. In this work, we propose Knowledge-Guided Reasoning over Clinical Evidence with LLMs (KREL), a framework that leverages LLMs for clinical text understanding and reasoning while integrating external ICD coding guidelines as structured knowledge. This design enables tight coupling between domain knowledge and LLM reasoning, reducing hallucinations and improving compliance with coding standards. Experiments on benchmark datasets show that KREL consistently outperforms strong PLM-based and state-of-the-art LLM-based baselines.

## Metadata
- **Published**: 2026-08-21T09:05:15Z
- **Authors**: Xubin Chen, Yipeng Zhou, Wen Sun, Chengkai Huang, Xiaoming Fu, Quan Z. Sheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20887v1)