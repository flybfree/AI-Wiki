---
title: Modeling Decisions in Blockchain Analytics: A Leakage-Aware Evaluation of Tree-Based vs. Sequential Models
published: 2026-07-29T18:08:07Z
authors: Michał Bartnicki, Jarosław A. Chudziak
url: http://arxiv.org/abs/2607.27350v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Modeling Decisions in Blockchain Analytics: A Leakage-Aware Evaluation of Tree-Based vs. Sequential Models

## Abstract
Sybil bots are Ethereum actors that imitate legitimate users to extract airdrop rewards or influence governance. Recent Sybil detection methods increasingly use deep learning and treat blockchain activity as a quasi-linguistic sequence. However, complex sequence models are computationally expensive for real-time monitoring, and their reported performance may be inflated by label leakage from high-signal smart contracts. We ask whether and how organic users, Sybil bots, and MEV bots differ in the structural complexity of their transaction histories; whether sequential models outperform tree-based tabular models once leakage is reduced; whether transaction order or timing provides the stronger behavioral signal; and whether the resulting models are practical for low-latency deployment. Our approach to leakage-aware Sybil bot detection consists of a Blind-Spot protocol and a Transaction Grammar representation of wallet behavior. The former eliminates shortcuts associated with high-signal contracts, whereas the latter models wallets using rhythm, EVM execution structure, and intent. We evaluate this approach on Ethereum actor classification by comparing Transformer and BiLSTM sequence models against XGBoost and SVM baselines. We contribute a framework for leakage-aware Ethereum actor classification and a Transaction Grammar representation of wallet behavior. Our results demonstrate that, under leakage-aware evaluation, XGBoost outperforms Transformer-based sequence models while providing lower latency and estimated energy use.

## Metadata
- **Published**: 2026-07-29T18:08:07Z
- **Authors**: Michał Bartnicki, Jarosław A. Chudziak
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27350v1)