---
title: ArabicDialectSafety: A Dialect-Aware Benchmark for Arabic Content Safety Classification
published: 2026-08-02T15:00:58Z
authors: Wajdi Zaghouani, Md. Rafiul Biswas, Kholoud Khalil Aldous, Mabrouka Bessghaier
url: http://arxiv.org/abs/2608.01291v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ArabicDialectSafety: A Dialect-Aware Benchmark for Arabic Content Safety Classification

## Abstract
We present ArabicDialectSafety, a human-curated Arabic safety dataset of 25,071 prompts covering six Arabic varieties: Modern Standard Arabic, Syrian, Egyptian, Algerian, Palestinian, and Moroccan. The dataset is annotated with dialect labels and seven fine-grained harm categories. We introduce a dual-task evaluation framework for binary safe/unsafe detection and granular harm classification across dialects. Benchmarking seven supervised and generative models, we find that fine-tuned MARBERTv2 achieves the strongest performance, with Macro-F1 scores of 0.95 for binary classification and 0.90 for granular classification, substantially outperforming prompted frontier LLMs, including Arabic-specialized models. Our analyses show that dialect conditioning is most effective when integrated at the representation level, while significant performance gaps remain for low-resource Maghrebi dialects. We further evaluate seven frontier LLMs as response generators on harmful dialectal Arabic prompts and observe unsafe generation rates below 5 percent across models. We release the dataset and code upon acceptance to support future research on dialect-aware Arabic safety evaluation. Warning: This paper contains examples of harmful and potentially offensive content included solely for research purposes.

## Metadata
- **Published**: 2026-08-02T15:00:58Z
- **Authors**: Wajdi Zaghouani, Md. Rafiul Biswas, Kholoud Khalil Aldous, Mabrouka Bessghaier
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01291v1)