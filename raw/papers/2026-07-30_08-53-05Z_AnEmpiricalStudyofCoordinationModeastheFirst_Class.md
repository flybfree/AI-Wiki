---
title: An Empirical Study of Coordination Mode as the First-Class Citizen in From-Scratch Multi-Agent Coding
published: 2026-07-30T08:53:05Z
authors: Yanyu Ren, Yunfeng Bai, Xizheng Wang, Li Chen, Dan Li
url: http://arxiv.org/abs/2607.27877v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Empirical Study of Coordination Mode as the First-Class Citizen in From-Scratch Multi-Agent Coding

## Abstract
Multi-agent vibe coding promises to accelerate software development, yet existing benchmarks rely on synthetic environments that ignore practical time and monetary costs, conflate reasoning with communication, and reward only superficial completion. We introduce multi-agent from-scratch evaluation benchmark, MSEval, evaluating multi-agent coding on real-world tasks. Grounded in 10 authentic, full-stack projects across 10 domains, MSEval scores performance using hierarchical requirements and deterministic rubrics.   Its execution engine, LegoGent, tests 10 collaboration topologies where agents coordinate via periodic sync intervals and deploy through native CI/CD pipelines. Concurrently, the automated grader TAgent dynamically probes implementations to jointly measure functional success, latency, and prefix-cached token cost. Across 100 runs, MSEval reveals that organizational topology rivals model capability in shaping the speed--cost--quality trade-off. For identical tasks and models, varying the topology shifts scores by over 30 points and doubles wall-clock time. Structured pipelines converge fastest with the highest quality, whereas heavy managerial oversight degrades performance. Ultimately, MSEval establishes a rigorous, reproducible standard for measuring how multi-agent teams actually build software. The benchmark is released at https://github.com/robinren03/MSEval.

## Metadata
- **Published**: 2026-07-30T08:53:05Z
- **Authors**: Yanyu Ren, Yunfeng Bai, Xizheng Wang, Li Chen, Dan Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27877v1)