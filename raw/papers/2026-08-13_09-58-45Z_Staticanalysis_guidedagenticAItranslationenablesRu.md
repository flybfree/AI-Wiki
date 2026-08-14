---
title: Static analysis-guided agentic AI translation enables Rust as a full stack bioinformatics language
published: 2026-08-13T09:58:45Z
authors: Johan Henriksson
url: http://arxiv.org/abs/2608.13029v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Static analysis-guided agentic AI translation enables Rust as a full stack bioinformatics language

## Abstract
The field of bioinformatics struggles with legacy code - old code that is commonly used but may no longer have a maintainer, or may be written in an now-unfamiliar language (e.g. Perl, Fortran). This incurs maintenance cost (technical debt), but dynamically typed languages also negatively impacts the environment and fail to make use of modern hardware. Legacy code may also have security or safety problems that make it unsuited for use in clinical settings. Here we show that agentic AI, combined with static analysis, can be used to translate legacy code to the modern language Rust. We provide prompts and supporting software to aid systematic translation, and evaluate it on common software for NGS and imaging. We showcase the result on our software Bascet: Size was reduced by ~80x, build time decreased by ~10x, and performance of key steps improved >3x. Unix dependencies were also removed, making Bascet the only single-cell pipeline able to run on native Windows, without a container. Large-scale refactoring of bioinformatics software is thus now possible at a limited budget, enabling more complex tools to be developed.

## Metadata
- **Published**: 2026-08-13T09:58:45Z
- **Authors**: Johan Henriksson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13029v1)