---
title: From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning
published: 2026-08-28T04:50:09Z
authors: Lokendra Birla, Milind Savagaonkar, Visnu Srinivasan, Sowmya Rasipuram, Shubhashis Sengupta
url: http://arxiv.org/abs/2608.27919v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Documents to Reasoning: A Validated Synthetic Data Pipeline and Semantic-Aware Fine-Tuning for Financial Numerical Reasoning

## Abstract
Financial question answering (QA) has emerged as a key benchmark for evaluating the performance of Large Language Models (LLMs) on domain-specific tasks involving complex data formats such as tables, charts, and rich textual narratives. While recent advancements have enabled models to reason across modalities and perform multi-step arithmetic operations, limitations remain in performance consistency, and evaluation reliability. In particular, standard evaluation metrics like Exact Match (EM) often fail to account for minor variations such as differences in units or formats, misleading performance assessments.   In this work, we propose a comprehensive pipeline for improving financial QA systems through high-quality synthetic data generation and fine-tuning of smaller language models (SLMs) using Quantized Low-Rank Adaptation (QLoRA). Our pipeline includes aggressive data validation for synthetic question answer generation to ensure the relevance and correctness of synthetic question-answer pairs. We introduce a novel evaluation metric that matches answers computed from arithmetic expressions rather than ground-truth answers; providing a more accurate reflection of model reasoning capability. Furthermore, we propose a modified loss function that aligns predicted and reference expressions using semantic similarity, our novel evaluation metric and standard cross-entropy, resulting in improved performance. Experimental results on benchmark datasets, ConvFinQA demonstrate significant gains in QA accuracy after fine-tuning using synthetic dataset and proposed loss function.

## Metadata
- **Published**: 2026-08-28T04:50:09Z
- **Authors**: Lokendra Birla, Milind Savagaonkar, Visnu Srinivasan, Sowmya Rasipuram, Shubhashis Sengupta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27919v1)