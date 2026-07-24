---
title: Search-on-Graph-R1: Training Large Language Models to Search Knowledge Graphs with Reinforcement Learning
url: http://arxiv.org/abs/2607.18481v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_19-58-32Z_Search_on_Graph_R1_TrainingLargeLanguageModelstoSe.md
generated_at: 2026-07-23 23:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Search-on-Graph-R1 (Sogrone{}) which trains an 8B language model to answer knowledge graph questions by integrating a live search tool directly into the model’s reasoning process. It achieves state-of-the-art performance on WebQSP, CWQ, and GrailQA without auxiliary modules or LLM judges during training.

## Key Takeaways
- Sogrone{} embeds navigation of the KG directly within an 8B model via supervised fine-tuning with gold SPARQL queries and reinforcement learning that minimizes search calls.
- The method eliminates reliance on external inference tools at inference time, using only the model’s own capacity to produce SPARQL queries.
- Training stages are separable: SFT provides a baseline path while RL refines it to reach answers faster.

## Context
Knowledge graph question answering remains challenging because models must discover answer paths without explicit supervision. Recent frontier LLM approaches require costly retrieval tools and large inference budgets, limiting practical deployment.

## Implications
This work demonstrates that compact, self‑contained models can outperform larger frozen systems on KGQA tasks, reducing operational costs for enterprise applications that need real‑time graph reasoning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18481v1)
