---
title: GRACE: Graph-Grounded Reflective Agent Copilot Engine for Expert-in-the-Loop Knowledge Expansion
published: 2026-09-03T20:03:20Z
authors: John Seon Keun Yi, Joshua R. Minot, Dokyun Lee
url: http://arxiv.org/abs/2609.04442v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GRACE: Graph-Grounded Reflective Agent Copilot Engine for Expert-in-the-Loop Knowledge Expansion

## Abstract
Large language models deployed in high-stakes settings frequently generate plausible but ungrounded claims. Standard retrieval-augmented generation (RAG) pipelines offer limited remedy, since they retrieve isolated passages without tracking cross-document evidence relationships or quantifying uncertainty. We introduce GRACE (Graph-grounded Reflective Agent Copilot Engine), a framework that deconstructs LLM responses into atomic claims and grounds them against trusted knowledge priors within a weighted bipartite graph. Edge weights encode the closeness of each claim to the priors, enabling weighted centrality analysis that classifies claims as Grounded, Refuted, or Boundary. Such classification identifies not just hallucinations but also novel or contested claims at the frontier of the model's knowledge. To efficiently allocate human or agent resources, we formulate a Return on Attention (RoA) objective that defers a claim to expert review only when its priority-weighted uncertainty exceeds the cost of verification. Claims verified by experts are promoted to new evidence anchors, closing a validator-LLM evolutionary loop that expands the knowledge base across iterations. We evaluate GRACE across multiple language models and on datasets spanning both general and domain-specific knowledge. Our results show that our knowledge base serves as a reliable foundation for retrieval that outperforms RAG baselines, and that the RoA framework efficiently selects valuable boundary knowledge for expert verification. These findings demonstrate that graph-structured representations combined with expert-in-the-loop verification can mitigate hallucination at the system level rather than at the generation level. Code available at https://github.com/johnsk95/grace_code

## Metadata
- **Published**: 2026-09-03T20:03:20Z
- **Authors**: John Seon Keun Yi, Joshua R. Minot, Dokyun Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04442v1)