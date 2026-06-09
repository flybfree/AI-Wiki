---
title: Natural Language Query to Configuration for Retrieval Agents
published: 2026-05-26T17:58:47Z
authors: Melissa Z. Pan, Negar Arabzadeh, Mathew Jacob, Fiodar Kazhamiaka, Esha Choukse, Matei Zaharia
url: http://arxiv.org/abs/2605.27361v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Natural Language Query to Configuration for Retrieval Agents

## Abstract
Modern retrieval agents expose many configuration choices -- LLM, retriever, number of documents, number of hops, and synthesis strategy -- each shaping both answer quality and serving cost. Today, these pipelines are typically hand-tuned once per workload, leaving substantial per-query optimization untapped. We formulate the problem: given a natural-language query and either an accuracy or a budget target, select from a predefined pipeline catalog the configuration that minimizes cost or maximizes accuracy at inference time. We propose **BRANE**, which uses an LLM to convert each query into workload-specific characteristics, then trains a lightweight per-configuration predictor that estimates whether the pipeline will answer the query correctly. At inference time, **BRANE** selects the configuration that maximizes predicted correctness penalized by cost, exposing a tunable cost-quality tradeoff without retraining. Across MuSiQue, BrowseComp-Plus, and FinanceBench, **BRANE** consistently pushes the cost-quality Pareto frontier, matches the best fixed configuration's accuracy at up to 89% lower cost, and outperforms LLM-routing, rule-based, and fine-tuned Qwen3-4B baselines. These results show that per-query configuration of the full retrieval pipeline is a practical alternative to static workload-level tuning.

## Metadata
- **Published**: 2026-05-26T17:58:47Z
- **Authors**: Melissa Z. Pan, Negar Arabzadeh, Mathew Jacob, Fiodar Kazhamiaka, Esha Choukse, Matei Zaharia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.27361v1)