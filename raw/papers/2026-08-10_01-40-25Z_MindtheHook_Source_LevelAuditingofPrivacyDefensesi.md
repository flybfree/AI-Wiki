---
title: Mind the Hook: Source-Level Auditing of Privacy Defenses in Retrieval-Augmented Generation
published: 2026-08-10T01:40:25Z
authors: Yanhang Li, Zhichao Fan, Zexin Zhuang
url: http://arxiv.org/abs/2608.09001v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mind the Hook: Source-Level Auditing of Privacy Defenses in Retrieval-Augmented Generation

## Abstract
Black-box privacy scores for retrieval-augmented generation (RAG) are difficult to interpret unless the audited defense's active pipeline hook is known. We propose an active-path audit: inventory source-level hooks over retrieval, retrieved content, and generation; map each metric to the leakage channel it observes; and validate generated-text effects with exact-match canaries. In our benchmark reimplementations, the DP-style defenses modify retrieval scores only: their generation hooks are TODO-flagged stubs that return responses unchanged. This active path explains why they affect membership-inference behavior but track No-Defense on generated-text named-entity leakage, measured by NEL_strict. By contrast, the end-to-end LPRAG path is canary-validated on the email channel, recovering 53/150 canaries under No-Defense and 0/150 under LPRAG. These findings concern our reimplementations on our stack, not released defenses or defense families; the contribution is a methodology and case study, not a universal ranking

## Metadata
- **Published**: 2026-08-10T01:40:25Z
- **Authors**: Yanhang Li, Zhichao Fan, Zexin Zhuang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09001v1)