---
title: Recycling computational processes of dynamic programming for combinatorial optimization problems: a reservoir computing approach
published: 2026-07-25T02:54:32Z
authors: Sora Todaka, Akihiro Yamamoto, Nozomi Akashi
url: http://arxiv.org/abs/2607.23009v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Recycling computational processes of dynamic programming for combinatorial optimization problems: a reservoir computing approach

## Abstract
Reusing previously computed results is a long-standing principle for reducing computational cost, but such reuse has largely been confined to a single problem's computation. Sharing computational processes across multiple simultaneously solved problems remains possible in principle, yet designing algorithms that exploit nontrivial cross-task relationships is difficult to do manually. Here, we use machine learning to discover such algorithms automatically. Specifically, based on reservoir computing, we propose a method that uses computation results recorded by dynamic programming for combinatorial optimization problems as features for linear regression, leveraging them to assist other combinatorial optimization computations. We validate the approach on the traveling salesman and subset sum problems. Multiplexing the dynamic programming process improves approximation accuracy over generic features and reduces computation time compared with independent solutions. These results suggest a new form of computation, distinct from conventional computational design, in which multiple processes efficiently share and recycle intermediate results and states.

## Metadata
- **Published**: 2026-07-25T02:54:32Z
- **Authors**: Sora Todaka, Akihiro Yamamoto, Nozomi Akashi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23009v1)