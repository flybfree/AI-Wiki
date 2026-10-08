---
title: HGP:An on-device personalized agent memory via hybrid graph storage
published: 2026-10-07T13:37:38Z
authors: Ran Zhou, Xueming Han, Jiaheng Liu, Yuyao Zhang, Fanyu Meng, Junlan Feng, Yuxiang Ren
url: http://arxiv.org/abs/2610.10071v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HGP:An on-device personalized agent memory via hybrid graph storage

## Abstract
LLM-based agents face challenges in personalized interactive tasks due to heterogeneous, multi-typed, and implicitly constrained long-term traces. Existing memory mechanisms struggle with accurate routing and retrieval, especially on-device where personalization is critical. Most methods use single-vector representations, blurring type distinctions and relational structure. We propose HGP, a hybrid graph memory framework. HGP employs a lightweight self-enhancement classifier for personalized memory routing and constructs episodic, semantic, and procedural memories as graphs. It also extracts working memory as a state trajectory to capture current state and implicit constraints, ensuring reliable decision-making. The classifier reduces large-model calls, enabling on-device deployment, while graph storage enables accurate retrieval and incremental user profile refinement. Experiments on two benchmarks show that on PAL-Set solution selection, HGP achieves an S-score of 35.58, nearly 7 points above the strongest baseline. Code and data are at https://github.com/Ouan6/HGP-.git.

## Metadata
- **Published**: 2026-10-07T13:37:38Z
- **Authors**: Ran Zhou, Xueming Han, Jiaheng Liu, Yuyao Zhang, Fanyu Meng, Junlan Feng, Yuxiang Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.10071v1)