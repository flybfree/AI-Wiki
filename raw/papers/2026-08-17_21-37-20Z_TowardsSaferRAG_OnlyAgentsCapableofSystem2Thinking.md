---
title: Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents
published: 2026-08-17T21:37:20Z
authors: Mehrdad Ghassabi
url: http://arxiv.org/abs/2608.17153v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents

## Abstract
Retrieval-Augmented Generation (RAG) has significantly enhanced the performance of large language models (LLMs), yet these systems remain vulnerable to knowledge-poisoning attacks, in which misinformation in retrieved documents can influence the model's final outputs. Notably, an LLM may correctly detect that a document contains incorrect information while nevertheless being influenced by it. Prior work has addressed this vulnerability through the Cordon Principle, which prevents models responsible for final answer synthesis from directly accessing raw evidence. Although effective, this strict isolation can introduce substantial computational overhead. In this work, we propose a refined security principle: only agents capable of deliberative System 2 reasoning may access untrusted documents. To evaluate this principle, we introduce novel metrics that quantify the discrepancy between misinformation detection and downstream influence. We then empirically compare state-of-the-art reasoning language models with standard language models across these metrics. Our results show that reasoning-capable models are substantially more robust to corrupted evidence, without requiring the strict isolation imposed by the Cordon Principle. These findings provide empirical support for our refined principle and suggest a more practical foundation for secure RAG system design.

## Metadata
- **Published**: 2026-08-17T21:37:20Z
- **Authors**: Mehrdad Ghassabi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17153v1)