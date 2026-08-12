---
title: REAP: Relation-Aware Elicitation and Parsing for Closed-Book Knowledge Base Construction from LLMs
published: 2026-08-11T14:28:50Z
authors: Thanh-Dan Bui, Thanh-Trung Do, Tuan-Phong Nguyen
url: http://arxiv.org/abs/2608.10963v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# REAP: Relation-Aware Elicitation and Parsing for Closed-Book Knowledge Base Construction from LLMs

## Abstract
We present the REAP system for the AKBC Shared Task 2026 on constructing knowledge bases from language models in a closed-book setting, subject to a budget of at most 32B parameters and no model fine-tuning. Our system combines structured chain-of-thought reasoning, relation-specific query strategies, and a reasoning-based empty-set gate to elicit parametric knowledge, followed by direct extraction into valid JSON arrays. On the test set, the system, built on the Mistral-Small-24B-Instruct-2501 model, achieves a macro-F1 score of 0.62, with particularly strong results on countryLandBordersCountry (F1 = 0.95), companyTradesAtStockExchange (F1 = 0.73), and hasArea (F1 = 0.77). Our code is publicly available at https://github.com/yammdd/AKBC-Shared-Task-2026.

## Metadata
- **Published**: 2026-08-11T14:28:50Z
- **Authors**: Thanh-Dan Bui, Thanh-Trung Do, Tuan-Phong Nguyen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10963v1)