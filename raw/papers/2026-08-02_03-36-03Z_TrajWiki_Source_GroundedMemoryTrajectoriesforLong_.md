---
title: TrajWiki: Source-Grounded Memory Trajectories for Long-Horizon Dialogue Agents
published: 2026-08-02T03:36:03Z
authors: Jingyu Sun, Yuyang Xue, Mingyang Li, Zhengtao Yao, Jiachen Li, Yang Cui, Wenhao Cai, Haozhe Liu, Fangying Wang, Magdalene Katharina Montgomery, Syed Murtuza Baker, Hongpeng Zhou
url: http://arxiv.org/abs/2608.00967v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TrajWiki: Source-Grounded Memory Trajectories for Long-Horizon Dialogue Agents

## Abstract
Large language model agents have shown strong capabilities in generating coherent and contextually appropriate responses, yet robust long-horizon dialogue remains limited by the lack of external memory that is traceable, updatable, and diagnostically transparent. Existing memory-augmented agents often store memories as isolated records or overwritable states, making it difficult to preserve how information originates, evolves, conflicts, or becomes obsolete over time. We propose TrajWiki, a trajectory-based memory framework for long-horizon conversational agents. Instead of treating memory as static entries, TrajWiki represents each memory as a source-grounded evolution trajectory, maintained through immutable episodic snapshots and claim-level operations such as ADD, REVISE, and DEPRECATE. To reduce fragmentation and retrieval cost, TrajWiki further introduces Memory Wiki, a persistent intermediate layer that incrementally compiles dialogue history into structured and interlinked wiki pages capturing salient entities, events, quantities, topics, and conflicts. At inference time, queries are routed hierarchically from relevant wiki pages to linked memory trajectories, then to corresponding snapshots and source messages for evidence-grounded answer synthesis. Experiments on LoCoMo and MedMT show that TrajWiki improves long-horizon dialogue performance across both open-source and closed-source LLM backbones, while providing greater interpretability and diagnostic visibility into memory evolution, retrieval failures, and answer generation.

## Metadata
- **Published**: 2026-08-02T03:36:03Z
- **Authors**: Jingyu Sun, Yuyang Xue, Mingyang Li, Zhengtao Yao, Jiachen Li, Yang Cui, Wenhao Cai, Haozhe Liu, Fangying Wang, Magdalene Katharina Montgomery, Syed Murtuza Baker, Hongpeng Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00967v1)