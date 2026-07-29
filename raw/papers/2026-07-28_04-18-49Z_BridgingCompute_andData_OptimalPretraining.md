---
title: Bridging Compute- and Data-Optimal Pretraining
published: 2026-07-28T04:18:49Z
authors: Tian Qin, Kimia Hamidieh, David Alvarez-Melis
url: http://arxiv.org/abs/2607.25271v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bridging Compute- and Data-Optimal Pretraining

## Abstract
Classical compute-optimal scaling laws assume an unbounded supply of fresh pretraining data, yet pretraining is increasingly entering a regime in which compute grows faster than the availability of high-quality data. We propose Compute-Data (CD) scaling laws, a unified framework that bridges compute-optimal scaling, where data scales freely with compute, and data-optimal scaling, where the corpus is fixed while compute can grow without bound. CD scaling extends classical scaling laws by introducing a token-effectiveness function, $η$, which quantifies the value of a derived token-produced, for example, through multi-epoch repetition or paraphrasing-relative to a fresh token, ranging from a perfect substitute to having no value. We fit $η$ for two data-expansion strategies, multi-epoch repetition and paraphrasing, across model sizes from 14M to 600M parameters using the Dolma-3 corpus. We find that token effectiveness is far from constant: it depends jointly on model size, the tokens-per-parameter ratio, and the amount of derived data, and it saturates as the corpus is expanded. The functional form of $η$ implies diminishing returns when substituting compute for data as either model size or data availability increases. It also partitions training into three operational regimes---compute-bound, data-bound, and model-bound---and shows that classical compute-optimal allocation is suboptimal across most practically relevant settings.

## Metadata
- **Published**: 2026-07-28T04:18:49Z
- **Authors**: Tian Qin, Kimia Hamidieh, David Alvarez-Melis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25271v1)