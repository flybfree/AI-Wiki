---
title: Can LLMs Normalize Databases? A Benchmark and Multi-Agent Framework for Schema Normalization
published: 2026-09-10T06:34:35Z
authors: Dong-Jae Koh, Huisu Kim, SeongHwan Yoon, Lasse M. Jantsch, Chun-Hee Lee, Seonghyeon Lee, Young-Kyoon Suh
url: http://arxiv.org/abs/2609.11141v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can LLMs Normalize Databases? A Benchmark and Multi-Agent Framework for Schema Normalization

## Abstract
Large Language Models (LLMs) are increasingly used to generate structured outputs, but their reliability remains unclear when those outputs must satisfy database-level constraints. We study this issue through database normalization, involving reasoning about functional dependencies, lossless join decompositions, and inter-table constraints. We introduce a Database Normalization Benchmark (DNBENCH), comprising 3,275 samples for evaluating LLM-driven database normalization from 1NF to BCNF. DNBENCH uses a three-axis protocol to measure semantic equivalence, structural accuracy, and logical validity. Across Single, Complex, and Real World levels, DNBENCH uncovers recurring failures in dependency inference, schema decomposition, and inter-table constraint reconstruction. We further propose Multi-Agent Reasoning for Schemas (MARS), which separates evidence extraction, violation diagnosis, and decomposition planning from schema generation and verification. MARS improves the DNB-SCORE by 82.0% over the single-prompt baseline. All artifacts will be released upon acceptance.

## Metadata
- **Published**: 2026-09-10T06:34:35Z
- **Authors**: Dong-Jae Koh, Huisu Kim, SeongHwan Yoon, Lasse M. Jantsch, Chun-Hee Lee, Seonghyeon Lee, Young-Kyoon Suh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.11141v1)