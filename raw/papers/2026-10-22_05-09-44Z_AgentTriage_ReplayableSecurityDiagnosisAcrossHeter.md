---
title: AgentTriage: Replayable Security Diagnosis Across Heterogeneous Agent Runtimes
published: 2026-10-22T05:09:44Z
authors: Jie Ying, Xutao Zhang, Ningyuan Chen, Mengce Zheng, Jun Li, Zhongjie Zhu, Tiantian Zhu
url: http://arxiv.org/abs/2610.30738v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentTriage: Replayable Security Diagnosis Across Heterogeneous Agent Runtimes

## Abstract
When tool-use agents write files, execute code, or send data, their final responses do not explain the resulting security events, and heterogeneous runtimes expose the relevant evidence through incompatible interfaces. We present AgentTriage, an executable contract for replayable security diagnosis across heterogeneous runtimes. The contract admits conclusions whose claims cite canonical runtime events and requires abstention when mandatory evidence is missing. Runtime overlays normalize native observations, while a deterministic pipeline joins invocation and result lifecycles, constructs a typed provenance graph, selects a policy-decisive slice, and binds claims to recorded evidence. Given the same normalized trace, overlay version, and pre-run policy oracle, the diagnosis can be recomputed and its claims re-checked without language-model judgment. Across five runtimes, one contract captures all 159 applicable executions, with an audit of native and synthesized identifiers. On 120 adjudicated cases, AgentTriage achieves 0.858 grounded joint diagnosis, 0.966 required-evidence coverage, and a 0.036 unsupported-claim rate, improving joint diagnosis by 0.175 (95% CI [0.092, 0.258]) over the strongest same-schema baseline. These results quantify the precision of replayable diagnosis and the observation boundaries that require abstention. We release an open-source implementation and selected sanitized evidence at https://github.com/AsnGs/agenttriage-open-source.

## Metadata
- **Published**: 2026-10-22T05:09:44Z
- **Authors**: Jie Ying, Xutao Zhang, Ningyuan Chen, Mengce Zheng, Jun Li, Zhongjie Zhu, Tiantian Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.30738v1)