---
title: Key-Interval A*: Accelerating Grid Pathfinding via Structural Abstraction
published: 2026-07-25T23:41:35Z
authors: Taiquan Sui
url: http://arxiv.org/abs/2607.23393v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Key-Interval A*: Accelerating Grid Pathfinding via Structural Abstraction

## Abstract
Existing exact methods for 4-connected grid pathfinding reduce online search, but often either retain fine-grained search states or require substantial preprocessing. This paper presents Key-Interval A* (KIA*), an optimal pathfinding algorithm that uses lightweight preprocessing to construct and search over a compact interval-level abstraction of free space. KIA* represents free space using intervals: maximal contiguous runs of traversable cells. It extracts key intervals that capture structural boundary changes and connects them through contiguous non-key regions. KIA* then performs A*-style search on the resulting key-interval graph and constructively reconstructs grid paths from interval chains, without cell-level local search. We prove the completeness and optimality of KIA* on 4-connected grids. Experiments on standard benchmarks show that KIA* preserves exact shortest-path lengths and achieves the fastest runtime on seven of eight benchmark groups, with the largest gains on structured and game maps.

## Metadata
- **Published**: 2026-07-25T23:41:35Z
- **Authors**: Taiquan Sui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23393v1)