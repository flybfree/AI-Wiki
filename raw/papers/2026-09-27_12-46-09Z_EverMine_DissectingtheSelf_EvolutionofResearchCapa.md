---
title: EverMine: Dissecting the Self-Evolution of Research Capabilities in Long-Horizon Alpha Research
published: 2026-09-27T12:46:09Z
authors: Siyuan Li, Jiangfeng Zhang, Rui Yao, Weihua Qiu, Mingyang Xu, Zixuan Yuan
url: http://arxiv.org/abs/2609.33524v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EverMine: Dissecting the Self-Evolution of Research Capabilities in Long-Horizon Alpha Research

## Abstract
Self-evolving agents aim to turn research feedback into reusable skills, tools, and research rules. Whether these accumulated capabilities continue to improve later research requires controlled evaluation. Long-horizon alpha discovery provides a state-dependent setting: once a new factor enters the portfolio, the predictive information already covered changes, so the value of the same candidate or experience may change over time. We introduce EverMine, an empirical framework for studying self-evolving research capabilities in long-horizon alpha discovery. EverMine decomposes the research state into history (Hist), the current factor portfolio (Frontier), and reusable capabilities (Cap). Under matched resource limits, we compare complete runs with fixed or evolving Cap, and replace Cap while holding Hist and Frontier fixed to estimate the conditional value of accumulated capabilities. We also combine full trajectories with historical-state replay to examine how experience-based decisions affect candidate selection and portfolio outcomes. Across 18 long-horizon trajectories, end-to-end comparisons show no consistent gain from Cap evolution. Across 48 continuation branches from shared Hist and Frontier states, accumulated Cap also does not consistently outperform the initial Cap. Parameter tuning of existing factor structures can still improve the portfolio. In an exploratory replay of two screening batches from one Evolving trajectory, some screened-out candidates have positive marginal value at the original state, yet submitting all screened-out candidates sequentially slightly lowers final portfolio IC in both batches. These results show that candidate value depends on the evolving portfolio and submission order, and motivate evaluating self-evolving research capabilities through end-to-end outcomes, conditional capability value, and the consequences of experience-based decisions.

## Metadata
- **Published**: 2026-09-27T12:46:09Z
- **Authors**: Siyuan Li, Jiangfeng Zhang, Rui Yao, Weihua Qiu, Mingyang Xu, Zixuan Yuan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33524v1)