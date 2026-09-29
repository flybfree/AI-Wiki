---
title: How code helps different tasks? A decompositional lens on LLM post-training
published: 2026-09-27T18:57:54Z
authors: Zheng Yu, Yiwei Li, Yishen Chen, Xiang Li, Jiale Han, Benyou Wang, Jingbang Chen
url: http://arxiv.org/abs/2609.33845v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How code helps different tasks? A decompositional lens on LLM post-training

## Abstract
Evaluating code data as a single corpus can obscure which types of code data benefit which models and downstream tasks. Effective data selection requires understanding both the benefits of individual categories and whether these benefits persist when categories are combined. We introduce a decompositional lens for studying these effects in LLM post-training. We first decompose an execution-verified code corpus into interpretable categories based on the computational patterns of its solutions. Through controlled fine-tuning experiments, we compare individual categories with a balanced mixture across instruction-tuned models on question answering, mathematics, and code generation. The resulting response maps reveal recurring gains in average question-answering performance, while the same category can improve one model or task and degrade another. The best-performing category also varies with the starting model and target task. We then compose compact mixtures guided by these results and examine whether benefits observed in individual categories persist under joint training. On selected model--task pairs, mixtures whose constituents each improve the target task outperform both their best constituent and full-corpus training while using roughly 10--15\% of the full corpus. These exploratory findings illustrate a \emph{less is more} pattern and highlight how the value of code data in post training depends on which categories are combined for which model and task.

## Metadata
- **Published**: 2026-09-27T18:57:54Z
- **Authors**: Zheng Yu, Yiwei Li, Yishen Chen, Xiang Li, Jiale Han, Benyou Wang, Jingbang Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33845v1)