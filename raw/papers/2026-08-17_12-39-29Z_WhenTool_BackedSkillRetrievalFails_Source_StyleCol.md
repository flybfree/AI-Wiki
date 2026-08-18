---
title: When Tool-Backed Skill Retrieval Fails: Source-Style Collapse in Executable Capability Retrieval
published: 2026-08-17T12:39:29Z
authors: Yiqi Liu, Joseph James, Yang Wang, Chenghao Xiao, Chenghua Lin
url: http://arxiv.org/abs/2608.16502v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Tool-Backed Skill Retrieval Fails: Source-Style Collapse in Executable Capability Retrieval

## Abstract
Large-scale agents increasingly rely on retrieval to access external capabilities. We study this retrieval gate in structured tools and APIs, a measurable class of tool-backed executable skills that must be surfaced before an agent can plan, incorporate, or act. In this setting the retrieval layer can silently fail even when the capability corpus is fixed: on ToolRet, a retriever fine-tuned on one source-specific slice collapses on another source-specific slice of the same benchmark, with FT-1100 despite its higher lexical overlap with the gold tools. We call this failure mode source-style collapse. Query-side TF-IDF fingerprints flag source styles on which the fine-tuned retriever is likely to fail better than semantic or length-based proxies, giving a cheap signal for mismatch over a fixed tool corpus. We propose ToolScout, a source-aware routing method that uses this signal as a routing guard: on the mixed 4,996-query stream, TF-IDF-based routing raises coverage from 22.3% to 86.1%, and across five collapsed sources 20 matched examples raise the coverage-weighted global top-1 proxy from 1.3% to 53.9%. The same failure and routing behaviors persist when tools are rerendered as executable skill cards, which rules out raw API-schema format as the sole cause.

## Metadata
- **Published**: 2026-08-17T12:39:29Z
- **Authors**: Yiqi Liu, Joseph James, Yang Wang, Chenghao Xiao, Chenghua Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16502v1)