---
title: AquiLLM: Evaluating Faithfulness in Open-Weight RAG-LLM Systems for Scientific Research
published: 2026-09-15T02:09:45Z
authors: Bernie Boscoe, Srinath Saikrishnan, Vikram Seenivasan, Jack Stark, Andrew Lizarraga, Morgan Himes, Jonathan Soriano, PJ Allen, Tuan Do
url: http://arxiv.org/abs/2609.16519v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AquiLLM: Evaluating Faithfulness in Open-Weight RAG-LLM Systems for Scientific Research

## Abstract
Scientific research increasingly relies on large, heterogeneous data sources, motivating interest in retrieval-augmented generation (RAG) systems that provide natural language access to scientific knowledge and research workflows. Researchers are exploring the viability of these systems as natural language interfaces for document search and for generating analysis code and pipeline components. At the same time, concerns about data privacy and control over research infrastructure have motivated interest in open-weight models and open-source deployments hosted within research institutions.   In astronomy, this development follows a long history of computational infrastructure development, from archival databases and SQL-based systems to LLM-assisted research tools. This paper presents a domain-expert evaluation of faithfulness for AquiLLM, an open-weight, offline RAG-LLM platform designed to support scientific research groups in the use and preservation of tacit and formal knowledge.   We define faithfulness as the extent to which generated responses remain grounded in retrieved scientific context without unsupported claims or omissions. We report results from an astronomy case study evaluating AquiLLM across retrieval and scientific analysis tasks. AquiLLM performs most reliably on explicit retrieval-oriented questions grounded in the RAG collection, while faithfulness degrades for queries requiring synthesis or ambiguity resolution. These results highlight both the promise and limitations of open-weight RAG-LLM systems for scientific research and demonstrate the importance of domain-expert evaluation beyond standard benchmark leaderboards.

## Metadata
- **Published**: 2026-09-15T02:09:45Z
- **Authors**: Bernie Boscoe, Srinath Saikrishnan, Vikram Seenivasan, Jack Stark, Andrew Lizarraga, Morgan Himes, Jonathan Soriano, PJ Allen, Tuan Do
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16519v1)