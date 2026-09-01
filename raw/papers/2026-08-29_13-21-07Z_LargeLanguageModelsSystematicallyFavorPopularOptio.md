---
title: Large Language Models Systematically Favor Popular Options: Evidence and Mitigation Across MCQs
published: 2026-08-29T13:21:07Z
authors: Abdelrahman Abdallah, Mohammed Ali, Bhawna Piryani, Mahmoud Abdalla, Adam Jatowt
url: http://arxiv.org/abs/2608.29257v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Large Language Models Systematically Favor Popular Options: Evidence and Mitigation Across MCQs

## Abstract
Multiple-choice questions (MCQs) are a standard format for evaluating large language models (LLMs), yet the popularity of answer options can confound evaluation. Modern LLMs systematically prefer popular but incorrect options over less popular correct ones, a vulnerability we call \textbf{popularity bias}. This pattern aligns with confidence miscalibration: model confidence remains high even as accuracy collapses for popular options. To systematically isolate this phenomenon, we introduce \textbf{PopMCQ}, a benchmark with six controlled strategies that vary option popularity while keeping the correct answer fixed. In our most adversarial setting, where all distractors are more popular than the correct option, models choose popular but wrong answers 66\% of the time. To mitigate this bias, we propose \textbf{PopDebias}, a lightweight inference-time correction that estimates and removes a popularity prior from model predictions. It requires no fine-tuning, is label-free at test time (using only a small calibration split for parameter fitting), and adds negligible computational cost. Experiments on 22 open-source LLMs (0.5B to 32B parameters) show consistent improvements, with accuracy gains up to 54.1 percentage points under strong popularity pressure. The code and data are available https://github.com/DataScienceUIBK/PopMCQ

## Metadata
- **Published**: 2026-08-29T13:21:07Z
- **Authors**: Abdelrahman Abdallah, Mohammed Ali, Bhawna Piryani, Mahmoud Abdalla, Adam Jatowt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29257v1)