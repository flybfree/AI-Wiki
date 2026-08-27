---
title: Cross-Dataset Stability of Expert-Informed Skill Prompting and Fine-Tuning for Chinese Metaphor Identification
published: 2026-08-26T09:40:10Z
authors: Yufeng Wu, Meichun Liu
url: http://arxiv.org/abs/2608.25579v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Dataset Stability of Expert-Informed Skill Prompting and Fine-Tuning for Chinese Metaphor Identification

## Abstract
Metaphor-identification performance can change markedly across datasets that differ in text distribution and annotation policy. We examine whether a fixed expert-informed procedure produces a more even cross-dataset profile than task-specific parameter adaptation. Four prespecified conditions are compared for Chinese sentence-level metaphor identification: BERT fine-tuning (BERT-FT), QLoRA-based large language model fine-tuning (LLM-FT), direct zero-shot LLM prompting (LLM-ZS), and zero-shot prompting with a frozen procedural Skill (Skill-ZS). The Skill operationalizes established criteria involving contextual meaning, basic meaning, contrast, and comparison. Evaluation covers CMRE Test and two external datasets, CCIME and CMC. Fine-tuned scores are means over three seeds, whereas each zero-shot score comes from one deterministic configuration. Fine-tuning remains strongest on the native test set: BERT-FT reaches 91.76 Macro-F1. LLM-FT has the highest external mean (83.52), while Skill-ZS is close at 82.92 and has both the highest external floor (82.64) and the smallest observed range across all three datasets (4.08 points). In the matched zero-shot comparison, adding the Skill reduces metaphorical predictions on every dataset. This sharply lowers false positives on CCIME but increases false negatives on CMRE Test and CMC. The results position expert-informed Skill prompting as a complementary route to more even observed cross-dataset performance, while fine-tuning retains its advantage in native-data accuracy. To our knowledge, this is the first study to compare an expert-informed procedural Skill with task-specific fine-tuning in the same cross-dataset evaluation of Chinese sentence-level metaphor identification.

## Metadata
- **Published**: 2026-08-26T09:40:10Z
- **Authors**: Yufeng Wu, Meichun Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25579v1)