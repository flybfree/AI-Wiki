---
title: OneShot: Index-in-Ranking with Neural Scoring for Large-Scale Retrieval
published: 2026-07-29T21:29:00Z
authors: Ziwei Li, Shuyao Li, Xufeng Cai, Xue Zou, Yiming Ma, Huiting Lu, Wujie Yan, Zhichen Zhao, Yang Lu, Zhe Wang, Rui Luo, Zhengyu Su, Dan Zhang, Ji Liu
url: http://arxiv.org/abs/2607.27475v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OneShot: Index-in-Ranking with Neural Scoring for Large-Scale Retrieval

## Abstract
In modern recommendation systems, retrieval serves as a primary stage responsible for filtering billions of candidate items down to thousands prior to refined ranking. To make this massive search effective and efficient, the system relies on ranking accuracy and indexing efficiency. However, these two objectives are traditionally misaligned: while the former optimizes for the alignment between ranking predictions and user behavior, the latter optimizes for a structural grouping of item representations which enables fast search among billions of candidates. Thus, despite extensive efforts to scale up interaction modeling for retrieval, they remain fundamentally limited by the structural misalignment between the ranking objectives and the proximity-learned index. In this work, we address this long-standing dichotomy by proposing a new holistic retrieval framework, OneShot. It is an end-to-end, in-model index learning framework that natively aligns index learning with ranking objectives. Using this joint learning as a structural foundation, OneShot pushes the boundaries of retrieval expressiveness by scaling interaction modeling with neural scoring beyond the persistent dot-product bottleneck. OneShot is fully deployed in Instagram's industrial short-video recommendation system, driving significant wins in user daily sessions, engagement, and time-spent. Additionally, OneShot achieves a $20\%$ recall gain at the operational ranking volume and a 10x efficiency improvement at an equivalent recall level.

## Metadata
- **Published**: 2026-07-29T21:29:00Z
- **Authors**: Ziwei Li, Shuyao Li, Xufeng Cai, Xue Zou, Yiming Ma, Huiting Lu, Wujie Yan, Zhichen Zhao, Yang Lu, Zhe Wang, Rui Luo, Zhengyu Su, Dan Zhang, Ji Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27475v1)