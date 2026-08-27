---
title: When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory
published: 2026-08-26T09:04:21Z
authors: Kazuki Nakayashiki
url: http://arxiv.org/abs/2608.25553v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory

## Abstract
An agent that inherits a consolidated memory may inherit a constraint that was true when written and has since been withdrawn by a newer authoritative record. Under a scarce verification budget, does the agent recover the withdrawal, and if not, is the error avoidable without spending more? We model supersession explicitly -- historical provenance is immutable; what changes is which record is current -- and assign by design the memory's form, the world's state (source current or superseded), and the verification policy at a fixed budget of two records: the agent's own allocation, or the same budget with one slot re-assigned to the critical provenance path or to a random record. With a constraint stated, agents inspected its provenance path in about one episode in five; when that constraint had been superseded, native allocation produced stale-consistent decisions in 77.3%, 74.7% and 74.7% of episodes across a primary run, a fresh-wording replication and a held-out domain. Re-assigning one slot to the critical path raised current-record-consistent decisions by +74.0, +72.7 and +61.3 points, positive in six of six models in each of those runs, and changed nothing when the record agreed with the memory. The held-out scenario was later found to contain a temporal inconsistency; a robustness replication with one sentence corrected, deposited externally before execution, gave +73.3 points and is reported alongside the original. The intervention uses knowledge of the critical path and is not a scheduler; it identifies that the share of stale-memory error attributable to verification allocation is close to its structural ceiling. Memory systems may need freshness or supersession signals separate from relevance.

## Metadata
- **Published**: 2026-08-26T09:04:21Z
- **Authors**: Kazuki Nakayashiki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25553v1)