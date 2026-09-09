---
title: Risk-Conditioned Fine-Tuning of Large Language Models
published: 2026-09-08T00:12:05Z
authors: Zixuan Liu, Fangzheng Wu, Brian Summa, Zizhan zheng
url: http://arxiv.org/abs/2609.08064v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Risk-Conditioned Fine-Tuning of Large Language Models

## Abstract
Large Language Models (LLMs) are increasingly deployed in settings where rare but severe harmful generations can have significant consequences. Existing Risk-Averse RLHF addresses this issue by optimizing Conditional Value-at-Risk (CVaR), but it trains policies for fixed risk levels and therefore cannot adjust the desired degree of risk aversion at inference time. In this paper, we propose risk-conditioned RLHF, a framework that trains a single policy that provides a continuous risk-control interface, enabling users to select different degrees of risk aversion without retraining or deploying multiple risk-specific models. Experiments across multiple benchmarks demonstrate that a single risk-conditioned policy can adapt to different risk levels at inference time, enabling more flexible and risk-aware LLM deployment.

## Metadata
- **Published**: 2026-09-08T00:12:05Z
- **Authors**: Zixuan Liu, Fangzheng Wu, Brian Summa, Zizhan zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08064v1)