---
title: SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving
published: 2026-07-27T02:10:35Z
authors: Yihui Zhang, Tianyu Wo, Jinghao Wang, Xiaoyang Sun, Menghao Zhang, Cangzhou Yuan, Li Li, Chunming Hu, Albert Y. Zomaya, Renyu Yang
url: http://arxiv.org/abs/2607.23933v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving

## Abstract
As LLM agents increasingly rely on the Model Context Protocol (MCP) to invoke isolated external sandboxes, disaggregated sandbox deployment introduces a fundamental tension between resource utilization and interactive tail latency. Persistent long-lived sandbox reservations incur excessive memory overhead at scale, while lazy on-demand instantiation generates severe cold-start penalties that degrade response performance under multi-tenant, multi-turn agent workloads. To resolve this dilemma, we present SpecBox, a runtime built around speculative sandbox preallocation tailored for dynamic LLM agent execution pipelines.   At its core, SpecBox implements keyword matching and streaming semantic embedding to enable intent-driven sandbox prewarming, which identifies pending tool execution demands mid-LLM token generation and fully overlaps sandbox bootstrapping with model inference. To extend prewarming windows across sequential agent steps, the framework leverages context-aware stochastic prefetching atop a sandbox dependency graph to probabilistically forecast future sandbox switches ahead of execution. We complement these speculative mechanisms with two orthogonal optimizations: a semantic result cache that prunes redundant repeated sandbox invocations, and a dedicated out-of-band shared-memory transport plane that bypasses conventional network serialization to deliver zero-copy artifact transfers. Evaluated on high-concurrency multi-turn agent traces, our prototype demonstrates that SpecBox cuts P99 end-to-end latency by up to $2.9\times$ relative to the on-demand sandbox baseline, while slashing peak memory consumption by $45.9\%$ compared to permanently reserved sandbox deployments.

## Metadata
- **Published**: 2026-07-27T02:10:35Z
- **Authors**: Yihui Zhang, Tianyu Wo, Jinghao Wang, Xiaoyang Sun, Menghao Zhang, Cangzhou Yuan, Li Li, Chunming Hu, Albert Y. Zomaya, Renyu Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23933v1)