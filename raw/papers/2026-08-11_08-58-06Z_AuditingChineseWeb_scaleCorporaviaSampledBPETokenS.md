---
title: Auditing Chinese Web-scale Corpora via Sampled BPE Token Statistics
published: 2026-08-11T08:58:06Z
authors: Qingjie Zhang, Ziqi Tang, Jie Zhang, Gelei Deng, Jinfeng Li, YueFeng Chen, Yitong Yang, Hui Xue, Tianwei Zhang, Han Qiu
url: http://arxiv.org/abs/2608.10678v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auditing Chinese Web-scale Corpora via Sampled BPE Token Statistics

## Abstract
Chinese web pollution has surfaced in LLMs, motivating audits of upstream Chinese corpora. However, auditing such corpora faces three challenges: (1) their web-scale size makes full scan costly; (2) prior analyses are often too coarse to expose token-level pollution; (3) Chinese web pollution is implicit and rapidly changing. We propose Sampled-BPE, a lightweight token-level auditing pipeline that sample a small subset and train BPE tokenizer to surface polluted tokens. Experiments show that Sampled-BPE preserves usable estimates while substantially reducing runtime and memory: a 148.4 $\times$ speedup and a 35.8 $\times$ memory reduction induce only 4.25% relative error for pollution categories. We apply the pipeline to 11 open Chinese corpora and 6 Chinese Common Crawl snapshots from 2021 to 2026. The audit reveals widespread but uneven pollution across open corpora, as well as highly polluted and temporally shifting Chinese web content. We further release a hierarchical Chinese web token dataset with 660k+ token records, each with web context, category, and explanation fields, organized as trees to support review and tracing of pollution.

## Metadata
- **Published**: 2026-08-11T08:58:06Z
- **Authors**: Qingjie Zhang, Ziqi Tang, Jie Zhang, Gelei Deng, Jinfeng Li, YueFeng Chen, Yitong Yang, Hui Xue, Tianwei Zhang, Han Qiu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10678v1)