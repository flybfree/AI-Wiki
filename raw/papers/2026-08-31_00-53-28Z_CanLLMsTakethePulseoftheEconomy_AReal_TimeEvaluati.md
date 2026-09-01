---
title: Can LLMs Take the Pulse of the Economy? A Real-Time Evaluation of LLM Nowcasts on Macroeconomic Indicators
published: 2026-08-31T00:53:28Z
authors: Xinyue Zhao, Ruiyi Zhang, Liqin Ye, Rui Cao, Pengtao Xie, Sudheer Chava
url: http://arxiv.org/abs/2608.30110v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can LLMs Take the Pulse of the Economy? A Real-Time Evaluation of LLM Nowcasts on Macroeconomic Indicators

## Abstract
Nowcasting headline macroeconomic indicators, i.e., estimating an indicator's value for the current reference period before its official release, is critical for monetary policy and financial markets, and central banks devote dedicated teams of expert economists to producing such estimates. Large language model (LLM) agents are a promising candidate for this task, combining broad world knowledge with real-time web search and supporting queries at higher frequency than institutional nowcasts. Evaluating their nowcasting capability is, however, challenging: headline indicators such as GDP and CPI are widely reported and likely memorized during pretraining, so any evaluation on historical releases is vulnerable to data contamination. To address this, we introduce LiveMacroEval, a live, contamination-resistant benchmark in which LLM agents produce hourly nowcasts for sixteen major U.S. macroeconomic indicators over a pre-release window closing at each official release. Nowcast quality is assessed through a LiveMacro Score against announcement-window equity returns and a LiveBetting Score from simulated Polymarket-style trading, with Federal Reserve regional-bank nowcasts, the Bloomberg ECOS professional consensus, and an auto-ARIMA baseline as comparators. Over six months with four state-of-the-art LLM agents configured with web search, aggregate nowcast accuracy is broadly comparable to the institutional and professional benchmarks, with performance varying widely across individual indicators. This highlights LLM agents' potential as real-time estimators of macroeconomic conditions.

## Metadata
- **Published**: 2026-08-31T00:53:28Z
- **Authors**: Xinyue Zhao, Ruiyi Zhang, Liqin Ye, Rui Cao, Pengtao Xie, Sudheer Chava
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30110v1)