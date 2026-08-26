---
title: PARTAB: Partition-Aware Reasoning with Structured Evidence for Scalable Table Understanding
published: 2026-08-25T05:26:23Z
authors: Md Mahadi Hasan Nahid, Davood Rafiei
url: http://arxiv.org/abs/2608.24082v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PARTAB: Partition-Aware Reasoning with Structured Evidence for Scalable Table Understanding

## Abstract
Large Language Models (LLMs) have shown strong capabilities in table reasoning, but their effectiveness degrades as tables grow in size and complexity due to irrelevant context and difficulty localizing the evidence required for reasoning. Existing approaches typically reason over either the full table or a single reduced view, which can still obscure important row-column relationships. We introducePARTAB (Partition-Aware Reasoning overTables), a framework that constructs a structured evidence interface between the LLM and the table. PARTAB represents query-relevant evidence as semantically coherent, row-linked table regions and performs hierarchical selection over column groups and row-level partitions before composing the selected evidence for answer generation. We evaluate PARTAB on multiple table reasoning benchmarks, covering question answering, fact verification, and numerical reasoning. PARTAB consistently improves over full-table prompting and several recent table reasoning methods, achieving strong performance on WikiTableQuestions and TabFact while remaining competitive on numerical reasoning. Additional analyses show that semantic partitioning and targeted evidence selection improve evidence localization, substantially reduce the reasoning context, and provide larger benefits on complex tables. These results demonstrate the value of structured, partition aware evidence construction for scalable table reasoning.

## Metadata
- **Published**: 2026-08-25T05:26:23Z
- **Authors**: Md Mahadi Hasan Nahid, Davood Rafiei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24082v1)