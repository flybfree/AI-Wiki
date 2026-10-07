---
title: Trajectory-Retrieval Speculative Decoding: When Does a Model's Own History Help?
published: 2026-10-05T20:19:28Z
authors: Yuyang Dai, Yushun Dong
url: http://arxiv.org/abs/2610.07350v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trajectory-Retrieval Speculative Decoding: When Does a Model's Own History Help?

## Abstract
Long chain-of-thought reasoning increases sequential decoding cost while creating a growing history of potentially reusable continuations. We investigate when this history supplies useful drafts and complements an existing drafter. Controlled source comparisons reveal trajectory-specific reuse, motivating our method Trajectory-Local Adaptive Retrieval (TLAR). TLAR retrieves approximately matched continuations from the current trajectory and uses recent verification outcomes to adapt retrieval activation and candidate width. TLAR combines retrieved continuations with model-generated drafts in a shared candidate tree, preserving the target model's output distribution through exact verification. Across code debugging, mathematics, and open-ended writing, our evaluation connects source reuse, incremental acceptance, and execution cost. Combining TLAR with strong retrieval baselines improves token acceptance under matched verification budgets and increases end-to-end throughput over the draft-model baseline. These findings support generated trajectories as runtime memory for adaptive inference.

## Metadata
- **Published**: 2026-10-05T20:19:28Z
- **Authors**: Yuyang Dai, Yushun Dong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07350v1)