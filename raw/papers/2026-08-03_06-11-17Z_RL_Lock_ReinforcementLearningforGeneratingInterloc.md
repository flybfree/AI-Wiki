---
title: RL-Lock: Reinforcement Learning for Generating Interlocking Assemblies
published: 2026-08-03T06:11:17Z
authors: Xuyang Ma, Chaewoon Kim, Haonan Zhang, Rulin Chen, Ziqi Wang, Peng Song
url: http://arxiv.org/abs/2608.01744v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RL-Lock: Reinforcement Learning for Generating Interlocking Assemblies

## Abstract
An interlocking assembly is an assembly in which component parts are connected purely through their geometric arrangement, without relying on external connectors such as glue and nails. Such assemblies have been widely used in a variety of real-world applications due to their structural stability. The problem of generating interlocking assemblies is generally formulated as a shape decomposition problem, where a target 3D object represented as a voxel grid is partitioned into a prescribed number of interlocking pieces. We observe that generating interlocking assemblies is inherently a sequential decision-making problem, where an agent repeatedly decides which piece each voxel should be assigned to. Inspired by the observation, we propose the first reinforcement learning framework RL-Lock for generating interlocking assemblies, without relying on handcrafted search heuristics as existing works did. RL-Lock combines structured action chunking with MCTS-guided policy-value learning to efficiently navigate the large combinatorial search space for interlocking assembly generation. We demonstrate through experiments that RL-Lock allows effective generation of interlocking assemblies, especially for challenging cases in which existing approaches take too long or even fail to find a valid solution.

## Metadata
- **Published**: 2026-08-03T06:11:17Z
- **Authors**: Xuyang Ma, Chaewoon Kim, Haonan Zhang, Rulin Chen, Ziqi Wang, Peng Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01744v1)