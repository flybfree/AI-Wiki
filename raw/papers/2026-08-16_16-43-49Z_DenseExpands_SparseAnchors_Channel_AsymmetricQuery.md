---
title: Dense Expands, Sparse Anchors: Channel-Asymmetric Query Expansion for Hybrid Retrieval
published: 2026-08-16T16:43:49Z
authors: Chunran Zhang
url: http://arxiv.org/abs/2608.15851v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dense Expands, Sparse Anchors: Channel-Asymmetric Query Expansion for Hybrid Retrieval

## Abstract
LLM-based query expansion improves retrieval by generating document-like passages. In hybrid retrieval, however, most evaluations fuse fixed top-$L$ dense and sparse rankings. Because the cutoff controls both which cross-channel contributions enter fusion and how much of each ranking is accessed, gains measured at one $L$ can change or reverse at another. We separate these effects by evaluating retrieval effectiveness under complete-list fusion and recording the policy-specific per-channel replay stopping depths at which its ordered top-$K$ is certified. We then introduce DESA (Dense Expansion and Sparse Anchoring), a channel-asymmetric query expansion method. An LLM generates complementary reference passages; orthogonal residual expansion adds their new semantic directions to the dense query, while score-product anchoring incorporates their lexical cues into sparse retrieval without broadening the original query's lexical support. Across seven BEIR datasets, DESA improves nDCG@10 and Recall@20 over the unexpanded query by 3.82% and 2.38%, while reducing dense and sparse access depths by 36.90% and 36.56%. With equal dataset weighting, 63.31% of queries become shallower in both channels. However, both depths increase with Contriever on Touché-2020. These results support channel-specific integration of generated passages and joint evaluation of retrieval effectiveness and access depth.

## Metadata
- **Published**: 2026-08-16T16:43:49Z
- **Authors**: Chunran Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15851v1)