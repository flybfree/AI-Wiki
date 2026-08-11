---
title: Complete, Scalable, and Robust Prioritized Planning for Multi-Robot Ordered Storage and Retrieval at Maximum Capacity
published: 2026-08-07T19:55:58Z
authors: William Zhang, Tzvika Geft, Jingjin Yu, Kostas Bekris
url: http://arxiv.org/abs/2608.07734v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Complete, Scalable, and Robust Prioritized Planning for Multi-Robot Ordered Storage and Retrieval at Maximum Capacity

## Abstract
Automated warehouses face a fundamental trade-off between maximizing storage density and achieving high retrieval throughput. While puzzle-based storage (PBS) architectures increase capacity by eliminating aisles, coordinating multiple robots in these high-density spaces is computationally challenging due to the potential for deadlocks. This paper introduces a novel multi-robot formulation for the ``ordered storage and retrieval problem at maximum capacity''. The focus is on rectangular grids accessible from a single boundary, where loads need to be first stored up to full capacity and then efficiently retrieved, given a planned departure sequence. This work bridges the gap between geometric feasibility and execution efficiency by leveraging the properties of relocation-free arrangements. These properties guide an online, prioritized multi-agent path-finding algorithm, which is the main contribution of this work. Unlike general centralized planners, the approach exploits the specific invariants of the storage arrangement to guarantee completeness and prevent deadlocks, enabling scalability. Experiments demonstrate that the method achieves near-linear improvement in makespan with respect to the number of robots, up to $m = C$, where $C$ is the grid width. Crucially, the algorithmic overhead of supporting robustness is negligible; the system handles uncertainty in departure sequences using robust storage arrangements with no significant penalty in execution speed compared to the non-robust baseline.

## Metadata
- **Published**: 2026-08-07T19:55:58Z
- **Authors**: William Zhang, Tzvika Geft, Jingjin Yu, Kostas Bekris
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07734v1)