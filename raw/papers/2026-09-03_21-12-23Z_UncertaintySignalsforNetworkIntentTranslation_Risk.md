---
title: Uncertainty Signals for Network Intent Translation: Risk Ranking and Ambiguity Localization
published: 2026-09-03T21:12:23Z
authors: Ala' A. Alsamarneh, Omar Alhussein
url: http://arxiv.org/abs/2609.04486v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Uncertainty Signals for Network Intent Translation: Risk Ranking and Ambiguity Localization

## Abstract
Intent-based networking realization starts by translating high-level intents into low-level network configurations. Recent approaches have shifted toward LLM-based translation. Despite promising results, most studies focus on translation accuracy and overlook risks associated with deploying the resulting configurations. In this work, we investigate the pre-deployment translation risk of LLM-generated configurations by analyzing the model's uncertainty. We propose to use two uncertainty signals, namely sampling-based predictive uncertainty for translation-risk ranking and token-level entropy for ambiguity-source localization. We evaluate these signals on an ambiguity-controlled test set across different context types and sampling budgets, using a Llama-3.1-8B-Instruct model fine-tuned for intent translation on a vendor-specific switch platform (Juniper EX3300). The results demonstrate that predictive uncertainty provides a useful signal for ranking translations by risk across context types and sampling budgets, albeit with substantial miscalibration under less informative contexts. Moreover, we show that parameter-token entropy correlates with parameter-sourced ambiguity and keyword-token entropy correlates with description-sourced ambiguity. These results indicate the potential of using uncertainty signals in an LLM-generated configuration deployment pipeline, where predictive uncertainty can support selective deployment, while token-level entropy can identify sources of ambiguity.

## Metadata
- **Published**: 2026-09-03T21:12:23Z
- **Authors**: Ala' A. Alsamarneh, Omar Alhussein
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04486v1)