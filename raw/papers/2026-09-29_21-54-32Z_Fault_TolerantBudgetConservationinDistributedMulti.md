---
title: Fault-Tolerant Budget Conservation in Distributed Multi-Agent Delegation
published: 2026-09-29T21:54:32Z
authors: Genliang Zhu, Chu Wang
url: http://arxiv.org/abs/2610.00349v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fault-Tolerant Budget Conservation in Distributed Multi-Agent Delegation

## Abstract
Resource limits are becoming an authorization boundary for AI agents that delegate work across concurrent and failure-prone workers. Parent-child allocation constraints, affine objects, and distributed escrow do not by themselves prevent overspend when replies are lost, effects complete after timeout, messages repeat, branches partition, or DAG joins alias one lineage. We formalize fault-tolerant budget conservation for distributed multi-agent delegation. Budgets are quantized resource vectors represented by exclusive escrow credits that move through a delegation DAG. Before dispatch, a branch converts credit into an operation reservation bound to lineage, epoch, normalized effect, maximum charge, receiver, and idempotency key. It persists a signed dispatch permit with quarantine; the gateway verifies that permit before first acceptance. Uncertain effects remain charged until authenticated settlement, a fenced authoritative no-effect proof, or permanent retirement. We prove ownership partition, ledger and effect conservation, descendant non-amplification, at-most-once settlement, late-completion safety, and partition confinement under explicit mediation, durability, authentication, normalization, and gateway assumptions. An indistinguishability result shows that partition-local availability requires exclusive preallocation. Bounded TLA+ checking, an independent JavaScript explorer, and crash-injected two-process SQLite experiments exercise the declared scope and detect timeout-refund and historical-certificate-validation mutants. The mechanism preserves the issued budget bound across the evaluated crash, retry, duplicate, partition, join, and late-completion schedules.

## Metadata
- **Published**: 2026-09-29T21:54:32Z
- **Authors**: Genliang Zhu, Chu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00349v1)