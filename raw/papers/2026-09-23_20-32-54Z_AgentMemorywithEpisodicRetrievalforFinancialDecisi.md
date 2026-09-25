---
title: Agent Memory with Episodic Retrieval for Financial Decision-Making
published: 2026-09-23T20:32:54Z
authors: Nuoyue Xu, Jiang Liu, Wenxuan Huang, Xiang Zhang, Juntai Cao, Jiaqi Wei
url: http://arxiv.org/abs/2609.28771v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agent Memory with Episodic Retrieval for Financial Decision-Making

## Abstract
Large language models (LLMs) have demonstrated strong capabilities in financial analysis and reasoning, inspiring recent advances in agent-based trading frameworks. While these systems show promise, prior approaches either emphasize long-horizon forecasting or operate as stateless analyzers, limiting their applicability to the demands of trading in complicated settings. To address these gaps, we introduce META (Memory Enhanced Trading Agent), the first RAG-like episodic-memory-augmented multi-agent framework for financial decision making. META integrates a family of specialized indicator agents (e.g., Trend, MACD, Stochastic, RSI, SMA, AVWAP, Heikin-Ashi) with a Decision Agent that fuses their reports, and a Memory module that retrieves and updates past trading episodes encoded as market state embeddings with outcomes and reflections. By recalling relevant experiences and adaptively reweighting signals under similar market regimes, META achieves improved directional accuracy and robustness under short-horizon evaluation. Our results demonstrate that episodic memory provides a powerful mechanism for regime-aware, interpretable, and low-latency decision-making in trading and decision making. The code of this project is released on GitHub.

## Metadata
- **Published**: 2026-09-23T20:32:54Z
- **Authors**: Nuoyue Xu, Jiang Liu, Wenxuan Huang, Xiang Zhang, Juntai Cao, Jiaqi Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.28771v1)