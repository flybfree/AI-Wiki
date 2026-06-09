---
title: KoRe: Compact Knowledge Representations for Large Language Models
published: 2026-05-19T17:53:29Z
authors: Davide Cavicchini, Fausto Giunchiglia, Jacopo Staiano
url: http://arxiv.org/abs/2605.20170v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KoRe: Compact Knowledge Representations for Large Language Models

## Abstract
Modern Large Language Models (LLMs) have shown impressive performances in user-facing tasks such as question answering, as well as consistent improvements in reasoning capabilities. Still, the way these models encode knowledge seems inherently flawed: by design, LLMs encode world-knowledge within their parameters. This way of representing knowledge is inherently opaque, difficult to debug and update, and prone to hallucinations. On the other hand, Knowledge Graphs can provide human-readable and easily editable world knowledge representations, and their application in knowledge-intensive tasks has consistently proven beneficial to downstream performance. Nonetheless, current integration techniques require extensive retraining or finetuning. To overcome this issue, we introduce KoRe, a methodology to encode 1-hop sub-graphs into compact discrete knowledge tokens and inject them into a LLM backbone. We test the proposed approach on three established benchmarks, and report competitive performances coupled with a significant reduction (up to 10x) in token usage. Our results show that compact discrete KG representations can efficiently and effectively be used to ground modern LLMs.

## Metadata
- **Published**: 2026-05-19T17:53:29Z
- **Authors**: Davide Cavicchini, Fausto Giunchiglia, Jacopo Staiano
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.20170v1)