---
title: Deep Research Pretraining via Predictive Navigation
published: 2026-08-01T04:17:14Z
authors: Jiang Zhou, Zhiyuan Fan, Xing Wu, Tinghao Yu, Feng Zhang, Lilin Wang
url: http://arxiv.org/abs/2608.00432v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Deep Research Pretraining via Predictive Navigation

## Abstract
Deep research agents are often trained on expensive, environment-grounded tool-use trajectories that require repeated retrieval, document inspection, and report evaluation. We introduce Deep Research Pretraining (DRP), an offline framework that derives predictive navigation supervision from naturally occurring evidence structures. Given a citation-bearing or hyperlinked passage, DRP constructs a proxy research objective, recovers linked evidence and graph-related alternatives, and converts them into search-open-write trajectories. This teaches models what to search for, which documents to inspect, and how to synthesize evidence, without a live retrieval environment or executed policy rollout. We instantiate DRP on scholarly citation graphs (DRP-Paper) and Wikipedia hyperlinks (DRP-Web), continually pretrain separate Qwen3-14B-Base models on 1B tokens, and fine-tune them on controlled fractions of 13K agent trajectories. Across five independently sampled subsets at each low-data budget, both variants consistently outperform matched no-DRP models on DeepResearch Bench. With one quarter of the SFT data, DRP-Web even surpasses a fixed no-DRP full-data checkpoint, with gains transferring to ResearchQA, WebWalkerQA, and SimpleQA. Starting from matched low-data SFT checkpoints, the DRP-Web advantage also persists through subsequent agentic RL. Source-matched and evidence-mismatch controls indicate that these improvements arise from evidence-conditioned navigation rather than domain exposure or agent-format imitation. DRP thus provides a promising complementary approach to trajectory-based agent training.

## Metadata
- **Published**: 2026-08-01T04:17:14Z
- **Authors**: Jiang Zhou, Zhiyuan Fan, Xing Wu, Tinghao Yu, Feng Zhang, Lilin Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00432v1)