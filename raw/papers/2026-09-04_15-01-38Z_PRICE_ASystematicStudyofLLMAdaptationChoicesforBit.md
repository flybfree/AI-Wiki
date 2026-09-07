---
title: PRICE: A Systematic Study of LLM Adaptation Choices for Bitcoin Price Forecasting
published: 2026-09-04T15:01:38Z
authors: Maryam Fakhari, Mehran Safayani
url: http://arxiv.org/abs/2609.05235v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PRICE: A Systematic Study of LLM Adaptation Choices for Bitcoin Price Forecasting

## Abstract
Cryptocurrency markets exhibit extreme volatility and non-stationary dynamics that challenge conventional forecasting methods. Although Large Language Models (LLMs) have shown promise for time series forecasting, the combined effects of adaptation choices remain largely unexplored in financial settings. This study introduces PRICE, a structured approach for adapting LLMs to short-term Bitcoin price forecasting. Built on a 4-bit quantized LLaMA-3 8B model, PRICE investigates how fine-tuning, numerical representation, prompting, inference, and decoding jointly influence forecasting performance. PRICE integrates Parameter-efficient fine-tuning with Low-Rank Adaptation (LoRA), Recursive multi-step inference, Integer-rounded numerical representation, Context-Task-Format (CTF) prompting, and Exact zero-temperature decoding. Ablation studies show that each component contributes to forecasting accuracy and reliability. LoRA enables efficient training on limited hardware, recursive inference improves accuracy, integer-rounded values reduce errors, CTF prompting outperforms Chain-of-Thought, Implicit Chain-of-Thought (iCoT), and few-shot prompting, and zero-temperature decoding improves stability during recursive forecasting. Comparative evaluation against eight transformer-based and time-series foundation models shows that PRICE achieves the lowest forecasting errors on both validation and test sets while maintaining robust performance across evaluation periods. Despite being based on a model primarily pretrained on text rather than time-series data, PRICE achieves competitive or superior performance relative to specialized foundation models. These findings demonstrate that adaptation choices critically determine the accuracy and robustness of LLMs for numerical time-series forecasting.

## Metadata
- **Published**: 2026-09-04T15:01:38Z
- **Authors**: Maryam Fakhari, Mehran Safayani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05235v1)