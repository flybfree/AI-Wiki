---
title: Context Compaction Theory
published: 2026-08-02T15:45:54Z
authors: Hayder Tirmazi, Sam Markelon, Allison Bishop, Michael Mitzenmacher
url: http://arxiv.org/abs/2608.01326v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Context Compaction Theory

## Abstract
Large Language Models (LLMs) have a bounded context window. The context window is the maximum input size an LLM can consume for a single inference. AI agents rely on a process called context compaction to fit their state within the context window when calling an LLM. Despite its ubiquity, context compaction has received essentially no formal analysis. In this paper, we initiate a formal study of context compaction. We first introduce a framework consisting of two games that capture the two algorithmic strategies for context compaction used by contemporary AI agents in practice. The Context Selection Game models context compaction algorithms that select a subset of an agent's accumulated state to retain. The Context Generation Game models context compaction algorithms that summarize an agent's state by an arbitrary message of bounded length. We then prove an equivalence between the Context Generation Game and one-way communication complexity. The minimum context compaction budget for answering a set of queries within a target error is equal to the one-way communication complexity of the induced communication problem at the same error. Known bounds from communication complexity therefore transfer directly to context compaction. We also show that the Context Selection Game corresponds to a restricted class of one-way communication protocols. Any gap between selection and generation is therefore a gap between two classes of communication protocols. We prove that there exists a set of queries for which generation needs strictly less budget than selection. The equivalence between the Context Generation Game and one-way communication also lets us measure how well a deployed context compaction algorithm performs on a query relative to the optimal strategy. As an example, we present a case study that evaluates Anthropic's context compaction endpoint on set membership queries.

## Metadata
- **Published**: 2026-08-02T15:45:54Z
- **Authors**: Hayder Tirmazi, Sam Markelon, Allison Bishop, Michael Mitzenmacher
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01326v1)