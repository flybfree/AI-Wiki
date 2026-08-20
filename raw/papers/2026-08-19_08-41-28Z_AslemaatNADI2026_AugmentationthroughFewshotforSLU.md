---
title: Aslema at NADI 2026: Augmentation through Fewshot for SLU
published: 2026-08-19T08:41:28Z
authors: Tajwaar Shafiq, Hunzalah Hassan Bhatti, Shammur Absar Chowdhury, Firoj Alam
url: http://arxiv.org/abs/2608.18689v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Aslema at NADI 2026: Augmentation through Fewshot for SLU

## Abstract
We present Aslema, our system for NADI 2026 Shared Task 5, which consists of two subtasks: intent recognition and slot filling. We evaluate four omni LLMs in a zero-shot setting and compare them with fine-tuned models. Our results show that fine-tuning consistently outperforms zero-shot inference. We further explore synthetic data augmentation by using an LLM to generate culturally grounded Tunisian Derja utterances, followed by voice cloning to generate synthetic speech. Incorporating this synthetic data improves performance on both tasks. Our final submitted system, based on Qwen3-Omni-30B and trained with a mixture of original and synthetic data, achieves 86.8% intent accuracy and 34.7 WER on the devtest split. On the official test set it ranks 1st in slot filling (59.5 CoER) and 4th among 8 teams in intent recognition (66.1% accuracy). We release our experimental scripts and will soon share the synthetic dataset to support further research in this area.

## Metadata
- **Published**: 2026-08-19T08:41:28Z
- **Authors**: Tajwaar Shafiq, Hunzalah Hassan Bhatti, Shammur Absar Chowdhury, Firoj Alam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18689v1)