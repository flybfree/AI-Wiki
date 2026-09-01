---
title: AdaPath: Query-Adaptive Path-Finding via Path-Bank for Multi-Hop Implicit Biomedical KGQA
published: 2026-08-31T10:32:23Z
authors: Jun Hyeong Kim, Dongki Kim, Yinhua Piao, Sung Ju Hwang
url: http://arxiv.org/abs/2608.30556v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AdaPath: Query-Adaptive Path-Finding via Path-Bank for Multi-Hop Implicit Biomedical KGQA

## Abstract
Path-finding over knowledge graphs has become an effective way to ground LLM reasoning on multi-hop questions. However, biomedical QA introduces two distinct challenges that general-domain methods are not designed for: (i) queries do not expose intermediate reasoning and can be answered through multiple valid pathways, and (ii) biomedical knowledge graphs are densely connected, so path-finding methods easily take wrong turns. To address these challenges, we propose AdaPath, a path-finding framework that retrieves query-adaptive meta-paths from Path-Bank, which captures both query semantics and biomedical knowledge graph structure. AdaPath provides the missing cues in biomedical queries while effectively pruning dense knowledge graph neighborhoods during multi-hop reasoning. We further release BioStrat-QA, a biomedical KGQA benchmark that stratifies multi-hop queries by how much intermediate reasoning they expose. Across biomedical KGQA benchmarks, AdaPath consistently outperforms baselines, sustaining meaningful path-finding even when multi-hop queries expose less surface information. The source code is available at https://github.com/Jun-Hyeong-Kim/AdaPath.

## Metadata
- **Published**: 2026-08-31T10:32:23Z
- **Authors**: Jun Hyeong Kim, Dongki Kim, Yinhua Piao, Sung Ju Hwang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30556v1)