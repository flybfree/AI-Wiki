---
title: Multi-step SWE: Can Coding Agents Keep Building on Their Own Code Over Long Horizons?
published: 2026-11-04T21:49:40Z
authors: Xiangkai Zeng, Zheng Liu, Zihao Lin
url: http://arxiv.org/abs/2611.07166v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-step SWE: Can Coding Agents Keep Building on Their Own Code Over Long Horizons?

## Abstract
Developers rarely give a coding agent a single request: they ask it to build a component and then to extend, upgrade, and optimize it, each time on code the agent itself wrote. Most benchmarks, however, score one task at a time. We introduce Multi-step SWE, a long-horizon benchmark of 69 software engineering tasks, each a chain of 5-15 dependent steps on a single codebase. Every step is a complete, multi-hour engineering request that starts from the code the agent produced in the preceding steps, so early design decisions and errors carry forward. The tasks span four families of engineering work and nine languages, include both from-scratch builds and existing open-source codebases, and ground every step in an existing source of truth that defines both the instruction and its verifier. Across nine frontier models, the strongest model reaches a solve rate of only 18.5%, and 38 of the 69 tasks are not solved by any model. We release Multi-step SWE publicly at https://multistepswe.com.

## Metadata
- **Published**: 2026-11-04T21:49:40Z
- **Authors**: Xiangkai Zeng, Zheng Liu, Zihao Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.07166v1)