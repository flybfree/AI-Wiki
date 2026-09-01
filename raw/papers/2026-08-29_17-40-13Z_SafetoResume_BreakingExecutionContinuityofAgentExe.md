---
title: Safe to Resume? Breaking Execution Continuity of Agent Execution via Rollback
published: 2026-08-29T17:40:13Z
authors: Guanlong Wu, Dahui Li, Ke Jiang, Jianyu Niu, Cong Wang, Yinqian Zhang
url: http://arxiv.org/abs/2608.29381v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Safe to Resume? Breaking Execution Continuity of Agent Execution via Rollback

## Abstract
AI agents are moving toward persistent, stateful execution across various applications, accumulating execution state and external effects that are costly to reconstruct after failures. Checkpoint and rollback (C/R) are becoming essential for recovery, yet their security implications remain largely unexplored. Correct rollback does not imply secure recovery: a faithfully restored checkpoint may resume an execution whose states, assumptions, and external effects never coexisted in any valid history. In this paper, we present the first systematic security study of checkpoint and rollback in existing agent systems. By examining representative agent C/R systems, we characterize the design space of existing C/R mechanisms and develop a general execution model that captures their recovery boundaries and state dependencies. From this model, we identify five fundamental failure modes spanning incomplete or inconsistent internal state, stale external dependencies, nondeterministic replay, and unrecorded external effects. We further demonstrate their security impact through three end-to-end attacks on Hermes, Cline, and LangGraph, enabling malware-verification bypass, unauthorized mail forwarding, and double payment. To systematically study these failures in practice, we develop a multi-agent analysis pipeline that reconstructs execution semantics, identifies violations of the five failure conditions, and validates them through actual rollback. Across five representative frameworks, our evaluation shows that these failures recur across heterogeneous C/R designs and stem from a common gap between the state restored by a checkpoint and the dependencies required for secure continuation.

## Metadata
- **Published**: 2026-08-29T17:40:13Z
- **Authors**: Guanlong Wu, Dahui Li, Ke Jiang, Jianyu Niu, Cong Wang, Yinqian Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29381v1)