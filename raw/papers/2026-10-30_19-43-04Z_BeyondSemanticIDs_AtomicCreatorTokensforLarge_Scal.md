---
title: Beyond Semantic IDs: Atomic Creator Tokens for Large-Scale Generative Recommendation
published: 2026-10-30T19:43:04Z
authors: Zhuosheng Liu, Yihan Wu, Ziyun Xu, Xiaoxuan Liu, Longfei Yun, Kevin Han, Mingze Gao, Pengfei Wang, Junfeng Pan, Wenjie Fu, Haoran Liu
url: http://arxiv.org/abs/2611.00323v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Semantic IDs: Atomic Creator Tokens for Large-Scale Generative Recommendation

## Abstract
Recommending creators that a user does not yet follow is a cold-start problem: from hundreds of thousands of popular creators and only a short trail of prior engagements, the system must predict the next creator worth surfacing. The prevailing generative recommendation recipe tokenizes each creator into a \emph{Semantic ID} (SID) by quantizing a frozen embedding and trains a language model to generate SIDs. We show that this SID layer, not the language model, is the binding constraint. The creator-to-SID map is many-to-one, so colliding creators must be resolved by a popularity tie-break that caps creator-level recall and favors already-popular creators, and the frozen quantizer stops the training gradient from reaching the creator representation. We propose Atomic Creator Token (ACT), which gives every creator its own vocabulary token trained end-to-end. The map is bijective, so collisions are impossible and inference is a direct top-$k$ over creator logits. In a controlled comparison on production data in which the token layer is the only variable, ACT improves creator-level Recall@15 by 19.8 points ($1.84\times$) over a matched SID baseline, still leads when the SID codebook is enlarged $64\times$, and serves at ${\sim}2.7\times$ lower per-user latency. The advantage carries over to the public KuaiRand dataset, where ACT is the only method that beats a global-popularity baseline, provided each creator token sees enough training examples. In a live A/B test, ACT is directionally positive on every reported metric against both the SID-enhanced and the classic production rankers.

## Metadata
- **Published**: 2026-10-30T19:43:04Z
- **Authors**: Zhuosheng Liu, Yihan Wu, Ziyun Xu, Xiaoxuan Liu, Longfei Yun, Kevin Han, Mingze Gao, Pengfei Wang, Junfeng Pan, Wenjie Fu, Haoran Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.00323v1)