---
title: PremiseCheck: Efficient Fact-Checking of Human and AI Peer Reviews
published: 2026-10-15T00:42:49Z
authors: Dingjie Song, Zhiling Yan, Ziqian Zhang, Yuxuan Zhang, Lichao Sun
url: http://arxiv.org/abs/2610.21046v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PremiseCheck: Efficient Fact-Checking of Human and AI Peer Reviews

## Abstract
Peer review is under strain from the growth of submissions, and review comments written by humans or AI can misstate what a paper says. We introduce ReviewFact, a benchmark that labels such factual errors in review comments under one definition across NLP, machine learning, and the natural sciences, and that measures cost and latency alongside accuracy. A frontier LLM checks comments well but must read the whole paper for each check, while cheap decision models, which score whether a statement holds in a text, fall far short on whole comments that mix several implicit assertions. PremiseCheck is a framework that combines the two. An LLM rewrites each comment as explicit premises without reading the paper, and a decision model checks each premise against the paper. When each comment is checked on its own, PremiseCheck reaches accuracy comparable to GPT-5.5 across all three fields at about half its cost, and on NLP reviews at a quarter of its cost and less than half its latency.

## Metadata
- **Published**: 2026-10-15T00:42:49Z
- **Authors**: Dingjie Song, Zhiling Yan, Ziqian Zhang, Yuxuan Zhang, Lichao Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21046v1)