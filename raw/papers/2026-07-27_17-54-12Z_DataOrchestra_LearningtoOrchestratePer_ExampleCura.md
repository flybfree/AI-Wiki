---
title: DataOrchestra: Learning to Orchestrate Per-Example Curation of Pretraining Data
published: 2026-07-27T17:54:12Z
authors: Zhen Huang, Yikun Wang, Shijie Xia, Pengfei Liu
url: http://arxiv.org/abs/2607.24717v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DataOrchestra: Learning to Orchestrate Per-Example Curation of Pretraining Data

## Abstract
Pretraining data processing is critical to the downstream performance of Large Language Models (LLMs). However, many existing approaches define a fixed processing strategy at the corpus or domain level and apply it uniformly to many examples, without adapting to the needs of each example. We propose DataOrchestra, a framework that unifies different processing operations and orchestrates an example-specific pipeline for each example. Given a chunk of pretraining data, an orchestrator decides whether to drop, untouch, or clean it. For a chunk to be cleaned, it selects one or more downstream operations, ranging from programmatic editing to different forms of LLM-based rewriting. For each rewriting step, it further generates a concrete instruction, which is executed by the corresponding downstream tool model. We pretrain models from 0.5B to 7B from scratch on web data processed by DataOrchestra and observe stable average gains over individual data-processing methods across 11 benchmarks. DataOrchestra is also effective for math continued pretraining and outperforms stronger processing baselines, while reducing processing compute by skipping unnecessary downstream operations.

## Metadata
- **Published**: 2026-07-27T17:54:12Z
- **Authors**: Zhen Huang, Yikun Wang, Shijie Xia, Pengfei Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24717v1)