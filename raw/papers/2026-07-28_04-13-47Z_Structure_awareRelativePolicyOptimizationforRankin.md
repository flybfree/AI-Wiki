---
title: Structure-aware Relative Policy Optimization for Ranking
published: 2026-07-28T04:13:47Z
authors: Yiteng Tu, Weihang Su, Zitao Su, Yiqun Liu, Min Zhang, Qingyao Ai
url: http://arxiv.org/abs/2607.25268v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Structure-aware Relative Policy Optimization for Ranking

## Abstract
Ranking is a fundamental component of modern information access systems. Reinforcement learning (RL) provides a flexible framework for directly optimizing coarse-grained feedback and system-level objectives defined over the complete ranking list. However, existing RL-based ranking methods typically treat each sampled permutation as an atomic output and evaluate it primarily through a scalar reward, overlooking the structural relationships among different ranking lists. Consequently, permutations with similar rewards but substantially different permutation patterns may receive comparable optimization signals, potentially leading to inaccurate credit assignment and overly aggressive policy updates. To address this limitation, we propose SRPO, a \textbf{S}tructure-aware \textbf{R}elative \textbf{P}olicy \textbf{O}ptimization framework for listwise ranking. SRPO measures the discrepancy between sampled permutations using a top-weighted Kendall-tau distance and normalizes their pairwise reward differences by the corresponding distances. It quantifies the reward improvement per unit of ranking change, thereby emphasizing efficient local refinements, particularly those involving top-ranked positions. Experimental results across two ranking scenarios demonstrate that explicitly modeling permutation-level differences improves the effectiveness and stability of listwise ranking, with particularly favorable performance in limited-feedback and complex list-level optimization settings.

## Metadata
- **Published**: 2026-07-28T04:13:47Z
- **Authors**: Yiteng Tu, Weihang Su, Zitao Su, Yiqun Liu, Min Zhang, Qingyao Ai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25268v1)