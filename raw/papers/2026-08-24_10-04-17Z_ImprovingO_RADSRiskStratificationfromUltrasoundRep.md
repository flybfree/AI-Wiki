---
title: Improving O-RADS Risk Stratification from Ultrasound Reports: A Comparative Evaluation of Hybrid versus End-to-End LLM Reasoning Strategies
published: 2026-08-24T10:04:17Z
authors: Xiaotong Tan, Chunli Qiu, Xin Liu, Qing Huang, Guangli Zhou, Bo Gao, Xiaoyan Song, Shuyan Wang, Xiuqin Wang, Wufeng Xue, Ruobing Huang, Dong Ni, Guowei Tao, Jun Cheng
url: http://arxiv.org/abs/2608.23061v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Improving O-RADS Risk Stratification from Ultrasound Reports: A Comparative Evaluation of Hybrid versus End-to-End LLM Reasoning Strategies

## Abstract
Background: Automating clinical guideline-based decision-making with large language models (LLMs) remains challenging because of reliability, hallucination, and limited interpretability. We compared the performance of LLMs and reasoning strategies for automated Ovarian-Adnexal Reporting and Data System (O-RADS) classification from free-text pelvic ultrasound reports. Methods: In this retrospective study, consecutive patients with ovarian masses who underwent pelvic ultrasound were included. Eight LLMs were tested with three reasoning strategies: implicit-knowledge end-to-end, rule-informed end-to-end, and a feature-based hybrid architecture that decoupled feature extraction from rule-based classification. The reference standard was O-RADS categorization established by expert consensus. Results: A total of 310 women with 390 ovarian masses were evaluated. The feature-based hybrid architecture using Gemini 3.6 Flash demonstrated the best performance, achieving an accuracy of 99.2% (387 of 390) and almost perfect agreement with the reference standard (weighted kappa = 1.00; 95% CI: 0.99-1.00). Its performance surpassed that of original clinical reports (accuracy, 87.7% [342 of 390]; weighted kappa = 0.94; 95% CI: 0.91-0.96) and end-to-end LLM strategies (accuracy range, 65.6% [256 of 390] to 95.9% [374 of 390]). For structured feature extraction, Gemini 3.6 Flash demonstrated higher overall accuracy than Claude Fable 5 (98.9% vs 97.8%; P < 0.001). The hybrid architecture reduced misclassification errors and mitigated the overstaging tendency observed in original reports. Conclusion: The feature-based hybrid LLM architecture that separates clinical feature extraction from deterministic guideline execution enables highly accurate, reliable, and interpretable automated O-RADS classification, providing a promising approach for standardized, guideline-based clinical decision-making.

## Metadata
- **Published**: 2026-08-24T10:04:17Z
- **Authors**: Xiaotong Tan, Chunli Qiu, Xin Liu, Qing Huang, Guangli Zhou, Bo Gao, Xiaoyan Song, Shuyan Wang, Xiuqin Wang, Wufeng Xue, Ruobing Huang, Dong Ni, Guowei Tao, Jun Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23061v1)