---
title: PAUSE: A User-Centric Benchmark for Personal AI Assistants in Unified Service Environments
published: 2026-07-29T18:10:06Z
authors: Haoyu Chen, Xirui Shi, Yuyao Wang, Jerry Chen, Di Niu
url: http://arxiv.org/abs/2607.27354v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PAUSE: A User-Centric Benchmark for Personal AI Assistants in Unified Service Environments

## Abstract
Personal AI assistants are increasingly deployed as task-oriented, tool-augmented agents that operate within unified service environments to support everyday user activities. In realistic settings, such assistants must reason over persistent user state, respect user-specific configurations and permissions, and sustain long-horizon, constraint-aware interactions across multiple services. Existing benchmarks, however, often fragment service contexts or abstract away user state, limiting their ability to evaluate user-centric personal assistant behavior in realistic service settings. We introduce PAUSE, a user-centric benchmark for evaluating personal AI assistants in stateful, service-integrated environments. PAUSE captures core challenges of real-world assistant deployment by requiring agents to coordinate actions across heterogeneous user-owned resources while maintaining consistency with environment state, authorization constraints over multi-turn interactions. The benchmark incorporates explicit user-agent interaction via realistic user simulation, enabling evaluation beyond static tool execution. To support principled and reproducible evaluation, PAUSE adopts a multi-regime evaluation framework aligned with task characteristics. Open-ended service management tasks are assessed using semantic and trajectory-level behavioral metrics, while constraint-intensive tasks admit deterministic, state-based verification. Benchmark results show that even state-of-the-art proprietary models fail to reach 70% task completion on scenarios requiring stateful reasoning and configuration awareness, revealing consistent and interpretable failure patterns. Finally, we present a user-centric synthesis pipeline that enables scalable generation of coherent service environments, user configurations, and reliably annotated tasks, supporting benchmark extensibility and future research.

## Metadata
- **Published**: 2026-07-29T18:10:06Z
- **Authors**: Haoyu Chen, Xirui Shi, Yuyao Wang, Jerry Chen, Di Niu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27354v1)