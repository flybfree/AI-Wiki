---
title: Beyond Memory: A Transactional Continuity Kernel for Long-Lived AI Agents
published: 2026-08-12T04:28:49Z
authors: Jun He, Deying Yu
url: http://arxiv.org/abs/2608.11632v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Memory: A Transactional Continuity Kernel for Long-Lived AI Agents

## Abstract
Persistent AI agents accumulate versioned state across long horizons, but storage retention alone does not identify authoritative state. Without an explicit control plane, unmediated updates by models, tools, and background workers risk stale overwrites, un-audited exposures, and self-authorizing privilege escalation. We argue that agent state governance is an infrastructural activation problem, defining continuity as an unbroken, authorized lineage of accepted branch heads. We present the Continuity Kernel (CK), an activation contract that decouples off-commit candidate evaluation from atomic state activation. Untrusted components propose typed changes against an exact predecessor head or typed absence. A short activation transaction revalidates ownership, pre-state authority, freshness, and effect uniqueness, recording one stable disposition (Commit, Reject, Quarantine, or Defer). Only Commit atomically advances the branch head and installs the complete accepted unit (state, authority, lineage, effects, outcome, and receipt). A bounded executable model verifies the protocol across 2,808,230 reachable states and 5,526,474 state-changing transitions with zero invariant violations.

## Metadata
- **Published**: 2026-08-12T04:28:49Z
- **Authors**: Jun He, Deying Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11632v1)