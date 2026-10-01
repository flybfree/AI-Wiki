---
title: RankEvolve: A Reliable Multi-Agent Auto-Research Harness for Evolving Ranking Models
published: 2026-09-30T11:50:46Z
authors: Zheng Chen, Linfeng Liu, Hong Li, Hong Yan
url: http://arxiv.org/abs/2609.39551v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RankEvolve: A Reliable Multi-Agent Auto-Research Harness for Evolving Ranking Models

## Abstract
Auto-research agents, LLM systems that propose, implement, train, and evaluate model changes across iterations, promise to automate applied ML's experimental loop. Over long horizons, execution accuracy is a binding constraint: a change can silently leak held-out data, omit normalization, disconnect a gradient, or leave a train/eval flag unwired, invalidating expensive runs and compounding error across iterations. We present RankEvolve, an auto-research framework for evolving generative ranking models. An Executable Operating Protocol (EOP) declares phases, gates, branches, and loops, and the runtime enforces the compiled state machine. A meta-meta-harness composes complete black-box coding-agent products, including Claude Code and Codex, as execution-graph nodes that review and repair one another's work. In a budget-matched evaluation, heterogeneous composition raises all-oracle execution accuracy from the best single-product baseline of 45.8 percent to 62.5 percent (paired +16.7 points, 95 percent CI [6.6, 26.7]) while achieving a 10.4 percent silent critical-defect rate. An implemented knowledge layer carries findings, including negative results, across iterations. In a twelve-iteration deployment on the open-source HSTU recommender, RankEvolve reported NDCG@10 of 0.2192 on MovieLens-20M LARGE (+4.48 percent over the published anchor) and 0.1948 on BASE (+2.80 percent). ExecML-HSTU, seeded by incidents from that deployment, provides the oracle benchmark for the execution-accuracy evaluation. A pre-specified LitGPT transfer split replicates the heterogeneous-composition effect beyond recommendation (+12.5 points, 95 percent CI [3.0, 22.0]), and a paired ablation isolates per-step from full-protocol instruction injection. These results characterize when runtime-controlled composition of coding-agent products improves execution accuracy.

## Metadata
- **Published**: 2026-09-30T11:50:46Z
- **Authors**: Zheng Chen, Linfeng Liu, Hong Li, Hong Yan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39551v1)