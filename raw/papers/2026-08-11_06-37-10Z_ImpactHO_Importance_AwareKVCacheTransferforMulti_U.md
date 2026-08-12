---
title: ImpactHO: Importance-Aware KV Cache Transfer for Multi-User Edge LLM Handover
published: 2026-08-11T06:37:10Z
authors: Minwoo Kim, Soochang Song, Namyoon Lee, Bang Chul Jung, Yongjune Kim
url: http://arxiv.org/abs/2608.10545v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ImpactHO: Importance-Aware KV Cache Transfer for Multi-User Edge LLM Handover

## Abstract
Edge LLMs must preserve inference continuity when a user hands over between edge nodes, requiring key-value (KV) cache transfer to the target node. However, simultaneous handovers saturate the backhaul, preventing full cache delivery within the mobility-imposed transfer window. Rather than allocating bandwidth as if all cache entries were equally valuable, we order each user's KV cache by importance and transmit only its most informative fraction, turning token-level sparsity into communication savings. We cast the transfer as a multi-user backhaul allocation problem that maximizes average accuracy across users. Each user's partial-cache accuracy serves as its utility: a sigmoid that fits measurements on the RULER benchmark with $R^2>0.99$ across models and context lengths. Because importance ordering front-loads the high-value entries, the concave region of the accuracy curve spans nearly the entire cache. Our proposed allocator keeps served users within this region, making each per-slot allocation problem convex. The optimum is derived via a closed-form weighted water-filling solution that generalizes information-theoretic water-filling and enables online scheduling. The proposed allocator attains over 93.7% average accuracy in a 500ms transfer window, within 0.5pp of the full-cache ceiling, and reaches 98.2-99.5% of a clairvoyant upper bound.

## Metadata
- **Published**: 2026-08-11T06:37:10Z
- **Authors**: Minwoo Kim, Soochang Song, Namyoon Lee, Bang Chul Jung, Yongjune Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10545v1)