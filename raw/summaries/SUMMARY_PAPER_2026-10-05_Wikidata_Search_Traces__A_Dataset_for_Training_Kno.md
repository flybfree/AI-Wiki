---
title: Wikidata Search Traces: A Dataset for Training Knowledge Graph Search Agents
url: http://arxiv.org/abs/2610.06650v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-05_16-29-22Z_WikidataSearchTraces_ADatasetforTrainingKnowledgeG.md
generated_at: 2026-10-05 22:58
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a dataset of 10,235 solving traces designed to train agents that answer complex questions over Wikidata by actively exploring the knowledge graph rather than relying on memorized facts. The authors construct multi-hop questions on a frozen Wikidata snapshot by replacing named entities with nested conditions, ensuring each expansion preserves a unique target and that every added condition is necessary. They also release a recursive language model (RLM) harness that batches graph calls, stores results in persistent Python state, and interprets selected evidence through sub-calls, demonstrating that this structured environment substantially improves both commercial and open-weight model performance on graph search tasks.

## Key Takeaways
- The difficulty of graph search can be systematically controlled through the structural design of questions—specifically by nesting conditions and replacing named entities—rather than relying solely on obscure entities or adversarial wording. This means researchers can generate questions at precise difficulty levels, enabling more rigorous and reproducible evaluation of graph-search agents.
- A significant portion of failure in long-horizon graph search stems not from the language model's reasoning capability but from how retrieved evidence is managed within the model's context window. The RLM harness addresses this by batching graph calls, keeping results in persistent Python state, and delegating interpretation of selected evidence to sub-calls, which prevents large graph results from overwhelming the model's context.
- In a well-designed environment with proper evidence management, open-weight models can match commercial closed models. Specifically, Qwen3.8-27B served on a single GPU improved from 60 to 74 correct answers out of 100 questions, while gpt-6-luna rose from 49 to 61 correct answers with its multi-hop accuracy doubling, showing that architectural scaffolding can close the gap between open and proprietary models.

## Context
This work sits at the intersection of knowledge graph reasoning, agentic AI, and retrieval-augmented generation. As language models increasingly serve as interfaces to structured knowledge bases, the community has struggled with the absence of training data that records how a solver navigates a graph step by step, as well as with interfaces that dump large graph query results directly into a model's context, causing degradation on multi-hop tasks. By providing both a curated dataset of solving traces and a reusable harness, the paper addresses two foundational gaps that have limited progress in training and evaluating graph-search agents.

## Implications
For practitioners building question-answering systems over knowledge graphs, the RLM harness offers a practical blueprint for managing retrieved evidence without inflating context windows, which could reduce costs and improve reliability in production deployments. For the broader AI research community, the dataset and methodology provide a reproducible benchmark for training agents to explore structured data, potentially accelerating progress toward reliable multi-hop reasoning without dependence on proprietary model access. The finding that open-weight models can match commercial ones under proper scaffolding also has implications for democratizing access to high-quality graph-search capabilities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.06650v1)
