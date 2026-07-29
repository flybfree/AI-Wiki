---
title: Detecting Knowledge Inconsistencies Across Text, Tables, and Knowledge Graphs
published: 2026-07-28T16:43:56Z
authors: Fanfu Wei, Thibault Ehrhart, Raphaël Troncy
url: http://arxiv.org/abs/2607.25959v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Detecting Knowledge Inconsistencies Across Text, Tables, and Knowledge Graphs

## Abstract
Wikipedia and Wikidata are widely used for information access, LLM pre-training, and retrieval-augmented generation. Their knowledge is deeply connected but scattered across text, tables, and knowledge graphs. This raises a practical question: when these modalities disagree, how can we detect and explain the conflict? We study this problem as \emph{modality-level inconsistency detection}. We first introduce a taxonomy of cross-modal knowledge inconsistencies, covering information granularity differences, direct conflicts, temporal changes, and KG incompleteness. We then present \textsc{Kontrast}, an automatic framework that uses Text-to-SPARQL and LLM reasoning to compare table-based answers with KG evidence and categorize the resulting inconsistencies. Experiments on various Table-QA datasets show that cross-modal inconsistencies are common and informative. They reveal not only true knowledge conflicts, but also missing KG structure and temporal mismatches while being limited by Text-to-SPARQL errors and noise. Our analysis shows that text, tables, and KGs can complement and correct one another through systematic comparison. \textsc{Kontrast} provides a practical tool for large-scale knowledge auditing and establishes a benchmark for future work on cross-modal knowledge consistency. Code and data are available at https://github.com/ECLADATTA/KONTRAST.

## Metadata
- **Published**: 2026-07-28T16:43:56Z
- **Authors**: Fanfu Wei, Thibault Ehrhart, Raphaël Troncy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25959v1)