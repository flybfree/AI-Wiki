---
title: TideRL: Boosting Agentic RL Goodput with Readiness-Aware Scheduling
published: 2026-08-11T02:49:33Z
authors: Yanyu Ren, Xizheng Wang, Xiao Liu, Bowen Lv, Hanchen Zhang, Shudan Zhang, Hanyu Lai, Shuai Wang, Li Chen, Dan Li, Jie Tang
url: http://arxiv.org/abs/2608.10402v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TideRL: Boosting Agentic RL Goodput with Readiness-Aware Scheduling

## Abstract
Reinforcement learning (RL) for large language models is moving toward multi-turn agentic workloads, where rollout tasks repeatedly pause for external environments, resume with growing contexts, and finish at highly variable times. In this setting, RL training goodput, measured by training throughput, matters more than raw GPU occupancy: GPU waiting and repeated prefill recomputation are pure overhead. We present TideRL, a readiness-aware elastic RL system with Continuous Task Batching, Resource-Aware Ref-Actor Pipelining, and Elastic Resource Scaling. CTB preserves useful rollout state, $\textrm{RA}^2\textrm{P}$ selects between decoupled streaming and colocated aggregation from the ready backlog and arrival interval, and ERS moves ranks between rollout and training using the same readiness signals. Across text-only and multi-modal agentic workloads, TideRL improves RL training goodput by up to 5.6$\times$ over synchronous baselines and over 33% over asynchronous baselines, while reaching similar task performance. It also improves KV cache hit rate by 1.58$\times$, reduces per-step training time by up to 44.3%, and cuts total waiting time by up to 77.6%.

## Metadata
- **Published**: 2026-08-11T02:49:33Z
- **Authors**: Yanyu Ren, Xizheng Wang, Xiao Liu, Bowen Lv, Hanchen Zhang, Shudan Zhang, Hanyu Lai, Shuai Wang, Li Chen, Dan Li, Jie Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10402v1)