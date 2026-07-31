---
title: Cocktail-Talker: Multi-Speaker Dialog Modeling in Noisy Social Environments with Turn Action GRPO
published: 2026-07-30T06:53:15Z
authors: Xilin Jiang, Riki Shimizu, Sukru Samet Dindar, Junkai Wu, Zhongweiyang Xu, Nima Mesgarani
url: http://arxiv.org/abs/2607.27756v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cocktail-Talker: Multi-Speaker Dialog Modeling in Noisy Social Environments with Turn Action GRPO

## Abstract
Spoken dialog systems are typically designed for clean, dyadic interactions in which a single user and an assistant take turns speaking. Real-world social conversations, however, are often more ambiguous: multiple speakers may participate in the same conversation amid irrelevant speech and background noise. Each utterance may be directed to the assistant, addressed to another speaker, or completely irrelevant. In such settings, the assistant must decide not only what to say, but also whether to speak at all. In this paper, we introduce Cocktail-Talker, a speech LLM framework for multi-speaker spoken dialog modeling in noisy social environments. We model the assistant's behavior with three action tokens: <|respond|>, <|listen|>, and <|ignore|>, placed before a response or silence. Cocktail-Talker is trained via supervised finetuning and reinforcement learning to generate the appropriate action token and, only in <|respond|> mode, a speech response. To prepare the training data, we develop Cocktail-DialogGen, an LLM-based data pipeline that simulates realistic multi-speaker dialogs with speaker roles across diverse social settings. Together, these components take a step toward spoken dialog systems that interact more naturally and selectively in complex social environments.

## Metadata
- **Published**: 2026-07-30T06:53:15Z
- **Authors**: Xilin Jiang, Riki Shimizu, Sukru Samet Dindar, Junkai Wu, Zhongweiyang Xu, Nima Mesgarani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27756v1)