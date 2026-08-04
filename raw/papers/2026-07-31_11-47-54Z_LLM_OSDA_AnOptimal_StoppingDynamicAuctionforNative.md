---
title: LLM-OSDA: An Optimal-Stopping Dynamic Auction for Native Advertising in Multi-Turn LLM Conversations
published: 2026-07-31T11:47:54Z
authors: Yan Fang, Jialin Chen, Chun Gan, Hang Yu, Mingjun Nie, Yeyu Zhang, Fengxiang He, Ching Law
url: http://arxiv.org/abs/2608.00123v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM-OSDA: An Optimal-Stopping Dynamic Auction for Native Advertising in Multi-Turn LLM Conversations

## Abstract
LLM-native advertising embeds sponsored content directly into model-generated responses, shifting the unit of sale from a fixed slot to a moment within an evolving conversation. Existing LLM ad-auction mechanisms primarily operate within a single response, settling the winner but not the timing. The extension is nontrivial: with one native insertion opportunity per session, the stopping time depends on bids, coupling timing with allocation, so static truthfulness arguments no longer apply. We propose the LLM-based Optimal Stopping Dynamic Auction (LLM-OSDA), a dynamic cost-per-click auction that integrates Bellman optimal stopping, winner allocation, and envelope pricing. A bid-independent LLM layer estimates contextual click quality and seamlessly renders the winning ad, while bids enter only the committed auction mechanism. Under an exact Bellman oracle, the expected discounted-click allocation is monotone in each advertiser's bid, and the corresponding envelope payment makes truthful bidding weakly dominant in expectation. For practical deployment, a learned StopNet approximates the Bellman action values. We show that its decisions differ from the optimal policy only near the stopping boundary and bound the resulting incentive loss in terms of its approximation error. Experiments on a simulated conversational advertising corpus show that LLM-OSDA improves net revenue by 11 percent over the strongest fixed-timing baseline while maintaining comparable user retention. Code is at https://github.com/2025Fang2025/llm-osda.

## Metadata
- **Published**: 2026-07-31T11:47:54Z
- **Authors**: Yan Fang, Jialin Chen, Chun Gan, Hang Yu, Mingjun Nie, Yeyu Zhang, Fengxiang He, Ching Law
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00123v1)