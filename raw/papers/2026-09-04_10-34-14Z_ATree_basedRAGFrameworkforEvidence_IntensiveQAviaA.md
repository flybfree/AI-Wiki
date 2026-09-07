---
title: A Tree-based RAG Framework for Evidence-Intensive QA via Adaptive Planning and Topology-Aware Evidence Gathering
published: 2026-09-04T10:34:14Z
authors: Songeun Lee, Kyungjin Min, Injae Na, Suyeong Lee, Chiyoung Kim, Woohwan Jung
url: http://arxiv.org/abs/2609.04981v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Tree-based RAG Framework for Evidence-Intensive QA via Adaptive Planning and Topology-Aware Evidence Gathering

## Abstract
Recent structured RAG methods leverage tree- or graph-based reasoning structures to improve multi-hop QA. However, they face key limitations in evidence-intensive QA, where answering a question requires synthesizing information scattered across dozens or even hundreds of documents: structural rigidity, which limits adaptive reasoning expansion, and topology-ignorant evidence gathering, which prevents effective integration of evidence across different reasoning nodes. To address these issues, we propose APT-RAG, an Adaptive Planning and Topology-aware evidence gathering RAG framework. Adaptive planning dynamically expands the reasoning structure based on question dependencies and evidence requirements, while topology-aware evidence gathering improves evidence coverage through sibling evidence reuse, direct retrieval, and evidence aggregation from child nodes. We further introduce evidence-guided batched answer generation to reduce significant generation overhead in evidence-intensive QA. In the experiments on evidence-intensive QA benchmarks, APT-RAG outperforms existing structured RAG methods. Our code is available at https://github.com/hyudsl/APT-RAG.

## Metadata
- **Published**: 2026-09-04T10:34:14Z
- **Authors**: Songeun Lee, Kyungjin Min, Injae Na, Suyeong Lee, Chiyoung Kim, Woohwan Jung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04981v1)