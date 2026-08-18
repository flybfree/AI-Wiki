---
title: LongDocBench: Benchmarking TOC Hierarchy and Contextual Relationship Recovery in Long Documents
published: 2026-08-15T06:25:26Z
authors: Yuefeng Zou, Yichen Lu, Jingxiao Yang, Bingtao Fu, Gaoyang Zhang, Xiongfei Bai, Tian Chen, Xiang Qi
url: http://arxiv.org/abs/2608.15064v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LongDocBench: Benchmarking TOC Hierarchy and Contextual Relationship Recovery in Long Documents

## Abstract
Parsing visual documents into machine-readable representations is fundamental to document intelligence. Existing benchmarks focus on page-level element recognition, reading order, formula recognition, and table structure. Long documents, however, also require document-level structure recovery. This includes reconstructing cross-page table-of-contents (TOC) hierarchies and identifying typed links from tables and figures to their captions, notes, and sources, often in one-to-many form. Because these structures are covered only partially or subsumed within broader parsing protocols, existing benchmarks cannot directly evaluate two key document-level tasks: \emph{Table-of-Contents Hierarchy Recovery} and \emph{Contextual Relationship Recovery}. To benchmark these two tasks, we introduce \textsc{LongDocBench}, comprising 85 real-world financial reports, textbooks, and academic papers spanning 2,582 pages, with up to 105 pages per document. It provides human-verified annotations for 3,937 heading nodes (mean node depth 3.55; maximum depth 9) and 3,258 contextual relationships annotated across 2,680 table and figure objects. We further evaluate both the downstream utility and recoverability of these structures. Long-document question-answering experiments show that human-verified TOC hierarchies and contextual relationships improve reasoning, with their combination providing complementary benefits. Meanwhile, representative document parsers remain limited on both recovery tasks despite strong page-level performance. To support further progress, we publicly release \textsc{LongDocBench} and its evaluation protocol and reproducible testbed for advancing document-level structure recovery in long documents.

## Metadata
- **Published**: 2026-08-15T06:25:26Z
- **Authors**: Yuefeng Zou, Yichen Lu, Jingxiao Yang, Bingtao Fu, Gaoyang Zhang, Xiongfei Bai, Tian Chen, Xiang Qi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15064v1)