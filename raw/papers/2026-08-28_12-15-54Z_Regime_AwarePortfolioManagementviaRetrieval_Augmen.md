---
title: Regime-Aware Portfolio Management via Retrieval-Augmented LLM-Guided Expert Switching
published: 2026-08-28T12:15:54Z
authors: Ahmad Asadi, Reza Safabakhsh
url: http://arxiv.org/abs/2608.28252v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Regime-Aware Portfolio Management via Retrieval-Augmented LLM-Guided Expert Switching

## Abstract
Financial markets are inherently non-stationary, making the effectiveness of individual portfolio-management strategies highly dependent on changing market conditions. This work proposes a retrieval-augmented expert-switching framework that dynamically selects portfolio management experts based on their historical performance under similar market situations. A dual-stream variational autoencoder represents asset-level and market-wide information, while a retrieval-based knowledge base stores historical situations and expert performance. During inference, an instruction-tuned LLM reasons over the retrieved evidence to identify the most appropriate expert rather than directly generating portfolio actions. We further establish a monotonicity property showing that adding a locally superior expert cannot degrade the switching mechanism's performance. Experiments across cryptocurrency, stock, and foreign-exchange markets show that the proposed selector achieves the highest cumulative return and Sharpe ratio among the evaluated selection strategies in all three markets. In the stock market, for example, cumulative return increases from 26% for the best fixed expert to 34%, while the Sharpe ratio improves from 0.74 to 0.96. Ablation results confirm the importance of both retrieval and LLM reasoning, while experiments with different expert-pool sizes demonstrate the value of complementary expertise. Overall, the findings support retrieval-grounded expert switching as an effective approach to adaptive portfolio management in non-stationary financial environments.

## Metadata
- **Published**: 2026-08-28T12:15:54Z
- **Authors**: Ahmad Asadi, Reza Safabakhsh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28252v1)