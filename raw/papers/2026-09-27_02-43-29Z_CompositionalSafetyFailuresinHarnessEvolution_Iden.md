---
title: Compositional Safety Failures in Harness Evolution: Identification and Runtime Monitoring
published: 2026-09-27T02:43:29Z
authors: Zhixiang Zhang, Zesen Liu, Wai Ip Lai, Hongxu chen, Dongdong She
url: http://arxiv.org/abs/2609.33123v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Compositional Safety Failures in Harness Evolution: Identification and Runtime Monitoring

## Abstract
Self-evolving agent harnesses continually update persistent components such as memory, prompts, skills, and tools. We call this process harness evolution. However, such evolution could introduce unexpected safety risks. Existing work studies harness misevolution and validates candidate harnesses or attributed individual component updates, leaving safety analysis of cross-component update interactions largely unexamined. To address this gap, we study compositional safety failures in harness evolution, where interactions among individually safe and utility-preserving component updates can produce undesirable or unsafe agent behavior, revealing a safety risk intrinsic to harness evolution. Across three safety-related benchmarks, we identify 43 pairwise and 18 irreducible 3-way compositional safety failures. Conventional solution incurs combinatorial complexity in validating cross-component interactions, leaving the safety checking impractical as the harness evolves. To solve this, we introduced a typed hypergraph that represents component states as nodes and safety-relevant higher-order interactions as hyperedges. When the harness changes, the hypergraph updates only the interaction neighborhood of the changed states rather than reconstructing the global composition space. Building on that, we develop a hypergraph-guided runtime monitoring mechanism. Experiments show that our method effectively mitigates compositional safety risks while preserving task utility and reducing interaction-checking costs, and further reveal an empirical safety-utility-cost trade-off across different safety mechanisms.

## Metadata
- **Published**: 2026-09-27T02:43:29Z
- **Authors**: Zhixiang Zhang, Zesen Liu, Wai Ip Lai, Hongxu chen, Dongdong She
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33123v1)