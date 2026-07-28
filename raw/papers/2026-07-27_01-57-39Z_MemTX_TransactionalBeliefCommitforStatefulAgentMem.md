---
title: MemTX: Transactional Belief Commit for Stateful Agent Memory
published: 2026-07-27T01:57:39Z
authors: Xiaoyang Li, Yiqi Wang, Haohui Lu, Zhi Chen, Mo Li, Pingan Song, Taotao Cai
url: http://arxiv.org/abs/2607.23929v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemTX: Transactional Belief Commit for Stateful Agent Memory

## Abstract
LLM agents increasingly coordinate through persistent shared memory: one agent's write becomes another agent's premise, and eventually a tool call with real side effects. Current agent memory systems treat every accepted write as immediately actionable truth, so a polluted tool result, a stale update, or a teammate's half-finished note can silently drive an irreversible action. We argue that a memory write is not a belief commit. We present MemTX, a transactional belief-commit protocol. Each record carries evidence, permissions, provenance, and validity. Writes are staged inside snapshot-isolated transactions and admitted by a validate-and-commit pipeline, irreversible tool calls are gated on in-flight belief state, and retracting a belief triggers typed cascading repair of its derived records and tool side effects. Two invariants, action-safety gating and cascade-repair completeness, are machine-checked by property-based testing and bounded exhaustive enumeration of 5.5 million protocol states, with zero violations. Across five backbones from three model families, MemTX leads all eight baselines with paired-McNemar significance on four backbones and statistically ties the best baseline on the fifth and strongest, while remaining the only method with zero downstream harm on every backbone. Backbone capability does not substitute for commit discipline.

## Metadata
- **Published**: 2026-07-27T01:57:39Z
- **Authors**: Xiaoyang Li, Yiqi Wang, Haohui Lu, Zhi Chen, Mo Li, Pingan Song, Taotao Cai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23929v1)