---
title: GUIDE: Generative Unsupervised Chinese Query Correction via Phonetic and Visual Shared-ID Encoding
published: 2026-08-26T03:54:26Z
authors: Lei Yang, Binbin Huang, Jiwei Tan, Xuhui Sui, Chang Tu, Yi Wang, Han Li
url: http://arxiv.org/abs/2608.25343v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GUIDE: Generative Unsupervised Chinese Query Correction via Phonetic and Visual Shared-ID Encoding

## Abstract
Chinese query correction (CQC) is important for search and query recommendation on content platforms, but supervised methods rely on large annotated correction pairs that are costly to maintain as query vocabularies evolve. Unsupervised correction with language models is attractive, yet in the short-query setting, unconstrained generation often over-corrects ambiguous inputs toward high-frequency phrases, causing intent drift. We propose \textsc{GUIDE}, a generative unsupervised framework for CQC based on a confuse-then-clarify paradigm. \textsc{GUIDE} encodes phonetically or visually confusable characters with shared-IDs and reconstructs the original query with an encoder--decoder architecture, which constrains correction to plausible confusion neighborhoods while learning from unlabeled query streams. A time-decayed, query-frequency-weighted objective further supports adaptation to rapidly changing query vocabularies. Experiments on \textit{QSpell 250K} and a large-scale real-world dataset (\textit{KwaiSearch}) show that \textsc{GUIDE} consistently outperforms strong baselines, while online A/B testing further confirms gains in correction quality and downstream engagement.

## Metadata
- **Published**: 2026-08-26T03:54:26Z
- **Authors**: Lei Yang, Binbin Huang, Jiwei Tan, Xuhui Sui, Chang Tu, Yi Wang, Han Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25343v1)