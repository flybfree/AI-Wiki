---
title: MEMONDEMAND: A Memory Management System for Large-Scale Enterprise Data
published: 2026-08-22T23:54:38Z
authors: Xinyuan Song, Bowen Zhu, Hasibul Haque, Liang Zhao
url: http://arxiv.org/abs/2608.22141v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MEMONDEMAND: A Memory Management System for Large-Scale Enterprise Data

## Abstract
Enterprise repositories are large, heteroge- neous, and continuously updated, making re- trieval difficult when efficient access, source- faithful evidence, and cross-query adaptation must be supported together. Enterprise mem- ory extends retrieval beyond the model con- text, but existing systems do not jointly address collection-specific hierarchy construction, low- cost routing, detailed evidence loading, and workload-aware memory updates at this scale. We introduce MEMONDEMAND, short for On- Demand Memory, a memory management sys- tem with three coordinated mechanisms: a dy- namic multi-level hierarchy that determines the abstraction structure and depth for each col- lection, dual memory at every hierarchy level that separates distilled routing from detailed evidence, and on-demand memory promotion that updates node priority under a bounded active-state budget. On EnterpriseRAG-Bench, MEMONDEMAND outperforms the strongest published LB#1 result at every evaluated scale from 10M tokens through the complete 618M- token collection, with gains of 12.23% at 10M and 4.66% at 618M. Results on FinanceBench, HotpotQA, and FRAMES further show strong performance across financial, multi-hop, and fact-retrieval settings. Together, these results establish MEMONDEMAND as an accurate, ef- ficient, and scalable memory solution for very large enterprise repositories across data scales, domains, and evidence requirements. Our code is available at https://github.com/ xfab-xinyuansong/MemOnDemand.git.

## Metadata
- **Published**: 2026-08-22T23:54:38Z
- **Authors**: Xinyuan Song, Bowen Zhu, Hasibul Haque, Liang Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22141v1)