---
title: Benchmarking Resource-Efficient LLMs for Research Topic Ontology Generation in the Biomedical Field
published: 2026-07-20T12:48:41Z
authors: Tanay Aggarwal, Angelo Salatino, Francesco Osborne, Enrico Motta
url: http://arxiv.org/abs/2607.17902v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benchmarking Resource-Efficient LLMs for Research Topic Ontology Generation in the Biomedical Field

## Abstract
Knowledge Organization Systems like Ontologies and taxonomies are fundamental for structuring scientific knowledge, yet their manual curation presents a persistent bottleneck in knowledge management. While Large Language Models (LLMs) offer a scalable mechanism for automated ontology generation, their capacity to classify complex, domain-specific semantics requires systematic evaluation. In this paper, we assess the performance of five small, open-source LLMs (up to 9 billion parameters) in identifying semantic relationships between biomedical concepts. To support this evaluation, we introduce MeSH-Rel-4K, a dataset comprising 4K semantic relationships extracted from the Medical Subject Headings (MeSH). We analyse three adaptation strategies: standard prompting, Chain-of-Thought prompting, and fine-tuning. While parameter-constrained models traditionally struggle with the nuances of in-context logic, our results reveal that targeted fine-tuning increases the average F1-score by 34.1 percentage points. These results confirm that direct fine-tuning effectively exceeds the reasoning bottlenecks of smaller LLMs, providing an accurate, automated methodology for the construction and evolution of specialised biomedical ontologies.

## Metadata
- **Published**: 2026-07-20T12:48:41Z
- **Authors**: Tanay Aggarwal, Angelo Salatino, Francesco Osborne, Enrico Motta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17902v1)