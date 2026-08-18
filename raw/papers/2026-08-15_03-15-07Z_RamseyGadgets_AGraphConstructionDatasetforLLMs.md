---
title: RamseyGadgets: A Graph Construction Dataset for LLMs
published: 2026-08-15T03:15:07Z
authors: Zohair Raza Hassan, Deepak Pandita
url: http://arxiv.org/abs/2608.14999v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RamseyGadgets: A Graph Construction Dataset for LLMs

## Abstract
Constructing special graphs is an important task within graph theory and computer science. Many popular graph constructions are the result of a comprehensive exploration of relevant graphs and human ingenuity. Given the rise of generative AI usage in mathematics, it is natural to test whether LLMs are able to construct graphs with specified properties using their reasoning capabilities. Unfortunately, many natural graph construction problems, such as finding extremal Ramsey-good graphs (i.e., avoiding specific monochromatic subgraphs), have been explored extensively in the literature, making it difficult to ascertain whether a construction is the product of an LLM's reasoning capabilities or its recollection from training data. In this work, we introduce \textbf{RamseyGadgets}, a novel dataset of 70 underexplored graph construction problems that require finding Ramsey-good graphs with special properties (e.g., containing an edge with a fixed color). These problems have reasonably sized solutions (at most 10 vertices) that can be verified by SAT solvers, making them suitable for automatic evaluation. Our dataset is easily expandable, as one can simply change the monochromatic subgraphs being avoided to obtain a new set of problems. We evaluate the performance of five open-source LLMs on our dataset and report the results. Our findings show that LLMs achieve only 37.70% accuracy on the hard-tier problems in our dataset, with Gemma-4-31B achieving the highest performance out of the five. We also showcase how our dataset allows us to ascertain what kind of hints help LLMs perform better at this task.

## Metadata
- **Published**: 2026-08-15T03:15:07Z
- **Authors**: Zohair Raza Hassan, Deepak Pandita
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14999v1)