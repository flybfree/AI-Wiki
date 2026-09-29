---
title: CoMemBench: Benchmarking Collaborative Memory Boundaries across Multi-Agent Workflow Topologies
published: 2026-09-26T03:33:15Z
authors: Sen Zhao, Ruiqi Kong, Zuyu Zhang, Lifeng Shen, Xinyu He, Ding Zou, Xu Zhang, Qinghua Zhang
url: http://arxiv.org/abs/2609.32192v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoMemBench: Benchmarking Collaborative Memory Boundaries across Multi-Agent Workflow Topologies

## Abstract
Multi-agent workflows require task-relevant information to be shared across agents, while irrelevant, stale, unverified, or incompatible information must remain isolated. We call this task-conditioned scope of information a collaborative memory boundary. Workflow topology determines which intermediate artifacts are applicable to which downstream workers and when they cease to be valid, thereby providing a structural stress dimension for sharing and isolation. Existing memory benchmarks primarily evaluate retention and retrieval, whereas multi-agent benchmarks emphasize coordination and end-to-end completion, leaving topology-conditioned memory boundaries largely unmeasured. We introduce CoMemBench, an execution-grounded benchmark for collaborative memory sharing and isolation across multi-agent workflow topologies. It constructs 800 composite workflows across four domains from source-grounded dependency graphs, with node-local specifications, verifiable artifact handoffs, native evaluators, and matched isolation challenges. CoMemBench measures workflow completion, verified node progress, required-handoff reliability, isolation robustness, and token cost. Experiments reveal a sharing-isolation trade-off: broader context improves information availability but can weaken isolation, while system rankings shift across topologies and artifact violations.

## Metadata
- **Published**: 2026-09-26T03:33:15Z
- **Authors**: Sen Zhao, Ruiqi Kong, Zuyu Zhang, Lifeng Shen, Xinyu He, Ding Zou, Xu Zhang, Qinghua Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32192v1)