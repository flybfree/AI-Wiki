---
title: Runtime-Independent Persistent Agents: Preserving Identity, Memory, and Code Across Models, Harnesses, and Servers
published: 2026-09-01T01:32:22Z
authors: Zhenyu Zhao, Roy Zhao
url: http://arxiv.org/abs/2609.00546v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Runtime-Independent Persistent Agents: Preserving Identity, Memory, and Code Across Models, Harnesses, and Servers

## Abstract
Agent systems are commonly described by the model and harness that currently produce their behavior. That boundary is useful for one execution but underspecifies a long-lived agent that may change models, orchestration harnesses, interaction sessions, and host servers while retaining one identity, memory, and executable code lineage. We present a runtime-independent architecture for persistent agents. A continuity-bearing substrate $P_t=(I_t,M_t,B_t)$ contains an architectural identity representation, private durable memory, and a versioned software body. A replaceable deployment binding comprises an execution substrate $E_t=(R_t,H_t,D_t)$, which supplies a reasoner, harness, and host, and a set of interaction surfaces $S_t$, such as chat, API, or user interface bindings. A deployed execution is $A_t=P_t\triangleright(E_t,S_t)$; changing either replaceable layer is migration, not agent creation, when an authorized protocol preserves attributable lineage and transfers continuation authority within a governed deployment boundary.   We define six continuity invariants and a quiesce--checkpoint--validate--bind--rehydrate--resume protocol. Enoch realizes the design as a reusable body plus private installed identity, memory, workflow state, and continuation authority, with infrastructure dependencies behind versioned provider contracts. A clean-room run of the frozen public commit passes 833 core tests and 92 provider and library tests executed separately from the core suite; deployments have exercised reasoner-version, interaction-surface, and host-machine substitutions while retaining continuity-bearing state. This evidence supports mechanical substitutability and authorized system continuity, not behavioral invariance or exhaustive pairwise evaluation. The downstream measurement question is whether an authorized continuation still recalls, composes, and enacts its identity.

## Metadata
- **Published**: 2026-09-01T01:32:22Z
- **Authors**: Zhenyu Zhao, Roy Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00546v1)