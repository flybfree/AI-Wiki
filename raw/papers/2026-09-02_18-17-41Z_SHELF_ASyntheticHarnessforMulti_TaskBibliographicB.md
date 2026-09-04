---
title: SHELF: A Synthetic Harness for Multi-Task Bibliographic Benchmarking
published: 2026-09-02T18:17:41Z
authors: Michael J. Bommarito
url: http://arxiv.org/abs/2609.03047v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SHELF: A Synthetic Harness for Multi-Task Bibliographic Benchmarking

## Abstract
Libraries and archives manage large collections with limited staff and computing budgets, yet common benchmarks do not systematically test their bibliographic work. They need to know which methods work for their tasks and what those methods require to run. SHELF, the Synthetic Harness for Evaluating LLM Fitness, addresses this gap. It is a Python system that turns labelled taxonomies, writing specifications, and a generation budget into controlled benchmark data and evaluation tasks. This first release contains 62,899 model-written documents based on Library of Congress vocabularies, with tasks for classification, clustering, retrieval, pair classification, and instruction retrieval. We compare TF, TF-IDF, BM25, popular encoders, and, on subject classification only, zero-shot decoders; each method appears only on tasks that support it. Subject classification reaches 0.8887, while genre-form classification reaches only 0.2605, and several pair and clustering tasks remain near chance. Sparse methods remain competitive on classification, while TF-IDF is the fastest measured arm in the subject timing experiment. SHELF also varies bibliographic facets independently and can generate new, verifiably unseen documents after a model's training cutoff. Comparisons with LCSHBench and Project Gutenberg show that model rankings transfer more reliably than absolute scores, but SHELF scores do not estimate accuracy on production catalogue data. We release all source code and data under permissive licenses on GitHub and Hugging Face.

## Metadata
- **Published**: 2026-09-02T18:17:41Z
- **Authors**: Michael J. Bommarito
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03047v1)