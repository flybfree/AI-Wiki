---
title: LLMBDC: Language Model for Biological Domains Oriented Clustering of Gene Ontology
published: 2026-07-30T19:29:22Z
authors: Ximing Ran, Jie Xu, Peng Jin, Zhaohui Qin, Zhexing Wen, Jiaying Lu
url: http://arxiv.org/abs/2608.00099v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLMBDC: Language Model for Biological Domains Oriented Clustering of Gene Ontology

## Abstract
Gene Ontology (GO) enrichment analysis is a foundational tool for translating large-scale genomic data into biological insights, but typically yields hundreds of redundant terms that obscure overarching themes. Existing summarization tools rely on fixed similarity metrics (REVIGO, GOSemSim, clusterProfiler::simplify()), gene-overlap measures (Metascape), or static hierarchy mappings (GO-slim), and therefore cannot incorporate biological context. Manual curation provides context-aware grouping but is subjective and labor-intensive. A scalable, context-aware framework is needed to cluster GO terms into interpretable higher-order biological domains. Here we present LLMBDC (Large Language Model for Biological Domains Oriented Clustering of Gene Ontology), a training-free framework that leverages zero-shot semantic reasoning of LLMs with confidence scoring to cluster GO terms into BioDomains using only ontology information at inference time. Benchmarked across Alzheimer's disease (AD) and Fragile X syndrome (FXS) against six baseline methods including SapBERT, LLMBDC achieved substantially higher precision, recall, and clustering performance. Against ground-truth annotations, LLMBDC improved ARI from 9.7% to 73.3% (AD) and from 15.7% to 66.6% (FXS) over REVIGO, with corresponding NMI gains from 59.9% to 73.4% (AD) and 66.0% to 79.5% (FXS). A Cauchy combination test further confirmed that aggregated BioDomains retained statistically significant functional signals. LLMBDC provides a scalable, reproducible, and interpretable route to context-aware, system-level interpretation of GO enrichment results while preserving biological specificity.

## Metadata
- **Published**: 2026-07-30T19:29:22Z
- **Authors**: Ximing Ran, Jie Xu, Peng Jin, Zhaohui Qin, Zhexing Wen, Jiaying Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00099v1)