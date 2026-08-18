---
title: Agentic-SQL Revisited: Autonomy-Based Taxonomy and Empirical Benchmark Analysis for LLM Text-to-SQL
published: 2026-08-15T19:40:05Z
authors: Changruo Zhao, Zujun Peng, Yu Tian, Yuting Liu, Yiyun Su, Huiying Zhu, Luyan Zhang, Heming Zeng
url: http://arxiv.org/abs/2608.15389v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agentic-SQL Revisited: Autonomy-Based Taxonomy and Empirical Benchmark Analysis for LLM Text-to-SQL

## Abstract
LLM-based Text-to-SQL progress is reported across heterogeneous benchmarks, backbones, and inference protocols, making cross-system comparison fragile. We reframe the field as a leaderboard aggregation: we collect the metrics authors themselves report and organize them along an inference-autonomy axis spanning constrained, in-context, iterative, agentic, and reasoning-internalized generation, with traceable provenance for every cell. To anchor the aggregation empirically, we run a focused case study on Spider, comparing 8B open-source backbones with and without chain-of-thought (CoT) supervision against few-shot DeepSeek~V3 and GLM-4 baselines. Four patterns emerge: Spider gains transfer unevenly to BIRD and Spider~2.0; autonomy buys robustness at non-trivial cost; reasoning internalization sits between answer-only decoding and externally orchestrated agents; and CoT gains concentrate on Hard and Extra-Hard queries. We release a Python harness mirroring the autonomy axis so that future methods can be added directly to the leaderboard.

## Metadata
- **Published**: 2026-08-15T19:40:05Z
- **Authors**: Changruo Zhao, Zujun Peng, Yu Tian, Yuting Liu, Yiyun Su, Huiying Zhu, Luyan Zhang, Heming Zeng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15389v1)