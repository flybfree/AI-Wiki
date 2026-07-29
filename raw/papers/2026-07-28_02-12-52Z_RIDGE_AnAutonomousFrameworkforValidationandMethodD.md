---
title: RIDGE: An Autonomous Framework for Validation and Method Discovery in LLM-Generated Option Pricing
published: 2026-07-28T02:12:52Z
authors: Liexin Cheng, Xue Cheng, Shuaiqiang Liu, Cornelis W. Oosterlee
url: http://arxiv.org/abs/2607.25199v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RIDGE: An Autonomous Framework for Validation and Method Discovery in LLM-Generated Option Pricing

## Abstract
Automated code generation is becoming an important tool in quantitative finance, where large language models can generate option pricing implementations directly from mathematical model specifications. Validating such implementations, however, requires considerably more than conventional software testing: numerical pricing methods must remain mathematically consistent, numerically stable, and reliable across a wide range of model parameters.   We introduce RIDGE, an autonomous validation framework in which generated pricing implementations are subjected to structured no-arbitrage tests, stress tests, benchmark comparisons, and consistency checks. Validation evidence is interpreted diagnostically, while the resulting knowledge is accumulated in a repository and reused across models and successive validation iterations. This enables systematic refinement of both the pricing implementation and the validation methodology.   The framework is applied to five stochastic volatility models. Across these studies, all detected implementation defects are removed and, in two cases, the validation process itself leads to new semi-analytic pricing methodologies. The supplementary material is available in the GitHub repository: https://github.com/ShQiangLiu/ridge.

## Metadata
- **Published**: 2026-07-28T02:12:52Z
- **Authors**: Liexin Cheng, Xue Cheng, Shuaiqiang Liu, Cornelis W. Oosterlee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25199v1)