---
title: Assessing Reliability of BERT-Based Models on Question Answering Tasks
published: 2026-08-11T11:24:07Z
authors: Pooja Yadav, Priyanka Harjule, Basant Agarwal, Marko Robnik Šikonja
url: http://arxiv.org/abs/2608.10806v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Assessing Reliability of BERT-Based Models on Question Answering Tasks

## Abstract
Reliability estimation of large language models is in many cases as crucial as their accuracy, as reliable models are more trustworthy, robust, and suitable for practical applications. Recent advancements in natural language processing (NLP), particularly those based on transformer architectures, have significantly accelerated progress across various NLP tasks. This study focuses on the reliability of transformer-based question answering (QA) models, specifically BERT models and its variants (RoBERTa, ALBERT, DistilBERT). These encoder-only pretrained transformers have demonstrated remarkable accuracy in QA tasks that can be treated as classification tasks. However, their reliability remains underexplored. This study evaluates the reliability of four BERT-based models by assessing response stability under two conditions: (1) internal model variations induced via Monte Carlo Dropout (MCD) and (2) input perturbations through paraphrasing. Using the SQuAD and QuAC datasets, we investigate how dropout rates affect prediction consistency and whether lexical changes impact answer stability. Our findings reveal that RoBERTa maintains higher reliability, whereas AlBERT and DistilBERT exhibit significant inconsistencies. Statistical analyses confirm that enabling MCD during prediction does not disrupt inference dynamics, validating its effectiveness as a reliability metric. These findings underscore the importance of evaluating both accuracy and stability in QA models to ensure stability in real-world applications.

## Metadata
- **Published**: 2026-08-11T11:24:07Z
- **Authors**: Pooja Yadav, Priyanka Harjule, Basant Agarwal, Marko Robnik Šikonja
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10806v1)