---
title: Decoupling Generation and Selection for Budget-Constrained Faithful Summarization
published: 2026-08-04T13:36:25Z
authors: Zeyu Wang, Guanghua Wang, Meng Xu
url: http://arxiv.org/abs/2608.03655v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decoupling Generation and Selection for Budget-Constrained Faithful Summarization

## Abstract
Abstractive summarization models remain vulnerable to factual inconsistency, redundancy, and weak length control. We propose a modular generation-and-selection framework for sentence-budget-constrained summarization. A pretrained generator produces multiple candidate summaries, which are decomposed into sentence-level candidates. A combinatorial selector then constructs the final summary by balancing relevance, factuality, and redundancy under an explicit budget. The framework supports MMR, ILP, and a DPP-inspired log-determinant objective without retraining the generator. Experiments on CNN/DailyMail, Multi-News, FaithBench, and TofuEval show consistent improvements in factuality and source-grounding metrics, especially for multi-document summarization, at the cost of lower reference-overlap scores. Human evaluation further indicates higher perceived consistency, relevance, clarity, and conciseness, with a small reduction in coherence. These results show that decoupling generation from selection provides a model-agnostic mechanism for improving factual grounding. Code is available at https://anonymous.4open.science/r/bcfs-D05E/.

## Metadata
- **Published**: 2026-08-04T13:36:25Z
- **Authors**: Zeyu Wang, Guanghua Wang, Meng Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03655v1)