---
title: Evidence-Aligned Entity Verification for Hallucination Detection in Retrieval-Augmented Generation
published: 2026-09-08T05:22:29Z
authors: Runsong Jia, Zhen Fang, Mengjia Wu, Jie Lu, Yi Zhang
url: http://arxiv.org/abs/2609.08267v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evidence-Aligned Entity Verification for Hallucination Detection in Retrieval-Augmented Generation

## Abstract
Hallucination detection is crucial for large language models (LLMs), as hallucinated content creates significant barriers in applications requiring factual accuracy. Current detection methods mainly depend on internal signals like uncertainty and self-consistency checks, using the model's pre-trained knowledge to identify unreliable outputs. However, pre-trained knowledge may become outdated and has coverage limitations, especially for specialized or recent information. To address these limitations, retrieval-augmented generation (RAG) has emerged as a promising solution by retrieving relevant evidence at inference time, grounding outputs beyond the model's parametric knowledge. In this paper, we target a critical and practical learning problem RAG-based hallucination detection (RHD), where RAG is employed to enhance hallucination detection by addressing information updating challenges. To address RHD, we propose a novel method Evidence-Aligned Entity Verification (EAEV), which detects entity-level hallucinations by leveraging RAG to align generated entities with retrieved evidence contexts. Specifically, EAEV evaluates entity-evidence alignment through three complementary dimensions and introduces counterfactual stability analysis to ensure robust alignments under evidence perturbations. Experiments across multiple RAG benchmarks demonstrate that EAEV achieves consistent improvements over existing methods with strong generalization capabilities.

## Metadata
- **Published**: 2026-09-08T05:22:29Z
- **Authors**: Runsong Jia, Zhen Fang, Mengjia Wu, Jie Lu, Yi Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08267v1)