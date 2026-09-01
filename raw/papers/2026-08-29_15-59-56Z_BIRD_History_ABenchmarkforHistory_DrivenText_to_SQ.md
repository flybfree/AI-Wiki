---
title: BIRD-History: A Benchmark for History-Driven Text-to-SQL with Fine-Grained Knowledge Annotations
published: 2026-08-29T15:59:56Z
authors: Yunfan Zhou, Qiming Shi, Yizhou Yang, Di Weng, Yingcai Wu
url: http://arxiv.org/abs/2608.29345v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BIRD-History: A Benchmark for History-Driven Text-to-SQL with Fine-Grained Knowledge Annotations

## Abstract
While recent Large Language Model (LLM)-based text-to-SQL systems achieve impressive performance on standard benchmarks, they struggle when user queries implicitly rely on domain-specific knowledge, such as business logic, data conventions, and analytical practices, that is neither captured by the schema nor explicitly stated in the natural language question. Historical SQL query logs offer a valuable source of such knowledge, yet existing benchmarks do not adequately support evaluation of history-driven approaches. To address this gap, we introduce BIRD-History, a benchmark consisting of 1,393 tasks across 11 databases, designed to evaluate text-to-SQL systems' ability to ground underspecified natural language questions using historical SQL scripts. Each task is annotated with ground-truth labels specifying which historical queries contain relevant knowledge and which SQL clauses encode it, enabling systematic evaluation of both retrieval effectiveness and knowledge utilization. Alongside the benchmark, we propose a plug-in retriever that extracts five types of external knowledge from historical SQL scripts, then retrieves and reranks relevant fragments for query generation. The retriever integrates seamlessly into existing few-shot text-to-SQL pipelines without requiring prompt modifications. Experiments demonstrate consistent improvements across four text-to-SQL systems, highlighting the value of leveraging historical query logs for handling underspecified queries. Dataset and code are open-sourced on https://github.com/zjuidg/BIRD-History.

## Metadata
- **Published**: 2026-08-29T15:59:56Z
- **Authors**: Yunfan Zhou, Qiming Shi, Yizhou Yang, Di Weng, Yingcai Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29345v1)