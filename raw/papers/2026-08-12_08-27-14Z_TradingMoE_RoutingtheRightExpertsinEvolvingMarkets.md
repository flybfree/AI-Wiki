---
title: TradingMoE: Routing the Right Experts in Evolving Markets
published: 2026-08-12T08:27:14Z
authors: Chang Zhou, Xingtong Yu, Minbin Huang, Zhennan Wu, Yuan Fang, Hong Cheng, Xinming Zhang
url: http://arxiv.org/abs/2608.11785v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TradingMoE: Routing the Right Experts in Evolving Markets

## Abstract
Large language models (LLMs) have shown strong potential for financial analysis and trading, but direct trading remains challenging because the predictive capabilities required can vary across assets, decision fields, and market conditions. Existing LLM-based trading systems either coordinate human-defined external experts or adopt conventional internal Mixture-of-Experts (MoE) routers that do not directly evaluate how individual experts contribute to trading decisions. Moreover, these routers receive no direct signal indicating when an inactive expert has become more suitable as market conditions change. We find that native router scores poorly reflect how much individual experts improve trading decisions, frequently leaving better alternatives unselected. We further reveal that token-specific expert usefulness exhibits a compact low-dimensional structure. Based on these findings, we propose TradingMoE, a trading-oriented sparse MoE that augments a frozen dense LLM with lightweight residual experts. We introduce a Query-Key router that represents the expertise required by each token under the current market context as a low-dimensional query and matches it with learnable expert keys. We further propose a sparse expert selection update mechanism that samples a few inactive experts during training and estimates whether they should replace the weakest expert in the current Top-k route. This mechanism enables the router to update expert selection as market conditions change while preserving sparse computation. Experiments against 22 baselines on stock and cryptocurrency markets show that TradingMoE improves cumulative return over the best-performing baselines by 30.89% and 30.7%, respectively. Rolling paper-trading experiments further demonstrate that its advantage persists under forward-only deployment.

## Metadata
- **Published**: 2026-08-12T08:27:14Z
- **Authors**: Chang Zhou, Xingtong Yu, Minbin Huang, Zhennan Wu, Yuan Fang, Hong Cheng, Xinming Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11785v1)