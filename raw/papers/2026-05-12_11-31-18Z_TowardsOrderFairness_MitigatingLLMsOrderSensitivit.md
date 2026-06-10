---
title: 'Towards Order Fairness: Mitigating LLMs Order Sensitivity through Dual Group Advantage Optimization'
published: 2026-05-12T11:31:18Z
authors: Xu Chu, Guanyu Wang, Zhijie Tan, Xinrong Chen, Ziyu Li, Tong Mo, Weiping Li
url: http://arxiv.org/abs/2605.11974v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Order Fairness: Mitigating LLMs Order Sensitivity through Dual Group Advantage Optimization

## Abstract
Large Language Models (LLMs) suffer from order bias, where their performance is affected by the arrangement order of input elements. This unfairness limits the model's applications in scenarios such as in-context learning and Retrieval-Augmented Generation (RAG). Recent studies attempt to obtain optimal or suboptimal arrangements based on statistical results or using dataset-based search, but these methods increase inference overhead while leaving the model's inherent order bias unresolved. Other studies mitigate order sensitivity through supervised fine-tuning using augmented training sets with multiple order variants, but often at the cost of accuracy, trapping the model in consistent yet incorrect hallucinations. In this paper, we propose \textbf{D}ual \textbf{G}roup \textbf{A}dvantage \textbf{O}ptimization (\textbf{DGAO}), which aims to improve model accuracy and order stability simultaneously. DGAO calculates and balances intra-group relative accuracy advantage and inter-group relative stability advantage, rewarding the policy model for generating order-stable and correct outputs while penalizing order-sensitive or incorrect responses. This marks the first time reinforcement learning has been used to mitigate LLMs' order sensitivity. We also propose two new metrics, Consistency Rate and Overconfidence Rate, to reveal the pseudo-stability of previous methods and guide more comprehensive evaluation. Extensive experiments demonstrate that DGAO achieves superior order fairness while improving performance on RAG, mathematical reasoning, and classification tasks. Our code is available at: https://github.com/Hyalinesky/DGAO.

## Metadata
- **Published**: 2026-05-12T11:31:18Z
- **Authors**: Xu Chu, Guanyu Wang, Zhijie Tan, Xinrong Chen, Ziyu Li, Tong Mo, Weiping Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.11974v1)