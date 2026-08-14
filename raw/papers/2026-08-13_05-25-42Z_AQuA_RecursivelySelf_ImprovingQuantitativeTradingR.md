---
title: AQuA: Recursively Self-Improving Quantitative Trading Research Agents
published: 2026-08-13T05:25:42Z
authors: Jiacheng Guo, Suozhi Huang, Yunlong Gao, Zihao Li, Jian Ge, Xu Kuang, Mengdi Wang
url: http://arxiv.org/abs/2608.12841v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AQuA: Recursively Self-Improving Quantitative Trading Research Agents

## Abstract
We study recursive self-improvement at the level of quantitative-investment research: whether an autonomous system can use evidence from earlier experiments to improve the hypotheses and candidates proposed in later iterations. We present AQuA, which comprises two separate language-model-driven research systems: one for symbolic factor discovery and one for trainable model development. The two systems do not share agents, memories, candidate spaces, or research state. Instead, each independently closes its own research loop by retaining validated evidence and using it to guide subsequent proposals. In this bounded sense, both systems implement recursive self-improvement at the level of the research process. Each system also uses its own sealed sandbox, which fixes the data splits, feature and label definitions, and evaluator while allowing the model to act only through constrained factor expressions or configuration diffs. The factor system, a manager-mediated multi-agent pipeline, discovers and combines factors into a signal that reaches a combined information coefficient of about $0.190$ on a crypto universe. The model system, a config-driven loop over a hybrid time-series architecture, reaches a per-stock information coefficient of $+0.0843$ on US equities and converts it into a threshold long/short strategy with a held-out Sharpe of up to $+2.50$ at a two-leg cost. The strategy is positive in every year from 2021 to 2025.

## Metadata
- **Published**: 2026-08-13T05:25:42Z
- **Authors**: Jiacheng Guo, Suozhi Huang, Yunlong Gao, Zihao Li, Jian Ge, Xu Kuang, Mengdi Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12841v1)