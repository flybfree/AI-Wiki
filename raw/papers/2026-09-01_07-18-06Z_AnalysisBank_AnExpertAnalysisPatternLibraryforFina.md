---
title: AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation
published: 2026-09-01T07:18:06Z
authors: Yajing Yang, Yunshan Ma, Kelvin J. L. Koa, Min-Yen Kan
url: http://arxiv.org/abs/2609.00818v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation

## Abstract
We argue that financial report generation should operate at the analytical rather than structural level, composing content from data-derived insights rather than high-level topics or sections. To this end, we propose AnalysisBank, which distills expert reports into a reusable library of Analyses, each pairing a data signal, an analytical move, and the expert span it was derived from. At inference time, AnalysisBank matches input signals to library entries and applies the retrieved moves to compose the report. A study of Analyses distilled from 550 expert reports reveals a heavy-tailed distribution of 47-52 signal types spanning 13 move types. On two financial benchmarks across four LLM backbones, AnalysisBank increases the proportion of novel, data-grounded insights by 1.7-3.7x over structural-level baselines. Transfer to scientific writing suggests that the distinction generalizes beyond finance. Code and the distilled Analysis library are available at https://github.com/yajingyang/AnalysisBank.

## Metadata
- **Published**: 2026-09-01T07:18:06Z
- **Authors**: Yajing Yang, Yunshan Ma, Kelvin J. L. Koa, Min-Yen Kan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00818v1)