---
title: Goal-Persistent Coding Agents as Scientific Performance Engineers: A Fixed-Radius Nearest-Neighbor Case Study
published: 2026-09-25T20:32:33Z
authors: Xiangyang Ju
url: http://arxiv.org/abs/2609.31980v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Goal-Persistent Coding Agents as Scientific Performance Engineers: A Fixed-Radius Nearest-Neighbor Case Study

## Abstract
Coding agents can pursue persistent objectives across many tool-use turns, but evidence that general-purpose agents can conduct rigorous scientific performance engineering remains limited. We present a repository-scale case study in which off-the-shelf Codex and Claude Code agents optimize fixed-radius nearest-neighbor (FRNN) search for particle tracking. Starting from a PyTorch-dependent CUDA implementation, the agents follow an executable goal that specifies exact-correctness tests, profiling requirements, and acceptance criteria without prescribing code transformations. In the primary sequential trajectory, they autonomously remove the PyTorch dependency and conduct hypothesis-driven optimization experiments. The resulting standalone C++/CUDA library exactly reproduces the targeted reference result. Its synchronous NumPy interface achieved 1.6-fold speedup over the original GPU-resident PyTorch interface, despite including host transfers. Similar speedups were observed across different GPU architectures and software stacks. An independent optimization rerun followed a different sequence of hypotheses and reached even better performance on the target workload. These results show that goal-persistent coding agents can act as experimental performance engineers, and that executable scientific contracts are needed both to guide and to validate their optimization.

## Metadata
- **Published**: 2026-09-25T20:32:33Z
- **Authors**: Xiangyang Ju
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.31980v1)