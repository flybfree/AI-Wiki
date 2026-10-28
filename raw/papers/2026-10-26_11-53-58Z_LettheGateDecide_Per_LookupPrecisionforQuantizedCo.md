---
title: Let the Gate Decide: Per-Lookup Precision for Quantized Conditional Memory in LLMs
published: 2026-10-26T11:53:58Z
authors: Tianqi Chen, Xunchao Li, Linchuan Xie, Guanghua Yu, Jianchen Zhu, Peisong Wang, Jian Cheng
url: http://arxiv.org/abs/2610.35985v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Let the Gate Decide: Per-Lookup Precision for Quantized Conditional Memory in LLMs

## Abstract
Conditional memory layers, such as DeepSeek's Engram, attach large hashed n-gram tables to a language model, and removing them from DeepSeek-V4.1-Flash costs 36.8 PopQA points. Low-bit quantization loses long-tail facts first, and the standard remedy, giving more bits to frequently accessed rows, backfires: refining lookups by access frequency is worse than refining them at random. We trace this to the gate that scales each retrieved row. A lookup's quantization error is weighted by its gate, which is small for frequent n-grams, large for the rare n-grams of long-tail entities, and computable from a 1-bit code. GateRQ therefore stores each row as a ladder of 1-bit residual codes, keeps level 1 in GPU memory to compute the gate, and reads deeper levels only for the lookups the gate ranks highest. Without retraining, GateRQ cuts GPU table memory by 7.8x on DeepSeek-V4.1-Flash, which raises vLLM throughput by 11%-31% over FP8 tables, while losing about 1 PopQA point at 1.50 bits read per lookup and 0.2 points at 2.10 bits across two models.

## Metadata
- **Published**: 2026-10-26T11:53:58Z
- **Authors**: Tianqi Chen, Xunchao Li, Linchuan Xie, Guanghua Yu, Jianchen Zhu, Peisong Wang, Jian Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.35985v1)