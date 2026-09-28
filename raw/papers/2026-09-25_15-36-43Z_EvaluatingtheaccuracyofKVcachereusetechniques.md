---
title: Evaluating the accuracy of KV cache reuse techniques
published: 2026-09-25T15:36:43Z
authors: Samuel Cestola, Tianxiang Xia, Pengfei Zheng, Weiyan Zheng, Bo Wang, Yi Zhao, Diego Didona
url: http://arxiv.org/abs/2609.31415v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating the accuracy of KV cache reuse techniques

## Abstract
Position-independent KV cache reuse aims to reduce latency in retrieval-augmented generation by reusing chunk-level KV caches across prompts. We show that current evaluations of KV cache reuse techniques rely on measurements that fail to faithfully capture the loss of accuracy attributable to reuse, often artificially inflating the reported effectiveness. We also show that existing datasets do not exhibit the reuse dynamics needed to thoroughly evaluate such techniques. To address these issues, we propose an evaluation methodology that measures this accuracy loss without ambiguity and we introduce Boxoffice, a tool that programmatically generates evaluation datasets that exercise challenging KV cache reuse patterns.

## Metadata
- **Published**: 2026-09-25T15:36:43Z
- **Authors**: Samuel Cestola, Tianxiang Xia, Pengfei Zheng, Weiyan Zheng, Bo Wang, Yi Zhao, Diego Didona
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.31415v1)