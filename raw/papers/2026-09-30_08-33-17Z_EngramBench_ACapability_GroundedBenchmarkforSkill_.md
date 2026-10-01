---
title: EngramBench: A Capability-Grounded Benchmark for Skill-Evolution Harnesses
published: 2026-09-30T08:33:17Z
authors: Zhixuan Tan, Pengjie Gu, Zhao Li, Yihan Hu, Xu He, Dong Li, Jianye Hao
url: http://arxiv.org/abs/2609.39284v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EngramBench: A Capability-Grounded Benchmark for Skill-Evolution Harnesses

## Abstract
While large language models have achieved remarkable success in isolated code generation, authentic software engineering requires sustained reasoning, complex state management, and continuous cross-domain abstraction. However, current evaluations of skill evolution in autonomous agents suffer from a critical identifiability problem: they structurally confound genuine capability abstraction with rote solution leakage (i.e., copying highly similar code from historical training data). To resolve this, we introduce EngramBench, a rigorous, capability-grounded benchmark governed by the strict axiom of capability overlap without solution overlap. Comprising 30 diverse learning tasks and 13 unseen transfer tasks, EngramBench challenges agents to navigate interactive, multi-hour development cycles driven by LLM-simulated users. Our extensive evaluation across 48 multi-hour execution trajectories -- corroborated by human-expert validation -- reveals a profound insight into procedural memory. We demonstrate that static skill banks do not magically bypass the "last mile" of exact code implementation, which remains bottlenecked by the base model's inherent reasoning limits. However, they serve as an indispensable execution compass. By navigating agents away from catastrophic, token-heavy trial-and-error, genuine capability abstraction slashes redundant context bloat and reduces overall coding time by over 55%. Ultimately, EngramBench shifts the evaluation paradigm from trivial pattern matching to the verifiable measurement of deep, cross-domain capability transfer.

## Metadata
- **Published**: 2026-09-30T08:33:17Z
- **Authors**: Zhixuan Tan, Pengjie Gu, Zhao Li, Yihan Hu, Xu He, Dong Li, Jianye Hao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39284v1)