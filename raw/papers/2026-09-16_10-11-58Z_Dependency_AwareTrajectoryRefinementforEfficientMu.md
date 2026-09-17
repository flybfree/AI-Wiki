---
title: Dependency-Aware Trajectory Refinement for Efficient Multi-Turn Agent Fine-Tuning
published: 2026-09-16T10:11:58Z
authors: Zhuo Chen, Zhen Zhang, Xinyu Wang, Kewei Tu
url: http://arxiv.org/abs/2609.18417v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dependency-Aware Trajectory Refinement for Efficient Multi-Turn Agent Fine-Tuning

## Abstract
Multi-turn agent trajectories often contain redundant rounds (failed tool calls, parallel sub-queries, verification-only steps) that inflate both training and inference cost. We propose viewing each trajectory as a \emph{round-level dependency DAG} that exposes which rounds are globally load-bearing for the final answer, and fine-tune agents on trajectories refined through this DAG. Given an LLM-annotated DAG, these edits are deterministic and interpretable, with optional rephrasing. Models trained on these refined trajectories consistently outperform those trained on the original trajectories at lower inference cost. Specifically, across four multi-modal QA benchmarks, our refinements improve downstream accuracy by up to $1.7$\,pp over vanilla SFT (and $5.7$\,pp over an LLM-deletion baseline) while reducing per-sample inference messages by up to approximately $40\%$ and inference tokens by up to approximately $48\%$, translating to substantial savings in compute and serving cost. Code is available.

## Metadata
- **Published**: 2026-09-16T10:11:58Z
- **Authors**: Zhuo Chen, Zhen Zhang, Xinyu Wang, Kewei Tu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.18417v1)