---
title: Safeguarding LLMs via Model-Agnostic Latent Safety Signals from Dark Knowledge
published: 2026-10-05T23:59:28Z
authors: Wonjun Lee, Kyungsik Yang, Gaeun Ji, Vaidehi Patil, Haon Park, Bumsub Ham, Mohit Bansal, Suhyun Kim
url: http://arxiv.org/abs/2610.07532v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Safeguarding LLMs via Model-Agnostic Latent Safety Signals from Dark Knowledge

## Abstract
LLMs have advanced rapidly, raising growing concerns about their safety. Recent work has proposed approaches to detect and defend against attacks including defenses at decoding stage that leverage models' hidden states. However, existing decoding-stage defenses suffer from two limitations. First, they introduce a trade-off between safety and over-refusal, where strengthening safety degrades the model's helpfulness on benign queries. Second, many of these methods rely on internal hidden states and are thus restricted to specific architectures, incurring substantial overhead and limited generalization across models. To address these limitations, we introduce LADE (Latent Safety Signals for Defense), which leverages latent safety signals extracted by contrasting harmful and benign queries from dark knowledge (i.e., information carried by the output probability distribution beyond its argmax) in the first-token output probability distribution. Our key insight is that, beyond surface-level refusal tokens, the dark knowledge in the first-token distribution contains latent safety signals, defined as tokens whose probabilities differ sharply between harmful and benign queries. We show that these signals consistently align across LLMs, forming a model-agnostic direction that emerges from safety alignment. LADE consists of three components: (1) Extracting Latent Safety Signals from Dark Knowledge, which selects top-k safety-discriminative tokens from the first-token probability distribution; (2) Tokenizer Mapping, which maps these tokens across different tokenizers to enable model-agnostic application; and (3) kNN-based Discrimination, which classifies queries via a k-Nearest Neighbors search over the mapped tokens. Across diverse LLMs and benchmarks, LADE is robust against a wide range of jailbreak attacks and lowers attack success rates while maintaining a competitive safety-utility trade-off.

## Metadata
- **Published**: 2026-10-05T23:59:28Z
- **Authors**: Wonjun Lee, Kyungsik Yang, Gaeun Ji, Vaidehi Patil, Haon Park, Bumsub Ham, Mohit Bansal, Suhyun Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07532v1)