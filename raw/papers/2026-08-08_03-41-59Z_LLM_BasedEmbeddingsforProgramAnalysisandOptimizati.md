---
title: LLM-Based Embeddings for Program Analysis and Optimization
published: 2026-08-08T03:41:59Z
authors: Calvin Higgins, Marco Alvarez
url: http://arxiv.org/abs/2608.07894v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM-Based Embeddings for Program Analysis and Optimization

## Abstract
Recent advances have highlighted the potential of machine learning, particularly Large Language Models (LLMs), for analyzing and optimizing programs. We present the first application of program embeddings from LLMCompiler---an LLM massively pretrained on intermediate representation (IR) code---to representative program analysis and optimization tasks. We generate program embeddings directly from source and IR code using a simple approach: split programs into chunks, independently embed each chunk with pretrained LLMs, and then aggregate the chunk embeddings into a single program embedding. Our experiments show that combining source and IR code embeddings achieves an error rate of 1.54\% in algorithm classification, a 12\% improvement over the current state-of-the-art, and a competitive accuracy on heterogeneous device mapping. These findings suggest that training a performance-aware LLM for embedding IR code might yield state-of-the-art results in code optimization tasks.

## Metadata
- **Published**: 2026-08-08T03:41:59Z
- **Authors**: Calvin Higgins, Marco Alvarez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07894v1)