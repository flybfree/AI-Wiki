---
title: Share First, Route What Remains: A Unified Framework for Token-Adaptive MoE Computation
published: 2026-08-11T02:40:58Z
authors: Gongli Zhang, Zhulin Liu, C. L. Philip Chen
url: http://arxiv.org/abs/2608.10392v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Share First, Route What Remains: A Unified Framework for Token-Adaptive MoE Computation

## Abstract
Mixture-of-experts (MoE) models have recently moved beyond routing a fixed number of complete experts. Shared-expert designs preserve reusable knowledge, fine-grained methods vary computation within experts, and dynamic routers adapt the number of active experts. Yet these decisions are usually made independently, overlooking a basic dependency: extracting reusable computation changes both what remains and how much expert capacity the remainder needs. We study this dependency by decomposing sparsely upcycled feed-forward experts into key-value channels. Co-activated experts align at a subset of value positions; removing these positions changes expert preference; and greater shared coverage is associated with lower residual expert demand. These observations lead to one principle: share first, then route what remains. We instantiate it in UniF-MoE, a unified framework for token-adaptive MoE computation. Each expert is partitioned into aligned blocks. A shared-demand score sets the shared block count and pathway weight, key prototypes select the shared content, and the complementary demand determines the residual expert count through cumulative routing mass. A Gram regularizer separates and normalizes router embeddings, promoting diverse routing directions, sparse expert overlap, and a simple routing geometry. Experiments on DomainBed and GLUE show that this unified design improves predictive performance over representative static and dynamic MoEs while reducing activated computation, inference latency, and memory. Code is available at https://github.com/existence0420/UniF-MoE.

## Metadata
- **Published**: 2026-08-11T02:40:58Z
- **Authors**: Gongli Zhang, Zhulin Liu, C. L. Philip Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10392v1)