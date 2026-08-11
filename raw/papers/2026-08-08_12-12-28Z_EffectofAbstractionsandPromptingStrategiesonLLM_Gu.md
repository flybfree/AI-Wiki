---
title: Effect of Abstractions and Prompting Strategies on LLM-Guided High-Performance Optimizations
published: 2026-08-08T12:12:28Z
authors: Jiří Klepl, Maty'aš Brabec, Martin Kruliš
url: http://arxiv.org/abs/2608.08085v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Effect of Abstractions and Prompting Strategies on LLM-Guided High-Performance Optimizations

## Abstract
Code performance optimization is a vital aspect of modern software development, as it enables faster response times and reduced resource usage. These optimizations require a deep understanding of low-level hardware details and the intricacies of parallel processing, making them challenging even for experienced developers. With the advent of Large Language Models (LLMs), which are increasingly capable of generating and understanding code, there is growing interest in incorporating these models into automated code optimization processes. Traditionally, this automation involves transcribing the source code into a domain-specific representation that can be auto-tuned using grid search or machine learning algorithms, while adhering to strict rules and a limited set of feasible transformations to ensure verifiability. LLMs incorporate high-level code semantics and can thus perform transformations that go beyond verifiable automated optimizations. This paper investigates whether the traditional abstractions used in automated code optimization improve the performance and correctness of LLM-guided optimizations of parallel HPC applications. We evaluate this using the PolyBench benchmark suite and demonstrate that, in our evaluated setting, LLMs provided with specific optimization goals achieve better measured performance and validity rates when generating C code compared to creating computation pipelines and optimization schedules with established frameworks, suggesting that future development should explore alternative approaches for verifiable LLM-guided code optimization.

## Metadata
- **Published**: 2026-08-08T12:12:28Z
- **Authors**: Jiří Klepl, Maty'aš Brabec, Martin Kruliš
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08085v1)