---
title: FinDeepIndicator: Benchmarking Deep Research Agents in End-to-End Financial Indicator Construction
published: 2026-08-01T16:54:41Z
authors: Chaoqun Yang, Fengbin Zhu, Xinyu Lin, Long Bai, Xiaoluan Liu, Ke-Wei Huang, Roger Zimmermann, Tat-Seng Chua
url: http://arxiv.org/abs/2608.00764v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FinDeepIndicator: Benchmarking Deep Research Agents in End-to-End Financial Indicator Construction

## Abstract
Financial indicators are essential tools for transforming raw financial data into interpretable measures for various downstream tasks, such as valuation, risk assessment, and economic analysis. However, existing financial benchmarks largely focus on answer-level accuracy and often assume that relevant data are already provided, leaving the assessment of the intermediate process of indicator construction underexplored. In this work, we propose FinDeepIndicator, the first benchmark dedicated to evaluating Deep Research (DR) agents in end-to-end financial indicator construction. Specifically, FinDeepIndicator evaluates DR agents across four stages in indicator construction: formula specification, data collection, indicator calculation, and answer generation, and covers fundamental, technical, and macroeconomic indicators organized into 21 fine-grained sub-categories. It contains 3,350 curated question-answer (QA) pairs derived from both U.S. and Chinese markets, 10 years of historical financial data, and 800 listed companies. Extensive experiments on search-equipped Large Language Models (LLMs) and DR agents show that, while LLMs generally perform well in formula specification, their accuracy drops substantially during data retrieval and numerical execution. DR agents consistently outperform search-equipped LLMs, yet remain unreliable in realistic financial analysis settings. These findings provide insights for developing more capable and trustworthy DR agents in finance.

## Metadata
- **Published**: 2026-08-01T16:54:41Z
- **Authors**: Chaoqun Yang, Fengbin Zhu, Xinyu Lin, Long Bai, Xiaoluan Liu, Ke-Wei Huang, Roger Zimmermann, Tat-Seng Chua
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00764v1)