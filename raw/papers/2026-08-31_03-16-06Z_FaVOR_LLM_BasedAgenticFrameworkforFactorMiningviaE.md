---
title: FaVOR: LLM-Based Agentic Framework for Factor Mining via Empirical Validation
published: 2026-08-31T03:16:06Z
authors: Hyeonjin Kim, Minseok Kim, Seunghyeon Jung, Sujin Pyo, Huisu Jang, Woojin Lee
url: http://arxiv.org/abs/2608.30192v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FaVOR: LLM-Based Agentic Framework for Factor Mining via Empirical Validation

## Abstract
Traditional finance relies on experts to hand-craft factors through a principled process grounded in economic rationale. Recent LLM-based multi-agent systems have automated this process, scaling factor mining far beyond manual effort. However, these automated approaches optimize directly for returns and rarely check whether a generated factor still expresses the economic hypothesis that motivated it. We identify this inconsistency between mathematical form and economic meaning as a structural failure mode of return-oriented automation. The resulting factors blur the line between real signals and spurious correlations and break down across regime shifts. We propose FaVOR (Factor Validation through Observable Reasoning), an agentic framework that restructures factor mining around hypothesis-level evidence rather than return outcomes. In place of the standard hypothesis-to-formula leap, FaVOR enforces a three-stage consistency loop tying mathematical form to economic rationale throughout. (1) Decomposition splits a broad economic hypothesis into independent observable conditions. (2) Validation checks whether each factor reflects its intended condition. (3) Integration merges them into a composite whose structure remains interpretable. On the CSI 500 and S&P 500 in 2025, FaVOR outperforms existing baselines while remaining effective across regimes. FaVOR shows that hypothesis-grounded factor discovery produces signals that are interpretable by construction, regime-robust, and economically faithful. The code is available at https://github.com/damilab/FaVOR.

## Metadata
- **Published**: 2026-08-31T03:16:06Z
- **Authors**: Hyeonjin Kim, Minseok Kim, Seunghyeon Jung, Sujin Pyo, Huisu Jang, Woojin Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30192v1)