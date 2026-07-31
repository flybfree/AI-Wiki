---
title: Heterogeneous Ranking in Industrial-Scale Recommender Systems: A Case Study
published: 2026-07-30T01:41:42Z
authors: Di Bai, Jintao Liu, Zhenwei Tang, Peifan Wu, Nada Al-Thawr, Luoshu Wang
url: http://arxiv.org/abs/2607.27577v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Heterogeneous Ranking in Industrial-Scale Recommender Systems: A Case Study

## Abstract
Heterogeneous recommendation feeds present complex challenges that extend beyond those found in highly homogeneous environments (e.g., music-only or video-only closed-ecosystem platforms). In Google Discover, a unified feed integrates diverse content sourced from the decentralized open web, including web articles, long-form and short-form videos, user-generated content (UGC), and beyond. Different content types exhibit distinct feature densities and user interaction patterns. Building a unified ranking model that sustains high performance across such heterogeneity, while avoiding negative transfer or majority bias, remains a significant industrial challenge.   This paper presents an end-to-end case study on the industrial-scale multi-task ranking of heterogeneous feeds, grounded in real-world deployment. We introduce HA-MoE, a heterogeneity-adaptive multi-gated mixture-of-experts architecture that incorporates explicit heterogeneity context into both gating networks and expert representations. This approach enables effective specialization without significantly increasing operational overhead. To support reliable deployment, we introduce LENS, a lightweight observability framework that provides interpretable diagnostics of expert specialization and tracks this functional heterogeneity across continuous retraining. We evaluate our method using Dual-Level AUC (DL-AUC), a heterogeneity-aware evaluation metric that combines global ranking performance with cross-segment ranking correctness. Offline evaluations on a large-scale industrial dataset demonstrate consistent improvements over baseline models. Furthermore, online A/B testing confirms gains in feed activity and exploration metrics. Together, offline and online results validate the effectiveness of our approach for managing heterogeneity in industrial-scale recommender systems.

## Metadata
- **Published**: 2026-07-30T01:41:42Z
- **Authors**: Di Bai, Jintao Liu, Zhenwei Tang, Peifan Wu, Nada Al-Thawr, Luoshu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27577v1)