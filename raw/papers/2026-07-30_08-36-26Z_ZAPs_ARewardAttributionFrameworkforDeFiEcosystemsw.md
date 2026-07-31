---
title: ZAPs: A Reward Attribution Framework for DeFi Ecosystems with Adversarial-Robust Scoring via Parallel Anomaly Ensemble Detection
published: 2026-07-30T08:36:26Z
authors: Girish G N, Ashutosh Sahoo, Ajay Bhat, Akshay SP, Gurukiran S, Parag Paul, Dhanashekar Kandaswamy
url: http://arxiv.org/abs/2607.27859v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ZAPs: A Reward Attribution Framework for DeFi Ecosystems with Adversarial-Robust Scoring via Parallel Anomaly Ensemble Detection

## Abstract
Incentive programs are central to user acquisition in decentralized finance, but many reward systems rely on raw volume, transaction count, and wallet count, making them vulnerable to bots and sybil operations. We present ZAPs, a reward attribution framework that combines economic contribution scoring with adversarial robustness. A composite activity score uses protocol-specific percentile normalization to limit whale dominance while preserving differentiation among users. A two-layer weighting mechanism combines protocol share within sector and sector share within the ecosystem, which reduces the profitability of farming small protocols. We show that the maximum reward obtainable from any protocol is bounded by that protocol's global volume share.   ZAPs also introduces a four-layer defense stack consisting of transaction-level integrity checks, a parallel anomaly ensemble, post-distribution behavioral memory, and graph-based sybil clustering. The anomaly ensemble combines a one-class reconstruction model with an isolation forest and applies graduated rather than binary penalties. On 1,073 labeled malicious wallets covering 124,638 transactions, the ensemble achieves 0.923 +/- 0.013 ROC-AUC, compared with 0.891 +/- 0.016 for the reconstruction model alone, when the isolation forest is trained on benign wallets. Training it on the pooled population reverses its polarity and removes the ensemble gain. Controlled simulations reduce adversarial reward capture by 30-90 percent while legitimate-user scenarios change by 1-8 percent. Live campaigns recorded a 56 percent reduction in sybil allocation, a 49 percent increase in quality-wallet participation, and a 50 percent reduction in sell pressure.

## Metadata
- **Published**: 2026-07-30T08:36:26Z
- **Authors**: Girish G N, Ashutosh Sahoo, Ajay Bhat, Akshay SP, Gurukiran S, Parag Paul, Dhanashekar Kandaswamy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27859v1)