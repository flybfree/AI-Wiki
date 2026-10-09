---
title: MemTrial: Learning When to Trust Memory in LLM Portfolio Agents
published: 2026-10-08T11:27:49Z
authors: Guanghao Wu, Zhuo Cai, Shoujin Wang
url: http://arxiv.org/abs/2610.11732v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemTrial: Learning When to Trust Memory in LLM Portfolio Agents

## Abstract
Large language model (LLM) agents for portfolio management learn from experience: they credit each experience in their memory with the outcome of the decisions that used it. In financial markets, however, this outcome mostly reflects the market move shared by all decisions on that date, so the credit tracks the market rather than the experience, and these agents often do worse than simply holding the equal-weight (1/$N$) portfolio. We ask how an agent can credit an experience with what it changes, and answer it by putting memory on trial: drafts of the same decision with and without an experience face the same market, so the outcome they share cancels in their difference. Our agent, MemTrial, drafts each decision with eight combinations of its retrieved experiences, chosen by a fractional factorial design, and credits each experience with its Banzhaf value, the average of these differences. As each date occurs once and each draft is a noisy LLM sample, these credits are noisy and may not hold on new dates. MemTrial therefore pools them across dates and similar experiences with a hierarchical Bayesian model, acts on them only after they have predicted unseen dates, and otherwise stays anchored at a conservative reference such as 1/$N$. On four benchmarks, MemTrial not only benefits from experiences that matter (the best of 15 methods on a semi-synthetic benchmark with known experience quality) but also limits its losses when its values do not hold (at most 2.2\% below 1/$N$ on PortBench and InvestorBench, against 15--38\% for the best experience-learning agent). Averaged over five settings, it improves the utility of the best experience-learning agent by 21.2\%, and with eight LLMs it beats every LLM-based baseline on InvestorBench.

## Metadata
- **Published**: 2026-10-08T11:27:49Z
- **Authors**: Guanghao Wu, Zhuo Cai, Shoujin Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11732v1)