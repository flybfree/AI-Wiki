---
title: STAGE: Stateful Translation to Agentic Graph Execution with Policy-Scoped Context and Deterministic Control
published: 2026-08-23T18:17:09Z
authors: Mengxi Luo, Changjia Chen, An Cao, Zirong Huang, Wanyi Dai
url: http://arxiv.org/abs/2608.22538v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# STAGE: Stateful Translation to Agentic Graph Execution with Policy-Scoped Context and Deterministic Control

## Abstract
Policy-governed agents must interpret case evidence while following an authorized procedure. We present \textsc{Stage}, an executable-graph framework that confines model judgment to policy-scoped nodes while placing procedural control in deterministic code. At each node, the model receives task-relevant policy context and returns a typed result, while the coordinator enforces the reviewed execution contract. We evaluate \textsc{Stage} on SOP-Bench Referral Abuse, two $τ^2$-bench domains, and Smart Dispute, a proprietary banking benchmark. Compared with monolithic full-policy execution, \textsc{Stage} generally improves task success and repeated-run reliability across workflows of varying procedural complexity. The largest gains occur on the deeper Telecom and Smart Dispute workflows, where $\mathrm{Pass}^3$ increases by 7.5--55.0 and 57.2--65.7 percentage points, respectively, depending on the model. These results show that combining policy-scoped context with deterministic procedural control can improve the reliability of policy execution.

## Metadata
- **Published**: 2026-08-23T18:17:09Z
- **Authors**: Mengxi Luo, Changjia Chen, An Cao, Zirong Huang, Wanyi Dai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22538v1)