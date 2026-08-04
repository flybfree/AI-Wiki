---
title: 402Pilot: An x402 Decision Layer for Autonomous Agent Micropayments
published: 2026-08-02T16:04:57Z
authors: Yin Li, Yanbo He, Boo-Ho Yang, Rav Lawana, Ziyue Li, Wei Zeng, Jing Tang, Fugee Tsung
url: http://arxiv.org/abs/2608.01341v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# 402Pilot: An x402 Decision Layer for Autonomous Agent Micropayments

## Abstract
Programmable-payment protocols such as x402 enable per-request micropayments, but they do not determine which payable service an autonomous agent should buy under a finite wallet. We formulate this buyer-side problem as agent-native payment decision-making: contextual provider selection under wallet pressure, chosen-only paid feedback, and changing market conditions. We propose 402Pilot, a protocol-agnostic buyer-side decision layer between autonomous agents and payment execution that implements purchasing policies for selecting among payable providers. We instantiate it with PA-DCT, a payment-aware discounted contextual Thompson-sampling policy that adapts purchasing decisions under wallet pressure while learning from post-payment feedback. To evaluate buyer-side payment policies, we introduce 402Pilot-Bench, a frozen-replay benchmark spanning 823 tasks, five heterogeneous provider pipelines, and three market regimes, each evaluated over 30 paired seeds. PA-DCT achieves the strongest fixed-wallet adaptive trade-off among non-oracle policies: it maintains competitive service quality while spending only 39 to 43 percent of the wallet and reallocates spending as market conditions change. It attains the best non-oracle PA-gap/T under the price shock and the best mean and worst-case ranks across the nine scenario-metric combinations of quality, ROI, and PA-gap/T. Comparisons with learning baselines and component ablations further support the effectiveness and design of the proposed decision policy. These results suggest that programmable payment must be complemented by buyer-side decision-making capable of learning service value and adapting purchasing decisions accordingly.

## Metadata
- **Published**: 2026-08-02T16:04:57Z
- **Authors**: Yin Li, Yanbo He, Boo-Ho Yang, Rav Lawana, Ziyue Li, Wei Zeng, Jing Tang, Fugee Tsung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01341v1)