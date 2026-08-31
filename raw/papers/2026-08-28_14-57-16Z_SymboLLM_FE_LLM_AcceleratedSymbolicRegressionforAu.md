---
title: SymboLLM-FE: LLM-Accelerated Symbolic Regression for Automated Feature Engineering on Tabular Data
published: 2026-08-28T14:57:16Z
authors: Zi-Jian Cheng, Zi-Yi Jia, Zhi Zhou, Yu-Feng Li, Lan-Zhe Guo
url: http://arxiv.org/abs/2608.28408v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SymboLLM-FE: LLM-Accelerated Symbolic Regression for Automated Feature Engineering on Tabular Data

## Abstract
Tabular data, as a core data format in machine learning, often lacks the discriminative power needed for high-performance modeling due to insufficient feature informativeness. Automated Feature Engineering (AutoFE) overcomes this by automating feature generation and selection, ensuring both model performance and operational efficiency. However, traditional AutoFE often yield features with poor interpretability because they rely on blind mathematical transformations, while large language models (LLM)-based AutoFE faces challenges in requiring costly multi-round iterations to generate high-utility features to effectively enhance model performance, compounded by inherent risks of bias and hallucination. In this paper, we combine symbolic regression with LLMs for feature engineering (SymboLLM-FE) to solve these challenges. We extract mathematically expressive formulas strongly correlated with the target via symbolic regression, which can enhance model performance, then refine them by LLMs with rich prior knowledge to ensure interpretability. Empirical results on six real-world datasets and four Kaggle competitions demonstrate that SymboLLM-FE outperforms existing AutoFE. SymboLLM-FE also addresses the dual challenges of poor interpretability and numerous iterations by employing a statistical prior-grounded LLM refinement mechanism and single-digit LLM calls.

## Metadata
- **Published**: 2026-08-28T14:57:16Z
- **Authors**: Zi-Jian Cheng, Zi-Yi Jia, Zhi Zhou, Yu-Feng Li, Lan-Zhe Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28408v1)